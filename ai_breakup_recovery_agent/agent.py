"""
AI Breakup Recovery Agent
An empathetic conversational agent that helps users process a breakup,
offers emotional support, reframing exercises, and actionable recovery steps.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a compassionate, non-judgmental breakup recovery coach with a background
in positive psychology and cognitive behavioural therapy.

Your role:
- Listen actively and validate the user's feelings
- Ask thoughtful follow-up questions to help them process emotions
- Gently introduce reframing techniques when appropriate
- Suggest one concrete micro-action per conversation turn (journaling prompt,
  self-care activity, social connection, etc.)
- Never minimise pain or rush the healing process
- Remind users you are an AI and encourage professional support when needed

Tone: warm, calm, honest, encouraging — like a wise friend, not a therapist.
"""


def chat(history: list[dict]) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
        temperature=0.7,
    )
    return response.choices[0].message.content


def run() -> None:
    print("💔 AI Breakup Recovery Agent")
    print("Type 'quit' to exit.\n")
    print("Hi, I'm here for you. Would you like to tell me a little about what happened?\n")

    history = []
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit", "bye"}:
            print("\nAgent: Take care of yourself. Healing takes time — be patient with yourself. 💙")
            break
        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})
        reply = chat(history)
        history.append({"role": "assistant", "content": reply})
        print(f"\nAgent: {reply}\n")


if __name__ == "__main__":
    run()
