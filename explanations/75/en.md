## Explanation

### Strategy (The "Why")

Given an array `nums` with $n$ objects colored red, white, or blue, we need to sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue (represented by 0, 1, and 2).

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $300$.
- **Value Range:** Array elements are 0, 1, or 2.
- **Time Complexity:** $O(n)$ - We use the Dutch National Flag algorithm, which processes each element at most once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If all elements are the same color, the array is already sorted. If the array has only one element, it's already sorted.

**1.2 High-level approach:**

The goal is to sort an array containing only 0s, 1s, and 2s in one pass.

We use the Dutch National Flag algorithm with three pointers: `left` (end of 0s), `right` (start of 2s), and `i` (current). We swap elements to maintain the invariant: all elements before `left` are 0, all elements after `right` are 2, and elements between are 1.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Count occurrences of 0, 1, and 2, then overwrite the array. This takes two passes.
- **Optimized Strategy (Dutch National Flag):** Use three pointers to sort in one pass. This takes $O(n)$ time in a single pass.
- **Why it's better:** The Dutch National Flag algorithm sorts in one pass instead of two, making it more efficient while maintaining the same time complexity.

**1.4 Decomposition:**

1. Initialize three pointers: `left = 0` (end of 0s), `right = n-1` (start of 2s), `i = 0` (current).
2. While `i <= right`:
   - If `nums[i] == 0`, swap with `nums[left]` and increment both `left` and `i`.
   - If `nums[i] == 2`, swap with `nums[right]` and decrement `right` (don't increment `i`).
   - If `nums[i] == 1`, just increment `i`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [2,0,2,1,1,0]$

We initialize:
- `left = 0`
- `right = 5`
- `i = 0`

**2.2 Start Processing:**

We begin processing elements.

**2.3 Trace Walkthrough:**

| i | nums[i] | Action | nums After | left | right | i After |
|---|---------|--------|-------------|------|-------|---------|
| 0 | 2 | Swap with right | [0,0,2,1,1,2] | 0 | 4 | 0 |
| 0 | 0 | Swap with left | [0,0,2,1,1,2] | 1 | 4 | 1 |
| 1 | 0 | Swap with left | [0,0,2,1,1,2] | 2 | 4 | 2 |
| 2 | 2 | Swap with right | [0,0,1,1,2,2] | 2 | 3 | 2 |
| 2 | 1 | Continue | [0,0,1,1,2,2] | 2 | 3 | 3 |
| 3 | 1 | Continue | [0,0,1,1,2,2] | 2 | 3 | 4 |

**2.4 Final Result:**

After processing: $[0,0,1,1,2,2]$ (sorted)

**2.5 Return Result:**

The array is sorted in-place: $[0,0,1,1,2,2]$.

> **Note:** The key insight of the Dutch National Flag algorithm is to maintain three regions: 0s on the left, 2s on the right, and 1s in the middle. By swapping elements to the correct regions, we sort the array in one pass.

