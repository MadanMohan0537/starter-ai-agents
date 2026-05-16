# 💔 AI Breakup Recovery Agent

An empathetic conversational agent that helps users process breakups using positive psychology and CBT-inspired techniques.

## How it works
- GPT-4o-mini plays the role of a compassionate recovery coach
- Maintains full conversation history for context-aware support
- Suggests one concrete micro-action per turn (journaling, self-care, social reconnection)
- Gently reminds users to seek professional help when appropriate

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py
```

## Stack
- `openai` — GPT-4o-mini with a carefully crafted system prompt
