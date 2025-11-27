# Problem 724: Find Pivot Index

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/find-pivot-index/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the leftmost index where the sum of all elements to the left equals the sum of all elements to the right. At the pivot index, the element itself is not included in either sum.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most $10^4$ elements, and each element is between -1000 and 1000.
- **Time Complexity:** $O(n)$ where $n$ is the array length. We calculate the total sum in $O(n)$ time, then iterate through the array once.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space to track the left sum.
- **Edge Case:** If the pivot index is at position 0, the left sum is 0 (no elements to the left). Similarly, if at the last position, the right sum is 0.

**1.2 High-level approach:**

The goal is to find an index where the sum of left elements equals the sum of right elements. We can calculate the total sum first, then for each index, check if the left sum equals the right sum (which is total sum minus left sum minus current element).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each index, calculate the left sum and right sum separately by iterating through the array. This is $O(n^2)$ time.
- **Optimized Strategy:** Calculate the total sum once, then maintain a running left sum as we iterate. For each index, the right sum is simply `total_sum - left_sum - nums[i]`. This is $O(n)$ time.
- **Optimization:** By maintaining a running left sum and using the total sum, we avoid recalculating sums for each index, reducing time complexity from $O(n^2)$ to $O(n)$.

**1.4 Decomposition:**

1. Calculate the total sum of all elements in the array.
2. Initialize left sum to 0.
3. For each index from left to right:
   - Check if left sum equals right sum (total_sum - left_sum - nums[i]).
   - If equal, return the current index.
   - Otherwise, add the current element to left sum and continue.
4. If no pivot index is found, return -1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `nums = [1, 7, 3, 6, 5, 6]`.

- Total sum = $1 + 7 + 3 + 6 + 5 + 6 = 28$
- Initialize `left_sum = 0`

**2.2 Start Checking:**

We begin with index `i = 0` and check if it's a pivot index.

**2.3 Trace Walkthrough:**

| Index i | nums[i] | left_sum | Right Sum (total - left - nums[i]) | left_sum == right_sum? | Action |
|---------|---------|----------|-----------------------------------|------------------------|--------|
| 0       | 1       | 0        | 28 - 0 - 1 = 27                   | No (0 ≠ 27)            | Update left_sum = 1 |
| 1       | 7       | 1        | 28 - 1 - 7 = 20                   | No (1 ≠ 20)            | Update left_sum = 8 |
| 2       | 3       | 8        | 28 - 8 - 3 = 17                   | No (8 ≠ 17)            | Update left_sum = 11 |
| 3       | 6       | 11       | 28 - 11 - 6 = 11                  | Yes (11 == 11)         | Return 3 |

**2.4 Increment and Loop:**

After checking each index, we add the current element to `left_sum` and move to the next index until we find a pivot or reach the end.

**2.5 Return Result:**

At index 3, we found that `left_sum = 11` equals `right_sum = 11`, so we return `res = 3`.

