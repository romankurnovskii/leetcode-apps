## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the length of the longest subarray where the absolute difference between any two elements is at most a given limit. This means the subarray's maximum and minimum values should differ by at most the limit.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be up to 10^5, and each element can be up to 10^9.
- **Time Complexity:** O(n) - we use a sliding window approach where each element is added and removed from the deques at most once.
- **Space Complexity:** O(n) - in the worst case, the deques can store all elements (when the array is strictly increasing or decreasing).
- **Edge Case:** If limit is 0, all elements in the subarray must be the same. If the entire array satisfies the condition, the answer is the array length.

**1.2 High-level approach:**

The goal is to use a sliding window technique with two deques to efficiently track the maximum and minimum values in the current window, allowing us to quickly check if the window satisfies the limit condition.

![Sliding window with deques visualization](https://assets.leetcode.com/static_assets/others/sliding-window-deques.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all possible subarrays and find the maximum and minimum in each, then check if their difference is <= limit. This is O(n³) time.
- **Optimized Strategy:** Use a sliding window with two monotonic deques to track max and min in O(1) amortized time per operation. This is O(n) time.
- **Optimization:** Monotonic deques allow us to maintain max and min in the current window efficiently, avoiding repeated scans of the window.

**1.4 Decomposition:**

1. Initialize two deques: one for tracking maximum (decreasing), one for tracking minimum (increasing).
2. Use a sliding window with left and right pointers.
3. For each new element, maintain the deques by removing elements that are no longer candidates for max/min.
4. If the current window violates the limit (max - min > limit), shrink the window from the left.
5. Update the result with the maximum window size found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [8,2,4,7]`, `limit = 4`

- Array: `[8, 2, 4, 7]`
- Max deque: `max_deque = deque()` (stores indices)
- Min deque: `min_deque = deque()` (stores indices)
- Left pointer: `left = 0`
- Result: `res = 0`

**2.2 Start Checking:**

We begin expanding the window from right = 0.

**2.3 Trace Walkthrough:**

| Step | right | nums[right] | max_deque | min_deque | max-min | Valid? | Action | res |
| ---- | ----- | ----------- | --------- | --------- | ------- | ------ | ------ | --- |
| 1    | 0     | 8           | [0]       | [0]       | 0       | Yes    | Update res | 1 |
| 2    | 1     | 2           | [0]       | [1]       | 6       | No     | Shrink left to 1 | 1 |
| 3    | 1     | 2           | [1]       | [1]       | 0       | Yes    | Update res | 1 |
| 4    | 2     | 4           | [2]       | [1]       | 2       | Yes    | Update res | 2 |
| 5    | 3     | 7           | [3]       | [1]       | 5       | No     | Shrink left to 2 | 2 |
| 6    | 3     | 7           | [3]       | [2]       | 3       | Yes    | Update res | 2 |

**2.4 Increment and Loop:**

After processing each element, we increment `right` and continue until we've processed all elements.

**2.5 Return Result:**

The result is `2`, which is the length of the longest subarray ([2,4] or [4,7]) where the absolute difference is at most 4.

