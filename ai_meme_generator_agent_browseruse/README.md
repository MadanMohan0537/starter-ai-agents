# 😂 AI Meme Generator Agent (Browser Use)

Enter any topic and the agent generates meme captions with GPT-4o-mini, then uses `browser-use` to create the meme on imgflip.com automatically.

## How it works
1. GPT-4o-mini picks the best meme template + writes top/bottom captions
2. `browser-use` autonomously navigates imgflip.com, fills in the text, and generates the meme

## Quickstart
```bash
pip install -r requirements.txt
playwright install chromium
cp ../.env.example .env
python agent.py
```

## Stack
- `openai` — GPT-4o-mini meme caption generation
- `browser-use` — autonomous browser navigation
- `langchain-openai` — LLM interface for browser-use agent
