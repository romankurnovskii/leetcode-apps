## Explanation

### Strategy (The "Why")

Given a binary array `nums`, we need to find the longest subarray containing only 1's after deleting exactly one element. We can delete at most one element.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $10^5$.
- **Value Range:** Array elements are 0 or 1.
- **Time Complexity:** $O(n)$ - We use sliding window that processes each element at most twice.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the array contains only 1's, return length-1 (we must delete one element). If the array contains no 1's, return 0.

**1.2 High-level approach:**

The goal is to find the longest subarray of 1's after deleting at most one 0.

We use a sliding window approach. We maintain a window that contains at most one 0. When we encounter a second 0, we shrink the window from the left until we have at most one 0 again.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subarrays and check if they contain at most one 0. This takes $O(n^2)$ time.
- **Optimized Strategy (Sliding Window):** Use two pointers to maintain a window with at most one 0. This takes $O(n)$ time.
- **Why it's better:** The sliding window approach reduces time complexity from $O(n^2)$ to $O(n)$ by maintaining a valid window and only moving pointers forward.

**1.4 Decomposition:**

1. Initialize two pointers (left and right) and a zero count.
2. Expand the window by moving the right pointer.
3. When we encounter a 0, increment the zero count.
4. If zero count exceeds 1, shrink the window from the left until zero count is at most 1.
5. Update the maximum length (subtract 1 because we must delete one element).
6. Return the maximum length.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [0,1,1,1,0,1,1,0,1]$

We initialize:
- `left = 0`
- `max_length = 0`
- `zero_count = 0`

**2.2 Start Processing:**

We begin expanding the window.

**2.3 Trace Walkthrough:**

| right | nums[right] | zero_count | Action | left | max_length |
|-------|-------------|------------|--------|------|------------|
| 0 | 0 | 1 | Continue | 0 | 0 |
| 1 | 1 | 1 | Continue | 0 | 1 |
| 2 | 1 | 1 | Continue | 0 | 2 |
| 3 | 1 | 1 | Continue | 0 | 3 |
| 4 | 0 | 2 | Shrink | 1 | 3 |
| 5 | 1 | 1 | Continue | 1 | 4 |
| 6 | 1 | 1 | Continue | 1 | 5 |
| 7 | 0 | 2 | Shrink | 5 | 5 |
| 8 | 1 | 1 | Continue | 5 | 4 |

**2.4 Explanation:**

- Maximum subarray after deleting one element: `[1,1,1,0,1,1]` (delete the first 0) or `[1,1,1,0,1,1]` (delete the last 0)
- Length = 6, but we must delete one element, so result = 5

**2.5 Return Result:**

We return 5, which is the longest subarray of 1's after deleting exactly one element.

> **Note:** The key insight is that we can have at most one 0 in our window. When we have two 0's, we must shrink the window to remove one of them. The result is the window length minus 1 (because we must delete one element).

