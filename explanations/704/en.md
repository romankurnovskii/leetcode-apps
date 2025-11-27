## Explanation

### Strategy (The "Why")

Given an array of integers `nums` which is sorted in ascending order, and a target value, we need to return the index of the target if it exists in the array, or -1 if it doesn't.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be up to $10^4$.
- **Value Range:** Array elements and target can be between $-10^4$ and $10^4$.
- **Time Complexity:** $O(\log n)$ - Binary search eliminates half of the remaining elements in each iteration, so we need at most $\log_2 n$ comparisons.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables like `left`, `right`, and `mid`.
- **Edge Case:** If the array is empty, we return -1. If the target is at the first or last index, we still find it correctly.

**1.2 High-level approach:**

The goal is to find the target value in a sorted array efficiently.

![Binary Search Visualization](https://assets.leetcode.com/uploads/2021/07/21/binary-search.jpg)

Since the array is sorted, we can use binary search: compare the target with the middle element, and based on the comparison, eliminate half of the remaining search space.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Iterate through the array from left to right, checking each element until we find the target or reach the end. This takes $O(n)$ time.
- **Optimized Strategy (Binary Search):** Use two pointers (`left` and `right`) to maintain the search space. Compare the target with the middle element, and eliminate half of the remaining elements in each step. This takes $O(\log n)$ time.
- **Why it's better:** Binary search reduces the time complexity from linear to logarithmic, which is a significant improvement, especially for large arrays. For an array of size $10^4$, binary search needs at most 14 comparisons, while linear search might need up to $10^4$ comparisons.

**1.4 Decomposition:**

1. Initialize two pointers: `left` at the start (index 0) and `right` at the end (index $n-1$).
2. While `left <= right`, continue searching.
3. Calculate the middle index: `mid = (left + right) // 2`.
4. Compare the element at `mid` with the target.
5. If they are equal, return `mid`.
6. If the element at `mid` is greater than the target, search the left half by setting `right = mid - 1`.
7. If the element at `mid` is less than the target, search the right half by setting `left = mid + 1`.
8. If the loop ends without finding the target, return -1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [-1, 0, 3, 5, 9, 12]$, $target = 9$

We initialize:
- `left = 0`
- `right = 5` (length - 1)
- The array is already sorted

**2.2 Start Checking:**

We begin the binary search with the entire array as the search space.

**2.3 Trace Walkthrough:**

| Iteration | Left | Right | Mid | nums[Mid] | Comparison | Action |
|-----------|------|-------|-----|-----------|------------|--------|
| 1 | 0 | 5 | 2 | 3 | $3 < 9$ | Search right: `left = 3` |
| 2 | 3 | 5 | 4 | 9 | $9 == 9$ | **Found! Return 4** |

Detailed steps:
- **Iteration 1:** 
  - `mid = (0 + 5) // 2 = 2`
  - `nums[2] = 3`
  - Since $3 < 9$, the target must be in the right half
  - Update `left = 3`
- **Iteration 2:**
  - `mid = (3 + 5) // 2 = 4`
  - `nums[4] = 9`
  - Since $9 == 9$, we found the target
  - Return 4

**2.4 Increment and Loop:**

If the target wasn't found in iteration 2, we would continue:
- The search space would keep narrowing until either the target is found or `left > right`.

**2.5 Return Result:**

Since we found the target at index 4, we return 4.

For a target that doesn't exist, like $target = 2$:
- Iteration 1: `mid = 2`, `nums[2] = 3`, since $3 > 2$, search left: `right = 1`
- Iteration 2: `mid = 0`, `nums[0] = -1`, since $-1 < 2$, search right: `left = 1`
- Iteration 3: `mid = 1`, `nums[1] = 0`, since $0 < 2$, search right: `left = 2`
- Now `left = 2 > right = 1`, so the loop ends
- Return -1 (not found)

> **Note:** The key to binary search is that the array must be sorted. The algorithm works by repeatedly dividing the search space in half, which is why it achieves logarithmic time complexity.


