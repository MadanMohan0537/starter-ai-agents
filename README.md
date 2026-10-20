# Starter AI Agents

**Sixteen small Python examples of LLM "agent" patterns, such as a prompted itinerary, CSV question answering, parallel specialist calls, and browser automation. Each example lives in its own folder with its own `requirements.txt`. This is learning work.**

## Upstream attribution

These examples follow the **starter agents** in [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) by [@Shubhamsaboo](https://github.com/Shubhamsaboo). That project is Apache-2.0. The folder names here match sixteen directories under [`starter_ai_agents/`](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents). Upstream also has `ai_x402_paying_agent`, which this repo does not include.

This repo is a separate project. GitHub does not mark it as a fork, and the git history starts at the initial import of these scripts. Upstream entry points use other filenames (for example `travel_agent.py`, and a Streamlit command in the upstream README). The files here are separate `agent.py` scripts on the OpenAI Python SDK. They were not compared line by line with the upstream sources.

## Problem and who it's for

Large frameworks can hide the basic steps of an LLM application: the prompt, the client call, and the bit of code that turns the reply into something you can read. This repo is for someone who wants to read and run one small example at a time, including people who are not professional engineers.

## Approach

- One folder per example: `agent.py`, `requirements.txt`, and a short README. There is no shared Python package. The shared setup file is the root `.env.example`.
- Every example imports the OpenAI Python SDK and calls `load_dotenv()`. With no path argument, that searches for `.env` starting in the script's directory and then in parent directories.
- The usual chat model is `gpt-4o-mini`. The vision examples (`ai_medical_imaging_agent`, `multimodal_ai_agent`) call `gpt-4o`.
- Other model strings in the code: `tts-1` for blog audio, optional `o1-mini` in the reasoning example, and `grok-beta` in the finance example when `XAI_API_KEY` is set.
- `REPLICATE_API_TOKEN`, `TAVILY_API_KEY`, and `XAI_API_KEY` are read from the environment. A missing key is handled differently in each example (see the table and Limitations). A missing `OPENAI_API_KEY` is not checked before the client is constructed.

| # | Folder | What the script does |
|---|---|---|
| 1 | `ai_blog_to_podcast_agent` | Fetch paragraph text with BeautifulSoup, ask `gpt-4o-mini` for a podcast script, write `podcast.mp3` with OpenAI TTS (`tts-1`, voice `alloy`) |
| 2 | `ai_breakup_recovery_agent` | Multi-turn chat. One system prompt sets a supportive-coach persona |
| 3 | `ai_data_analysis_agent` | Load a CSV with pandas, ask `gpt-4o-mini` for pandas code, run it with `exec()`, then ask the model to explain `result` |
| 4 | `ai_data_visualisation_agent` | From a CSV and a chart description, generate Plotly code, run it with `exec()`, and call `fig.show()` |
| 5 | `ai_life_insurance_advisor_agent` | Fixed questionnaire. The system prompt tells the model to estimate coverage and names DIME as an example formula. The script does not calculate DIME itself |
| 6 | `ai_medical_imaging_agent` | Send a local image to `gpt-4o`. The system prompt requires an educational disclaimer and says the reply is not a diagnosis |
| 7 | `ai_meme_generator_agent_browseruse` | `gpt-4o-mini` returns caption JSON. `browser-use` plus `langchain-openai` then drives imgflip. If `browser-use` cannot be imported, the script prints the captions |
| 8 | `ai_music_generator_agent` | `gpt-4o-mini` writes lyrics and a MusicGen prompt. Audio is a Replicate HTTP call (15 seconds) and runs only when `REPLICATE_API_TOKEN` is set |
| 9 | `ai_reasoning_agent` | Default path sends a step-by-step system prompt to `gpt-4o-mini`. Answering `y` switches to `o1-mini` and sends only the user message |
| 10 | `ai_startup_trend_analysis_agent` | Two Tavily searches, then a `gpt-4o-mini` report. With no `TAVILY_API_KEY`, each search returns one placeholder result and the OpenAI call still runs |
| 11 | `ai_travel_agent` | Five prompts, then one `gpt-4o-mini` reply. The system prompt asks for a day-by-day itinerary. The script prints that text and does not parse a schema |
| 12 | `mixture_of_agents` | Four specialists (Analytical, Creative, Devil's Advocate, Practical) via `AsyncOpenAI` and `asyncio.gather`, then one synthesizer call. All use `gpt-4o-mini` |
| 13 | `multimodal_ai_agent` | Chat loop. Each turn can include text and local image paths, sent to `gpt-4o`. History stays in memory for that process |
| 14 | `openai_research_agent` | `client.responses.create` with tool `web_search_preview` and model `gpt-4o-mini`. The strings `quick`, `standard`, and `deep` select length instructions (3 bullets, about 400 words, about 800 words). Any other string makes the instruction the single word `standard` |
| 15 | `web_scraping_ai_agent` | `requests` plus BeautifulSoup, then `gpt-4o-mini` answers a plain-English extraction question about that page |
| 16 | `xai_finance_agent` | With `XAI_API_KEY`, chat goes to `https://api.x.ai/v1` with model `grok-beta`. With no xAI key, the script builds a normal OpenAI client and uses `gpt-4o-mini` |

## What exists today

Checked by reading the files in this repository. None of the examples were executed for this README.

- All sixteen folders above, each with `agent.py`, `requirements.txt`, and a README.
- Root files: `.env.example`, `.gitignore`, and this README. `.env.example` lists `OPENAI_API_KEY`, `XAI_API_KEY`, `REPLICATE_API_TOKEN`, and `TAVILY_API_KEY`.
- No sample CSV, image, or audio file is in the repo. `ai_data_analysis_agent` and `ai_data_visualisation_agent` default to `data.csv`. `ai_medical_imaging_agent` defaults to `sample.jpg` and exits when that path is missing.
- No tests, no CI configuration, no `LICENSE`, and no `NOTICE`.
- `ai_x402_paying_agent` exists upstream and is not in this repo. Nothing in this repo implements it.

## How success would be measured

**Not yet measured.** The repo has no run logs, test results, or usage numbers. A reasonable bar for each example would be: from a clean virtual environment, following only that folder's README, the script starts and finishes one prompt with a real API key. Nothing in the repo records that check, and the examples were not run while this README was written.

## Limitations

- **Generated code is executed.** `ai_data_analysis_agent` and `ai_data_visualisation_agent` pass model-written Python to `exec()`. Use a CSV you trust, in a throwaway environment.
- Model calls cost money on your provider account. This README does not record prices.
- Replies from the travel, finance, insurance, and medical examples are model text. The medical script's prompt says the analysis is educational and is not a diagnosis. The insurance script prints a line telling you to consult a licensed advisor. The finance prompt says the reply is not financial advice.
- Optional keys do not share one failure mode. The music script prints a warning and skips audio when `REPLICATE_API_TOKEN` is unset. The startup script substitutes a placeholder search result when `TAVILY_API_KEY` is unset. The finance script changes client and model when `XAI_API_KEY` is unset and does not print a missing-key line. None of the scripts print a dedicated error when `OPENAI_API_KEY` is unset.
- The meme folder README tells you to run `playwright install chromium`. That command is not in `requirements.txt`.
- Every dependency line uses a lower bound (`>=`). The research script calls `client.responses.create`. Its requirement is only `openai>=1.0.0`, which does not record the SDK release that added that method.
- `load_dotenv()` looks for `.env` from the script directory upward. The quick start copies `.env` into the example folder and runs `python agent.py` from that folder.
- **There is no license file in this repo.** The upstream project is Apache-2.0. This repo does not yet include an Apache-2.0 `LICENSE` or a `NOTICE` crediting upstream.

## Quick start

The music example uses the annotation `str | None`, which needs Python 3.10 or newer. No file in the repo pins the interpreter.

The travel example only needs `OPENAI_API_KEY`. It prompts in the terminal. The commands below were not run while this README was written.

```bash
git clone https://github.com/MadanMohan0537/starter-ai-agents.git
cd starter-ai-agents/ai_travel_agent
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example .env                             # then set OPENAI_API_KEY
python agent.py
```

For any other example, read that folder's README first. Some need another key, a CSV or image you supply, or an extra tool.

Suggested reading order: `ai_reasoning_agent` → `ai_travel_agent` → `ai_data_analysis_agent` → `mixture_of_agents` → `ai_blog_to_podcast_agent` → `ai_meme_generator_agent_browseruse`.

## License

No `LICENSE` file is included yet (see Limitations). Upstream: [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps), Apache-2.0.
