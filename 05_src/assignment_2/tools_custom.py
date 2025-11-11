# --- tools_custom.py ---
# This tool uses the OpenAI API to explain finance or tech terms
# in simple, beginner-friendly language.

from openai import OpenAI
import os

# Load your API key (from .secrets_f or environment)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_simple(concept: str) -> str:
    """
    Explain a finance or tech concept in plain, beginner-friendly language.
    The model keeps the answer short and easy to understand.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a patient financial educator who explains "
                    "complex ideas simply, using short sentences and no jargon."
                ),
            },
            {
                "role": "user",
                "content": f"Explain {concept} in simple, clear terms. Keep it under 80 words."
            },
        ],
    )
    return response.choices[0].message.content.strip()
