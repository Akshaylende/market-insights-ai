# Fetching stock related news using APIs

import requests
from app.config.settings import GNEWS_API_KEY

def get_news(query: str):
    url = f"https://gnews.io/api/v4/search?q={query}&token={GNEWS_API_KEY}&lang=en"

    response = requests.get(url)
    articles = response.json().get("articles", [])

    return [
        {
            "title": a["title"],
            "description":a["description"]
        }
        for a in articles[:5]
    ]