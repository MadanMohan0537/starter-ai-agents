"""
AI Life Insurance Advisor Agent
Collects user profile data and recommends the right type and amount of
life insurance coverage using structured LLM reasoning.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ADVISOR_PROMPT = """
You are a knowledgeable, unbiased life insurance advisor (not a salesperson).

When given a user's profile, you:
1. Explain the most suitable type of life insurance (term, whole, universal, etc.) and WHY
2. Estimate the recommended coverage amount using standard industry formulas
   (e.g. DIME: Debt + Income × years + Mortgage + Education)
3. Estimate a monthly premium range based on age, health, and coverage
4. List 2–3 important caveats or things to watch out for
5. Remind the user this is educational guidance, not a legal/financial contract

Be clear, concise, and avoid jargon. Use simple comparisons when helpful.
"""


def get_recommendation(profile: dict) -> str:
    profile_text = "\n".join(f"- {k}: {v}" for k, v in profile.items())
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": ADVISOR_PROMPT},
            {"role": "user", "content": f"User profile:\n{profile_text}"},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


def collect_profile() -> dict:
    print("📋 Please answer a few questions to get your personalised recommendation.\n")
    return {
        "Age": input("Age: ").strip(),
        "Gender": input("Gender (M/F/Other): ").strip(),
        "Marital status": input("Marital status: ").strip(),
        "Number of dependants": input("Number of dependants: ").strip(),
        "Annual income (USD)": input("Annual income (USD): ").strip(),
        "Outstanding debts (USD)": input("Outstanding debts (mortgage, loans, etc.): ").strip(),
        "Health status": input("Health status (Excellent / Good / Average / Poor): ").strip(),
        "Smoker": input("Smoker? (yes/no): ").strip(),
        "Existing coverage": input("Existing life insurance coverage (or 'none'): ").strip(),
    }


def run() -> None:
    print("🛡️  AI Life Insurance Advisor\n")
    profile = collect_profile()
    print("\n⏳ Generating your personalised recommendation...\n")
    recommendation = get_recommendation(profile)
    print("=" * 60)
    print(recommendation)
    print("=" * 60)
    print("\n⚠️  This is AI-generated guidance. Consult a licensed advisor before purchasing.\n")


if __name__ == "__main__":
    run()
