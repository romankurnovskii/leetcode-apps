## Explanation

### Strategy (The "Why")

Given a rotated sorted array of unique integers, we need to find the minimum element. The array was originally sorted in ascending order and then rotated.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $1$ and $5000$.
- **Value Range:** Array elements are unique and between $-5000$ and $5000$.
- **Time Complexity:** $O(\log n)$ - Binary search eliminates half of the remaining elements in each step.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the array has only one element, return that element. If the array is not rotated (sorted), the minimum is at index 0.

**1.2 High-level approach:**

The goal is to find the minimum element in a rotated sorted array.

![Find Minimum](https://assets.leetcode.com/uploads/2020/03/17/minkey.jpg)

We use binary search. The key insight is that if the right half is sorted (nums[mid] < nums[right]), the minimum is in the left half (including mid). Otherwise, the minimum is in the right half.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Iterate through the array to find the minimum. This takes $O(n)$ time.
- **Optimized Strategy (Binary Search):** Use binary search to eliminate half of the remaining elements at each step. This takes $O(\log n)$ time.
- **Why it's better:** Binary search reduces the time complexity from $O(n)$ to $O(\log n)$, which is a significant improvement for large arrays.

**1.4 Decomposition:**

1. Initialize `left = 0` and `right = len(nums) - 1`.
2. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] < nums[right]`, the right half is sorted, so minimum is in the left half (including mid) → set `right = mid`.
   - Otherwise, the minimum is in the right half → set `left = mid + 1`.
3. Return `nums[left]` (which is the minimum).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [3,4,5,1,2]$

We initialize:
- `left = 0`, `right = 4`

**2.2 Start Binary Search:**

We begin checking the middle element.

**2.3 Trace Walkthrough:**

| Iteration | left | right | mid | nums[mid] | nums[right] | Comparison | Action |
|-----------|------|-------|-----|-----------|-------------|------------|--------|
| 1 | 0 | 4 | 2 | 5 | 2 | $5 > 2$ | Set `left = 3` |
| 2 | 3 | 4 | 3 | 1 | 2 | $1 < 2$ | Set `right = 3` |
| 3 | 3 | 3 | - | - | - | `left == right` | Exit |

**2.4 Explanation:**

- Mid = 2, nums[2] = 5, nums[4] = 2: Since $5 > 2$, the right half is not sorted, so minimum is in right half → `left = 3`
- Mid = 3, nums[3] = 1, nums[4] = 2: Since $1 < 2$, the right half is sorted, so minimum is in left half (including mid) → `right = 3`
- `left == right = 3`, so return `nums[3] = 1`

**2.5 Return Result:**

We return 1, which is the minimum element in the rotated array.

> **Note:** The key insight is that in a rotated sorted array, at least one half is always sorted. By comparing `nums[mid]` with `nums[right]`, we can determine which half contains the minimum and eliminate the other half.

