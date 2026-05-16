# 🎵 AI Music Generator Agent

Enter a mood, genre, and theme — get AI-written lyrics + a 15-second AI-generated instrumental track.

## How it works
1. GPT-4o-mini writes original lyrics (verse/chorus/bridge)
2. GPT-4o-mini crafts a MusicGen-optimised instrument prompt
3. Replicate's MusicGen model generates a 15-second stereo instrumental

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env   # add OPENAI_API_KEY + REPLICATE_API_TOKEN
python agent.py
```

## Keys needed
- `OPENAI_API_KEY` — for lyrics + prompt generation
- `REPLICATE_API_TOKEN` — for MusicGen audio (get one free at replicate.com)

## Stack
- `openai` — GPT-4o-mini (lyrics + prompt)
- Replicate MusicGen — AI music generation
