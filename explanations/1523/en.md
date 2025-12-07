## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Range:** `low` and `high` are non-negative integers where `0 <= low <= high <= 10^9`.
- **Time Complexity:** O(1) - we calculate the answer directly using a mathematical formula without iterating through the range.
- **Space Complexity:** O(1) - we only use a constant amount of extra space.
- **Edge Case:** When `low == high`, if the number is odd, return 1; otherwise return 0.

**1.2 High-level approach:**

The goal is to count how many odd numbers exist in the inclusive range `[low, high]`. Instead of iterating through all numbers, we use a mathematical observation: in any range of consecutive integers, roughly half are odd. The exact count depends on whether the range length is even or odd, and whether the starting number is odd or even.

![Visualization showing odd numbers in a range, highlighting the pattern of alternating odd and even numbers]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Iterate through all numbers from `low` to `high`, checking each one to see if it's odd. This takes O(high - low) time, which can be very slow for large ranges.
- **Optimized Strategy:** Use a mathematical formula based on the range length and the parity of the endpoints. This gives us O(1) time complexity.
- **Why it's better:** The optimized approach is constant time regardless of the range size, making it extremely efficient even for very large ranges.

**1.4 Decomposition:**

1. Calculate the total number of integers in the range: `total = high - low + 1`.
2. If the total is even, exactly half are odd: return `total // 2`.
3. If the total is odd, check if `low` is odd. If `low` is odd, we have one more odd number than even numbers.
4. Return the calculated count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `low = 3`, `high = 7`.

The range contains: `[3, 4, 5, 6, 7]`. The odd numbers are: `[3, 5, 7]`, so the answer should be 3.

**2.2 Start Checking:**

We calculate `total = high - low + 1 = 7 - 3 + 1 = 5`.

**2.3 Trace Walkthrough:**

| Step | total | total % 2 | low % 2 | Calculation | Result |
|------|-------|-----------|---------|-------------|--------|
| 1 | 5 | 1 (odd) | 1 (odd) | `5 // 2 + 1 = 2 + 1` | 3 |

Since `total` is odd (5) and `low` is odd (3), we have one more odd number than even numbers. The calculation is: `5 // 2 + 1 = 2 + 1 = 3`.

**2.4 Increment and Loop:**

Not applicable - this is a direct calculation.

**2.5 Return Result:**

Return `res = 3`, which matches our expected answer.

