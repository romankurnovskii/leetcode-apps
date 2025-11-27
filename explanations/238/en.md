## Explanation

### Strategy (The "Why")

Given an integer array `nums`, we need to return an array `res` such that `res[i]` is equal to the product of all elements of `nums` except `nums[i]`. We must solve it without using the division operator and in $O(n)$ time.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $2$ and $10^5$.
- **Value Range:** Array elements are between $-30$ and $30$.
- **Time Complexity:** $O(n)$ - We make two passes through the array.
- **Space Complexity:** $O(1)$ - We only use the output array and a variable for the right product. The output array doesn't count as extra space.
- **Edge Case:** The product is guaranteed to fit in a 32-bit integer. The array cannot contain zeros in a way that would cause division issues.

**1.2 High-level approach:**

The goal is to compute the product of all elements except the current one.

![Product Except Self](https://assets.leetcode.com/uploads/2021/03/15/product-of-array-except-self.png)

We use two passes: first pass calculates left products (product of all elements to the left), second pass calculates right products and multiplies with left products.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each element, calculate the product of all other elements. This takes $O(n^2)$ time.
- **Optimized Strategy (Two Passes):** First pass: store left products. Second pass: calculate right products on the fly and multiply with left products. This takes $O(n)$ time.
- **Why it's better:** The two-pass approach reduces time complexity from $O(n^2)$ to $O(n)$ by reusing previously computed products instead of recalculating them for each element.

**1.4 Decomposition:**

1. Initialize result array with 1s.
2. First pass (left to right): For each index $i$, `res[i] = product of all elements to the left of i`.
3. Second pass (right to left): Maintain a running right product. For each index $i$, multiply `res[i]` by the right product, then update the right product.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1,2,3,4]$

We initialize:
- `res = [1, 1, 1, 1]`

**2.2 Start First Pass:**

We calculate left products.

**2.3 Trace Walkthrough:**

**First Pass (Left Products):**

| i | nums[i-1] | res[i-1] | res[i] = res[i-1] * nums[i-1] |
|---|-----------|----------|-------------------------------|
| 0 | - | - | 1 (base case) |
| 1 | 1 | 1 | $1 \times 1 = 1$ |
| 2 | 2 | 1 | $1 \times 2 = 2$ |
| 3 | 3 | 2 | $2 \times 3 = 6$ |

After first pass: `res = [1, 1, 2, 6]`

**Second Pass (Right Products):**

| i | right_product Before | res[i] | res[i] *= right_product | right_product After |
|---|---------------------|--------|-------------------------|---------------------|
| 3 | 1 | 6 | $6 \times 1 = 6$ | $1 \times 4 = 4$ |
| 2 | 4 | 2 | $2 \times 4 = 8$ | $4 \times 3 = 12$ |
| 1 | 12 | 1 | $1 \times 12 = 12$ | $12 \times 2 = 24$ |
| 0 | 24 | 1 | $1 \times 24 = 24$ | $24 \times 1 = 24$ |

**2.4 Final Result:**

After both passes: `res = [24, 12, 8, 6]`

Verification:
- $24 = 2 \times 3 \times 4$ (all except 1)
- $12 = 1 \times 3 \times 4$ (all except 2)
- $8 = 1 \times 2 \times 4$ (all except 3)
- $6 = 1 \times 2 \times 3$ (all except 4)

**2.5 Return Result:**

We return `[24, 12, 8, 6]`, which is the product of all elements except self for each position.

> **Note:** The key insight is to separate the problem into left products and right products. We compute left products in the first pass and right products in the second pass, combining them to get the final result.
