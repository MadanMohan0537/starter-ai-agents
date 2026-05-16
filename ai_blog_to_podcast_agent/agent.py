"""
AI Blog to Podcast Agent
Fetches a blog post URL, summarizes it, and converts it to a podcast-style
audio script using OpenAI TTS.
"""

import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fetch_blog_text(url: str) -> str:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join(p.get_text() for p in paragraphs)[:8000]


def blog_to_podcast_script(blog_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional podcast scriptwriter. "
                    "Convert the blog content into a friendly, engaging 3-minute podcast script. "
                    "Use conversational language. Start with a hook. End with a call to action."
                ),
            },
            {"role": "user", "content": blog_text},
        ],
    )
    return response.choices[0].message.content


def text_to_audio(script: str, output_file: str = "podcast.mp3") -> str:
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=script,
    )
    response.stream_to_file(output_file)
    return output_file


def run(blog_url: str) -> None:
    print(f"📖 Fetching blog: {blog_url}")
    text = fetch_blog_text(blog_url)

    print("✍️  Generating podcast script...")
    script = blog_to_podcast_script(text)
    print("\n--- SCRIPT PREVIEW ---")
    print(script[:500], "...\n")

    print("🎙️  Converting to audio...")
    audio_file = text_to_audio(script)
    print(f"✅ Podcast saved to: {audio_file}")


if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com/blog"
    run(url)
