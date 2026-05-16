"""
AI Startup Trend Analysis Agent
Researches a market sector using web search (Tavily) and produces a
structured trend report with opportunities and competitive landscape.
"""

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")


def web_search(query: str, max_results: int = 5) -> list[dict]:
    """Search the web using Tavily API."""
    if not TAVILY_API_KEY:
        return [{"title": "Demo", "content": f"[Web search disabled — add TAVILY_API_KEY] Query was: {query}"}]
    import requests
    resp = requests.post(
        "https://api.tavily.com/search",
        json={"api_key": TAVILY_API_KEY, "query": query, "max_results": max_results},
    )
    return resp.json().get("results", [])


def analyse_trends(sector: str, search_results: list[dict]) -> str:
    context = "\n\n".join(f"Source: {r.get('title', '')}\n{r.get('content', '')}" for r in search_results)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a startup market analyst. Based on the provided search results, "
                    "write a structured trend report with these sections:\n"
                    "1. 📈 Market Size & Growth\n"
                    "2. 🔥 Top 5 Emerging Trends\n"
                    "3. 🏆 Key Players & Competitive Landscape\n"
                    "4. 💡 White Space Opportunities (gaps where new startups can win)\n"
                    "5. ⚠️ Key Risks & Headwinds\n"
                    "6. 🎯 Recommended Focus Areas for a New Startup\n"
                    "Be specific. Cite examples from the search results."
                ),
            },
            {
                "role": "user",
                "content": f"Sector: {sector}\n\nSearch Results:\n{context}",
            },
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content


def run() -> None:
    print("🚀 AI Startup Trend Analysis Agent\n")
    sector = input("Enter market sector to analyse (e.g. 'AI in healthcare', 'climate fintech'): ").strip()
    if not sector:
        sector = "AI productivity tools for SMBs"

    print(f"\n🔍 Searching the web for: {sector}...")
    results = web_search(f"{sector} startup trends 2024 2025 market analysis")
    results += web_search(f"{sector} funding rounds new startups opportunities")

    print("📊 Analysing trends...\n")
    report = analyse_trends(sector, results)

    print("=" * 60)
    print(f"  TREND REPORT: {sector.upper()}")
    print("=" * 60)
    print(report)
    print("=" * 60)


if __name__ == "__main__":
    run()
