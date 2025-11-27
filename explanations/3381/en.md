# Problem 3381: Maximum Subarray Sum With Length Divisible by K

**Difficulty:** Medium  
**LeetCode Link:** https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

## Problem Description

You are given an array of integers `nums` and an integer `k`.

Return the **maximum** sum of a **subarray** of `nums`, such that the size of the subarray is **divisible** by `k`.

**Example 1:**

```
Input: nums = [1,2], k = 1
Output: 3
Explanation: The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.
```

**Example 2:**

```
Input: nums = [-1,-2,-3,-4,-5], k = 4
Output: -10
Explanation: The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.
```

**Example 3:**

```
Input: nums = [-5,1,2,-3,4], k = 2
Output: 4
Explanation: The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.
```

**Constraints:**

- `1 <= k <= nums.length <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum sum among all subarrays whose length is divisible by `k`. A subarray from index `i` to `j` (inclusive) has length `j - i + 1`, and we require `(j - i + 1) % k == 0`.

**1.1 Constraints & Complexity:**

- **Input Size:** We have up to $2 \times 10^5$ elements.
- **Time Complexity:** $O(n)$ where $n$ is the array length. We compute prefix sums in one pass and then iterate through positions once.
- **Space Complexity:** $O(n + k)$ for the prefix array and the hash map storing minimum prefix sums for each residue class.
- **Edge Case:** All elements could be negative, so we need to handle negative sums correctly.

**1.2 High-level approach:**

The goal is to use prefix sums and the key insight that for a subarray from index `i` to `j`, if `(j - i + 1) % k == 0`, then `(j + 1) % k == i % k`. This means we can group prefix sums by their residue modulo `k` and find the maximum difference within each group.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all possible subarrays by fixing start and end positions, verify if length is divisible by `k`, and calculate the sum. This is $O(n^2)$ time.
- **Optimized Strategy:** Use prefix sums and maintain the minimum prefix sum for each residue class `(index % k)`. For each position, check the sum using the minimum prefix sum from the same residue class. This is $O(n)$ time.
- **Optimization:** By grouping positions by their residue modulo `k`, we can efficiently find valid subarrays without checking all pairs, reducing time complexity from $O(n^2)$ to $O(n)$.

**1.4 Decomposition:**

1. Calculate prefix sums where `prefix[i]` represents the sum of elements from index 0 to `i-1`.
2. For each position `i`, determine its residue class `r = i % k`.
3. Maintain the minimum prefix sum seen so far for each residue class.
4. For each position, calculate the subarray sum ending at `i-1` using `prefix[i] - min_prefix[r]`.
5. Track the maximum sum found across all valid subarrays.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `nums = [-5, 1, 2, -3, 4]`, `k = 2`.

- Prefix sums: `[0, -5, -4, -2, -5, -1]`
  - `prefix[0] = 0` (empty array)
  - `prefix[1] = -5` (sum of `[-5]`)
  - `prefix[2] = -4` (sum of `[-5, 1]`)
  - `prefix[3] = -2` (sum of `[-5, 1, 2]`)
  - `prefix[4] = -5` (sum of `[-5, 1, 2, -3]`)
  - `prefix[5] = -1` (sum of all elements)

- Initialize `min_prefix = {0: 0}` (prefix[0] = 0 has residue 0)
- Initialize `res = -inf`

**2.2 Start Checking:**

We begin with `i = 1` (position 1, residue `1 % 2 = 1`).

**2.3 Trace Walkthrough:**

| Position i | Residue r | prefix[i] | min_prefix[r] | Current Sum | Update min_prefix | `res` |
|-----------|-----------|-----------|----------------|-------------|-------------------|-------|
| 1         | 1         | -5        | Not found      | -           | `{0: 0, 1: -5}`   | -inf  |
| 2         | 0         | -4        | 0              | -4 - 0 = -4 | `{0: 0, 1: -5}`   | -4    |
| 3         | 1         | -2        | -5             | -2 - (-5) = 3 | `{0: 0, 1: -5}`   | 3     |
| 4         | 0         | -5        | 0              | -5 - 0 = -5 | `{0: 0, 1: -5}`   | 3     |
| 5         | 1         | -1        | -5             | -1 - (-5) = 4 | `{0: 0, 1: -5}`   | 4     |

**2.4 Increment and Loop:**

After processing each position, we move to the next position until all positions have been processed.

**2.5 Return Result:**

After processing all positions, `res = 4`, which corresponds to the subarray `[1, 2, -3, 4]` (indices 1 to 4, length 4, divisible by 2) with sum 4.

