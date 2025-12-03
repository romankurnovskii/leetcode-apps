## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq num \leq 2 \times 10^5$ digits, $1 \leq sum \leq 2 \times 10^6$.
- **Time Complexity:** $O(num)$ where $num$ is the number of digits. We iterate once to build the number.
- **Space Complexity:** $O(num)$ for storing the digit string.
- **Edge Case:** If $sum < num$ or $sum > 9 \times num$, no valid number exists, return empty string.

**1.2 High-level approach:**

The goal is to find a number with exactly `num` digits and digit sum `sum` that maximizes the sum of squares of digits. To maximize sum of squares, we want the largest possible digits (since $x^2$ grows faster for larger $x$). Use a greedy approach: fill leftmost positions with 9s first.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible numbers with `num` digits and sum `sum`, calculate scores. This is exponential.
- **Optimized Strategy:** Greedily place the largest possible digit (9) at each position from left to right, ensuring remaining positions can still achieve the required sum. This is $O(num)$ time.
- **Why optimized is better:** The greedy approach directly constructs the optimal number without trying all possibilities.

**1.4 Decomposition:**

1. Check feasibility: if $sum < num$ or $sum > 9 \times num$, return empty string.
2. For each digit position from left to right:
   - Calculate maximum digit we can place: `min(9, remaining_sum - remaining_positions)`
   - Place this digit and update remaining sum.
3. Return the constructed number as string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `num = 2`, `sum = 3`

We want a 2-digit number with digit sum 3 that maximizes sum of squares.

**2.2 Start Checking:**

We fill digits from left to right, placing the largest possible digit at each position.

**2.3 Trace Walkthrough:**

| Position | Remaining Sum | Remaining Positions | Max Digit | Digit Placed | Remaining After |
|----------|---------------|-------------------|-----------|--------------|-----------------|
| 0 | 3 | 2 | min(9, 3-1) = 2 | 3 | 0 |
| 1 | 0 | 1 | min(9, 0-0) = 0 | 0 | 0 |

Result: "30"

Check: digits are 3 and 0, sum = 3+0 = 3 ✓, squares = 3²+0² = 9+0 = 9

**2.4 Increment and Loop:**

For each position $i$ from 0 to $num-1$:
- `remaining_positions = num - i - 1`
- `max_digit = min(9, remaining_sum - remaining_positions)`
- If `max_digit < 1`, set `max_digit = 1` (minimum digit)
- Place `max_digit`, update `remaining_sum -= max_digit`

**2.5 Return Result:**

For `num = 2`, `sum = 3`, we get "30" which has the maximum sum of squares (9) among all valid numbers (12, 21, 30). We return "30".

