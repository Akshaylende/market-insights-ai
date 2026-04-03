# Implementing technical agent 

from app.services.technical_service import get_technical_indicators


# call to technical analyzer service  
def technical_agent(symbol: str):
    return get_technical_indicators(symbol)