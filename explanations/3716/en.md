## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find customers at risk of churning based on their subscription history. A customer is at churn risk if they: (1) currently have an active subscription (last event is not cancel), (2) have performed at least one downgrade, (3) their current monthly amount is less than 50% of their historical maximum, and (4) have been a subscriber for at least 60 days.

**1.1 Constraints & Complexity:**

- **Input Size:** The subscription_events table can have many rows per user, with multiple events over time.
- **Time Complexity:** O(n) where n is the number of events - we group by user_id and aggregate in a single pass.
- **Space Complexity:** O(m) where m is the number of distinct users - we store aggregated statistics per user.
- **Edge Case:** A user who cancels and then starts again should only be considered based on their current active subscription period.

**1.2 High-level approach:**

The goal is to use pandas groupby operations to compute aggregate statistics (latest event, downgrade history, max monthly amount, subscription duration) for each user, then filter based on the churn risk criteria.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Process each user separately, scanning all events multiple times to compute statistics. This would be O(n \* m) in worst case.
- **Optimized Strategy:** Use pandas groupby with aggregation functions to compute all statistics in a single pass, then filter in one step. This is O(n) time.
- **Optimization:** Pandas groupby operations are vectorized and efficient, allowing us to compute multiple aggregates simultaneously without multiple scans.

**1.4 Decomposition:**

1. Convert event_date to datetime format for date calculations.
2. Group events by user_id and aggregate:
   - Latest event type (to check if subscription is active)
   - Whether any downgrade event exists
   - Current monthly amount (last value)
   - Maximum historical monthly amount
   - Days as subscriber (max date - min date)
   - Current plan name (last value)
3. Filter users based on all four churn risk criteria.
4. Sort results by days_as_subscriber DESC, then user_id ASC.
5. Select and return the required columns.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's consider a user with events:

- 2024-01-01: start premium ($29.99)
- 2024-02-15: downgrade standard ($19.99)
- 2024-03-20: downgrade basic ($9.99)

**2.2 Start Processing:**

We group all events by user_id and compute aggregated statistics.

**2.3 Trace Walkthrough:**

| User | latest_event | has_downgrade | current_monthly_amount | max_historical_amount | days_as_subscriber | Meets criteria?   |
| ---- | ------------ | ------------- | ---------------------- | --------------------- | ------------------ | ----------------- |
| 501  | downgrade    | True          | 9.99                   | 29.99                 | 79                 | Yes (all 4)       |
| 502  | downgrade    | True          | 9.99                   | 29.99                 | 70                 | Yes (all 4)       |
| 503  | upgrade      | True          | 29.99                  | 29.99                 | 75                 | No (no downgrade) |
| 504  | cancel       | True          | 0.00                   | 29.99                 | 75                 | No (cancelled)    |
| 505  | upgrade      | False         | 19.99                  | 19.99                 | 27                 | No (no downgrade) |
| 506  | downgrade    | True          | 9.99                   | 29.99                 | 50                 | No (< 60 days)    |

For user 501:

- Active? Yes (latest_event = 'downgrade', not 'cancel') ✓
- Has downgrade? Yes ✓
- Current < 50% max? Yes (9.99 / 29.99 = 33.3% < 50%) ✓
- Duration >= 60? Yes (79 >= 60) ✓

**2.4 Increment and Loop:**

The pandas groupby operation processes all events for all users simultaneously, computing aggregates efficiently. The filtering then applies all churn risk criteria in one step.

**2.5 Return Result:**

The result includes users 501 and 502 with their current_plan, current_monthly_amount, max_historical_amount, and days_as_subscriber, ordered by days_as_subscriber DESC, user_id ASC.
