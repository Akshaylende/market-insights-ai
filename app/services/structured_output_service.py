# To structure the LLM response using pydantic and with_structured_output

from pydantic import BaseModel, Field

# Class to structure the LLM response for Insights
class StockInsight(BaseModel):
    summary: str = Field(description = "As short 1-2 sentence summary of the stock's current situation.")
    risk_level: str = Field(description = "Risk level: Low, Medium, or High.")
    recommendation: str = Field(description="Recommendation: Buy, Hold, or Sell.")
    reasoning: str = Field(description="A 2-3 sentence reasoning behind the recommendation.")