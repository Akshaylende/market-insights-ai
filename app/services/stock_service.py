# Fetching stock information using APIs

import yfinance as yf

# Function to extract stock pricing details from yfinance
def get_stock_data(symbol : str):
    stock = yf.Ticker(symbol)
    info = stock.info

    return{
        "price": info.get("currentPrice"),
        "pe_ratio": info.get("trailingPE"),
        "market_cap": info.get("marketCap"),
        "name": info.get("longName")
    }