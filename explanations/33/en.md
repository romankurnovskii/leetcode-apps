## Explanation

### Strategy (The "Why")

Given an integer array `nums` sorted in ascending order (with distinct values) that is rotated at some pivot, and a target value, we need to search for `target` in `nums`. If `target` exists, return its index, otherwise return -1.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $5000$.
- **Value Range:** Array elements are distinct and between $-10^4$ and $10^4$.
- **Time Complexity:** $O(\log n)$ - We use binary search, eliminating half of the remaining elements at each step.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the array is not rotated (fully sorted), standard binary search works. If the array has only one element, check if it equals the target.

**1.2 High-level approach:**

The goal is to search for a target in a rotated sorted array.

We use binary search, but we need to determine which half is sorted. If the left half is sorted and the target is within that range, search left. Otherwise, search right. Similar logic applies if the right half is sorted.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Linear search through the array. This takes $O(n)$ time.
- **Optimized Strategy (Binary Search):** Use binary search with logic to determine which half contains the target. This takes $O(\log n)$ time.
- **Why it's better:** Binary search reduces time complexity from $O(n)$ to $O(\log n)$ by eliminating half of the remaining elements at each step.

**1.4 Decomposition:**

1. Initialize two pointers at both ends.
2. While left <= right:
   - Calculate mid.
   - If nums[mid] equals target, return mid.
   - Determine which half is sorted (left or right).
   - If left half is sorted and target is in that range, search left. Otherwise, search right.
   - If right half is sorted and target is in that range, search right. Otherwise, search left.
3. Return -1 if not found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [4,5,6,7,0,1,2]$, $target = 0$

We initialize:
- `left = 0`, `right = 6`

**2.2 Start Binary Search:**

We begin searching.

**2.3 Trace Walkthrough:**

| Iteration | left | right | mid | nums[mid] | Sorted Half | Target Range | Action |
|-----------|------|-------|-----|-----------|------------|--------------|--------|
| 1 | 0 | 6 | 3 | 7 | Left (0-3) | Not in [4,7] | Search right |
| 2 | 4 | 6 | 5 | 1 | Right (4-6) | Not in [0,2] | Search left |
| 3 | 4 | 4 | 4 | 0 | - | Found! | Return 4 |

**2.4 Explanation:**

- Mid = 3, nums[3] = 7: Left half [4,5,6,7] is sorted, but target 0 is not in [4,7], so search right.
- Mid = 5, nums[5] = 1: Right half [0,1,2] is sorted, but target 0 is in [0,2], so search left.
- Mid = 4, nums[4] = 0: Found target!

**2.5 Return Result:**

We return 4, which is the index of target 0.

> **Note:** The key insight is that in a rotated sorted array, at least one half is always sorted. By checking which half is sorted and whether the target is in that range, we can determine which half to search, maintaining the $O(\log n)$ time complexity of binary search.

