## Explanation

### Strategy (The "Why")

Given an integer array `nums`, we need to move all 0's to the end while maintaining the relative order of non-zero elements. We must do this in-place without making a copy of the array.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be up to $10^4$.
- **Value Range:** Array elements can be between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(n)$ - We iterate through the array once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If there are no zeros, the array remains unchanged. If all elements are zeros, they all stay at the end.

**1.2 High-level approach:**

The goal is to move all zeros to the end while preserving the order of non-zero elements.

![Move Zeroes](https://assets.leetcode.com/uploads/2020/09/14/move-zeroes.gif)

We use two pointers: one to iterate through the array, and one to track the next position for a non-zero element. When we find a non-zero, we swap it to the next non-zero position.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Create a new array, copy non-zeros first, then fill with zeros. This takes $O(n)$ time and $O(n)$ space.
- **Optimized Strategy (Two Pointers):** Use two pointers to swap non-zero elements to the front in-place. This takes $O(n)$ time and $O(1)$ space.
- **Why it's better:** The two-pointer approach maintains $O(1)$ space complexity while still being $O(n)$ time, and it's done in-place as required.

**1.4 Decomposition:**

1. Initialize a pointer `next_non_zero` to track the next position for a non-zero element (starts at 0).
2. Iterate through the array with pointer `i`.
3. If `nums[i] != 0`, swap it with `nums[next_non_zero]` and increment `next_non_zero`.
4. After iteration, all non-zeros are at the front, and zeros are at the end.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [0,1,0,3,12]$

We initialize:
- `next_non_zero = 0`

**2.2 Start Processing:**

We iterate through each element.

**2.3 Trace Walkthrough:**

| i | nums[i] | next_non_zero | Action | Array After |
|---|---------|----------------|--------|-------------|
| 0 | 0 | 0 | Skip (zero) | $[0,1,0,3,12]$ |
| 1 | 1 | 0 | Swap, increment | $[1,0,0,3,12]$ |
| 2 | 0 | 1 | Skip (zero) | $[1,0,0,3,12]$ |
| 3 | 3 | 1 | Swap, increment | $[1,3,0,0,12]$ |
| 4 | 12 | 2 | Swap, increment | $[1,3,12,0,0]$ |

**2.4 Final State:**

After processing:
- Non-zeros: $[1,3,12]$ at positions 0, 1, 2
- Zeros: $[0,0]$ at positions 3, 4

**2.5 Return Result:**

The array is modified in-place to $[1,3,12,0,0]$ with all zeros at the end.

> **Note:** The two-pointer technique ensures that we maintain the relative order of non-zero elements while moving zeros to the end. Each non-zero element is placed in its correct position as we encounter it.
