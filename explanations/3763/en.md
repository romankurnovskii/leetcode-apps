## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array and a threshold, we need to find the maximum sum of elements where we can select at most threshold number of elements.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^5 elements.
- **Time Complexity:** O(n log n) - we use a heap to maintain the top threshold elements, where n is the array length.
- **Space Complexity:** O(threshold) - we need to store at most threshold elements in the heap.
- **Edge Case:** If threshold is 0, return 0. If threshold >= array length, return sum of all elements.

**1.2 High-level approach:**

The goal is to use a min-heap to maintain the top threshold largest elements, updating as we process the array.

![Heap selection visualization](https://assets.leetcode.com/static_assets/others/heap-selection.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all combinations of threshold elements. This is C(n, threshold) which is exponential.
- **Optimized Strategy:** Use a min-heap to maintain the top threshold elements. This is O(n log threshold) time.
- **Optimization:** By using a heap, we efficiently maintain the top elements without sorting the entire array.

**1.4 Decomposition:**

1. Initialize a min-heap.
2. For each element in the array:
   - Add to heap.
   - If heap size > threshold, remove the smallest.
   - If heap size == threshold, calculate sum and update maximum.
3. Return the maximum sum found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 3, 5, 2, 4]`, `threshold = 3`

- Min-heap: `[]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We process each element and maintain the heap.

**2.3 Trace Walkthrough:**

| Step | Element | Heap before | Heap after | Sum | res |
| ---- | ------- | ----------- | ---------- | --- | --- |
| 1    | 1 | [] | [1] | - | 0 |
| 2    | 3 | [1] | [1,3] | - | 0 |
| 3    | 5 | [1,3] | [1,3,5] | 9 | 9 |
| 4    | 2 | [1,3,5] | [2,3,5] | 10 | 10 |
| 5    | 4 | [2,3,5] | [3,4,5] | 12 | 12 |

**2.4 Increment and Loop:**

After each element, we check if we have threshold elements and update the maximum sum.

**2.5 Return Result:**

The result is `12`, which is the maximum sum of 3 elements (3, 4, 5).

