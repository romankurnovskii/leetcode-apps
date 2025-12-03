## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The array $prices$ has length $1 \leq n \leq 10^5$, with values in $[0, 10^5]$.
* **Time Complexity:** $O(n)$ - We iterate through the prices array once.
* **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for state variables.
* **Edge Case:** If prices are strictly decreasing, no profit can be made, return 0.

**1.2 High-level approach**

The goal is to find the maximum profit from at most two transactions. We use a state machine approach to track the best states for buying and selling in two transactions.

![State machine visualization showing buy1, sell1, buy2, sell2 states]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible combinations of two buy-sell pairs. This takes $O(n^4)$ time.
* **Optimized (State Machine):** Track four states: buy1 (first buy), sell1 (first sell), buy2 (second buy), sell2 (second sell). Update each state optimally as we iterate. This achieves $O(n)$ time.

**1.4 Decomposition**

1. **Initialize States:** Set buy states to negative infinity (maximize negative), sell states to 0.
2. **Update First Transaction:** For each price, update buy1 (lowest buy price) and sell1 (maximum profit from first transaction).
3. **Update Second Transaction:** Using profit from first transaction, update buy2 and sell2.
4. **Return Result:** Return sell2, which represents maximum profit from two transactions.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $prices = [3,3,5,0,0,3,1,4]$.

We initialize:
* `buy1 = -inf` (best first buy price, negative to maximize)
* `sell1 = 0` (best first sell profit)
* `buy2 = -inf` (best second buy price)
* `sell2 = 0` (best total profit)

**2.2 Start Processing**

We iterate through each price.

**2.3 Trace Walkthrough**

| Price | buy1 (before) | buy1 (after) | sell1 (before) | sell1 (after) | buy2 (before) | buy2 (after) | sell2 (before) | sell2 (after) |
|-------|---------------|--------------|----------------|---------------|---------------|--------------|-----------------|---------------|
| 3 | -inf | -3 | 0 | 0 | -inf | -inf | 0 | 0 |
| 3 | -3 | -3 | 0 | 0 | -inf | -inf | 0 | 0 |
| 5 | -3 | -3 | 0 | 2 | -inf | -2 | 0 | 0 |
| 0 | -3 | 0 | 2 | 2 | -2 | 2 | 0 | 2 |
| 0 | 0 | 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | 0 | 0 | 2 | 3 | 2 | 2 | 2 | 3 |
| 1 | 0 | 0 | 3 | 3 | 2 | 2 | 3 | 3 |
| 4 | 0 | 0 | 3 | 3 | 2 | 2 | 3 | 6 |

**2.4 State Updates**

For each price:
1. `buy1 = max(buy1, -price)` - Buy at lowest price
2. `sell1 = max(sell1, buy1 + price)` - Sell at highest profit
3. `buy2 = max(buy2, sell1 - price)` - Buy second time using first profit
4. `sell2 = max(sell2, buy2 + price)` - Sell second time for total profit

**2.5 Return Result**

After processing all prices, `sell2 = 6`, which is the maximum profit from two transactions:
- Transaction 1: Buy at 0 (day 4), sell at 3 (day 6) → profit = 3
- Transaction 2: Buy at 1 (day 7), sell at 4 (day 8) → profit = 3
- Total: 3 + 3 = 6

