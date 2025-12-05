## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the power of all subarrays of size k. The power is the maximum element if the subarray contains consecutive integers in ascending order, otherwise -1.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n == nums.length <= 500`, `1 <= nums[i] <= 10^5`, `1 <= k <= n`
- **Time Complexity:** O(n * k) where n is the array length and k is the subarray size, as we check each of the (n-k+1) subarrays and verify k-1 pairs
- **Space Complexity:** O(1) excluding the output array, as we use constant extra space
- **Edge Case:** If k = 1, each single element is a valid subarray with power equal to that element

**1.2 High-level approach:**
For each possible subarray of size k, we check if it's sorted in ascending order and contains consecutive integers. If both conditions are met, the power is the maximum (last) element; otherwise, it's -1.

![Sliding window visualization](https://assets.leetcode.com/static_assets/others/sliding-window.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Extract each subarray, sort it, check if it's consecutive. This would be O(n * k * log k) due to sorting.
- **Optimized Strategy:** For each subarray, check in one pass if elements are sorted and consecutive. This is O(n * k) without sorting overhead.

**1.4 Decomposition:**
1. Iterate through all possible starting positions for subarrays of size k
2. For each subarray, check if elements are in ascending order
3. If sorted, check if elements are consecutive (each element is previous + 1)
4. If both conditions are met, store the maximum element; otherwise store -1

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [1, 2, 3, 4, 3, 2, 5]`, `k = 3`
- Initialize `res = []` to store results
- There are `7 - 3 + 1 = 5` subarrays to check

**2.2 Start Checking:**
We begin checking each subarray starting from index 0.

**2.3 Trace Walkthrough:**
Using the example `nums = [1, 2, 3, 4, 3, 2, 5]`, `k = 3`:

| Start Index | Subarray | Is Sorted? | Is Consecutive? | Power (res) |
|-------------|----------|-------------|-----------------|-------------|
| 0 | [1, 2, 3] | Yes (1≤2≤3) | Yes (1+1=2, 2+1=3) | 3 |
| 1 | [2, 3, 4] | Yes (2≤3≤4) | Yes (2+1=3, 3+1=4) | 4 |
| 2 | [3, 4, 3] | Yes (3≤4≥3) | No (4+1≠3) | -1 |
| 3 | [4, 3, 2] | No (4>3) | N/A | -1 |
| 4 | [3, 2, 5] | No (3>2) | N/A | -1 |

**2.4 Increment and Loop:**
After checking each subarray, we move to the next starting position and repeat the process until all subarrays are processed.

**2.5 Return Result:**
After processing all subarrays, `res = [3, 4, -1, -1, -1]`, which represents the power of each subarray of size k.

