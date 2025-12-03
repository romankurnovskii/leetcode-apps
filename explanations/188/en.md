## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq k \leq 100$ transactions, $1 \leq n \leq 1000$ days. Prices are in the range $[0, 1000]$.
- **Time Complexity:** $O(n \times k)$ where $n$ is the number of days and $k$ is the number of transactions. In the optimized case when $k \geq n/2$, it's $O(n)$.
- **Space Complexity:** $O(k)$ for the `buy` and `sell` arrays.
- **Edge Case:** If $k = 0$ or prices is empty, return 0. If $k \geq n/2$, we can make unlimited transactions.

**1.2 High-level approach:**

The goal is to find the maximum profit from at most $k$ buy-sell transactions. We use dynamic programming with two arrays: `buy[i]` represents the maximum profit with at most $i$ transactions while holding stock, and `sell[i]` represents the maximum profit with at most $i$ transactions while not holding stock.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of $k$ transactions. This is exponential time.
- **Optimized Strategy:** Use DP with state tracking. For each day, update `buy[i]` and `sell[i]` for all transaction counts. If $k \geq n/2$, use the unlimited transactions approach. This is $O(n \times k)$ time.
- **Why optimized is better:** The DP approach efficiently tracks the best profit for each transaction count, avoiding exponential complexity.

**1.4 Decomposition:**

1. If $k \geq n/2$, treat as unlimited transactions: sum all positive price differences.
2. Otherwise, initialize `buy` and `sell` arrays of size $k+1$.
3. For each price:
   - For each transaction count from $k$ down to 1:
     - Update `buy[i] = max(buy[i], sell[i-1] - price)` (buy or keep holding)
     - Update `sell[i] = max(sell[i], buy[i] + price)` (sell or keep not holding)
4. Return `sell[k]`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `k = 2`, `prices = [3,2,6,5,0,3]`

Since $k = 2 < 6/2 = 3$, we use the DP approach.

We initialize:
- `buy = [-inf, -inf, -inf]` (for 0, 1, 2 transactions)
- `sell = [0, 0, 0]` (for 0, 1, 2 transactions)

**2.2 Start Checking:**

We process each price and update `buy` and `sell` for each transaction count.

**2.3 Trace Walkthrough:**

| Price | Transaction | buy[1] | sell[1] | buy[2] | sell[2] |
|-------|-------------|--------|---------|--------|---------|
| 3 | - | -inf | 0 | -inf | 0 |
| 2 | 1 | max(-inf, 0-2) = -2 | max(0, -2+2) = 0 | max(-inf, 0-2) = -2 | max(0, -2+2) = 0 |
| 6 | 1 | max(-2, 0-6) = -2 | max(0, -2+6) = 4 | max(-2, 0-6) = -2 | max(0, -2+6) = 4 |
| 5 | 1 | max(-2, 4-5) = -1 | max(4, -1+5) = 4 | max(-2, 4-5) = -1 | max(4, -1+5) = 4 |
| 0 | 1 | max(-1, 4-0) = 4 | max(4, 4+0) = 4 | max(-1, 4-0) = 4 | max(4, 4+0) = 4 |
| 3 | 1 | max(4, 4-3) = 4 | max(4, 4+3) = 7 | max(4, 4-3) = 4 | max(4, 4+3) = 7 |

**2.4 Increment and Loop:**

For each price:
- Process transaction counts from $k$ down to 1 (to avoid using updated values in the same iteration):
  - `buy[i] = max(buy[i], sell[i-1] - price)`: Either keep current holding or buy today using profit from $i-1$ transactions.
  - `sell[i] = max(sell[i], buy[i] + price)`: Either keep current state or sell today.

**2.5 Return Result:**

After processing all prices, `sell[2] = 7`. This represents the maximum profit with at most 2 transactions:
- Buy at day 2 (price 2), sell at day 3 (price 6): profit = 4
- Buy at day 5 (price 0), sell at day 6 (price 3): profit = 3
- Total: 4 + 3 = 7

We return `7`.

