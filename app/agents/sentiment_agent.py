# Sentiment Agent Implementation

from app.services.sentiment_service import analyze_sentiment


# Call to Sentiment analyzer service
def sentiment_agent(news):
    return analyze_sentiment(news)