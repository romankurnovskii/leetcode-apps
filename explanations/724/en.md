## Explanation

### Strategy (The "Why")

Given an array of integers `nums`, we need to find the "pivot index" where the sum of all elements to the left equals the sum of all elements to the right. If no such index exists, return -1.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be up to $10^4$.
- **Value Range:** Each element can be between $-1000$ and $1000$.
- **Time Complexity:** $O(n)$ - We iterate through the array once, calculating the total sum in $O(n)$ and then checking each index in a single pass.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables like `total_sum`, `left_sum`, and `right_sum`.
- **Edge Case:** If the array is empty or has only one element, we need to handle it appropriately. Also, the pivot index can be at index 0 (left sum is 0) or at the last index (right sum is 0).

**1.2 High-level approach:**

The goal is to find an index where the sum of elements to the left equals the sum of elements to the right.

![Pivot Index Visualization](https://assets.leetcode.com/uploads/2021/11/23/pivot1.jpg)

We can calculate the total sum of the array first. Then, as we iterate through each index, we can compute the right sum by subtracting the left sum and the current element from the total sum. This avoids recalculating sums repeatedly.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each index $i$, calculate the sum of elements from index 0 to $i-1$ (left sum) and from index $i+1$ to the end (right sum). This requires $O(n^2)$ time because for each index, we iterate through the array again to calculate sums.
- **Optimized Strategy:** Calculate the total sum once in $O(n)$. Then, maintain a running left sum as we iterate. For each index, compute the right sum as `total_sum - left_sum - nums[i]`. This gives us $O(n)$ time complexity.
- **Why it's better:** We trade a small amount of space (storing the total sum) for a significant time improvement, reducing from quadratic to linear time.

**1.4 Decomposition:**

1. Calculate the total sum of all elements in the array.
2. Initialize a variable to track the left sum (starts at 0).
3. Iterate through each index of the array.
4. For each index, calculate the right sum using the formula: `right_sum = total_sum - left_sum - current_element`.
5. If left sum equals right sum, return the current index.
6. Otherwise, add the current element to the left sum and continue.
7. If no pivot index is found after checking all indices, return -1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1, 7, 3, 6, 5, 6]$

First, we calculate the total sum:
- Total sum = $1 + 7 + 3 + 6 + 5 + 6 = 28$

We initialize:
- `left_sum = 0`
- We'll iterate through indices 0 to 5

**2.2 Start Checking:**

We begin at index 0. At this point, `left_sum = 0`.

**2.3 Trace Walkthrough:**

| Index | Element | Left Sum | Right Sum Calculation | Right Sum | Equal? | Action |
|-------|---------|----------|----------------------|-----------|--------|--------|
| 0 | 1 | 0 | $28 - 0 - 1 = 27$ | 27 | No | Add 1 to left_sum |
| 1 | 7 | 1 | $28 - 1 - 7 = 20$ | 20 | No | Add 7 to left_sum |
| 2 | 3 | 8 | $28 - 8 - 3 = 17$ | 17 | No | Add 3 to left_sum |
| 3 | 6 | 11 | $28 - 11 - 6 = 11$ | 11 | **Yes** | **Return 3** |

At index 3:
- Left sum = $1 + 7 + 3 = 11$
- Right sum = $5 + 6 = 11$
- They are equal, so index 3 is the pivot index.

**2.4 Increment and Loop:**

If we hadn't found a match at index 3, we would continue:
- At index 4: `left_sum = 17`, `right_sum = 28 - 17 - 5 = 6` (not equal)
- At index 5: `left_sum = 22`, `right_sum = 28 - 22 - 6 = 0` (not equal)

**2.5 Return Result:**

Since we found that at index 3, the left sum (11) equals the right sum (11), we return 3.

> **Note:** The pivot index can be at index 0 if the sum of all other elements is 0. Similarly, it can be at the last index if the sum of all previous elements is 0.


