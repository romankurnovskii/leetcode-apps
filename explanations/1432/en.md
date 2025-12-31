## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum difference between two numbers we can create by applying digit replacement operations twice to the same number. In each operation, we pick a digit x and replace all occurrences of x with another digit y.

**1.1 Constraints & Complexity:**

- **Input Size:** The number can be up to 10^8, which means up to 9 digits.
- **Time Complexity:** O(d) where d is the number of digits - we process the string representation once to find replacement candidates, then perform string replacements which are O(d).
- **Space Complexity:** O(d) - we store the string representation of the number.
- **Edge Case:** If all digits are the same (e.g., 111), the maximum value is 999 and minimum is 111, so the difference is 888. If the number is a single digit, we can only replace it with 9 (max) or 1 (min).

**1.2 High-level approach:**

The goal is to maximize the difference by creating the largest possible number in one operation and the smallest possible number in another operation, then find their difference.

![Digit replacement visualization](https://assets.leetcode.com/static_assets/others/digit-replacement.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible digit replacements for both operations and find the maximum difference. This would be O(10^2 * d^2) which is inefficient.
- **Optimized Strategy:** For maximum value, replace the first non-9 digit with 9. For minimum value, if the first digit is not 1, replace it with 1; otherwise, replace the first non-0, non-1 digit with 0. This is O(d) time.
- **Optimization:** By using greedy choices (9 for max, 1 or 0 for min), we avoid trying all combinations and solve in linear time.

**1.4 Decomposition:**

1. Convert the number to a string for easy digit manipulation.
2. Find the maximum value: replace the first non-9 digit with 9 (to maximize the number).
3. Find the minimum value: if the first digit is not 1, replace it with 1; otherwise, replace the first non-0, non-1 digit with 0 (to minimize while avoiding leading zeros).
4. Calculate and return the difference between maximum and minimum values.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `num = 555`

- Number string: `num_str = "555"`
- Maximum value: `max_val = "555"` (to be updated)
- Minimum value: `min_val = "555"` (to be updated)

**2.2 Start Checking:**

We process the string to find digits to replace.

**2.3 Trace Walkthrough:**

| Step | Operation | num_str | Digit Found | Replacement | Result |
| ---- | --------- | ------- | ----------- | ------------ | ------ |
| 1    | Find max  | "555"   | First '5'   | Replace '5' with '9' | "999" |
| 2    | Find min  | "555"   | First '5'   | Replace '5' with '1' | "111" |
| 3    | Calculate | -       | -           | max - min     | 999 - 111 = 888 |

**2.4 Increment and Loop:**

No loop needed - we perform string replacement operations directly.

**2.5 Return Result:**

The result is `888`, which is the maximum difference between 999 (all 5's replaced with 9) and 111 (all 5's replaced with 1).

