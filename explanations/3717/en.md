## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array, we need to find the minimum operations to make the array "beautiful" (no three consecutive equal elements).

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^5 elements.
- **Time Complexity:** O(n) - we iterate through the array once, where n is the array length.
- **Space Complexity:** O(1) - we only need variables to track operations.
- **Edge Case:** If the array already has no three consecutive equal elements, return 0. If all elements are the same, we need many operations.

**1.2 High-level approach:**

The goal is to scan the array and whenever we find three consecutive equal elements, remove one or two of them to break the pattern.

![Array beautification visualization](https://assets.leetcode.com/static_assets/others/array-beautiful.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible removal combinations. This is exponential.
- **Optimized Strategy:** Greedily remove elements when we detect three consecutive equals. This is O(n) time.
- **Optimization:** By processing left to right and removing immediately when we detect the pattern, we solve efficiently.

**1.4 Decomposition:**

1. Iterate through the array.
2. For each position, check if current and next two elements are equal.
3. If yes, increment operation count and skip ahead to avoid counting the same pattern multiple times.
4. Return total operations.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 1, 1, 2, 2, 2, 3]`

- Array: `[1, 1, 1, 2, 2, 2, 3]`
- Result variable: `res = 0`
- Current index: `i = 0`

**2.2 Start Checking:**

We scan for three consecutive equal elements.

**2.3 Trace Walkthrough:**

| Step | i | Check | Pattern? | Action | res | Next i |
| ---- | - | ----- | -------- | ------ | --- | ------ |
| 1    | 0 | [1,1,1] | Yes | Remove 1, i+=2 | 1 | 2 |
| 2    | 2 | [1,2,2] | No | Continue | 1 | 3 |
| 3    | 3 | [2,2,2] | Yes | Remove 1, i+=2 | 2 | 5 |

**2.4 Increment and Loop:**

After detecting a pattern, we skip ahead to avoid reprocessing.

**2.5 Return Result:**

The result is `2`, which is the minimum operations to make the array beautiful (remove one element from each triple).

