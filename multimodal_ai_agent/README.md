# 🖼️ Multimodal AI Agent

A conversational agent that understands text + images together, with memory across turns.

## How it works
- Accepts text and one or more image paths per turn
- GPT-4o processes all inputs together
- Maintains conversation history for contextual follow-up questions

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py
```

## Example use cases
- "What's wrong with this UI design?" + screenshot.png
- "Compare these two product photos" + img1.jpg, img2.jpg
- "Transcribe the text in this image" + handwritten_note.jpg

## Stack
- `openai` — GPT-4o multimodal with base64 image encoding
