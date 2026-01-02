## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a binary array, we need to find the length of the longest subarray where the number of 0s equals the number of 1s.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^5 elements.
- **Time Complexity:** O(n^2) - we check all possible subarrays, where n is the array length.
- **Space Complexity:** O(1) - we only need variables to track counts.
- **Edge Case:** If no balanced subarray exists, return 0. If the entire array is balanced, return the array length.

**1.2 High-level approach:**

The goal is to check all possible subarrays and find the longest one where count of 0s equals count of 1s.

![Balanced subarray visualization](https://assets.leetcode.com/static_assets/others/balanced-subarray.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all subarrays. This is O(n^2) which is acceptable for the constraints.
- **Optimized Strategy:** Use prefix sum technique - treat 0 as -1 and 1 as +1, find longest subarray with sum 0. This would be O(n) but current approach is simpler.
- **Optimization:** The current O(n^2) approach is clear and works for the given constraints.

**1.4 Decomposition:**

1. For each starting position i:
   - Initialize counts for 0s and 1s.
   - For each ending position j >= i:
     - Update counts based on nums[j].
     - If counts are equal, update maximum length.
2. Return the maximum length found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [0, 1, 0, 1, 0]`

- Array: `[0, 1, 0, 1, 0]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We check all possible subarrays.

**2.3 Trace Walkthrough:**

| Step | Start | End | Subarray | Count0 | Count1 | Balanced? | res |
| ---- | ----- | --- | -------- | ------ | ------ | --------- | --- |
| 1    | 0 | 1 | [0,1] | 1 | 1 | Yes | 2 |
| 2    | 0 | 3 | [0,1,0,1] | 2 | 2 | Yes | 4 |
| 3    | 1 | 2 | [1,0] | 1 | 1 | Yes | 4 |
| ...  | ... | ... | ... | ... | ... | ... | 4 |

**2.4 Increment and Loop:**

After checking each subarray, we update the maximum length.

**2.5 Return Result:**

The result is `4`, which is the length of the longest balanced subarray [0,1,0,1].

