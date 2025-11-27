## Explanation

### Strategy (The "Why")

Given an array `nums`, we need to return a running sum array where `runningSum[i] = sum(nums[0] + nums[1] + ... + nums[i])`.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $1000$.
- **Value Range:** Array elements are between $-10^6$ and $10^6$.
- **Time Complexity:** $O(n)$ - We iterate through the array once.
- **Space Complexity:** $O(n)$ - We create a result array of size $n$ (output space doesn't count as extra space, but we're creating a new array).
- **Edge Case:** If the array has only one element, return that element. If all elements are 0, return an array of zeros.

**1.2 High-level approach:**

The goal is to compute the prefix sum (running sum) of the array.

We iterate through the array, maintaining a running sum. For each element, we add it to the running sum and append the result to our output array.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each position, sum all elements from the beginning. This takes $O(n^2)$ time.
- **Optimized Strategy (Prefix Sum):** Maintain a running sum and add each element to it. This takes $O(n)$ time.
- **Why it's better:** The prefix sum approach reduces time complexity from $O(n^2)$ to $O(n)$ by reusing the previous sum instead of recalculating it for each position.

**1.4 Decomposition:**

1. Initialize an empty result array and a running sum variable set to 0.
2. Iterate through each element in the input array.
3. Add the current element to the running sum.
4. Append the running sum to the result array.
5. Return the result array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1,2,3,4]$

We initialize:
- `res = []`
- `current_sum = 0`

**2.2 Start Processing:**

We iterate through each element.

**2.3 Trace Walkthrough:**

| i | nums[i] | current_sum Before | current_sum After | res |
|---|---------|-------------------|-------------------|-----|
| 0 | 1 | 0 | $0 + 1 = 1$ | [1] |
| 1 | 2 | 1 | $1 + 2 = 3$ | [1, 3] |
| 2 | 3 | 3 | $3 + 3 = 6$ | [1, 3, 6] |
| 3 | 4 | 6 | $6 + 4 = 10$ | [1, 3, 6, 10] |

**2.4 Final Result:**

After processing all elements: `res = [1, 3, 6, 10]`

**2.5 Return Result:**

We return `[1, 3, 6, 10]`, which represents the running sums.

> **Note:** The key insight is that the running sum at position $i$ equals the running sum at position $i-1$ plus the current element. This allows us to compute each value in $O(1)$ time instead of $O(i)$ time.

