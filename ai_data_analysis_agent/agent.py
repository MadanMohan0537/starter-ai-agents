"""
AI Data Analysis Agent
Upload any CSV and ask questions in plain English.
The agent writes and executes Python/pandas code to answer your question.
"""

import os
import io
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"✅ Loaded {len(df)} rows × {len(df.columns)} columns")
    print(f"   Columns: {list(df.columns)}\n")
    return df


def describe_dataframe(df: pd.DataFrame) -> str:
    buf = io.StringIO()
    df.info(buf=buf)
    return f"Shape: {df.shape}\nColumns: {list(df.columns)}\nDtypes:\n{buf.getvalue()}\nSample:\n{df.head(3).to_string()}"


def generate_code(question: str, df_description: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior data analyst. Given a DataFrame `df` already loaded in memory, "
                    "write concise Python/pandas code to answer the user's question. "
                    "Store the final answer in a variable called `result`. "
                    "Return ONLY the Python code — no markdown, no explanation."
                ),
            },
            {
                "role": "user",
                "content": f"DataFrame info:\n{df_description}\n\nQuestion: {question}",
            },
        ],
    )
    return response.choices[0].message.content.strip()


def execute_code(code: str, df: pd.DataFrame) -> str:
    local_vars = {"df": df, "pd": pd}
    try:
        exec(code, {}, local_vars)  # noqa: S102
        result = local_vars.get("result", "Code ran but no `result` variable was set.")
        return str(result)
    except Exception as e:
        return f"Error executing code: {e}"


def explain_result(question: str, result: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a data analyst. Explain this result clearly in 1–3 sentences."},
            {"role": "user", "content": f"Question: {question}\nResult: {result}"},
        ],
    )
    return response.choices[0].message.content


def run(csv_path: str) -> None:
    df = load_csv(csv_path)
    df_desc = describe_dataframe(df)

    print("Ask questions about your data. Type 'quit' to exit.\n")
    while True:
        question = input("❓ Question: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        if not question:
            continue

        code = generate_code(question, df_desc)
        print(f"\n🐍 Generated code:\n{code}\n")

        raw_result = execute_code(code, df)
        explanation = explain_result(question, raw_result)

        print(f"📊 Result: {raw_result}")
        print(f"💡 Insight: {explanation}\n")


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    run(path)
