"""
Web Scraping AI Agent
Autonomously scrapes a website, extracts structured data, and answers
questions about the scraped content.
"""

import os
import sys
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def scrape_url(url: str, max_chars: int = 12000) -> dict:
    """Scrape a URL and return structured content."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; AIScraperBot/1.0)"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        return {"error": str(e), "url": url}

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else "No title"
    text = " ".join(soup.get_text(separator=" ").split())[:max_chars]

    links = [{"text": a.get_text(strip=True), "href": a.get("href", "")}
             for a in soup.find_all("a", href=True)[:20]]

    return {"url": url, "title": title, "text": text, "links": links}


def extract_structured_data(content: dict, extraction_goal: str) -> str:
    """Use LLM to extract structured data from scraped content."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a web data extraction specialist. "
                    "Extract the requested information from the scraped web content. "
                    "Return well-structured, clean data. If the information isn't present, say so clearly."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"URL: {content.get('url')}\n"
                    f"Page title: {content.get('title')}\n\n"
                    f"Page content:\n{content.get('text', '')}\n\n"
                    f"Extraction goal: {extraction_goal}"
                ),
            },
        ],
    )
    return response.choices[0].message.content


def run() -> None:
    print("🕷️  Web Scraping AI Agent\n")
    url = input("URL to scrape: ").strip()
    if not url:
        url = "https://news.ycombinator.com"

    if not url.startswith("http"):
        url = "https://" + url

    print(f"\n🌐 Scraping: {url}...")
    content = scrape_url(url)

    if "error" in content:
        print(f"❌ Scraping failed: {content['error']}")
        return

    print(f"✅ Scraped: '{content['title']}' ({len(content['text'])} chars)\n")

    print("Ask questions about this page. Type 'quit' to exit.\n")
    while True:
        goal = input("❓ What do you want to extract or know? ").strip()
        if goal.lower() in {"quit", "exit"}:
            break
        if not goal:
            continue

        result = extract_structured_data(content, goal)
        print(f"\n📋 Result:\n{result}\n")


if __name__ == "__main__":
    url_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    run()
