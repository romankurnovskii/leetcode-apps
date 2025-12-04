## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The input `n` is a positive integer from 1 to 2^31 - 1.
- **Time Complexity:** O(log n) in the worst case, but typically much better. The process either reaches 1 (happy) or enters a cycle (unhappy).
- **Space Complexity:** O(log n) to store seen numbers in the set. The cycle length is bounded.
- **Edge Case:** If `n = 1`, it's already happy, so we return true immediately.

**1.2 High-level approach:**
The goal is to determine if a number is "happy" by repeatedly replacing it with the sum of squares of its digits until we reach 1 or detect a cycle.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same approach, but without cycle detection. This could run infinitely for unhappy numbers.
- **Optimized Strategy:** Use a set to track seen numbers. If we encounter a number we've seen before, we've entered a cycle and the number is unhappy.
- **Why optimized is better:** Cycle detection prevents infinite loops and correctly identifies unhappy numbers.

**1.4 Decomposition:**
1. Use a set to track numbers we've seen during the process.
2. While the current number is not 1, calculate the sum of squares of its digits.
3. If we've seen this number before, we're in a cycle - return false.
4. Add the current number to the set and continue.
5. If we reach 1, return true.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 19`

Initialize `seen = set()`. We'll track numbers we've encountered.

**2.2 Start Checking:**
We repeatedly calculate the sum of squares of digits until we reach 1 or detect a cycle.

**2.3 Trace Walkthrough:**

| Iteration | n | Sum of Squares | In seen? | Action |
|-----------|---|----------------|----------|--------|
| 0 | 19 | 1² + 9² = 82 | No | Add 19 to seen, n = 82 |
| 1 | 82 | 8² + 2² = 68 | No | Add 82 to seen, n = 68 |
| 2 | 68 | 6² + 8² = 100 | No | Add 68 to seen, n = 100 |
| 3 | 100 | 1² + 0² + 0² = 1 | No | n = 1, return True |

**2.4 Increment and Loop:**
For each number:
- Calculate sum of squares of digits: `res = 0`, then for each digit: `res += digit * digit`
- Check if `n` is in `seen` (cycle detected)
- Add `n` to `seen` and update `n = res`

**2.5 Return Result:**
We reached 1, so `n = 19` is a happy number. Return `True`.

