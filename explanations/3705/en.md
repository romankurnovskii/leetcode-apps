## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find customers who meet all criteria for being "golden hour customers": at least 3 orders, at least 60% of orders during peak hours (11:00-14:00 or 18:00-21:00), average rating >= 4.0 for rated orders, and at least 50% of orders rated.

**1.1 Constraints & Complexity:**

- **Input Size:** The restaurant_orders table can have many rows, with timestamps, ratings, and customer information.
- **Time Complexity:** O(n) where n is the number of orders - we need to scan the table once and group by customer_id.
- **Space Complexity:** O(m) where m is the number of distinct customers - we store aggregated statistics per customer.
- **Edge Case:** Customers with NULL ratings need to be handled correctly when calculating percentages.

**1.2 High-level approach:**

The goal is to aggregate order data by customer, calculate peak hour percentages, rating statistics, and filter customers who meet all four criteria. We use pandas groupby operations with aggregation functions to compute the required metrics.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Process each customer separately, scanning all orders multiple times to compute statistics. This would be O(n * m) in worst case.
- **Optimized Strategy:** Use pandas groupby with aggregation functions to compute all statistics in a single pass, then filter in one step. This is O(n) time.
- **Optimization:** Pandas groupby operations are vectorized and efficient, allowing us to compute multiple aggregates simultaneously without multiple scans.

**1.4 Decomposition:**

1. Convert order_timestamp to datetime format for time calculations.
2. Group orders by customer_id and aggregate:
   - Count total orders
   - Count peak hour orders (11:00-14:00 or 18:00-21:00)
   - Count rated orders (non-null ratings)
   - Calculate average rating
3. Calculate peak hour percentage and rated percentage.
4. Filter customers based on all four criteria.
5. Format and order the results as specified.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example from the problem with customer 101:

- Orders: 4 total
- Peak hours: 12:30, 19:15, 13:45, 20:30 (all 4 are peak)
- Ratings: 5, 4, 5, NULL (3 rated out of 4)

**2.2 Start Processing:**

We group all orders by customer_id and compute aggregated statistics.

**2.3 Trace Walkthrough:**

| Customer | total_orders | peak_hour_orders | rated_orders | avg_rating | peak_hour_percentage | rated_percentage | Meets criteria? |
| -------- | ------------ | ---------------- | ------------ | ---------- | -------------------- | ---------------- | --------------- |
| 101      | 4            | 4                | 3            | 4.67       | 100%                 | 75%              | Yes (all 4)     |
| 102      | 3            | 2                | 2            | 3.5        | 66.67%               | 66.67%           | No (rating < 4) |
| 103      | 3            | 3                | 3            | 4.67       | 100%                 | 100%             | Yes (all 4)     |
| 104      | 3            | 0                | 3            | 2.67       | 0%                   | 100%             | No (peak < 60%) |
| 105      | 3            | 3                | 3            | 4.33       | 100%                 | 100%             | Yes (all 4)     |

Customer 101: 4 orders >= 3 ✓, 4/4 = 100% peak >= 60% ✓, avg 4.67 >= 4.0 ✓, 3/4 = 75% rated >= 50% ✓

**2.4 Increment and Loop:**

The pandas groupby operation processes all orders for all customers simultaneously, computing aggregates efficiently. The filtering then applies all criteria in one step.

**2.5 Return Result:**

After filtering and formatting, we return customers 103, 101, and 105 ordered by average_rating DESC, customer_id DESC.
