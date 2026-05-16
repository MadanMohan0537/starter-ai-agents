# 📈 AI Data Visualisation Agent

Describe a chart in plain English and the agent generates and renders it from your CSV using Plotly.

## How it works
1. Load your CSV
2. Describe the chart: "Bar chart of sales by region, sorted descending"
3. GPT-4o-mini generates Plotly code → executes it → opens the chart in your browser

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py your_data.csv
```

## Example requests
- "Line chart of monthly revenue over time"
- "Pie chart of order distribution by category"
- "Scatter plot of age vs. spend, coloured by segment"

## Stack
- `openai` — Plotly code generation
- `plotly` — interactive chart rendering
- `pandas` — data loading
