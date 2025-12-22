import pandas as pd


def find_churn_risk_customers(subscription_events: pd.DataFrame) -> pd.DataFrame:
    """
    Find customers at risk of churning.

    A customer is at churn risk if they:
    1. Currently have an active subscription (last event is not cancel)
    2. Have performed at least one downgrade
    3. Current plan revenue < 50% of historical maximum
    4. Have been a subscriber for at least 60 days
    """
    subscription_events.event_date = pd.to_datetime(subscription_events.event_date)

    df = (
        subscription_events.groupby("user_id")
        .agg(
            latest_event=("event_type", "last"),  # Constraint 1
            has_downgrade=(
                "event_type",
                lambda x: "downgrade" in x.values,
            ),  # Constraint 2
            current_monthly_amount=("monthly_amount", "last"),  # Constraint 3
            max_historical_amount=("monthly_amount", "max"),
            days_as_subscriber=(
                "event_date",
                lambda x: (x.max() - x.min()).days,
            ),  # Constraint 4
            current_plan=("plan_name", "last"),
        )
        .reset_index()
    )

    df = df[df.latest_event != "cancel"][  # Constraint 1
        df.has_downgrade == True
    ][  # Constraint 2
        df.current_monthly_amount / df.max_historical_amount <= 0.5
    ][  # Constraint 3
        df.days_as_subscriber >= 60
    ]  # Constraint 4

    return df.sort_values(
        ["days_as_subscriber", "user_id"], ascending=[False, True]
    ).iloc[:, [0, 6, 3, 4, 5]]
