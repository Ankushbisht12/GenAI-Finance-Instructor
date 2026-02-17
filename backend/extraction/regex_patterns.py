import re

# Matches amount like Rs.4500 or Rs4500
AMOUNT_PATTERN = re.compile(r"Rs\.?\s?(\d+)")

# Matches debit or credit keywords
TRANSACTION_TYPE_PATTERN = re.compile(r"\b(debited|credited)\b", re.IGNORECASE)

# Matches date format: 12-03-2024
DATE_PATTERN = re.compile(r"on (\d{2}-\d{2}-\d{4})")

# Matches merchant name after 'at'
MERCHANT_PATTERN = re.compile(r"at ([A-Z]+)")

# Matches available balance (optional but useful later)
BALANCE_PATTERN = re.compile(r"Avl bal Rs\.?(\d+)")
