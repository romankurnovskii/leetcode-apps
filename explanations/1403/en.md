## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of positive integers, we need to find the smallest subsequence (in non-increasing order) such that the sum of the subsequence is strictly greater than the sum of the remaining elements.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 500 elements, with each element between 1 and 100.
- **Time Complexity:** O(n log n) - we need to sort the array (O(n log n)) and then iterate through it once (O(n)).
- **Space Complexity:** O(n) - we need to store the result subsequence, which can be up to n elements.
- **Edge Case:** If the array has only one element, that element is the answer. If all elements are equal, we need at least half plus one elements.

**1.2 High-level approach:**

The goal is to select the largest elements first (to minimize the subsequence size) until their sum exceeds half of the total sum. This ensures the subsequence sum is greater than the remaining sum.

![Subsequence selection visualization](https://assets.leetcode.com/static_assets/others/subsequence-selection.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subsequences and check which one satisfies the condition with minimum size. This is exponential time.
- **Optimized Strategy:** Sort the array in descending order and greedily add elements until the sum exceeds half of the total. This is O(n log n) time.
- **Optimization:** By sorting and using a greedy approach, we ensure we select the minimum number of largest elements needed to satisfy the condition.

**1.4 Decomposition:**

1. Sort the array in descending order.
2. Calculate the total sum of all elements.
3. Initialize an empty subsequence and its sum.
4. Iterate through the sorted array, adding each element to the subsequence.
5. Check if the subsequence sum is greater than half of the total sum.
6. If yes, return the subsequence; otherwise, continue.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [4, 3, 10, 9, 8]`

- Sorted array: `[10, 9, 8, 4, 3]`
- Total sum: `34`
- Subsequence: `[]`
- Subsequence sum: `0`
- Result variable: `res = []`

**2.2 Start Checking:**

We begin adding elements from the sorted array to the subsequence.

**2.3 Trace Walkthrough:**

| Step | Element | Subsequence | Subsequence Sum | Remaining Sum | Condition | Action |
| ---- | ------- | ----------- | --------------- | ------------- | --------- | ------ |
| 1    | 10     | [10]        | 10              | 24            | 10 > 24? No | Continue |
| 2    | 9      | [10, 9]     | 19              | 15            | 19 > 15? Yes | Return |

**2.4 Increment and Loop:**

After each addition, we check if the condition is satisfied. Once satisfied, we break the loop.

**2.5 Return Result:**

The result is `[10, 9]`, which is the smallest subsequence whose sum (19) is greater than the remaining sum (15).

