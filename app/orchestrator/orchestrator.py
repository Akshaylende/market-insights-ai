# Orchestrator for Different Agents 

from app.agents.data_agent import data_agent
from app.agents.news_agent import news_agent
from app.agents.sentiment_agent import sentiment_agent
from app.agents.technical_agent import technical_agent
from app.agents.insight_agent import generate_insight

# Main Orchestrator Function to Invoke Different Agents
def run_analysis(symbol: str):
    stock_data = data_agent(symbol)
    news = news_agent(stock_data["name"])
    sentiment = sentiment_agent(news)
    technicals = technical_agent(symbol)

    insight = generate_insight(stock_data, news, technicals, sentiment)


    return {
        "stock_data": stock_data,
        "news": news,
        "sentiment": sentiment,
        "technicals": technicals,
        "insight": insight
    }