## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum score over all valid split indices. For a split at index i, the score is `prefixSum(i) - suffixMin(i)`, where `prefixSum(i)` is the sum of elements from index 0 to i, and `suffixMin(i)` is the minimum value from index i+1 to the end.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length n is between 2 and 10^5, and each element is between -10^9 and 10^9.
- **Time Complexity:** O(n) - we make two passes: one to compute suffix minimums (right to left) and one to compute prefix sums and scores (left to right).
- **Space Complexity:** O(n) - we store the suffix minimum array of length n.
- **Edge Case:** When n = 2, there's only one valid split at index 0.

**1.2 High-level approach:**

The goal is to efficiently compute prefix sums and suffix minimums for all split positions, then find the maximum score. We precompute suffix minimums in one pass, then iterate through split positions while maintaining a running prefix sum.

![Prefix sum and suffix minimum visualization](https://assets.leetcode.com/static_assets/others/prefix-suffix.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each split index i, calculate prefixSum by summing elements 0 to i, and calculate suffixMin by finding the minimum in elements i+1 to n-1. This requires O(n^2) time as we repeatedly scan the array.
- **Optimized Strategy:** Precompute suffix minimums in one pass from right to left, then iterate from left to right maintaining a running prefix sum. For each split index, we can compute the score in O(1) time. This is O(n) time and O(n) space.
- **Optimization:** By precomputing suffix minimums and using a running prefix sum, we avoid redundant calculations and reduce time complexity from O(n^2) to O(n).

**1.4 Decomposition:**

1. Precompute suffix minimums: iterate from right to left, storing the minimum value from each position to the end.
2. Initialize the result with the score at split index 0.
3. Iterate through split indices from 1 to n-2:
   - Add the current element to the running prefix sum.
   - Calculate the score: `prefixSum - suffixMin[i+1]`.
   - Update the maximum score.
4. Return the maximum score found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [10, -1, 3, -4, -5]`

- Array length: `n = 5`
- Valid split indices: 0, 1, 2, 3 (since we need at least one element on each side)

**2.2 Start Checking:**

First, we precompute suffix minimums from right to left.

**2.3 Trace Walkthrough:**

**Step 1: Precompute suffix minimums**
| i   | nums[i] | suffixMin[i] | Calculation              |
| --- | ------ | ------------ | ------------------------ |
| 4   | -5     | -5           | suffixMin[4] = nums[4]  |
| 3   | -4     | -5           | min(-4, -5) = -5         |
| 2   | 3      | -5           | min(3, -5) = -5          |
| 1   | -1     | -5           | min(-1, -5) = -5         |

**Step 2: Calculate scores for each split**
| Split i | prefixSum | suffixMin[i+1] | Score (prefixSum - suffixMin) | res (max so far) |
| ------- | --------- | -------------- | ----------------------------- | ---------------- |
| 0       | 10        | -5             | 10 - (-5) = 15                | 15               |
| 1       | 9         | -5             | 9 - (-5) = 14                 | 15               |
| 2       | 12        | -5             | 12 - (-5) = 17                | 17               |
| 3       | 8         | -5             | 8 - (-5) = 13                 | 17               |

**2.4 Increment and Loop:**

After precomputing suffix minimums, we iterate through split indices from left to right. For each split index i:
- We add `nums[i]` to our running prefix sum.
- We look up `suffixMin[i+1]` from our precomputed array.
- We calculate the score and update the maximum.

**2.5 Return Result:**

The result is 17, which is the maximum score achieved at split index 2. We verify: `prefixSum(2) = 10 + (-1) + 3 = 12`, `suffixMin(2) = min(-4, -5) = -5`, so `score(2) = 12 - (-5) = 17`.

