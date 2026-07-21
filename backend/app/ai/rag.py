import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-lite")  # or "gemini-2.0" for the full model


def generate_answer(question: str, context: str):

    prompt = f"""
You are an AI assistant.

Answer ONLY using the provided context.

If the answer is not present, say:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text