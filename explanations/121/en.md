## Explanation

### Strategy (The "Why")

Given an array `prices` where `prices[i]` is the price of a stock on day $i$, we need to find the maximum profit we can achieve by choosing a single day to buy and a different day in the future to sell.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be up to $10^5$.
- **Value Range:** Prices are between $0$ and $10^4$.
- **Time Complexity:** $O(n)$ - We iterate through the prices array once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If prices are in descending order, we cannot make a profit, so return 0.

**1.2 High-level approach:**

The goal is to find the maximum profit from buying and selling a stock once.

![Best Time to Buy and Sell Stock](https://assets.leetcode.com/uploads/2020/03/26/chart.png)

We track the minimum price seen so far and calculate the profit if we sell on each day. The maximum of these profits is our answer.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all pairs of buy and sell days, calculating profit for each. This takes $O(n^2)$ time.
- **Optimized Strategy (One Pass):** Track the minimum price as we iterate. For each day, calculate profit if we sell today (current price - minimum price seen). This takes $O(n)$ time.
- **Why it's better:** The one-pass approach reduces time complexity from $O(n^2)$ to $O(n)$ by maintaining the minimum price seen so far, eliminating the need to check all previous days for each day.

**1.4 Decomposition:**

1. Initialize `min_price` to infinity and `max_profit` to 0.
2. Iterate through each price.
3. Update `min_price` to be the minimum of current `min_price` and current price.
4. Calculate profit if we sell today: `profit = current_price - min_price`.
5. Update `max_profit` to be the maximum of current `max_profit` and calculated profit.
6. Return `max_profit`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $prices = [7,1,5,3,6,4]$

We initialize:
- `min_price = \infty`
- `max_profit = 0`

**2.2 Start Processing:**

We iterate through each price.

**2.3 Trace Walkthrough:**

| Day | Price | min_price | Profit (price - min_price) | max_profit |
|-----|-------|-----------|---------------------------|------------|
| 0 | 7 | 7 | $7 - 7 = 0$ | 0 |
| 1 | 1 | 1 | $1 - 1 = 0$ | 0 |
| 2 | 5 | 1 | $5 - 1 = 4$ | 4 |
| 3 | 3 | 1 | $3 - 1 = 2$ | 4 |
| 4 | 6 | 1 | $6 - 1 = 5$ | 5 |
| 5 | 4 | 1 | $4 - 1 = 3$ | 5 |

**2.4 Optimal Strategy:**

- Buy on day 1 (price = 1)
- Sell on day 4 (price = 6)
- Profit = $6 - 1 = 5$

**2.5 Return Result:**

We return 5, which is the maximum profit achievable.

> **Note:** The key insight is that we only need to track the minimum price seen so far. For each day, we calculate the profit if we had bought at the minimum price and sell today, then take the maximum of all such profits.
