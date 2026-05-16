# 🚀 AI Startup Trend Analysis Agent

Enter any market sector and get a structured trend report: market size, top trends, competitive landscape, white-space opportunities, and recommended focus areas.

## How it works
1. Tavily web search fetches real-time articles and reports
2. GPT-4o-mini synthesises the results into a 6-section trend report

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env   # add OPENAI_API_KEY + TAVILY_API_KEY
python agent.py
```

## Example sectors
- "AI in healthcare diagnostics"
- "Climate fintech"
- "B2B SaaS for construction"

## Stack
- `openai` — GPT-4o-mini trend synthesis
- Tavily API — real-time web search
