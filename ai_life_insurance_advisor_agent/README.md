# 🛡️ AI Life Insurance Advisor Agent

Collects your personal profile and recommends the right type and amount of life insurance coverage.

## How it works
1. Answers 9 questions about age, income, dependants, health, etc.
2. GPT-4o-mini applies the DIME formula + industry heuristics
3. Returns: policy type, coverage amount, premium estimate, and caveats

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py
```

## Disclaimer
This is educational guidance only. Always consult a licensed insurance advisor before purchasing.

## Stack
- `openai` — GPT-4o-mini with structured advisory prompt
