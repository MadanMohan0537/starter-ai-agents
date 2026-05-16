# 📊 AI Data Analysis Agent

Ask questions about any CSV in plain English. The agent generates and executes pandas code, then explains the result.

## How it works
1. Load any CSV file
2. Ask a natural language question ("What is the average revenue by region?")
3. GPT-4o-mini generates pandas code → executes it → explains the result

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py your_data.csv
```

## Example questions
- "Which category has the highest average sales?"
- "Show me the top 5 customers by order count"
- "What percentage of orders were delivered late?"

## Stack
- `openai` — code generation + result explanation
- `pandas` — data execution engine
