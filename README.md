# market-insights-ai

# 📊 AI Market Insights Agent (Multi-Agent System)

## 🚀 Overview

The **AI Market Insights Agent** is a multi-agent system that analyzes stock market data and generates actionable investment insights.
Instead of relying on a single model, it uses multiple specialized AI agents (like a team of analysts) to process different types of information such as stock data, news, sentiment, and technical indicators.

---

## 🧠 How It Works

1. The user sends a request (e.g., *“Analyze TCS stock”*).
2. The **Orchestrator** coordinates multiple agents:

   * **Data Agent** → Fetches stock data
   * **News Agent** → Retrieves latest news
   * **Sentiment Agent** → Analyzes market sentiment
   * **Technical Agent** → Computes indicators like RSI
3. All results are combined and passed to an **LLM (Gemini)**.
4. The system generates a final insight with:

   * Summary
   * Risk level
   * Recommendation (Buy / Hold / Sell)



## High-level Architecture

                ┌────────────────────┐
                │   User Query       │
                └────────┬───────────┘
                         ↓
                ┌────────────────────┐
                │  Orchestrator      │
                │  (Master Agent)    │
                └────────┬───────────┘
     ┌──────────────┬──────────────┬──────────────┐
     ↓              ↓              ↓              ↓
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│ Data     │  │ News     │  │ Sentiment│  │ Technical│
│ Agent    │  │ Agent    │  │ Agent    │  │ Agent    │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
     ↓              ↓              ↓              ↓
     └──────────────┴──────────────┴──────────────┘
                         ↓
                ┌────────────────────┐
                │ Insight Generator  │
                └────────────────────┘
                         ↓
                ┌────────────────────┐
                │ Final Report       │
                └────────────────────┘


## 🛠️ Tech Stack

### Backend

* Python
* FastAPI

### AI / Agents

* LangChain
* Gemini Flash (LLM)

### Data Sources

* yfinance (stock data)
* GNews API (news)

### Data Processing

* pandas
* numpy

### Vector Database (Optional)

* FAISS (for future RAG support)

---

## 📁 Project Structure

```
market-insights-agent/
│
├── app/
│   ├── agents/
│   │   ├── data_agent.py
│   │   ├── news_agent.py
│   │   └── insight_agent.py
│   │   └── sentiment_agent.py
│   │   └── technical_agent.py
│   │
│   ├── orchestrator/
│   │   └── orchestrator.py
│   │
│   ├── services/
│   │   ├── stock_service.py
│   │   └── news_service.py
|   |   └── sentiment_service.py
|   |   └── technical_service.py
|   |   └── structured_output_service.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-url>
cd market-insights-agent
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file:

```
GNEWS_API_KEY=your_api_key
GEMINI_API_KEY=your_api_key
```

### 4. Run the Application

```
uvicorn app.main:app --reload
```

### 5. Test API

Open in browser:

```
http://127.0.0.1:8000/analyze/TCS.NS
```

---

## 📦 Example Output

```
{
  "stock_data": {...},
  "news": [...],
  "sentiment": "bullish",
  "technicals": {
    "rsi": 72.4,
    "trend": "bullish"
  },
  "insight": "Stock shows strong momentum but is slightly overbought. Recommendation: HOLD"
}
```

---

## ✨ Features

* 📊 Real-time stock analysis
* 📰 News-based insights
* 💬 Sentiment analysis using AI
* 📈 Technical indicators (RSI, trend)
* 🧠 AI-generated investment recommendations
* ⚡ Modular multi-agent architecture

---

## 🔮 Future Enhancements

* Portfolio analysis
* Multi-stock comparison
* Alerts & notifications
* RAG (Retrieval-Augmented Generation) with FAISS
* Frontend dashboard (React)

---

## 🤝 Contribution

Feel free to fork the project and improve it. Contributions are welcome!

---

## 📌 Summary

This project demonstrates how **Agentic AI systems** can combine data, reasoning, and machine learning to solve real-world problems like market analysis. It is designed to be simple, scalable, and extensible.

---
