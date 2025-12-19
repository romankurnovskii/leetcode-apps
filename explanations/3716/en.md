## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find customers at risk of churning based on their subscription history. A customer is at churn risk if they: (1) currently have an active subscription (last event is not cancel), (2) have performed at least one downgrade, (3) their current monthly amount is less than 50% of their historical maximum, and (4) have been a subscriber for at least 60 days.

**1.1 Constraints & Complexity:**

- **Input Size:** The subscription_events table can have many rows per user, with multiple events over time.
- **Time Complexity:** O(n log n) where n is the number of events - window functions require sorting, and the EXISTS clause checks for downgrades.
- **Space Complexity:** O(n) for the CTE that stores window function results.
- **Edge Case:** A user who cancels and then starts again should only be considered based on their current active subscription period.

**1.2 High-level approach:**

The goal is to use window functions to compute aggregate statistics (max event date, max monthly amount, subscription duration) for each user, then filter based on the churn risk criteria.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use multiple subqueries or self-joins to compute max dates, max amounts, and check for downgrades separately for each user. This would be O(n^2) in worst case.
- **Optimized Strategy:** Use window functions (MAX() OVER()) to compute all aggregates in a single pass, then filter in the WHERE clause. This is O(n log n) due to window function sorting.
- **Optimization:** Window functions allow us to compute multiple aggregates simultaneously without multiple table scans, and the EXISTS clause efficiently checks for downgrade events.

**1.4 Decomposition:**

1. Create a CTE that computes window functions for each event: max event date, max monthly amount, and subscription duration (max date - min date).
2. Filter to only the most recent event for each user (where event_date = max_event_date).
3. Apply churn risk criteria: active subscription, has downgrade, current amount < 50% of max, duration >= 60 days.
4. Order results by days_as_subscriber DESC, then user_id ASC.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's consider a user with events:
- 2024-01-01: start premium ($29.99)
- 2024-02-15: downgrade standard ($19.99)
- 2024-03-20: downgrade basic ($9.99)

**2.2 Start Processing:**

The CTE computes for each row:
- `max_event_date`: 2024-03-20 (for all rows of this user)
- `max_historical_amount`: $29.99 (for all rows)
- `days_as_subscriber`: 79 days (2024-03-20 - 2024-01-01)

**2.3 Trace Walkthrough:**

| user_id | event_date | max_event_date | event_type | monthly_amount | max_historical_amount | days_as_subscriber | Keep? |
|---------|------------|----------------|------------|----------------|----------------------|-------------------|-------|
| 501 | 2024-01-01 | 2024-03-20 | start | 29.99 | 29.99 | 79 | No (not latest) |
| 501 | 2024-02-15 | 2024-03-20 | downgrade | 19.99 | 29.99 | 79 | No (not latest) |
| 501 | 2024-03-20 | 2024-03-20 | downgrade | 9.99 | 29.99 | 79 | Yes (meets all criteria) |

After filtering to latest event and applying criteria:
- Active? Yes (downgrade, not cancel)
- Has downgrade? Yes (EXISTS finds downgrade events)
- Current < 50% max? Yes (9.99 / 29.99 = 33.3% < 50%)
- Duration >= 60? Yes (79 >= 60)

**2.4 Increment and Loop:**

The window functions process all events for all users, computing aggregates efficiently. The WHERE clause then filters to only churn risk customers.

**2.5 Return Result:**

The result includes user 501 with current_plan='basic', current_monthly_amount=9.99, max_historical_amount=29.99, and days_as_subscriber=79, ordered by days_as_subscriber DESC, user_id ASC.

