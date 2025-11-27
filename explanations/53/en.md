## Explanation

### Strategy (The "Why")

Given an integer array `nums`, we need to find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $1$ and $10^5$.
- **Value Range:** Array elements are between $-10^4$ and $10^4$.
- **Time Complexity:** $O(n)$ - We iterate through the array once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If all numbers are negative, the maximum subarray is the single largest element.

**1.2 High-level approach:**

The goal is to find the maximum sum of a contiguous subarray.

![Maximum Subarray](https://assets.leetcode.com/uploads/2021/05/13/maxsubarray.png)

We use Kadane's algorithm: maintain a running sum, and whenever it becomes negative, reset it to 0. This is because a negative sum cannot contribute to a maximum sum.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subarrays, calculating the sum for each. This takes $O(n^2)$ time.
- **Optimized Strategy (Kadane's Algorithm):** Maintain a running sum. If it becomes negative, reset it to 0. Track the maximum sum seen. This takes $O(n)$ time.
- **Why it's better:** Kadane's algorithm reduces time complexity from $O(n^2)$ to $O(n)$ by recognizing that we don't need to check all subarrays - we can make a greedy decision to reset when the sum becomes negative.

**1.4 Decomposition:**

1. Initialize `max_sum` to the first element and `current_sum` to 0.
2. Iterate through each number.
3. If `current_sum` is negative, reset it to 0 (a negative sum cannot help).
4. Add the current number to `current_sum`.
5. Update `max_sum` to be the maximum of `max_sum` and `current_sum`.
6. Return `max_sum`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [-2,1,-3,4,-1,2,1,-5,4]$

We initialize:
- `max_sum = -2` (first element)
- `current_sum = 0`

**2.2 Start Processing:**

We iterate through each number.

**2.3 Trace Walkthrough:**

| Number | current_sum Before | Action | current_sum After | max_sum |
|--------|-------------------|--------|-------------------|---------|
| -2 | 0 | Reset (0), add -2 | -2 | -2 |
| 1 | -2 | Reset to 0, add 1 | 1 | 1 |
| -3 | 1 | Add -3 | -2 | 1 |
| 4 | -2 | Reset to 0, add 4 | 4 | 4 |
| -1 | 4 | Add -1 | 3 | 4 |
| 2 | 3 | Add 2 | 5 | 5 |
| 1 | 5 | Add 1 | 6 | 6 |
| -5 | 6 | Add -5 | 1 | 6 |
| 4 | 1 | Add 4 | 5 | 6 |

**2.4 Optimal Subarray:**

The maximum subarray is $[4,-1,2,1]$ with sum 6.

**2.5 Return Result:**

We return 6, which is the maximum sum of a contiguous subarray.

> **Note:** The key insight of Kadane's algorithm is that if the current sum becomes negative, we should reset it to 0 because a negative sum will only decrease any future sum. This allows us to find the maximum subarray in a single pass.

