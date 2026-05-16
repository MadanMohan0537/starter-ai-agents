# 🤖 Starter AI Agents

> A curated collection of 16 production-ready AI agent projects — each self-contained, fully documented, and runnable in under 5 minutes.

Inspired by [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps).

---

## 📦 What's Inside

| # | Agent | What it does | Key APIs |
|---|-------|-------------|----------|
| 1 | [🎙️ Blog to Podcast](#1-blog-to-podcast-agent) | Converts any blog URL into an MP3 podcast | OpenAI TTS |
| 2 | [💔 Breakup Recovery](#2-breakup-recovery-agent) | Empathetic CBT-inspired emotional support chat | GPT-4o-mini |
| 3 | [📊 Data Analysis](#3-data-analysis-agent) | Ask questions about any CSV in plain English | GPT-4o-mini + pandas |
| 4 | [📈 Data Visualisation](#4-data-visualisation-agent) | Describe a chart → get interactive Plotly output | GPT-4o-mini + Plotly |
| 5 | [🛡️ Life Insurance Advisor](#5-life-insurance-advisor-agent) | Personalised coverage recommendation (DIME formula) | GPT-4o-mini |
| 6 | [🏥 Medical Imaging](#6-medical-imaging-agent) | Educational analysis of X-rays, MRIs, CT scans | GPT-4o Vision |
| 7 | [😂 Meme Generator](#7-meme-generator-agent-browser-use) | AI captions + auto-creates meme on imgflip.com | GPT-4o-mini + browser-use |
| 8 | [🎵 Music Generator](#8-music-generator-agent) | Writes lyrics + generates 15-sec instrumental | GPT-4o-mini + MusicGen |
| 9 | [🧠 Reasoning Agent](#9-reasoning-agent) | Step-by-step chain-of-thought problem solver | GPT-4o-mini / o1-mini |
| 10 | [🚀 Startup Trend Analysis](#10-startup-trend-analysis-agent) | Market research report with web search | GPT-4o-mini + Tavily |
| 11 | [✈️ Travel Agent](#11-travel-agent) | Full day-by-day itinerary + budget breakdown | GPT-4o-mini |
| 12 | [🤖 Mixture of Agents](#12-mixture-of-agents) | 4 parallel specialists + 1 synthesiser | AsyncOpenAI |
| 13 | [🖼️ Multimodal Agent](#13-multimodal-ai-agent) | Chat with text + images together | GPT-4o Vision |
| 14 | [🔬 Research Agent](#14-openai-research-agent) | Web-searched research briefs (3 depth levels) | OpenAI Responses API |
| 15 | [🕷️ Web Scraping Agent](#15-web-scraping-agent) | Scrape any URL, extract data in plain English | GPT-4o-mini + BS4 |
| 16 | [💹 xAI Finance Agent](#16-xai-finance-agent) | Stock & market analysis with Grok / GPT-4o-mini | xAI Grok |

---

## ⚡ Quickstart (any agent)

```bash
# 1. Clone the repo
git clone https://github.com/MadanMohan0537/starter-ai-agents.git
cd starter-ai-agents

# 2. Go into any agent folder
cd ai_travel_agent

# 3. Create a virtual environment
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up your API key
cp ../.env.example .env   # then edit .env and add OPENAI_API_KEY

# 6. Run
python agent.py
```

That's it. Every agent follows the exact same pattern.

---

## 🗂️ Repository Structure

```
starter-ai-agents/
│
├── .env.example                        ← Shared API key template
├── .gitignore
├── README.md                           ← This file
│
├── ai_blog_to_podcast_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_breakup_recovery_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_data_analysis_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_data_visualisation_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_life_insurance_advisor_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_medical_imaging_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_meme_generator_agent_browseruse/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_music_generator_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_reasoning_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_startup_trend_analysis_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── ai_travel_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── mixture_of_agents/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── multimodal_ai_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── openai_research_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
├── web_scraping_ai_agent/
│   ├── agent.py
│   ├── requirements.txt
│   └── README.md
│
└── xai_finance_agent/
    ├── agent.py
    ├── requirements.txt
    └── README.md
```

---

## 🔑 API Keys Reference

| Key | Where to get it | Used by |
|-----|----------------|---------|
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com/api-keys) | 14 of 16 agents |
| `XAI_API_KEY` | [console.x.ai](https://console.x.ai) | xai_finance_agent (optional) |
| `REPLICATE_API_TOKEN` | [replicate.com/account](https://replicate.com/account) | ai_music_generator_agent (optional) |
| `TAVILY_API_KEY` | [tavily.com](https://tavily.com) | ai_startup_trend_analysis_agent (optional) |

Most agents only need `OPENAI_API_KEY`. Optional keys unlock extra capabilities.

---

## 📖 Agent Details

### 1. Blog to Podcast Agent
**Folder:** `ai_blog_to_podcast_agent`

Scrapes any blog URL → GPT-4o-mini writes a conversational 3-minute podcast script → OpenAI TTS converts it to `podcast.mp3`.

Perfect for: content creators who want audio versions of written articles.

---

### 2. Breakup Recovery Agent
**Folder:** `ai_breakup_recovery_agent`

An empathetic conversational companion using CBT and positive psychology techniques. Validates emotions, asks thoughtful questions, and suggests one concrete recovery micro-action per turn.

---

### 3. Data Analysis Agent
**Folder:** `ai_data_analysis_agent`

Load any CSV and ask data questions in plain English. The agent generates pandas code, executes it, and explains the result. Like having a junior data analyst on demand.

---

### 4. Data Visualisation Agent
**Folder:** `ai_data_visualisation_agent`

Describe the chart you want, get an interactive Plotly chart in your browser. "Bar chart of sales by region sorted descending" → working chart in 5 seconds.

---

### 5. Life Insurance Advisor Agent
**Folder:** `ai_life_insurance_advisor_agent`

Collects your profile (age, income, dependants, health) and applies the DIME formula to recommend policy type, coverage amount, and premium range. Educational only.

---

### 6. Medical Imaging Agent
**Folder:** `ai_medical_imaging_agent`

GPT-4o Vision analyses medical images: identifies modality and body region, describes anatomy, notes findings, and provides educational takeaways. **Not a diagnostic tool.**

---

### 7. Meme Generator Agent (Browser Use)
**Folder:** `ai_meme_generator_agent_browseruse`

GPT-4o-mini picks the meme template and writes captions. `browser-use` then autonomously navigates imgflip.com and creates the meme. Combines LLM + browser automation.

---

### 8. Music Generator Agent
**Folder:** `ai_music_generator_agent`

Enter a mood, genre, and theme → get AI lyrics + a 15-second AI-generated instrumental via Replicate's MusicGen model.

---

### 9. Reasoning Agent
**Folder:** `ai_reasoning_agent`

Solves complex problems (math, logic, code, science) with a fully visible chain-of-thought: break down → verify → answer. Optionally uses `o1-mini` for deeper reasoning.

---

### 10. Startup Trend Analysis Agent
**Folder:** `ai_startup_trend_analysis_agent`

Enter a market sector, get a 6-section trend report: market size, top trends, competitive landscape, white-space opportunities, risks, and recommended startup focus areas.

---

### 11. Travel Agent
**Folder:** `ai_travel_agent`

Personalised day-by-day itinerary for any destination: activities, accommodation, food, transport, budget breakdown, cultural tips, and packing list.

---

### 12. Mixture of Agents
**Folder:** `mixture_of_agents`

4 specialist agents (Analytical, Creative, Devil's Advocate, Practical) answer in parallel via `asyncio`. A coordinator synthesises all four into one superior response.

---

### 13. Multimodal AI Agent
**Folder:** `multimodal_ai_agent`

Conversational agent that understands text + images together. Pass one or more image paths per turn. Supports follow-up questions with full conversation memory.

---

### 14. OpenAI Research Agent
**Folder:** `openai_research_agent`

Uses OpenAI's native `web_search_preview` tool to research any topic. Three depth levels: quick (bullets) / standard (400 words) / deep (800 words).

---

### 15. Web Scraping Agent
**Folder:** `web_scraping_ai_agent`

Scrape any URL, then ask extraction questions in plain English. "List all pricing tiers" or "What are the top headlines?" — the agent extracts exactly what you need.

---

### 16. xAI Finance Agent
**Folder:** `xai_finance_agent`

Conversational finance analyst powered by xAI's Grok (falls back to GPT-4o-mini). Stock analysis, macro trends, earnings interpretation, risk management — with conversation memory.

---

## 🧠 Design Principles

Every agent in this collection follows the same three principles:

**1. Single file, single responsibility**
Each agent is one `agent.py` file. No complex architectures. You can read and understand any agent in 5 minutes.

**2. Graceful degradation**
Optional API keys (Replicate, Tavily, xAI) degrade gracefully — the agent still runs and tells you what's missing.

**3. Easy to extend**
The simplest extension to any agent is adding a new system prompt variant or chaining two agents together. Start here and build up.

---

## 📚 Learning Path

If you're new to AI agents, start in this order:

1. `ai_reasoning_agent` — learn how system prompts shape behaviour
2. `ai_travel_agent` — learn structured output from LLMs
3. `ai_data_analysis_agent` — learn code generation + execution
4. `mixture_of_agents` — learn parallel calls with asyncio
5. `ai_blog_to_podcast_agent` — learn multi-step pipelines
6. `ai_meme_generator_agent_browseruse` — learn browser automation

---

## 🙏 Credits

Built on top of the original [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) collection by [@Shubhamsaboo](https://github.com/Shubhamsaboo). This repo recreates all 16 starter agents with clean, modular, well-commented code.

---

## 📄 License

MIT — free to use, fork, and build upon.
