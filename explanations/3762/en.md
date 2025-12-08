## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to make all array values equal to k using operations. In each operation, we can select a valid integer h and set all values greater than h to h. A valid integer h means all values strictly greater than h are identical.

**1.1 Constraints & Complexity:**
- Input size: `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`
- **Time Complexity:** O(n) where n is the length of nums, as we iterate once to find distinct values
- **Space Complexity:** O(n) for the set storing distinct values greater than k
- **Edge Case:** If any element is less than k, it's impossible to make all elements equal to k, so we return -1

**1.2 High-level approach:**
We count the number of distinct values greater than k. Each distinct value requires one operation to reduce it. The answer is simply the count of distinct values greater than k.

![Array reduction visualization](https://assets.leetcode.com/static_assets/others/array-reduction.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible sequences of operations, which is exponential
- **Optimized Strategy:** Recognize that we need one operation per distinct value greater than k, giving us O(n) time
- **Emphasize the optimization:** We can directly count distinct values without simulating operations

**1.4 Decomposition:**
1. Check if any element is less than k (impossible case)
2. Collect all distinct values that are greater than k
3. Count the number of distinct values
4. Return the count as the minimum number of operations

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [5,2,5,4,5]`, `k = 2`
- Initialize an empty set: `distinct_greater = set()`

**2.2 Start Checking:**
We iterate through each number in the array.

**2.3 Trace Walkthrough:**

| Number | Is > k? | Add to Set? | distinct_greater |
|--------|---------|-------------|------------------|
| 5 | Yes | Yes | {5} |
| 2 | No | No | {5} |
| 5 | Yes | No (already in set) | {5} |
| 4 | Yes | Yes | {5, 4} |
| 5 | Yes | No (already in set) | {5, 4} |

**2.4 Increment and Loop:**
After processing all numbers, we have `distinct_greater = {5, 4}`.

**2.5 Return Result:**
The count of distinct values greater than k is 2, so we need 2 operations. First operation with h=4 reduces 5 to 4, second operation with h=2 reduces 4 to 2. The result is 2.
