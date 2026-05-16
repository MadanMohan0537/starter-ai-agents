# 💹 xAI Finance Agent

A conversational finance analyst powered by xAI's Grok model (falls back to GPT-4o-mini). Ask anything about stocks, markets, and financial strategy.

## How it works
- Uses xAI's OpenAI-compatible API with Grok for real-time financial knowledge
- Maintains conversation history for follow-up questions
- Covers: stock analysis, macro trends, earnings, portfolio strategy, risk

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env   # add XAI_API_KEY (or OPENAI_API_KEY as fallback)
python agent.py
```

## Keys needed
- `XAI_API_KEY` — from console.x.ai (preferred, uses Grok)
- `OPENAI_API_KEY` — fallback if no xAI key (uses GPT-4o-mini)

## Disclaimer
Educational purposes only. Not financial advice.

## Stack
- `openai` — SDK (OpenAI-compatible, pointed at xAI's endpoint for Grok)
