from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.genai.explanation_engine import (
    generate_general_explanation,
    explain_text,
    answer_question_with_data
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


class QuestionRequest(BaseModel):
    question: str


@app.get("/explain/general")
def explain_general():
    explanation = generate_general_explanation()
    print("Sending to frontend:", explanation)
    return {"response": explanation}


@app.post("/explain/text")
def explain_text_endpoint(request: TextRequest):
    explanation = explain_text(request.text)
    print("Sending to frontend:", explanation)
    return {"response": explanation}


@app.post("/ask")
def ask_question_endpoint(request: QuestionRequest):
    answer = answer_question_with_data(request.question)
    return {"response": answer}