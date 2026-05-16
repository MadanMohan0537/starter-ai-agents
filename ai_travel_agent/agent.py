"""
AI Travel Agent
Plans a complete trip itinerary based on destination, duration, budget,
and interests — with day-by-day activities, accommodation tips, and local advice.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TRAVEL_PROMPT = """
You are an expert travel planner with deep knowledge of global destinations.

Create a detailed trip itinerary that includes:
1. 🗓️ Day-by-day schedule (morning / afternoon / evening for each day)
2. 🏨 Accommodation recommendations (with neighbourhood and price range)
3. 🍽️ Must-try local dishes and restaurant suggestions
4. 🚌 Getting around (transport tips)
5. 💰 Budget breakdown (accommodation / food / activities / transport)
6. ⚠️ Important tips (safety, cultural etiquette, best time to visit)
7. 📦 Packing essentials for this destination

Tailor recommendations to the traveller's budget and interests.
Be specific — name real places, neighbourhoods, and attractions.
"""


def plan_trip(destination: str, days: int, budget: str, interests: str, travel_style: str) -> str:
    query = (
        f"Destination: {destination}\n"
        f"Duration: {days} days\n"
        f"Budget level: {budget}\n"
        f"Interests: {interests}\n"
        f"Travel style: {travel_style}"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": TRAVEL_PROMPT},
            {"role": "user", "content": query},
        ],
        temperature=0.6,
    )
    return response.choices[0].message.content


def run() -> None:
    print("✈️  AI Travel Agent\n")
    destination = input("Where do you want to go? ").strip() or "Kyoto, Japan"
    days = int(input("How many days? ").strip() or "7")
    budget = input("Budget level (budget / mid-range / luxury): ").strip() or "mid-range"
    interests = input("Interests (e.g. food, history, adventure, art): ").strip() or "food, history, temples"
    style = input("Travel style (solo / couple / family / group): ").strip() or "couple"

    print("\n⏳ Planning your perfect trip...\n")
    itinerary = plan_trip(destination, days, budget, interests, style)

    print("=" * 60)
    print(f"  YOUR {days}-DAY {destination.upper()} ITINERARY")
    print("=" * 60)
    print(itinerary)
    print("=" * 60)


if __name__ == "__main__":
    run()
