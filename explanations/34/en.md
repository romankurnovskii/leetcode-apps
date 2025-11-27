## Explanation

### Strategy (The "Why")

Given an array of integers `nums` sorted in non-decreasing order, and a target value, we need to find the starting and ending position of `target` in `nums`. If `target` is not found, return $[-1, -1]$.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $0$ and $10^5$.
- **Value Range:** Array elements and target are between $-10^9$ and $10^9$.
- **Time Complexity:** $O(\log n)$ - We use binary search twice: once to find the first occurrence and once to find the last occurrence.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the target is not in the array, return $[-1, -1]$. If the target appears only once, return $[index, index]$.

**1.2 High-level approach:**

The goal is to find the first and last occurrence of a target in a sorted array.

We use binary search twice: once to find the first occurrence (by continuing to search left when we find the target) and once to find the last occurrence (by continuing to search right when we find the target).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Linear search to find first and last occurrence. This takes $O(n)$ time.
- **Optimized Strategy (Binary Search):** Use binary search to find first and last occurrence. This takes $O(\log n)$ time.
- **Why it's better:** Binary search reduces time complexity from $O(n)$ to $O(\log n)$ by eliminating half of the remaining elements at each step.

**1.4 Decomposition:**

1. Use binary search to find the first occurrence:
   - When we find the target, continue searching left to find an earlier occurrence.
   - When we don't find it, search in the appropriate direction.
2. Use binary search to find the last occurrence:
   - When we find the target, continue searching right to find a later occurrence.
   - When we don't find it, search in the appropriate direction.
3. Return $[first, last]$ or $[-1, -1]$ if not found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [5,7,7,8,8,10]$, $target = 8$

We initialize:
- `left = 0`, `right = 5`

**2.2 Start Searching:**

We begin with finding the first occurrence.

**2.3 Trace Walkthrough:**

**Find First Occurrence:**

| Iteration | left | right | mid | nums[mid] | Action |
|-----------|------|-------|-----|-----------|--------|
| 1 | 0 | 5 | 2 | 7 | $7 < 8$, search right |
| 2 | 3 | 5 | 4 | 8 | Found! Continue left |
| 3 | 3 | 3 | 3 | 8 | Found! Continue left |
| 4 | 3 | 2 | - | - | Exit, first = 3 |

**Find Last Occurrence:**

| Iteration | left | right | mid | nums[mid] | Action |
|-----------|------|-------|-----|-----------|--------|
| 1 | 0 | 5 | 2 | 7 | $7 < 8$, search right |
| 2 | 3 | 5 | 4 | 8 | Found! Continue right |
| 3 | 5 | 5 | 5 | 10 | $10 > 8$, search left |
| 4 | 5 | 4 | - | - | Exit, last = 4 |

**2.4 Final Result:**

- First occurrence: index 3
- Last occurrence: index 4

**2.5 Return Result:**

We return $[3, 4]$, which are the starting and ending positions of target 8.

> **Note:** The key is to modify binary search to continue searching in one direction even after finding the target. For the first occurrence, we continue searching left. For the last occurrence, we continue searching right.

