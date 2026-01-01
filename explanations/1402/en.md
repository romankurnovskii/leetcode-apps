## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of satisfaction levels for dishes, we need to find the maximum sum of "like-time coefficients" by choosing which dishes to prepare and in what order. The like-time coefficient is calculated as satisfaction[i] * time[i], where time[i] is the order (1-indexed) in which the dish is prepared.

**1.1 Constraints & Complexity:**

- **Input Size:** The satisfaction array can have up to 500 elements, with each satisfaction value between -10^3 and 10^3.
- **Time Complexity:** O(n log n) - we need to sort the array (O(n log n)) and then iterate through it once (O(n)).
- **Space Complexity:** O(1) - we only use a constant amount of extra space for variables.
- **Edge Case:** If all satisfaction values are negative, the maximum sum is 0 (by not preparing any dishes). If all are positive, we should prepare all dishes.

**1.2 High-level approach:**

The goal is to maximize the sum by preparing dishes with higher satisfaction first (since they're multiplied by larger time coefficients). We sort dishes in descending order and greedily add dishes as long as they contribute positively to the total.

![Dish satisfaction visualization](https://assets.leetcode.com/static_assets/others/dish-satisfaction.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subsets of dishes and all possible orderings. This is factorial time complexity, completely impractical.
- **Optimized Strategy:** Sort dishes by satisfaction in descending order, then greedily add dishes while maintaining a cumulative sum. This is O(n log n) time.
- **Optimization:** By sorting and using a greedy approach, we ensure that higher-satisfaction dishes get higher time multipliers, maximizing the total sum efficiently.

**1.4 Decomposition:**

1. Sort the satisfaction array in descending order.
2. Initialize variables to track the cumulative sum and the maximum total.
3. Iterate through the sorted array, adding each dish's satisfaction to the cumulative sum.
4. Add the cumulative sum to the total (this represents the contribution of all dishes up to this point with their time multipliers).
5. If the cumulative sum becomes negative, stop (adding more dishes would decrease the total).
6. Return the maximum total achieved.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `satisfaction = [-1, -8, 0, 5, -9]`

- Sorted array: `[5, 0, -1, -8, -9]`
- Cumulative sum: `prefix_sum = 0`
- Result: `res = 0`

**2.2 Start Checking:**

We begin iterating through the sorted array, adding dishes one by one.

**2.3 Trace Walkthrough:**

| Step | Dish | prefix_sum | prefix_sum after | res before | res after |
| ---- | ---- | ---------- | ---------------- | ---------- | --------- |
| 1    | 5    | 0          | 5                | 0          | 5         |
| 2    | 0    | 5          | 5                | 5          | 10        |
| 3    | -1   | 5          | 4                | 10         | 14        |
| 4    | -8   | 4          | -4               | 14         | Stop      |

**2.4 Increment and Loop:**

After processing each dish, we check if the cumulative sum is still positive. If it becomes negative, we stop.

**2.5 Return Result:**

The result is `14`, which is the maximum like-time coefficient achieved by preparing dishes with satisfaction [5, 0, -1] in that order.

