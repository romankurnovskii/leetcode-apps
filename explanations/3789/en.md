## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum cost to acquire at least `need1` units of type 1 and `need2` units of type 2. We can buy three types of items: type 1 (costs `cost1`, gives 1 type 1), type 2 (costs `cost2`, gives 1 type 2), or type "both" (costs `costBoth`, gives 1 of both types).

**1.1 Constraints & Complexity:**

- **Input Size:** Costs are between 1 and 10^6, and needs are between 0 and 10^9.
- **Time Complexity:** O(1) - we perform a fixed number of comparisons and arithmetic operations, independent of input size.
- **Space Complexity:** O(1) - we only use a constant amount of extra space for variables.
- **Edge Case:** If both `need1` and `need2` are 0, we return 0 (no items needed).

**1.2 High-level approach:**

The goal is to find the minimum cost by considering three different purchasing strategies. The "both" item can satisfy both requirements simultaneously, and sometimes it's cheaper to over-satisfy one requirement if the "both" item is very cheap.

![Cost comparison visualization](https://assets.leetcode.com/static_assets/others/cost-comparison.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of the three item types. This would require checking exponentially many combinations, which is infeasible.
- **Optimized Strategy:** Consider only three key strategies: (1) buy all individual items, (2) buy "both" items for the overlap and individual items for the rest, (3) buy enough "both" items to satisfy the larger requirement. This is O(1) time.
- **Optimization:** By recognizing that only three strategies matter (no "both" items, optimal overlap, or maximum "both" items), we avoid checking all combinations and solve the problem in constant time.

**1.4 Decomposition:**

1. Handle the edge case where no items are needed (return 0).
2. Calculate cost of Strategy 1: buy all individual items separately.
3. Calculate cost of Strategy 2: buy "both" items for the overlap (min(need1, need2)), then buy individual items for remaining needs.
4. Calculate cost of Strategy 3: buy enough "both" items to satisfy the larger requirement (max(need1, need2)).
5. Return the minimum cost among all three strategies.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2`

- We need 3 units of type 1 and 2 units of type 2.
- Individual costs: type 1 costs 3, type 2 costs 2.
- Bundle cost: "both" item costs 1 (cheaper than buying one of each individually: 3 + 2 = 5).

**2.2 Start Checking:**

We evaluate three different purchasing strategies.

**2.3 Trace Walkthrough:**

| Strategy | Description                          | Calculation                                    | Cost |
| -------- | ------------------------------------ | ---------------------------------------------- | ---- |
| 1        | Buy all individual items              | 3 × 3 + 2 × 2                                 | 13   |
| 2        | Buy 2 "both" items (overlap), then 1 type 1 | 2 × 1 + 1 × 3                                 | 5    |
| 3        | Buy 3 "both" items (max need)        | 3 × 1                                          | 3    |

**Strategy 2 details:**
- Overlap = min(3, 2) = 2
- Buy 2 "both" items: satisfies 2 type 1 and 2 type 2
- Remaining: need1 = 1, need2 = 0
- Buy 1 type 1 item for remaining need1
- Total: 2 × 1 + 1 × 3 = 5

**Strategy 3 details:**
- Max need = max(3, 2) = 3
- Buy 3 "both" items: satisfies 3 type 1 and 3 type 2
- This over-satisfies type 2 (we only need 2, but get 3), but it's still optimal
- Total: 3 × 1 = 3

**2.4 Increment and Loop:**

We compare all three strategies and select the minimum cost. In this case, Strategy 3 gives the minimum cost of 3.

**2.5 Return Result:**

The result is 3, which is the minimum cost achieved by buying 3 "both" items. We verify: 3 "both" items cost 3 × 1 = 3, and they satisfy need1 = 3 (≥ 3) and need2 = 3 (≥ 2).

