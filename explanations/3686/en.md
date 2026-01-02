## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array, we need to count the number of stable subsequences, where stable means all elements in the subsequence are the same.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n^2) - we check all possible subarrays, where n is the array length.
- **Space Complexity:** O(1) - we only need variables for counting.
- **Edge Case:** If the array is empty, return 0. If all elements are the same, all subarrays are stable.

**1.2 High-level approach:**

The goal is to check all possible subarrays and count those where all elements are identical.

![Stable subsequence visualization](https://assets.leetcode.com/static_assets/others/stable-subseq.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all subarrays. This is O(n^2) which is acceptable.
- **Optimized Strategy:** We could optimize by grouping consecutive identical elements, but the current approach is clear.
- **Optimization:** The O(n^2) approach is straightforward for the given constraints.

**1.4 Decomposition:**

1. For each starting position i:
   - For each ending position j >= i:
     - Check if all elements in subarray nums[i:j+1] are the same.
     - If yes, increment count.
2. Return the count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 1, 2, 2]`

- Array: `[1, 1, 2, 2]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We check all possible subarrays.

**2.3 Trace Walkthrough:**

| Step | Start | End | Subarray | All same? | res |
| ---- | ----- | --- | -------- | --------- | --- |
| 1    | 0 | 0 | [1] | Yes | 1 |
| 2    | 0 | 1 | [1,1] | Yes | 2 |
| 3    | 0 | 2 | [1,1,2] | No | 2 |
| 4    | 1 | 1 | [1] | Yes | 3 |
| 5    | 2 | 2 | [2] | Yes | 4 |
| 6    | 2 | 3 | [2,2] | Yes | 5 |
| 7    | 3 | 3 | [2] | Yes | 6 |

**2.4 Increment and Loop:**

After checking each subarray, we update the count.

**2.5 Return Result:**

The result is `6`, which is the number of stable subsequences (all single elements and [1,1] and [2,2]).

