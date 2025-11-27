## Explanation

### Strategy (The "Why")

Given an array `nums` with $n$ objects colored red, white, or blue, we need to sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We use integers 0, 1, and 2 to represent red, white, and blue respectively.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be up to $300$.
- **Value Range:** Array elements are 0, 1, or 2.
- **Time Complexity:** $O(n)$ - We iterate through the array once with three pointers.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the array is already sorted, no swaps are needed. If the array contains only one color, it's already sorted.

**1.2 High-level approach:**

The goal is to sort the array in-place with only three distinct values.

We use the Dutch National Flag algorithm with three pointers: `left` (end of 0s), `right` (start of 2s), and `i` (current). We swap elements to place them in the correct regions.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Count occurrences of 0, 1, 2, then overwrite the array. This takes $O(n)$ time but requires two passes.
- **Optimized Strategy (Dutch National Flag):** Use three pointers to sort in one pass. This takes $O(n)$ time in a single pass.
- **Why it's better:** The Dutch National Flag algorithm sorts in one pass instead of two, making it more efficient and elegant.

**1.4 Decomposition:**

1. Initialize three pointers: `left = 0` (end of 0s), `right = n-1` (start of 2s), `i = 0` (current).
2. While `i <= right`:
   - If `nums[i] == 0`: swap with `nums[left]`, increment both `left` and `i`.
   - If `nums[i] == 2`: swap with `nums[right]`, decrement `right` (don't increment `i`).
   - If `nums[i] == 1`: just increment `i`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [2,0,2,1,1,0]$

We initialize:
- `left = 0`
- `right = 5`
- `i = 0`

**2.2 Start Sorting:**

We begin processing elements.

**2.3 Trace Walkthrough:**

| Step | i | nums[i] | Action | nums After | left | right |
|------|---|---------|--------|-------------|------|-------|
| 1 | 0 | 2 | Swap with right | [0,0,2,1,1,2] | 0 | 4 |
| 2 | 0 | 0 | Swap with left | [0,0,2,1,1,2] | 1 | 4 |
| 3 | 1 | 0 | Swap with left | [0,0,2,1,1,2] | 2 | 4 |
| 4 | 2 | 2 | Swap with right | [0,0,1,1,2,2] | 2 | 3 |
| 5 | 2 | 1 | Continue | [0,0,1,1,2,2] | 2 | 3 |
| 6 | 3 | 1 | Continue | [0,0,1,1,2,2] | 2 | 3 |

**2.4 Final Result:**

After sorting: $[0,0,1,1,2,2]$

**2.5 Return Result:**

The array is sorted in-place: $[0,0,1,1,2,2]$

> **Note:** The key insight is to maintain three regions: 0s at the left, 1s in the middle, and 2s at the right. We use three pointers to partition the array into these regions in one pass.

