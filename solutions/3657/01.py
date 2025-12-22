import pandas as pd


def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Find loyal customers who meet all criteria:
    1. At least 3 purchase transactions
    2. Active for at least 30 days
    3. Refund rate < 20%
    """
    customer_transactions.transaction_date = pd.to_datetime(
        customer_transactions.transaction_date
    )

    df = (
        customer_transactions.groupby("customer_id")
        .agg(
            purchase_count=(
                "transaction_type",
                lambda x: (x == "purchase").sum(),
            ),  # Constraint 1
            total_transactions=("transaction_type", "count"),
            refund_count=(
                "transaction_type",
                lambda x: (x == "refund").sum(),
            ),
            days_active=(
                "transaction_date",
                lambda x: (x.max() - x.min()).days,
            ),  # Constraint 2
        )
        .reset_index()
    )

    # Calculate refund rate
    df["refund_rate"] = df["refund_count"] / df["total_transactions"]

    # Apply all criteria
    result = df[
        (df["purchase_count"] >= 3)  # Constraint 1
        & (df["days_active"] >= 30)  # Constraint 2
        & (df["refund_rate"] < 0.20)
    ]  # Constraint 3

    return result[["customer_id"]].sort_values("customer_id").reset_index(drop=True)
