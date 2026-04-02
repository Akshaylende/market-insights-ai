# Fetching stock related news using APIs

import requests
from app.config.settings import GNEWS_API_KEY

# Function to extract stock news information from GNEWS
def get_news(query: str):
    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&apikey={GNEWS_API_KEY}"

    response = requests.get(url)
    articles = response.json().get("articles", [])

    return [
        {
            "title": a["title"],
            "description":a["description"]
        }
        for a in articles[:5]
    ]