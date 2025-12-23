import pandas as pd


def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    """
    Find customers who meet all criteria for being "golden hour customers":
    1. At least 3 orders
    2. At least 60% of orders during peak hours (11:00-14:00 or 18:00-21:00)
    3. Average rating >= 4.0 for rated orders
    4. At least 50% of orders rated
    """
    restaurant_orders.order_timestamp = pd.to_datetime(
        restaurant_orders.order_timestamp
    )

    df = (
        restaurant_orders.groupby("customer_id")
        .agg(
            total_orders=("order_id", "count"),
            peak_hour_orders=(
                "order_timestamp",
                lambda x: (
                    ((x.dt.hour >= 11) & (x.dt.hour < 14))
                    | ((x.dt.hour >= 18) & (x.dt.hour < 21))
                ).sum(),
            ),
            rated_orders=("order_rating", lambda x: x.notna().sum()),
            avg_rating=("order_rating", "mean"),
        )
        .reset_index()
    )

    # Calculate percentages
    df["peak_hour_percentage"] = (
        df["peak_hour_orders"] * 100.0 / df["total_orders"]
    )
    df["rated_percentage"] = df["rated_orders"] * 100.0 / df["total_orders"]

    # Apply all criteria
    result = df[
        (df["total_orders"] >= 3)  # Constraint 1
        & (df["peak_hour_percentage"] >= 60.0)  # Constraint 2
        & (df["avg_rating"] >= 4.0)  # Constraint 3
        & (df["rated_percentage"] >= 50.0)
    ]  # Constraint 4

    # Format output
    result["peak_hour_percentage"] = result["peak_hour_percentage"].round(0)
    result["average_rating"] = result["avg_rating"].round(2)

    return (
        result[
            ["customer_id", "total_orders", "peak_hour_percentage", "average_rating"]
        ]
        .sort_values(["average_rating", "customer_id"], ascending=[False, False])
        .reset_index(drop=True)
    )
