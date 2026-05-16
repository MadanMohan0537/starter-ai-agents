"""
OpenAI Research Agent
Uses OpenAI's built-in web search tool to research any topic and
produce a well-cited, structured research brief.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def research(topic: str, depth: str = "standard") -> str:
    instructions = {
        "quick":    "Write a 3-bullet summary with the most important facts.",
        "standard": "Write a structured 400-word research brief with key findings, context, and implications.",
        "deep":     "Write a comprehensive 800-word research report with background, current state, key players, data points, controversies, and outlook.",
    }.get(depth, "standard")

    response = client.responses.create(
        model="gpt-4o-mini",
        tools=[{"type": "web_search_preview"}],
        input=f"Research the following topic thoroughly: {topic}\n\n{instructions}",
    )
    # Extract text from the response
    for item in response.output:
        if hasattr(item, "content"):
            for block in item.content:
                if hasattr(block, "text"):
                    return block.text
    return str(response.output)


def run() -> None:
    print("🔬 OpenAI Research Agent\n")
    topic = input("What do you want to research? ").strip()
    if not topic:
        topic = "The current state of quantum computing"

    depth = input("Depth — quick / standard / deep (default: standard): ").strip() or "standard"

    print(f"\n🔍 Researching: {topic}...\n")
    report = research(topic, depth)

    print("=" * 60)
    print(report)
    print("=" * 60)


if __name__ == "__main__":
    run()
