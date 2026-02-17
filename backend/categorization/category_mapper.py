def get_category(merchant: str) -> str:
    """
    Map merchant name to expense category.
    """

    merchant = merchant.lower()

    if merchant in ["swiggy", "zomato", "bigbasket"]:
        return "Food"
    elif merchant in ["uber", "ola", "irctc"]:
        return "Transport"
    elif merchant in ["amazon", "flipkart", "myntra", "reliance"]:
        return "Shopping"
    elif merchant in ["netflix", "spotify", "amazonprime"]:
        return "Entertainment"
    elif merchant in ["airtel", "jio", "bses", "tatapower"]:
        return "Utilities"
    elif merchant in ["salary", "cashback", "refund"]:
        return "Income"
    else:
        return "Others"
