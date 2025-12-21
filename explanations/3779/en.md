## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given an integer array. In one operation, we remove the first three elements (or all remaining if fewer than three). We repeat until the array is empty or contains no duplicate values. We need to find the minimum number of operations required.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 10^5 elements in the array.
- **Time Complexity:** O(n) where n is the length of the array - we process from right to left once.
- **Space Complexity:** O(n) to store the set of seen elements.
- **Edge Case:** If all elements are already distinct, we return 0 without any operations.

**1.2 High-level approach:**

The goal is to process the array from right to left, tracking which elements we've seen. If we encounter a duplicate while going right to left, we know we need to remove elements from the left. The number of operations needed is calculated based on how many elements remain.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Simulate the operations step by step, removing first 3 elements each time and checking for duplicates. This could be O(n^2) in worst case.
- **Optimized Strategy:** Process from right to left, use a set to track seen elements. When we find a duplicate, calculate operations needed: (remaining elements + 2) // 3. This is O(n) time.
- **Optimization:** By processing from right to left, we can determine the answer without actually performing the removals, making the solution much more efficient.

**1.4 Decomposition:**

1. Process the array from right to left.
2. Use a set to track elements we've seen.
3. For each element from right to left:
   - If it's already in the set, we found a duplicate.
   - Calculate operations needed: (remaining elements + 2) // 3.
   - Return the calculated operations.
4. If no duplicates found, return 0.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [3, 8, 3, 6, 5, 8]`

- Start from right: `8` (last element)
- Seen set: `{8}`
- Process right to left

**2.2 Start Processing:**

We begin processing from the rightmost element, adding each to the seen set.

**2.3 Trace Walkthrough:**

| Step | Element | In Seen? | Action | Seen Set | Remaining Elements |
| ---- | ------- | -------- | ------ | -------- | ------------------ |
| 1    | 8 (rightmost) | No | Add to seen | `{8}` | 5 |
| 2    | 5 | No | Add to seen | `{8, 5}` | 4 |
| 3    | 6 | No | Add to seen | `{8, 5, 6}` | 3 |
| 4    | 3 | No | Add to seen | `{8, 5, 6, 3}` | 2 |
| 5    | 8 | Yes | Found duplicate! | `{8, 5, 6, 3}` | 2 |
| 6    | Calculate | - | `(2 + 2) // 3 = 1` | - | - |

When we find duplicate 8 at position 1 (0-indexed), we have 2 elements remaining (indices 0 and 1). Operations needed: (2 + 2) // 3 = 1.

**2.4 Increment and Loop:**

We continue processing from right to left until we find a duplicate or finish processing all elements.

**2.5 Return Result:**

The result is 1, meaning we need 1 operation to remove the first 3 elements, leaving `[6, 5, 8]` which are all distinct.

