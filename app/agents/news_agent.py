# News Agent Implementation

from app.services.news_service import get_news

# call to retrive stock news information service
def news_agent(company: str):
    return get_news(company)