## Explanation

### Strategy (The "Why")

Given a circular integer array `nums`, we need to find the maximum possible sum of a non-empty subarray. The array is circular, meaning the next element of `nums[nums.length - 1]` is `nums[0]`.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be up to $3 \times 10^4$.
- **Value Range:** Each element can be between $-3 \times 10^4$ and $3 \times 10^4$.
- **Time Complexity:** $O(n)$ - We iterate through the array once to compute both maximum and minimum subarray sums.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables.
- **Edge Case:** If all numbers are negative, the maximum subarray is the single largest element (normal case, not circular).

**1.2 High-level approach:**

The goal is to find the maximum subarray sum in a circular array.

![Circular Subarray](https://assets.leetcode.com/uploads/2023/02/15/image-20230215164738-2.png)

There are two cases: (1) the maximum subarray is in the middle (normal case), or (2) the maximum subarray wraps around (circular case). For the circular case, we find the minimum subarray sum and subtract it from the total sum.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subarrays, including wrapping ones. This would take $O(n^2)$ time.
- **Optimized Strategy (Kadane's Variant):** Use Kadane's algorithm to find both maximum and minimum subarray sums in one pass. The answer is the maximum of: (normal maximum) or (total sum - minimum subarray).
- **Why it's better:** The optimized approach reduces time complexity from $O(n^2)$ to $O(n)$ by computing both cases in a single pass.

**1.4 Decomposition:**

1. Compute the normal maximum subarray sum using Kadane's algorithm.
2. Compute the minimum subarray sum (for the circular case).
3. Calculate the total sum of all elements.
4. If all numbers are negative, return the normal maximum.
5. Otherwise, return the maximum of: (normal maximum) or (total sum - minimum).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [5,-3,5]$

We initialize:
- `max_sum = 5`, `current_max = 0`
- `min_sum = 5`, `current_min = 0`
- `total_sum = 0`

**2.2 Start Processing:**

We iterate through each element.

**2.3 Trace Walkthrough:**

| Element | current_max | max_sum | current_min | min_sum | total_sum |
|---------|-------------|---------|-------------|---------|-----------|
| 5 | $max(0+5, 5) = 5$ | 5 | $min(0+5, 5) = 5$ | 5 | 5 |
| -3 | $max(5-3, -3) = 2$ | 5 | $min(5-3, -3) = -3$ | -3 | 2 |
| 5 | $max(2+5, 5) = 7$ | 7 | $min(-3+5, 5) = 2$ | -3 | 7 |

**2.4 Calculate Result:**

- Normal maximum: `max_sum = 7`
- Circular case: `total_sum - min_sum = 7 - (-3) = 10`
- Result: `max(7, 10) = 10`

The circular subarray that gives 10: $[5, -3, 5]$ wraps to include all elements.

**2.5 Return Result:**

We return 10, which is the maximum circular subarray sum.

> **Note:** The circular case works because if we remove the minimum subarray from the middle, the remaining elements (which wrap around) form the maximum circular subarray.

