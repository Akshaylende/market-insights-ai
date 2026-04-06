# Insight Agent/Aggregator (LLM)

from langchain_google_genai import ChatGoogleGenerativeAI
from app.config.settings import GEMINI_API_KEY
from app.services.structured_output_service import StockInsight


# Google LLM Instantiation 
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=GEMINI_API_KEY,
    temperature=0.5
)

# Bind pydantic schema/ structured schema to LLM
structured_llm = llm.with_structured_output(StockInsight)


# Function to generate Insights on Stock based on news & stock prices from LLM
def generate_insight(stock_data, news, technicals, sentiment):
    prompt = f"""
    Analyze the following stock:

    Stock Data:
    {stock_data}

    News:
    {news}
 
    Sentiment:
    {sentiment}

    Technical Indicators:
    {technicals}

    Give a short Summary, Risk level (Low/Medium/High), Recommendation (Buy/Hold/Sell) and Reasoning within 5-6 sentences only.
    """

    response = structured_llm.invoke(prompt)
    
    return response.model_dump()