# Starting point for a web service
from fastapi import FastAPI


# Instanting FastAPI object 
app = FastAPI()


# Route for Research agent to accept the symbol  
@app.get("/analyze/{symbol}")
def analyze_stock(symbol: str):
    print(f"Research started for {symbol}")
    return {}