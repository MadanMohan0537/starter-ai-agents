"""
AI Music Generator Agent
Describes a mood/style, generates lyrics with GPT-4o-mini, and creates
an instrumental track using the Replicate API (MusicGen model).
"""

import os
import sys
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN", "")


def generate_lyrics(mood: str, genre: str, theme: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional songwriter. Write an original song with verse, chorus, and bridge. "
                    "Include emotional depth and vivid imagery. Format clearly with section labels."
                ),
            },
            {"role": "user", "content": f"Mood: {mood}\nGenre: {genre}\nTheme: {theme}"},
        ],
    )
    return response.choices[0].message.content


def generate_music_prompt(mood: str, genre: str) -> str:
    """Create a MusicGen-optimised prompt."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Convert music preferences into a concise MusicGen prompt (max 50 words). "
                    "Describe instruments, tempo, energy, and style. No lyrics."
                ),
            },
            {"role": "user", "content": f"Mood: {mood}, Genre: {genre}"},
        ],
    )
    return response.choices[0].message.content.strip()


def generate_music(prompt: str, duration: int = 15) -> str | None:
    """Call Replicate MusicGen API and return the audio URL."""
    if not REPLICATE_API_TOKEN:
        print("⚠️  REPLICATE_API_TOKEN not set — skipping audio generation.")
        return None

    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "version": "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
        "input": {"prompt": prompt, "duration": duration, "model_version": "stereo-large"},
    }
    resp = requests.post("https://api.replicate.com/v1/predictions", json=payload, headers=headers)
    prediction_id = resp.json().get("id")
    if not prediction_id:
        return None

    import time
    url = f"https://api.replicate.com/v1/predictions/{prediction_id}"
    for _ in range(30):
        time.sleep(3)
        result = requests.get(url, headers=headers).json()
        if result.get("status") == "succeeded":
            return result["output"]
        if result.get("status") == "failed":
            return None
    return None


def run() -> None:
    print("🎵 AI Music Generator Agent\n")
    mood = input("Mood (e.g. melancholic, uplifting, intense): ").strip() or "uplifting"
    genre = input("Genre (e.g. pop, jazz, lo-fi hip-hop, cinematic): ").strip() or "cinematic"
    theme = input("Song theme or story (e.g. late night city drive): ").strip() or "hope after loss"

    print("\n✍️  Writing lyrics...")
    lyrics = generate_lyrics(mood, genre, theme)
    print("\n--- LYRICS ---")
    print(lyrics)

    print("\n🎼 Generating music prompt...")
    music_prompt = generate_music_prompt(mood, genre)
    print(f"   Prompt: {music_prompt}")

    print("\n🎹 Generating instrumental track (15 seconds via MusicGen)...")
    audio_url = generate_music(music_prompt)
    if audio_url:
        print(f"\n🎧 Audio ready: {audio_url}")
    else:
        print("   Set REPLICATE_API_TOKEN in .env to enable audio generation.")


if __name__ == "__main__":
    run()
