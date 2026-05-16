# 🧠 AI Reasoning Agent

Solves complex problems with a fully visible chain-of-thought reasoning trace — math, logic, coding, science, and more.

## How it works
Uses structured Chain-of-Thought (CoT) prompting: the agent breaks the problem into sub-problems, verifies its work, then states the final answer.

Optionally uses `o1-mini` for problems that need deeper native reasoning.

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py
```

## Example problems
- "A train travels 60 mph for 2 hours then 80 mph for 1.5 hours. What is the average speed?"
- "What is the time complexity of merge sort and why?"
- "Explain why 0.1 + 0.2 ≠ 0.3 in floating point arithmetic"

## Stack
- `openai` — GPT-4o-mini with CoT system prompt, or o1-mini
