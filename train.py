# src/train.py
import pandas as pd
import torch
from torch import nn, optim
from model import LSTMModel
import numpy as np

# Load data
data = pd.read_csv("data/eurusd.csv")["Close"].fillna(method="ffill")
X = torch.tensor(data.values[:-1]).float().view(-1, 10, 1)
y = torch.tensor(data.values[1:]).float().view(-1, 1)

# Model
model = LSTMModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training
for epoch in range(1000):
    output = model(X)
    loss = criterion(output, y[:len(output)])
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"Epoch {epoch} Loss: {loss.item()}")

torch.save(model.state_dict(), "model/lstm.pth")
