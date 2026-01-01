## Explanation

### Strategy (The "Why")

**Restate the problem:** Two players (Alice and Bob) take turns picking 1, 2, or 3 stones from a row. Each stone has a value. The player with the higher total score wins. We need to determine the winner if both play optimally.

**1.1 Constraints & Complexity:**

- **Input Size:** The stone value array can have up to 5 * 10^4 elements, with each value between -10^4 and 10^4.
- **Time Complexity:** O(n) - we use dynamic programming to process each position once, where n is the number of stones.
- **Space Complexity:** O(n) - we need a DP array of size n+1 to store the maximum score difference from each position.
- **Edge Case:** If there's only one stone, Alice takes it. If all stones have negative values, both players try to minimize their losses.

**1.2 High-level approach:**

The goal is to use dynamic programming to calculate the maximum score difference the current player can achieve from each position, working backwards from the end of the array.

![Stone game visualization](https://assets.leetcode.com/static_assets/others/stone-game.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible move sequences for both players. This is exponential and impractical.
- **Optimized Strategy:** Use dynamic programming where dp[i] represents the maximum score difference the current player can achieve starting from position i. This is O(n) time.
- **Optimization:** By using DP and working backwards, we can determine the optimal outcome without trying all sequences.

**1.4 Decomposition:**

1. Initialize a DP array where dp[i] represents the maximum score difference from position i.
2. Start from the end of the array and work backwards.
3. For each position, consider taking 1, 2, or 3 stones and calculate the resulting score difference.
4. Choose the move that maximizes the score difference.
5. The value at dp[0] tells us the outcome: positive means Alice wins, negative means Bob wins, zero means tie.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `stoneValue = [1, 2, 3, 7]`

- Stone values: `[1, 2, 3, 7]`
- DP array: `dp = [0, 0, 0, 0, 0]` (size n+1)
- Result variable: `res = ""`

**2.2 Start Checking:**

We begin filling the DP array from the end.

**2.3 Trace Walkthrough:**

| Step | i | Take 1 | Take 2 | Take 3 | dp[i] | Meaning |
| ---- | - | ------ | ------ | ------ | ----- | ------- |
| 1    | 3 | 7 - 0 = 7 | - | - | 7 | Take 1 stone |
| 2    | 2 | 3 - 7 = -4 | 3+7 - 0 = 10 | - | 10 | Take 2 stones |
| 3    | 1 | 2 - 10 = -8 | 2+3 - 7 = -2 | 2+3+7 - 0 = 12 | 12 | Take 3 stones |
| 4    | 0 | 1 - 12 = -11 | 1+2 - 10 = -7 | 1+2+3 - 7 = -1 | -11 | Take 1 stone |

**2.4 Increment and Loop:**

We iterate backwards from n-1 to 0, calculating the optimal move at each position.

**2.5 Return Result:**

Since dp[0] = -11 (negative), the result is `"Bob"`, meaning Bob wins if both play optimally.

