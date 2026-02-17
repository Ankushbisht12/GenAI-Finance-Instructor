# backend/app.py

from pydantic import BaseModel
from typing import List
from backend.analysis.transaction_processor import process_sms_to_csv


# -----------------------------
# Request Models
# -----------------------------

class TextRequest(BaseModel):
    text: str


class QuestionRequest(BaseModel):
    question: str


class SMSBatchRequest(BaseModel):
    messages: List[str]


# -----------------------------
# Business Logic Wrapper
# -----------------------------

def process_sms_batch(messages: List[str]):
    """
    Takes list of SMS strings,
    processes them into structured transactions,
    and saves to CSV.
    """
    return process_sms_to_csv(messages)
