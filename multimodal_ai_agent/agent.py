"""
Multimodal AI Agent
Accepts text, images, and files in combination and responds with
rich understanding across all modalities.
"""

import os
import sys
import base64
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a highly capable multimodal AI assistant. You can:
- Analyse images in detail (describe, extract text, identify objects, compare)
- Answer questions about images + text combined
- Read documents and images together
- Generate creative content based on visual inputs

Be thorough, precise, and helpful. If you see text in an image, transcribe it.
"""


def encode_image(path: str) -> tuple[str, str]:
    ext = Path(path).suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "gif": "gif", "webp": "webp"}.get(ext, "jpeg")
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8"), mime


def chat_with_media(history: list, text: str, image_paths: list[str]) -> str:
    content = []

    if text:
        content.append({"type": "text", "text": text})

    for img_path in image_paths:
        if Path(img_path).exists():
            b64, mime = encode_image(img_path)
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/{mime};base64,{b64}"},
            })
        else:
            print(f"⚠️  Image not found: {img_path}")

    history.append({"role": "user", "content": content})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
        max_tokens=1500,
    )
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply


def run() -> None:
    print("🖼️  Multimodal AI Agent")
    print("Chat with text + images. Type 'quit' to exit.\n")

    history = []
    while True:
        text = input("💬 You (text): ").strip()
        if text.lower() in {"quit", "exit"}:
            break

        images_input = input("📎 Image paths (comma-separated, or Enter to skip): ").strip()
        image_paths = [p.strip() for p in images_input.split(",") if p.strip()] if images_input else []

        if not text and not image_paths:
            continue

        reply = chat_with_media(history, text, image_paths)
        print(f"\n🤖 Agent: {reply}\n")


if __name__ == "__main__":
    run()
