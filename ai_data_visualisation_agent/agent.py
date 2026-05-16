"""
AI Data Visualisation Agent
Describe the chart you want in plain English and the agent creates it
from your CSV using Plotly.
"""

import os
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"✅ Loaded: {df.shape[0]} rows × {df.shape[1]} cols | Columns: {list(df.columns)}\n")
    return df


def generate_plot_code(request: str, df_info: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a data visualisation expert. Given a DataFrame `df` already in memory, "
                    "write Python code using plotly.express (imported as `px`) or plotly.graph_objects (as `go`) "
                    "to create the requested chart. Store the figure in a variable called `fig`. "
                    "Return ONLY Python code — no markdown, no explanation."
                ),
            },
            {
                "role": "user",
                "content": f"DataFrame info:\n{df_info}\n\nChart request: {request}",
            },
        ],
    )
    return response.choices[0].message.content.strip()


def execute_and_show(code: str, df: pd.DataFrame) -> None:
    local_vars = {"df": df, "pd": pd, "px": px, "go": go}
    exec(code, {}, local_vars)  # noqa: S102
    fig = local_vars.get("fig")
    if fig:
        fig.show()
    else:
        print("⚠️  No `fig` variable found in generated code.")


def run(csv_path: str) -> None:
    df = load_csv(csv_path)
    df_info = f"Columns: {list(df.columns)}\nDtypes:\n{df.dtypes.to_string()}\nSample:\n{df.head(3).to_string()}"

    print("Describe the chart you want. Type 'quit' to exit.\n")
    while True:
        request = input("📈 Chart request: ").strip()
        if request.lower() in {"quit", "exit"}:
            break
        if not request:
            continue

        code = generate_plot_code(request, df_info)
        print(f"\n🐍 Generated code:\n{code}\n")
        try:
            execute_and_show(code, df)
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    run(path)
