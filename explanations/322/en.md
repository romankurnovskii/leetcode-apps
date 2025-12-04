## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= coins.length <= 12`, `0 <= amount <= 10^4`.
- **Time Complexity:** O(amount * coins.length) - we fill a DP table.
- **Space Complexity:** O(amount) - we store a DP array.
- **Edge Case:** amount = 0 returns 0, impossible amounts return -1.

**1.2 High-level approach:**
The goal is to find the minimum number of coins needed to make up the amount. We use dynamic programming where `dp[i]` represents the minimum coins needed for amount `i`.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all combinations recursively - exponential time.
- **Optimized Strategy:** Dynamic programming - O(amount * coins) time.

**1.4 Decomposition:**
1. Initialize DP array with infinity, except dp[0] = 0.
2. For each amount from 1 to target, try each coin.
3. If the coin can be used, update dp[amount] with minimum coins.
4. Return dp[amount] if it's not infinity, else -1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `coins = [1,2,5]`, `amount = 11`. We initialize `dp = [0, inf, inf, ..., inf]`.

**2.2 Start Checking:**
We fill the DP table for each amount.

**2.3 Trace Walkthrough:**

| Amount | Try coin 1 | Try coin 2 | Try coin 5 | dp[amount] |
|--------|------------|------------|------------|------------|
| 1 | dp[0]+1=1 | - | - | 1 |
| 2 | dp[1]+1=2 | dp[0]+1=1 | - | 1 |
| 3 | dp[2]+1=2 | dp[1]+1=2 | - | 2 |
| ... | ... | ... | ... | ... |
| 11 | dp[10]+1=3 | dp[9]+1=3 | dp[6]+1=3 | 3 |

**2.4 Increment and Loop:**
After processing each amount, we move to the next.

**2.5 Return Result:**
Return `res = 3`, the minimum coins needed (5+5+1).

