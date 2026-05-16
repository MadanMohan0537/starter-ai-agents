# 🎙️ AI Blog to Podcast Agent

Converts any blog post URL into a ready-to-publish podcast MP3 in three steps: scrape → script → speech.

## How it works
1. **Scrape** — Fetches and parses the blog HTML with BeautifulSoup
2. **Script** — GPT-4o-mini rewrites the content as a conversational 3-minute podcast script
3. **Speak** — OpenAI TTS (voice: `alloy`) renders the script as `podcast.mp3`

## Quickstart
```bash
pip install -r requirements.txt
cp ../.env.example .env   # add OPENAI_API_KEY
python agent.py https://your-blog-post-url.com
```

## Output
- `podcast.mp3` — ready to upload to Spotify, Apple Podcasts, etc.

## Stack
- `openai` — GPT-4o-mini (script) + TTS-1 (audio)
- `beautifulsoup4` — HTML scraping
- `requests` — HTTP fetching
