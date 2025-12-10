## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** Array `nums` has length `n` where `3 <= n <= 10^5`. Values range from `-10^5` to `10^5`. We can replace exactly one element with any value in `[-10^5, 10^5]`.
- **Time Complexity:** O(n) - We iterate through the array once to find the two largest absolute values.
- **Space Complexity:** O(1) - We only use a constant amount of extra space.
- **Edge Case:** If the array contains zeros and we can't avoid them, the product will be 0.

**1.2 High-level approach:**

The key insight is that we can always make the product positive by choosing the right sign for the replacement value. Since we can replace one element with either `10^5` or `-10^5`, we want to maximize the product of three elements. The optimal strategy is to find the two largest absolute values in the array, and multiply them by `10^5`.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try replacing each element with `10^5` and `-10^5`, then find the maximum product of three elements from all combinations. This would be O(n^2) or worse.
- **Optimized Strategy:** Recognize that we can always make the product positive by choosing the right sign. Therefore, we only need the two largest absolute values from the array. The answer is simply: `max_abs1 * max_abs2 * 10^5`. This is O(n) time.
- **Why optimized is better:** The insight eliminates the need to try all combinations. We can directly compute the answer by finding the two largest absolute values.

**1.4 Decomposition:**

1. Iterate through the array to find the two largest absolute values.
2. Multiply these two values by `10^5`.
3. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [-5, 7, 0]`

We initialize `max_abs1 = 0` and `max_abs2 = 0` to track the two largest absolute values.

**2.2 Start Checking:**

We iterate through each element in the array, updating our two largest absolute values.

**2.3 Trace Walkthrough:**

| Element | Absolute Value | max_abs1 | max_abs2 | Action |
|---------|----------------|----------|----------|--------|
| -5 | 5 | 0 → 5 | 0 | Update max_abs1 = 5, max_abs2 = 0 |
| 7 | 7 | 5 → 7 | 0 → 5 | Update max_abs1 = 7, max_abs2 = 5 |
| 0 | 0 | 7 | 5 | No update (0 < 5) |

After iteration: `max_abs1 = 7`, `max_abs2 = 5`

**2.4 Increment and Loop:**

For each element `x` in the array:
- Calculate `abs_x = abs(x)`
- If `abs_x >= max_abs1`: Update `max_abs2 = max_abs1`, then `max_abs1 = abs_x`
- Else if `abs_x > max_abs2`: Update `max_abs2 = abs_x`

**2.5 Return Result:**

For `nums = [-5, 7, 0]`, we have `max_abs1 = 7` and `max_abs2 = 5`.
The result is `7 * 5 * 100000 = 3500000`.

We can achieve this by replacing `0` with `-10^5`, giving us `[-5, 7, -10^5]` with product `(-5) * 7 * (-10^5) = 3500000`.
