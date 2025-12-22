## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum number of operations to make all elements in an array equal. In each operation, we can choose any subarray and replace all its elements with the bitwise AND of all elements in that subarray.

**1.1 Constraints & Complexity:**

- **Input Size:** Array length can be up to 100, and each element can be up to 10^5.
- **Time Complexity:** O(n) where n is the array length - we need to check if all elements are equal by creating a set.
- **Space Complexity:** O(n) - we create a set to check for distinct elements.
- **Edge Case:** If all elements are already equal, we need 0 operations.

**1.2 High-level approach:**

The goal is to determine if we can make all elements equal, and if so, how many operations are needed. The key insight is that we can always make all elements equal in at most 1 operation by applying the AND operation to the entire array.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subarrays and operations, which would be exponential.
- **Optimized Strategy:** Check if all elements are already equal. If yes, return 0. Otherwise, return 1 because we can apply AND to the entire array in one operation.
- **Optimization:** The bitwise AND operation is idempotent - applying it to the entire array makes all elements equal to the AND of all elements, and applying it again doesn't change anything.

**1.4 Decomposition:**

1. Check if all elements in the array are already equal.
2. If yes, return 0 (no operations needed).
3. If no, return 1 (one operation on the entire array is sufficient).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2]`

- We have 2 elements: 1 and 2.
- They are not equal, so we need at least 1 operation.

**2.2 Start Checking:**

We check if all elements are equal by creating a set and checking its size.

**2.3 Trace Walkthrough:**

| Step | Action | Array State | All Equal? | Operations Needed |
|------|--------|-------------|------------|-------------------|
| 0 | Initial | [1, 2] | No | - |
| 1 | Check distinct values | set([1, 2]) = {1, 2} | No (size > 1) | 1 |
| 2 | Apply AND to entire array | [1 AND 2] = [0, 0] | Yes | 1 |

For `nums = [5, 5, 5]`:
- Initial: [5, 5, 5]
- Check distinct values: set([5, 5, 5]) = {5}
- All equal? Yes (size == 1)
- Operations needed: 0

**2.4 Increment and Loop:**

The algorithm is straightforward - it's a single check with no loops needed after the initial check.

**2.5 Return Result:**

For `nums = [1, 2]`, the result is 1. We apply AND to the entire array, making all elements 0.

For `nums = [5, 5, 5]`, the result is 0 since all elements are already equal.

