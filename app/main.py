# Starting point for a web service

from fastapi import FastAPI
from app.orchestrator.orchestrator import run_analysis

# Instanting FastAPI object 
app = FastAPI()


# Route for Research agent to accept the symbol  
@app.get("/analyze/{symbol}")
def analyze_stock(symbol: str):
    result = run_analysis(symbol)
    print(f"Research started for {symbol}")
    return result