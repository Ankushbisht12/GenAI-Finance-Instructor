import csv
from collections import defaultdict


def analyze_spending(csv_file_path: str, month: str = None) -> dict:
    total_income = 0
    total_expense = 0
    category_expense = defaultdict(int)
    transaction_count = 0

    with open(csv_file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            date = row["date"]  # format: 01-09-2025

            if month:
                if f"-{month}-" not in date:
                    continue

            amount = int(row["amount"])
            tx_type = row["type"]
            category = row["category"]

            transaction_count += 1

            if tx_type == "Credited":
                total_income += amount
            elif tx_type == "Debited":
                total_expense += amount
                category_expense[category] += amount

    savings = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "savings": savings,
        "category_expense": dict(category_expense),
        "transaction_count": transaction_count
    }
