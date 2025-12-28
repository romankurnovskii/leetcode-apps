## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum possible sum of an array after repeatedly deleting contiguous subarrays whose sum is divisible by k. After each deletion, the remaining elements close the gap.

**1.1 Constraints & Complexity:**

- **Input Size:** Array length n is between 1 and 10^5, each element is between 1 and 10^6, and k is between 1 and 10^5.
- **Time Complexity:** O(n) - we iterate through the array once, performing constant-time operations at each step.
- **Space Complexity:** O(k) - we maintain a dp array of size k to track minimum sums for each remainder.
- **Edge Case:** If the entire array sum is divisible by k, we can delete everything, resulting in sum 0.

**1.2 High-level approach:**

The goal is to minimize the final sum by optimally deleting divisible subarrays. The key insight is that a subarray sum is divisible by k if and only if the prefix sums at its endpoints have the same remainder modulo k.

![Prefix sum remainder visualization](https://assets.leetcode.com/static_assets/others/prefix-remainder.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to delete subarrays recursively. For each position, try all subarrays starting there, check if divisible, delete, and recurse. This requires O(n^3) time in the worst case.
- **Optimized Strategy:** Use dynamic programming with prefix sum remainders. Maintain `dp[r]` as the minimum sum we've seen with remainder r. When we encounter a remainder we've seen before, we can "delete" the subarray between them by resetting to the previous minimum. This is O(n) time and O(k) space.
- **Optimization:** By tracking only the minimum sum for each remainder, we avoid storing all prefix sums and can make optimal deletion decisions in constant time, reducing complexity from O(n^3) to O(n).

**1.4 Decomposition:**

1. Initialize a dp array of size k, where `dp[r]` will store the minimum sum with remainder r. Set `dp[0] = 0` as the base case.
2. Iterate through the array, maintaining a running sum `res`.
3. For each element, add it to `res` and compute the remainder `res % k`.
4. If we've seen this remainder before (i.e., `dp[res % k]` is not infinity), we can delete the subarray between the previous occurrence and now by resetting `res` to the minimum value we've seen with this remainder.
5. Update `dp[res % k]` with the new minimum sum for this remainder.
6. Return the final value of `res`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 1, 1]`, `k = 2`

- Initialize `dp = [0, inf]` (for remainders 0 and 1)
- Initial running sum: `res = 0`

**2.2 Start Checking:**

We begin processing elements one by one, tracking the running sum and its remainder.

**2.3 Trace Walkthrough:**

| Step | Element | res (before) | res (after add) | res % k | dp[0] | dp[1] | Action                    | res (final) |
| ---- | ------- | ------------ | --------------- | ------- | ----- | ----- | ------------------------- | ----------- |
| 0    | -       | 0            | 0               | 0       | 0     | inf   | Initialize                | 0           |
| 1    | 1       | 0            | 1               | 1       | 0     | 1     | Update dp[1] = 1          | 1           |
| 2    | 1       | 1            | 2               | 0       | 0     | 1     | Reset to dp[0] = 0 (delete [1,1]) | 0           |
| 3    | 1       | 0            | 1               | 1       | 0     | 0     | Reset to dp[1] = 0        | 0           |

Wait, let me recalculate. After step 2, res = 2, res % k = 0. We check dp[0] = 0, so we reset res = min(0, 2) = 0. Then we update dp[0] = min(0, 0) = 0.

Actually, let me trace more carefully:

| Step | Element | res (before) | res (after add) | res % k | dp before | Action                    | res (final) | dp after |
| ---- | ------- | ------------ | --------------- | ------- | -------- | ------------------------- | ----------- | -------- |
| 0    | -       | 0            | 0               | 0       | [0,inf]  | Initialize                | 0           | [0,inf]  |
| 1    | 1       | 0            | 1               | 1       | [0,inf]  | res = min(inf, 1) = 1, update dp[1] = 1 | 1           | [0,1]    |
| 2    | 1       | 1            | 2               | 0       | [0,1]    | res = min(0, 2) = 0, update dp[0] = 0 | 0           | [0,1]    |
| 3    | 1       | 0            | 1               | 1       | [0,1]    | res = min(1, 1) = 1, update dp[1] = 1 | 1           | [0,1]    |

Final result: 1 ✓

**2.4 Increment and Loop:**

After processing each element:
- We add it to the running sum.
- We check if we've seen this remainder before by looking up `dp[res % k]`.
- If we have, we can delete the subarray between the previous occurrence and now by resetting to the minimum.
- We update the dp array to track the new minimum for this remainder.

**2.5 Return Result:**

The result is 1, which is the minimum sum after optimally deleting divisible subarrays. We deleted the subarray [1, 1] (sum = 2, divisible by 2), leaving [1] with sum 1.

