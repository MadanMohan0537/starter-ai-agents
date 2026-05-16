"""
AI Meme Generator Agent (Browser Use)
Takes a topic or caption idea, generates meme text with GPT-4o-mini,
then uses browser-use to navigate imgflip.com and create the meme.
"""

import os
import asyncio
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_meme_text(topic: str) -> dict:
    """Generate top and bottom meme captions for a given topic."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a comedy writer specialising in internet memes. "
                    "Given a topic, generate a funny meme with a top caption and bottom caption "
                    "in the classic two-line meme format. Also suggest which popular meme template fits best "
                    "(e.g. 'Drake', 'Distracted Boyfriend', 'This Is Fine', 'Expanding Brain', etc.). "
                    "Return JSON: {\"template\": \"...\", \"top\": \"...\", \"bottom\": \"...\"}"
                ),
            },
            {"role": "user", "content": f"Topic: {topic}"},
        ],
        response_format={"type": "json_object"},
    )
    import json
    return json.loads(response.choices[0].message.content)


async def create_meme_with_browser(meme_data: dict) -> None:
    """Use browser-use agent to navigate imgflip and generate the meme."""
    try:
        from browser_use import Agent
        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(model="gpt-4o-mini")
        task = (
            f"Go to https://imgflip.com/memegenerator . "
            f"Search for the meme template called '{meme_data['template']}'. "
            f"Click on it. "
            f"Fill the top text with: {meme_data['top']} "
            f"Fill the bottom text with: {meme_data['bottom']} "
            f"Click 'Generate Meme' and take a screenshot of the result."
        )
        agent = Agent(task=task, llm=llm)
        await agent.run()
    except ImportError:
        print("⚠️  browser-use not installed. Showing meme text only.")
        print(f"   Template : {meme_data['template']}")
        print(f"   Top text : {meme_data['top']}")
        print(f"   Bot text : {meme_data['bottom']}")
        print("\n   Install browser-use: pip install browser-use")


def run() -> None:
    print("😂 AI Meme Generator Agent\n")
    topic = input("Enter a topic or idea for the meme: ").strip()
    if not topic:
        topic = "developers who say they'll fix it later"

    print("\n✍️  Generating meme captions...")
    meme_data = generate_meme_text(topic)
    print(f"\n🖼️  Template : {meme_data.get('template')}")
    print(f"   Top      : {meme_data.get('top')}")
    print(f"   Bottom   : {meme_data.get('bottom')}\n")

    print("🌐 Opening browser to generate meme on imgflip...")
    asyncio.run(create_meme_with_browser(meme_data))


if __name__ == "__main__":
    run()
