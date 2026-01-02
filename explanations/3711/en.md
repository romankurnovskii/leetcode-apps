## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a list of transactions (each with amount and time), we need to find the maximum number of transactions we can process such that the balance never goes negative.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of transactions can be up to 10^5.
- **Time Complexity:** O(n log n) - we need to sort transactions, where n is the number of transactions.
- **Space Complexity:** O(1) - we only need variables to track balance.
- **Edge Case:** If all transactions are negative, return 0. If all are positive, return all.

**1.2 High-level approach:**

The goal is to sort transactions by time and process them greedily, accepting transactions that keep the balance non-negative.

![Transaction processing visualization](https://assets.leetcode.com/static_assets/others/transactions.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible transaction orders. This is factorial.
- **Optimized Strategy:** Sort by time and process in order, accepting if balance stays non-negative. This is O(n log n) time.
- **Optimization:** By sorting and processing greedily, we maximize the number of transactions we can accept.

**1.4 Decomposition:**

1. Sort transactions by time.
2. Initialize balance to 0.
3. For each transaction in sorted order:
   - Check if balance + amount >= 0.
   - If yes, add to balance and increment count.
4. Return the count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `transactions = [[10, 1], [-5, 2], [15, 3]]`

- Sorted: `[[10, 1], [-5, 2], [15, 3]]`
- Balance: `0`
- Result variable: `res = 0`

**2.2 Start Checking:**

We process transactions in time order.

**2.3 Trace Walkthrough:**

| Step | Transaction | Balance before | Balance after | Accept? | res |
| ---- | ----------- | -------------- | ------------- | ------- | --- |
| 1    | [10, 1] | 0 | 10 | Yes | 1 |
| 2    | [-5, 2] | 10 | 5 | Yes | 2 |
| 3    | [15, 3] | 5 | 20 | Yes | 3 |

**2.4 Increment and Loop:**

After each transaction, we check if it can be accepted.

**2.5 Return Result:**

The result is `3`, which is the maximum number of transactions we can process while keeping balance non-negative.

