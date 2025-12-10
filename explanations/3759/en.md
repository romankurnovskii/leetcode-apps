## Explanation

### Strategy

**1.1 Constraints & Complexity:**

- **Constraints:** The array `nums` has length `n` where `1 <= n <= 10^5`. Values range from `1` to `10^9`, and `0 <= k < n`.
- **Time Complexity:** O(n log n) - We sort the array once, then iterate through distinct values using binary search, which is O(n log n) overall.
- **Space Complexity:** O(n) - We create a sorted copy of the array.
- **Edge Case:** If `k = 0`, all elements except the maximum are qualified. If all elements are equal, no element is qualified.

**1.2 High-level approach:**

The goal is to count how many elements have at least `k` elements strictly greater than them.

We sort the array first, which allows us to efficiently determine how many elements are greater than any given value. For each distinct value, we count how many elements are strictly greater, and if that count is at least `k`, we add all occurrences of that value to our result.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each element, count how many other elements are strictly greater by comparing with all other elements. This takes O(n^2) time.
- **Optimized Strategy:** Sort the array first. Then for each distinct value, use binary search to find the first element strictly greater than it. The number of greater elements is `n - upper_bound_index`. This reduces the time complexity to O(n log n).

**1.4 Decomposition:**

1. Sort the array to enable efficient binary search.
2. Iterate through distinct values in the sorted array.
3. For each distinct value, count its occurrences.
4. Use binary search to find the first element strictly greater than the current value.
5. If the number of greater elements is at least `k`, add the count of current value to the result.
6. Move to the next distinct value and repeat.

  * **Brute Force:** For each element, count how many other elements are strictly greater by comparing with all other elements. This takes O(n^2) time.
  * **Optimized Strategy:** Sort the array first. Then for each distinct value, use binary search to find the first element strictly greater than it. The number of greater elements is `n - upper_bound_index`. This reduces the time complexity to O(n log n).

**2.1 Initialization & Example Setup:**

Let's use the example `nums = [3, 1, 2]`, `k = 1` to trace through the solution.

We sort the array: `sorted_nums = [1, 2, 3]`, and initialize `res = 0`.

**2.2 Start Checking/Processing:**

We iterate through distinct values, starting with the smallest value `1` at index 0.

**2.3 Trace Walkthrough:**

| Current Value | Count | Upper Bound Search                       | Greater Count | >= k?        | Add to res? | res |
| ------------- | ----- | ---------------------------------------- | ------------- | ------------ | ----------- | --- |
| 1 (index 0)   | 1     | Binary search finds first > 1 at index 1 | 3 - 1 = 2     | Yes (2 >= 1) | Yes, add 1  | 1   |
| 2 (index 1)   | 1     | Binary search finds first > 2 at index 2 | 3 - 2 = 1     | Yes (1 >= 1) | Yes, add 1  | 2   |
| 3 (index 2)   | 1     | Binary search finds first > 3 (none)     | 3 - 3 = 0     | No (0 < 1)   | No          | 2   |

**2.4 Increment and Loop:**

After processing each distinct value, we move to the next distinct value by skipping all occurrences of the current value.

**2.5 Return Result:**

The final result is `2`, meaning 2 elements (1 and 2) have at least `k = 1` element strictly greater than them.
