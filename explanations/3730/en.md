## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of calories and a window size k, we need to find the maximum sum of calories in any contiguous subarray of length k.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^5 elements.
- **Time Complexity:** O(n) - we use a sliding window approach, where n is the array length.
- **Space Complexity:** O(1) - we only need variables to track the current window sum.
- **Edge Case:** If k equals the array length, return the sum of all elements. If k is 0, return 0.

**1.2 High-level approach:**

The goal is to use a sliding window of size k and find the maximum sum among all windows.

![Sliding window visualization](https://assets.leetcode.com/static_assets/others/sliding-window.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Calculate sum for each window independently. This is O(n * k).
- **Optimized Strategy:** Use sliding window - calculate first window sum, then slide and update by subtracting left element and adding right element. This is O(n) time.
- **Optimization:** By reusing the previous window's sum, we avoid recalculating and solve in linear time.

**1.4 Decomposition:**

1. Calculate the sum of the first k elements.
2. Initialize maximum sum to this value.
3. For each position from k to n-1:
   - Subtract the element leaving the window.
   - Add the element entering the window.
   - Update maximum sum.
4. Return the maximum sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `calories = [1, 2, 3, 4, 5]`, `k = 3`

- First window sum: `1 + 2 + 3 = 6`
- Maximum sum: `res = 6`

**2.2 Start Checking:**

We slide the window and update the sum.

**2.3 Trace Walkthrough:**

| Step | Window | Sum | Action | res |
| ---- | ------ | --- | ------ | --- |
| 1    | [1,2,3] | 6 | Initial | 6 |
| 2    | [2,3,4] | 9 | Remove 1, add 4 | 9 |
| 3    | [3,4,5] | 12 | Remove 2, add 5 | 12 |

**2.4 Increment and Loop:**

After each slide, we update the maximum.

**2.5 Return Result:**

The result is `12`, which is the maximum sum in any window of size 3 (the window [3,4,5]).

