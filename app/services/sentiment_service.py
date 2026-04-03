# Sentiment Analyze service

import json
from google import genai
from google.genai import types
from app.config.settings import GEMINI_API_KEY


# New Client Initialization
client = genai.Client(api_key=GEMINI_API_KEY)



# Function to analyze sentiments from the information
def analyze_sentiment(news_list):
    content = "\n".join([n["title"] for n in news_list])

    prompt = f"""
    Analyze the overall sentiment of the following news headlines:

    Headlines:
    {content}

    Respond ONLY with a valid JSON object using this exact schema:
    {{
        "sentiment": "bullish" | "bearish" | "neutral",
        "confidence": float between 0.0 and 1.0
    }}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )
    return json.loads(response.text)