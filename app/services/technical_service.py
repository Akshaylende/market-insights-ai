# Technical Analysis using yfinance 

import yfinance as yf
import pandas as pd


def compute_rsi(data, window = 14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window = window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window = window).mean()

    rs = gain / loss

    return 100 - (100 / (1 + rs))



def get_technical_indicators(symbol: str):
    stock = yf.Ticker(symbol)
    df = stock.history(period="3mo")

    df['RSI'] = compute_rsi(df)

    latest = df.iloc[-1]

    return {
        "rsi": round(latest["RSI"], 2),
        "trend": "bullish" if latest["Close"] > df["Close"].mean() else "bearish"
    }