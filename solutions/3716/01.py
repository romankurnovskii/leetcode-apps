# SQL solution wrapped in Python for frontend display
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
    query = """
    WITH query_cte AS (
        SELECT 
            user_id, 
            event_date, 
            MAX(event_date) OVER(PARTITION BY user_id) max_event_date, 
            event_type, 
            plan_name current_plan, 
            monthly_amount,
            MAX(monthly_amount) OVER(PARTITION BY user_id) max_historical_amount,
            DATEDIFF(MAX(event_date) OVER(PARTITION BY user_id), MIN(event_date) OVER(PARTITION BY user_id)) days_as_subscriber
        FROM subscription_events
    )
    SELECT 
        user_id, 
        current_plan, 
        monthly_amount current_monthly_amount, 
        max_historical_amount, 
        days_as_subscriber
    FROM query_cte q
    WHERE event_date = max_event_date 
        AND monthly_amount > 0  -- Active subscription (not cancelled)
        AND EXISTS (
            SELECT 1 
            FROM query_cte q1 
            WHERE q.user_id = q1.user_id 
                AND q1.event_type = 'downgrade'
        )
        AND days_as_subscriber >= 60 
        AND monthly_amount / CAST(max_historical_amount AS FLOAT) < 0.5 
    ORDER BY days_as_subscriber DESC, user_id
    """
    # Note: This is a SQL solution. In actual LeetCode environment, 
    # this would be executed as raw SQL, not via pandas
    return pd.read_sql(query, con=None)  # Placeholder - actual execution depends on LeetCode environment

