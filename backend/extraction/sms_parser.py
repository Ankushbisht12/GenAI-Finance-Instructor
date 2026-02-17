from backend.extraction.regex_patterns import (
    AMOUNT_PATTERN,
    TRANSACTION_TYPE_PATTERN,
    DATE_PATTERN,
    MERCHANT_PATTERN,
    BALANCE_PATTERN
)


def parse_single_sms(sms_text: str) -> dict:
    """
    Parse a single bank SMS and extract transaction details.
    """

    amount_match = AMOUNT_PATTERN.search(sms_text)
    type_match = TRANSACTION_TYPE_PATTERN.search(sms_text)
    date_match = DATE_PATTERN.search(sms_text)
    merchant_match = MERCHANT_PATTERN.search(sms_text)
    balance_match = BALANCE_PATTERN.search(sms_text)

    transaction = {
        "amount": int(amount_match.group(1)) if amount_match else None,
        "type": type_match.group(1).capitalize() if type_match else None,
        "date": date_match.group(1) if date_match else None,
        "merchant": merchant_match.group(1).capitalize() if merchant_match else "Unknown",
        "balance": int(balance_match.group(1)) if balance_match else None
    }

    return transaction


def parse_sms_file(file_path: str) -> list:
    """
    Parse an SMS text file and return list of transactions.
    """

    transactions = []

    with open(file_path, "r") as file:
        for line in file:
            sms = line.strip()
            if sms:
                transactions.append(parse_single_sms(sms))

    return transactions
