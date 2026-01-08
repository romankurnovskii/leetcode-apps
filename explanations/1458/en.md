# 1458. Max Dot Product of Two Subsequences

You are given two integer arrays `nums1` and `nums2`.

A **subsequence** of an array is obtained by deleting some (possibly zero) elements without changing the order of the remaining elements.

The **dot product** of two arrays of the same length is the sum of the products of corresponding elements.

Your task is to return the **maximum dot product** that can be obtained from **non-empty subsequences** of `nums1` and `nums2`.

---

## Explanation

### Strategy

Let’s restate the problem in simple terms:

- We must pick **at least one pair** of numbers
- The picked numbers must respect the original order
- We want the **maximum possible dot product**

This is a **dynamic programming** problem because:
- We make choices step by step
- Subproblems repeat
- Brute force would be too slow

---

### Key Observations

- At each position, we can:
  1. Take the current pair
  2. Skip an element from `nums1`
  3. Skip an element from `nums2`
- We must ensure **at least one pair is chosen**
- Negative numbers make this tricky — we cannot just return `0`

> **Note:**  
> We use a flag to track whether we have already chosen at least one pair.

---

### Steps

1. Use a recursive function `dp(i, j, took)`
   - `i`: current index in `nums1`
   - `j`: current index in `nums2`
   - `took`: whether we have already chosen a pair

2. Base Case:
   - If we reach the end of either array:
     - If no pair was chosen → return negative infinity
     - Otherwise → return `0`

3. At each step, try:
   - Taking the current pair
   - Skipping `nums1[i]`
   - Skipping `nums2[j]`

4. Memoize results to avoid recomputation

---

> **Note:**  
> Negative infinity ensures we never accept an empty subsequence as a valid answer.

---

**Time Complexity:** `O(m × n)`  
**Space Complexity:** `O(m × n)`
