"""
Mixture of Agents
Multiple specialist LLM agents independently answer a question,
then a coordinator synthesises their responses into one superior answer.
"""

import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SPECIALISTS = [
    {
        "name": "Analytical Agent",
        "system": "You are a rigorous analytical thinker. Approach every question with logic, data, and structured reasoning. Focus on facts and evidence.",
    },
    {
        "name": "Creative Agent",
        "system": "You are a lateral and creative thinker. Approach every question with novel angles, analogies, and unconventional perspectives.",
    },
    {
        "name": "Devil's Advocate",
        "system": "You are a critical devil's advocate. Challenge assumptions, identify weaknesses, and present counterarguments for any position.",
    },
    {
        "name": "Practical Agent",
        "system": "You are a pragmatic problem solver. Focus on actionable, real-world insights. What actually works in practice?",
    },
]

COORDINATOR_PROMPT = """
You are a master synthesiser. You have received responses from multiple specialist agents.
Your job is to:
1. Identify the strongest insights from each response
2. Resolve any contradictions with reasoned judgment
3. Produce one comprehensive, nuanced, and well-structured final answer
4. Note where the agents agreed vs. diverged and why that matters

Label your synthesis: "🎯 SYNTHESISED ANSWER:"
"""


async def ask_specialist(specialist: dict, question: str) -> tuple[str, str]:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": specialist["system"]},
            {"role": "user", "content": question},
        ],
        temperature=0.7,
    )
    return specialist["name"], response.choices[0].message.content


async def synthesise(question: str, specialist_answers: list[tuple[str, str]]) -> str:
    combined = "\n\n".join(f"=== {name} ===\n{answer}" for name, answer in specialist_answers)
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": COORDINATOR_PROMPT},
            {"role": "user", "content": f"Question: {question}\n\nSpecialist responses:\n{combined}"},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


async def run_async(question: str) -> None:
    print(f"\n🤔 Question: {question}\n")
    print(f"⚡ Querying {len(SPECIALISTS)} specialist agents in parallel...\n")

    tasks = [ask_specialist(s, question) for s in SPECIALISTS]
    answers = await asyncio.gather(*tasks)

    for name, answer in answers:
        print(f"--- {name} ---")
        print(answer[:400], "...\n" if len(answer) > 400 else "\n")

    print("🔄 Synthesising...\n")
    final = await synthesise(question, answers)
    print("=" * 60)
    print(final)
    print("=" * 60)


def run() -> None:
    print("🤖 Mixture of Agents\nMultiple AI specialists + one synthesiser.\n")
    question = input("❓ Question: ").strip()
    if not question:
        question = "What are the most important skills for the next decade?"
    asyncio.run(run_async(question))


if __name__ == "__main__":
    run()
