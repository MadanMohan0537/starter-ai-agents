# 🔬 OpenAI Research Agent

Uses OpenAI's native `web_search_preview` tool to research any topic and produce a structured, cited research brief.

## How it works
- Uses OpenAI's built-in web search (no external API needed)
- Three depth levels: quick (bullets) / standard (400 words) / deep (800 words)

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py
```

## Example topics
- "Recent breakthroughs in fusion energy"
- "How Anthropic's Constitutional AI works"
- "Current state of CRISPR gene editing"

## Stack
- `openai` — GPT-4o-mini with `web_search_preview` tool (Responses API)
