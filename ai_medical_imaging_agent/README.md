# 🏥 AI Medical Imaging Agent

Analyses medical images (X-ray, MRI, CT) using GPT-4o vision and produces a structured educational report.

## ⚠️ Disclaimer
For educational purposes only. Not a diagnostic tool. Always consult a qualified radiologist.

## How it works
1. Pass any medical image file (JPG, PNG)
2. Optionally ask a specific question
3. GPT-4o vision identifies the modality, describes anatomy, notes findings, and provides educational takeaways

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env
python agent.py path/to/xray.jpg
```

## Stack
- `openai` — GPT-4o multimodal vision (base64 image encoding)
