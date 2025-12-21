## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given an integer array `nums` and an integer `k`. We need to find the absolute difference between the sum of the k largest elements and the sum of the k smallest elements.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 100 elements in the array, each value between 1 and 100.
- **Time Complexity:** O(n log n) where n is the length of nums - we need to sort the array, which dominates the time complexity.
- **Space Complexity:** O(1) if we sort in-place, or O(n) if we create a sorted copy.
- **Edge Case:** If k equals the array length, we're comparing the sum of all elements with itself, so the result is 0.

**1.2 High-level approach:**

The goal is to sort the array, then take the k largest elements (from the end) and k smallest elements (from the beginning), sum them separately, and return the absolute difference.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find the k largest and k smallest elements by scanning the array multiple times, which would be O(n × k) time.
- **Optimized Strategy:** Sort the array once, then directly access the first k and last k elements. This is O(n log n) time.
- **Optimization:** Sorting allows us to efficiently access the k smallest and k largest elements in sorted order, making the solution simple and efficient.

**1.4 Decomposition:**

1. Sort the array in ascending order.
2. Calculate the sum of the k smallest elements (first k elements).
3. Calculate the sum of the k largest elements (last k elements).
4. Return the absolute difference between these two sums.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [5, 2, 2, 4]`, `k = 2`

- Original array: `[5, 2, 2, 4]`
- After sorting: `[2, 2, 4, 5]`

**2.2 Start Processing:**

We sort the array to easily access the smallest and largest elements.

**2.3 Trace Walkthrough:**

| Step | Operation | Value | Description |
| ---- | --------- | ----- | ----------- |
| 1    | Sort array | `[2, 2, 4, 5]` | Sort in ascending order |
| 2    | k smallest | `[2, 2]` | First k=2 elements |
| 3    | Sum smallest | `2 + 2 = 4` | Sum of k smallest |
| 4    | k largest | `[4, 5]` | Last k=2 elements |
| 5    | Sum largest | `4 + 5 = 9` | Sum of k largest |
| 6    | Difference | `abs(9 - 4) = 5` | Absolute difference |

**2.4 Increment and Loop:**

This is a single-pass operation after sorting, with no additional loop needed.

**2.5 Return Result:**

The result is 5, which is the absolute difference between the sum of the 2 largest elements (9) and the sum of the 2 smallest elements (4).
