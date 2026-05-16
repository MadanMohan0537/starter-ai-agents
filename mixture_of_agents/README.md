# 🤖 Mixture of Agents

Four specialist AI agents answer a question in parallel, then a coordinator synthesises their perspectives into one superior answer.

## How it works
- **Analytical Agent** — logic, facts, structured reasoning
- **Creative Agent** — novel angles, analogies, lateral thinking
- **Devil's Advocate** — challenges assumptions, surfaces weaknesses
- **Practical Agent** — real-world, actionable insights
- **Coordinator** — synthesises all four into one final answer

All four specialists run concurrently via `asyncio`.

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py
```

## Stack
- `openai` — AsyncOpenAI for parallel specialist calls + synthesis
