from google import genai
from backend.config.settings import GEMINI_API_KEY
from backend.genai.prompt_templates import (
    GENERAL_EXPLANATION_PROMPT,
    TEXT_EXPLANATION_TEMPLATE,
)
from backend.analysis.spending_analysis import analyze_spending
import re

print("Loaded API KEY:", GEMINI_API_KEY)

client = genai.Client(api_key=GEMINI_API_KEY)


def _generate(prompt: str):
    try:
        print("Sending request to Gemini...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if hasattr(response, "text") and response.text:
            return response.text

        if hasattr(response, "candidates") and response.candidates:
            candidate = response.candidates[0]
            if candidate.content and candidate.content.parts:
                return candidate.content.parts[0].text

        return "Gemini returned empty response."

    except Exception as e:
        print("ERROR:", str(e))
        return f"Gemini API Error: {str(e)}"


# ===============================
# General Advice
# ===============================
def generate_general_explanation():
    return _generate(GENERAL_EXPLANATION_PROMPT)


# ===============================
# Explain Text
# ===============================
def explain_text(text: str):
    return _generate(TEXT_EXPLANATION_TEMPLATE.format(text=text))


MONTH_MAP = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12",
}

def detect_month(question: str):
    question = question.lower()
    for month_name, month_number in MONTH_MAP.items():
        if month_name in question:
            return month_number
    return None

# ===============================
# Ask Question Using REAL SMS DATA
# ===============================
def answer_question_with_data(question: str):
    try:
        csv_path = "backend/data/processed/transactions.csv"

        month = detect_month(question)

        analysis_result = analyze_spending(csv_path, month)

        summary_text = f"""
All amounts are in Indian Rupees (₹).

Total Income: ₹{analysis_result['total_income']}
Total Expense: ₹{analysis_result['total_expense']}
Savings: ₹{analysis_result['savings']}
Category Expenses: {analysis_result['category_expense']}
"""

        full_prompt = f"""
You are a financial assistant.
Use the real transaction data below to answer the question.

{summary_text}

Question: {question}
"""

        return _generate(full_prompt)

    except Exception as e:
        return f"Data Processing Error: {str(e)}"

