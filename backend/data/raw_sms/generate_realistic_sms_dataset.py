from datetime import datetime, timedelta

START_BALANCE = 12000
ACCOUNT = "XX2345"

MERCHANTS = {
    "Food": ["SWIGGY", "ZOMATO"],
    "Transport": ["UBER"],
    "Shopping": ["AMAZON", "FLIPKART"],
    "Entertainment": ["NETFLIX", "SPOTIFY"],
    "Utilities": ["AIRTEL", "JIO"],
    "Groceries": ["BIGBASKET"]
}

SUBSCRIPTIONS = {
    "NETFLIX": 299,
    "SPOTIFY": 299
}

SALARY_AMOUNT = 45000
RENT_AMOUNT = 12000


def format_date(date):
    return date.strftime("%d-%m-%Y")


def debit(balance, amount, date, merchant):
    balance -= amount
    if balance < 0:
        balance = 0
    sms = f"Rs.{amount} debited from A/c {ACCOUNT} on {format_date(date)} at {merchant}. Avl bal Rs.{balance}"
    return sms, balance


def credit(balance, amount, date, reason):
    balance += amount
    sms = f"Rs.{amount} credited to your A/c {ACCOUNT} on {format_date(date)}. {reason}"
    return sms, balance


def generate_month(month_start_date, balance):
    messages = []
    date = month_start_date

    # Salary
    sms, balance = credit(balance, SALARY_AMOUNT, date, "Salary credited")
    messages.append(sms)

    # Rent (3rd day)
    date += timedelta(days=2)
    sms, balance = debit(balance, RENT_AMOUNT, date, "RENT")
    messages.append(sms)

    # Daily expenses
    for day in range(4, 28):
        date = month_start_date + timedelta(days=day - 1)

        # Food (almost daily)
        sms, balance = debit(balance, 250, date, "SWIGGY")
        messages.append(sms)

        # Transport (weekdays)
        if date.weekday() < 5:
            sms, balance = debit(balance, 120, date, "UBER")
            messages.append(sms)

        # Groceries weekly
        if date.weekday() == 5:
            sms, balance = debit(balance, 1800, date, "BIGBASKET")
            messages.append(sms)

        # Shopping (weekends)
        if date.weekday() == 6:
            sms, balance = debit(balance, 2200, date, "AMAZON")
            messages.append(sms)

    # Subscriptions (end of month)
    for merchant, amount in SUBSCRIPTIONS.items():
        date = month_start_date + timedelta(days=27)
        sms, balance = debit(balance, amount, date, merchant)
        messages.append(sms)

    # Utilities
    date = month_start_date + timedelta(days=25)
    sms, balance = debit(balance, 799, date, "AIRTEL")
    messages.append(sms)

    return messages, balance


def generate_last_4_months():
    today = datetime.today().replace(day=1)
    start_month = today - timedelta(days=120)

    all_messages = []
    balance = START_BALANCE

    for i in range(4):
        month_start = (start_month + timedelta(days=30 * i)).replace(day=1)
        msgs, balance = generate_month(month_start, balance)
        all_messages.extend(msgs)

    return all_messages


if __name__ == "__main__":
    sms_messages = generate_last_4_months()

    with open("sample_sms.txt", "w") as file:
        for msg in sms_messages:
            file.write(msg + "\n")

    print(f"✅ Realistic 4-month SMS dataset generated: {len(sms_messages)} records")
