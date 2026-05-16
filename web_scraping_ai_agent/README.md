# 🕷️ Web Scraping AI Agent

Scrape any URL and ask questions about the content in plain English.

## How it works
1. BeautifulSoup scrapes and cleans the page (removes scripts, nav, footer)
2. GPT-4o-mini extracts exactly what you ask for from the content
3. Interactive Q&A loop — ask multiple questions about the same page

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py
```

## Example extractions
- "List all the article headlines and their links"
- "What are the pricing tiers on this page?"
- "Summarise the main value proposition"

## Stack
- `openai` — GPT-4o-mini structured extraction
- `beautifulsoup4` + `requests` — HTML scraping and cleaning
