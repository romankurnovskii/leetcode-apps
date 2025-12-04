## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nums.length <= 10^5`.
- **Time Complexity:** O(n) - we make two passes: one to find dominant element, one to check splits.
- **Space Complexity:** O(1) - we use constant space for frequency tracking.
- **Edge Case:** No valid split exists, return -1.

**1.2 High-level approach:**
The goal is to find the minimum index where we can split the array such that both parts have the same dominant element. We first find the dominant element, then check each possible split point.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each split, count frequencies in both parts - O(n²) time.
- **Optimized Strategy:** Find dominant element once, then track left frequency as we iterate - O(n) time.

**1.4 Decomposition:**
1. Find the dominant element and its total frequency.
2. Iterate through possible split indices.
3. Track the frequency of the dominant element in the left subarray.
4. Calculate the frequency in the right subarray.
5. Check if the dominant element is dominant in both subarrays.
6. Return the minimum valid index.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `nums = [1,2,2,2]`. The dominant element is 2 with frequency 3.

**2.2 Start Checking:**
We check splits at indices 0, 1, 2.

**2.3 Trace Walkthrough:**

| Split | Left | Right | Left Dom? | Right Dom? | Valid? |
|-------|------|-------|-----------|------------|--------|
| 0 | [1] | [2,2,2] | No (1/1 not > 1/2) | Yes (3/3 > 3/2) | No |
| 1 | [1,2] | [2,2] | No (1/2 not > 2/2) | Yes (2/2 > 2/2) | No |
| 2 | [1,2,2] | [2] | Yes (2/3 > 3/2) | Yes (1/1 > 1/2) | Yes |

**2.4 Increment and Loop:**
After checking each split, we move to the next index.

**2.5 Return Result:**
Return `res = 2`, the minimum valid split index.

