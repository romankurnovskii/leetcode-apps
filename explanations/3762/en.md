## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum number of operations to make all array values equal to k. In each operation, we can select a valid integer h and set all values greater than h to h. A valid h means all values strictly greater than h are identical.

**1.1 Constraints & Complexity:**
- Input size: `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`, `1 <= k <= 100`
- **Time Complexity:** O(n) where n is the length of nums, as we iterate through the array once to collect distinct values
- **Space Complexity:** O(n) in the worst case to store distinct values greater than k
- **Edge Case:** If any element is less than k, it's impossible to make all elements equal to k, so return -1

**1.2 High-level approach:**
The key insight is that we need one operation for each distinct value greater than k. We can reduce values from highest to lowest, and each distinct value requires one operation.

![Greedy reduction visualization](https://assets.leetcode.com/static_assets/others/greedy-algorithm.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible sequences of operations, which would be exponential.
- **Optimized Strategy:** Count the number of distinct values greater than k. This is exactly the number of operations needed, as we can reduce them one by one from highest to lowest.

**1.4 Decomposition:**
1. Check if any element is less than k (impossible case)
2. Collect all distinct values that are greater than k
3. Return the count of distinct values, which equals the number of operations needed

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [5, 2, 5, 4, 5]`, `k = 2`
- Initialize check for values less than k
- Initialize a set to collect distinct values greater than k

**2.2 Start Checking:**
We iterate through the array to check for impossible cases and collect distinct values.

**2.3 Trace Walkthrough:**
Using the example `nums = [5, 2, 5, 4, 5]`, `k = 2`:

| Element | Is < k? | Is > k? | Distinct Set | Action |
|---------|---------|---------|--------------|--------|
| 5 | No | Yes | {5} | Add 5 |
| 2 | No | No | {5} | Skip |
| 5 | No | Yes | {5} | Already in set |
| 4 | No | Yes | {5, 4} | Add 4 |
| 5 | No | Yes | {5, 4} | Already in set |

After processing: distinct values > k = {5, 4}, count = 2

**2.4 Increment and Loop:**
For each element greater than k, we add it to our set of distinct values. The loop continues until all elements are processed.

**2.5 Return Result:**
The result is the number of distinct values greater than k, which is 2. This means we need 2 operations: first reduce 5 to 4, then reduce 4 to 2.
