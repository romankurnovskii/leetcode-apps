## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find customers who are considered "loyal" based on their transaction history. A customer is loyal if they: (1) made at least 3 purchase transactions, (2) have been active for at least 30 days, and (3) have a refund rate less than 20%.

**1.1 Constraints & Complexity:**

- **Input Size:** The customer_transactions table can have many rows per customer, with multiple transactions over time.
- **Time Complexity:** O(n) where n is the number of transactions - we group by customer_id and aggregate in a single pass.
- **Space Complexity:** O(m) where m is the number of distinct customers - we store aggregated statistics per customer.
- **Edge Case:** A customer with no refunds has a refund rate of 0%, which is less than 20%.

**1.2 High-level approach:**

The goal is to use pandas groupby operations to compute aggregate statistics (purchase count, total transactions, refund count, active days) for each customer, then filter based on the loyalty criteria.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Process each customer separately, scanning all transactions multiple times to compute statistics. This would be O(n * m) in worst case.
- **Optimized Strategy:** Use pandas groupby with aggregation functions to compute all statistics in a single pass, then filter in one step. This is O(n) time.
- **Optimization:** Pandas groupby operations are vectorized and efficient, allowing us to compute multiple aggregates simultaneously without multiple scans.

**1.4 Decomposition:**

1. Convert transaction_date to datetime format for date calculations.
2. Group transactions by customer_id and aggregate:
   - Count purchase transactions
   - Count total transactions
   - Count refund transactions
   - Calculate days active (max date - min date)
3. Calculate refund rate: refund_count / total_transactions
4. Filter customers based on all three loyalty criteria.
5. Return customer_id sorted in ascending order.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's consider customer 101 with transactions:
- 2024-01-05: purchase $150.00
- 2024-01-15: purchase $200.00
- 2024-02-10: purchase $180.00
- 2024-02-20: purchase $250.00

**2.2 Start Processing:**

We group all transactions by customer_id and compute aggregated statistics.

**2.3 Trace Walkthrough:**

| Customer | purchase_count | total_transactions | refund_count | days_active | refund_rate | Meets criteria? |
|----------|----------------|-------------------|--------------|-------------|-------------|----------------|
| 101 | 4 | 4 | 0 | 46 | 0.00 (0%) | Yes (all 3) |
| 102 | 3 | 5 | 2 | 36 | 0.40 (40%) | No (refund rate > 20%) |
| 103 | 3 | 3 | 0 | 2 | 0.00 (0%) | No (< 30 days) |
| 104 | 5 | 6 | 1 | 73 | 0.17 (17%) | Yes (all 3) |

For customer 101:
- Purchase count >= 3? Yes (4 >= 3) ✓
- Days active >= 30? Yes (46 >= 30) ✓
- Refund rate < 20%? Yes (0% < 20%) ✓

**2.4 Increment and Loop:**

The pandas groupby operation processes all transactions for all customers simultaneously, computing aggregates efficiently. The filtering then applies all loyalty criteria in one step.

**2.5 Return Result:**

The result includes customers 101 and 104 with their customer_id, ordered by customer_id in ascending order.

