## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the smallest number made only of the digit 1 (like 1, 11, 111, 1111, ...) that is divisible by k, and return the number of digits in that number. If no such number exists, return -1.

**1.1 Constraints & Complexity:**

- **Input Size:** k is between 2 and 10^5.
- **Time Complexity:** O(k) - we iterate at most k times, checking remainders. Since remainders can only have k possible values (0 to k-1), if we don't find 0 within k steps, we're in a cycle.
- **Space Complexity:** O(1) - we only use a constant amount of extra space for variables.
- **Edge Case:** If k is divisible by 2 or 5, no number made only of 1s can be divisible by k, so we return -1 immediately.

**1.2 High-level approach:**

The goal is to find the smallest "all-ones" number divisible by k. Instead of building the actual large numbers, we use modulo arithmetic to track only the remainder, which determines divisibility.

![Modulo arithmetic visualization](https://assets.leetcode.com/static_assets/others/modulo-arithmetic.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Build numbers 1, 11, 111, 1111, ... and check if each is divisible by k. This fails because these numbers become extremely large very quickly, making them impossible to store in standard integer types.
- **Optimized Strategy:** Use modulo arithmetic to build the number digit by digit. We track only the remainder when divided by k, not the full number. When we append a new digit 1, the new remainder is `(old_remainder × 10 + 1) % k`. This is O(k) time and O(1) space.
- **Optimization:** By using modulo arithmetic, we avoid storing huge numbers and can determine divisibility using only small remainder values, making the solution feasible for large k.

**1.4 Decomposition:**

1. Check if k is divisible by 2 or 5 - if so, return -1 immediately (numbers ending in 1 can't be divisible by 2 or 5).
2. Initialize remainder to 0.
3. For each digit position from 1 to k:
   - Update remainder: `rem = (rem × 10 + 1) % k`
   - If remainder becomes 0, we found the answer - return the current length.
4. If we complete k iterations without finding remainder 0, return -1 (we're in a cycle).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `k = 7`

- Check: `7 % 2 = 1` and `7 % 5 = 2`, so we proceed (not divisible by 2 or 5).
- Initial remainder: `rem = 0`
- We'll build the number digit by digit.

**2.2 Start Checking:**

We begin with the first digit, which represents the number 1.

**2.3 Trace Walkthrough:**

| Step | Length | Previous rem | Calculation | New rem | Action                    |
| ---- | ------ | ------------ | ----------- | ------- | ------------------------- |
| 1    | 1      | 0            | (0×10+1)%7  | 1       | Continue                  |
| 2    | 2      | 1            | (1×10+1)%7  | 4       | Continue                  |
| 3    | 3      | 4            | (4×10+1)%7  | 6       | Continue                  |
| 4    | 4      | 6            | (6×10+1)%7  | 5       | Continue                  |
| 5    | 5      | 5            | (5×10+1)%7  | 2       | Continue                  |
| 6    | 6      | 2            | (2×10+1)%7  | 0       | Found! Return length = 6 |

**2.4 Increment and Loop:**

After each step, we update the remainder using the formula `rem = (rem × 10 + 1) % k`. This represents appending another digit 1 to our number. We continue until either:
- The remainder becomes 0 (we found a divisible number), or
- We've tried k times (indicating a cycle, so no solution exists).

**2.5 Return Result:**

The result is 6, meaning the number 111111 (6 digits) is divisible by 7. We verify: 111111 ÷ 7 = 15873.

