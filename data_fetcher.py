# src/data_fetcher.py
import yfinance as yf
import pandas as pd

data = yf.download("EURUSD=X", start="2000-01-01", end="2025-01-01", interval="1d")
data.to_csv("data/eurusd.csv")
print("Data EUR/USD berhasil disimpan.")
