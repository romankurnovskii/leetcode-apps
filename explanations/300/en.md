## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nums.length <= 2500`.
- **Time Complexity:** O(n²) - for each element, we check all previous elements.
- **Space Complexity:** O(n) - we store a DP array of length n.
- **Edge Case:** All elements are in decreasing order, result is 1.

**1.2 High-level approach:**
The goal is to find the length of the longest strictly increasing subsequence. We use dynamic programming where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible subsequences - exponential time.
- **Optimized Strategy:** Dynamic programming - O(n²) time, can be optimized to O(n log n) with binary search.

**1.4 Decomposition:**
1. Initialize DP array where each element is 1 (each element is a subsequence of length 1).
2. For each element, check all previous elements.
3. If a previous element is smaller, update the current DP value.
4. Return the maximum value in the DP array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `nums = [10,9,2,5,3,7,101,18]`. We initialize `dp = [1,1,1,1,1,1,1,1]`.

**2.2 Start Checking:**
We process each element and check previous elements.

**2.3 Trace Walkthrough:**

| i | nums[i] | Check previous | dp[i] |
|---|---------|----------------|-------|
| 0 | 10 | - | 1 |
| 1 | 9 | 10 (not <) | 1 |
| 2 | 2 | 10,9 (not <) | 1 |
| 3 | 5 | 2 (<) | 2 |
| 4 | 3 | 2 (<) | 2 |
| 5 | 7 | 2,5,3 (<) | 3 |
| 6 | 101 | 2,5,3,7 (<) | 4 |
| 7 | 18 | 2,5,3,7 (<) | 4 |

**2.4 Increment and Loop:**
After processing each element, we move to the next.

**2.5 Return Result:**
Return `res = 4`, the maximum value in dp array.

