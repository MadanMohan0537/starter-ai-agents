"""
AI Reasoning Agent
Solves complex problems step-by-step using chain-of-thought prompting.
Shows its full reasoning trace before delivering the final answer.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

REASONING_PROMPT = """
You are an expert problem solver. For every question:

1. THINK: Break the problem into sub-problems. Reason through each one carefully.
   Show all assumptions, intermediate steps, and calculations.
2. VERIFY: Check your reasoning for errors or edge cases.
3. ANSWER: State the final answer clearly and concisely.

Format your response exactly like this:
---
🧠 REASONING:
[Your detailed step-by-step thinking]

✅ VERIFICATION:
[Check your work]

💡 FINAL ANSWER:
[Clear, direct answer]
---
"""


def reason(question: str, use_o1: bool = False) -> str:
    model = "o1-mini" if use_o1 else "gpt-4o-mini"

    if use_o1:
        # o1 models have built-in CoT — simpler prompt
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
        )
    else:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": REASONING_PROMPT},
                {"role": "user", "content": question},
            ],
            temperature=0.1,
        )
    return response.choices[0].message.content


def run() -> None:
    print("🧠 AI Reasoning Agent")
    print("Solves problems with visible step-by-step reasoning.")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("❓ Problem: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        if not question:
            continue

        use_o1 = input("Use o1-mini for deeper reasoning? (y/N): ").strip().lower() == "y"

        print("\n⏳ Reasoning...\n")
        answer = reason(question, use_o1=use_o1)
        print(answer)
        print()


if __name__ == "__main__":
    run()
