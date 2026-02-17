import csv
import os

from backend.extraction.sms_parser import parse_sms_file
from backend.categorization.category_mapper import get_category


def process_sms_to_csv(
    sms_file_path: str,
    output_csv_path: str
):
    """
    Convert raw SMS file into structured transaction CSV.
    """

    transactions = parse_sms_file(sms_file_path)

    # ✅ FORCE create output directory
    output_dir = os.path.dirname(output_csv_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_csv_path, "w", newline="") as csvfile:
        fieldnames = [
            "date",
            "type",
            "merchant",
            "category",
            "amount",
            "balance"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for tx in transactions:
            writer.writerow({
                "date": tx["date"],
                "type": tx["type"],
                "merchant": tx["merchant"],
                "category": get_category(tx["merchant"]),
                "amount": tx["amount"],
                "balance": tx["balance"]
            })
