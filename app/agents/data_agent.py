# Data Agent Implementation

from app.services.stock_service import get_stock_data


# call to retrive stock data service
def data_agent(symbol: str):
    return get_stock_data(symbol)