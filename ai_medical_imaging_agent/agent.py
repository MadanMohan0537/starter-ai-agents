"""
AI Medical Imaging Agent
Analyses medical images (X-ray, MRI, CT scan) using GPT-4o vision
and provides a structured educational report.

⚠️  FOR EDUCATIONAL USE ONLY — NOT a diagnostic tool.
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
You are a medical imaging education assistant. When shown a medical image:

1. Identify the modality (X-ray, MRI, CT, ultrasound, etc.) and body region
2. Describe the key anatomical structures visible
3. Note any prominent findings or patterns that a student might observe
4. Explain what a radiologist typically looks for in this type of image
5. Suggest 2–3 educational takeaways

IMPORTANT: Always include this disclaimer at the end:
"⚠️ This analysis is for educational purposes only and does not constitute
medical advice or a clinical diagnosis. Always consult a qualified radiologist
or physician for any medical concerns."
"""


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyse_image(image_path: str, question: str = "") -> str:
    ext = Path(image_path).suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "gif": "gif", "webp": "webp"}.get(ext, "jpeg")

    b64 = encode_image(image_path)
    user_text = question if question else "Please analyse this medical image."

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    {"type": "image_url", "image_url": {"url": f"data:image/{mime};base64,{b64}"}},
                ],
            },
        ],
        max_tokens=1000,
    )
    return response.choices[0].message.content


def run(image_path: str) -> None:
    print(f"🏥 AI Medical Imaging Agent")
    print(f"📁 Image: {image_path}\n")

    if not Path(image_path).exists():
        print(f"❌ File not found: {image_path}")
        sys.exit(1)

    question = input("Any specific question about this image? (press Enter to skip): ").strip()
    print("\n⏳ Analysing image...\n")

    report = analyse_image(image_path, question)
    print("=" * 60)
    print(report)
    print("=" * 60)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.jpg"
    run(path)
