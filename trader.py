# src/trader.py
import MetaTrader5 as mt5
from model import LSTMModel
import torch

# Login ke akun
mt5.initialize()
mt5.login(12345678, password="abc123", server="Broker-Server")

# Prediksi (dummy dulu)
model = LSTMModel()
model.load_state_dict(torch.load("model/lstm.pth"))
model.eval()

# Eksekusi Buy/Sell (ini contoh, nanti bisa disesuaikan)
symbol = "EURUSD"
lot = 0.1
order = mt5.order_send({
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": 10,
    "magic": 123456,
    "comment": "LSTM Entry",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
})
