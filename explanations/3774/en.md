## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the absolute difference between the sum of the k largest elements and the sum of the k smallest elements in an array.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length n is at most 100, and each element is between 1 and 100. k is between 1 and n.
- **Time Complexity:** O(n log n) - dominated by sorting the array.
- **Space Complexity:** O(n) for the sorted array.
- **Edge Case:** If k equals the array length, we're comparing the sum of all elements with itself, so the difference is 0.

**1.2 High-level approach:**

The goal is to sort the array, then calculate the sum of the first k elements (smallest) and the sum of the last k elements (largest), and return their absolute difference.

![Array sorting and selection visualization](https://assets.leetcode.com/static_assets/others/array-sorting.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find k largest and k smallest elements without sorting, which would require multiple passes and be O(n*k) time.
- **Optimized Strategy:** Sort the array once in O(n log n) time, then directly access the first k and last k elements. This is simpler and efficient for the given constraints.
- **Optimization:** Sorting allows us to easily identify the k smallest (first k) and k largest (last k) elements in a single operation.

**1.4 Decomposition:**

1. Sort the array in ascending order.
2. Calculate the sum of the first k elements (smallest k).
3. Calculate the sum of the last k elements (largest k).
4. Return the absolute difference between these two sums.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [5, 2, 2, 4]`, `k = 2`.

- After sorting: `sorted_nums = [2, 2, 4, 5]`

**2.2 Start Processing:**

We calculate the sums of the smallest and largest k elements.

**2.3 Trace Walkthrough:**

| Step | Operation | Values | Result |
|------|-----------|--------|--------|
| 1 | Sort array | [5, 2, 2, 4] | [2, 2, 4, 5] |
| 2 | Sum of k smallest | sorted_nums[:2] = [2, 2] | 2 + 2 = 4 |
| 3 | Sum of k largest | sorted_nums[2:] = [4, 5] | 4 + 5 = 9 |
| 4 | Absolute difference | \|9 - 4\| | 5 |

**2.4 Increment and Loop:**

The calculation is straightforward after sorting - no loops needed for the sum calculation.

**2.5 Return Result:**

The result is 5, which is the absolute difference between the sum of the 2 largest elements (9) and the sum of the 2 smallest elements (4).
