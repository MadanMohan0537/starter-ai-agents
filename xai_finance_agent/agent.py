"""
xAI Finance Agent
Uses xAI's Grok model to analyse stocks, market trends, and financial news
with Grok's real-time knowledge and reasoning.
"""

import os
from openai import OpenAI  # xAI uses OpenAI-compatible API
from dotenv import load_dotenv

load_dotenv()

# xAI's API is OpenAI-compatible — just change the base_url and key
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY", os.getenv("OPENAI_API_KEY")),
    base_url="https://api.x.ai/v1",
)
# Fallback to OpenAI if no xAI key
if not os.getenv("XAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    MODEL = "gpt-4o-mini"
else:
    MODEL = "grok-beta"

FINANCE_PROMPT = """
You are a sophisticated financial analyst with expertise in:
- Equity analysis and stock valuation
- Macroeconomic trends and their market impact
- Technical and fundamental analysis
- Risk management and portfolio strategy
- Earnings interpretation and financial ratios

When answering:
1. Be precise with numbers and dates
2. Distinguish clearly between facts, estimates, and opinion
3. Always mention key risks alongside any bullish thesis
4. Use financial terminology correctly
5. Note if data might be outdated

Disclaimer: This is for educational purposes. Not financial advice.
"""


def analyse(question: str, history: list) -> str:
    history.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": FINANCE_PROMPT}] + history,
        temperature=0.2,
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply


def run() -> None:
    model_name = "Grok" if MODEL == "grok-beta" else "GPT-4o-mini"
    print(f"💹 xAI Finance Agent (powered by {model_name})")
    print("Ask anything about stocks, markets, or finance. Type 'quit' to exit.\n")

    history = []
    while True:
        question = input("📈 Question: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        if not question:
            continue

        print("\n⏳ Analysing...\n")
        answer = analyse(question, history)
        print(f"💡 {answer}\n")
        print("─" * 50)


if __name__ == "__main__":
    run()
