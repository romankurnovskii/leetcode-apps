## Explanation

### Strategy (The "Why")

We need to find the first bad version in a series of versions. Given $n$ versions, we need to find the first version that is bad (all versions after it are also bad).

**1.1 Constraints & Complexity:**

- **Input Size:** $n$ can be up to $2^{31} - 1$.
- **Value Range:** Version numbers are between $1$ and $n$.
- **Time Complexity:** $O(\log n)$ - Binary search eliminates half of the remaining versions in each step.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If version 1 is bad, return 1. If only the last version is bad, return $n$.

**1.2 High-level approach:**

The goal is to find the first bad version using the minimum number of API calls.

![First Bad Version](https://assets.leetcode.com/uploads/2019/01/15/trees.png)

We use binary search. If a version is bad, the first bad version is at that version or earlier. If a version is good, the first bad version is after it.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check versions from 1 to $n$ sequentially until finding the first bad version. This takes $O(n)$ time and $O(n)$ API calls.
- **Optimized Strategy (Binary Search):** Use binary search to eliminate half of the remaining versions at each step. This takes $O(\log n)$ time and $O(\log n)$ API calls.
- **Why it's better:** Binary search reduces the number of API calls from potentially $n$ to $\log n$, which is a significant improvement for large $n$.

**1.4 Decomposition:**

1. Initialize `left = 1` and `right = n`.
2. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `isBadVersion(mid)` is true, the first bad version is at `mid` or before, so set `right = mid`.
   - Otherwise, the first bad version is after `mid`, so set `left = mid + 1`.
3. Return `left` (which equals `right` at the end).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $n = 5$, first bad version is $4$

We initialize:
- `left = 1`, `right = 5`

**2.2 Start Binary Search:**

We begin checking the middle version.

**2.3 Trace Walkthrough:**

| Iteration | left | right | mid | isBadVersion(mid) | Action |
|-----------|------|-------|-----|-------------------|--------|
| 1 | 1 | 5 | 3 | false | Set `left = 4` |
| 2 | 4 | 5 | 4 | true | Set `right = 4` |
| 3 | 4 | 4 | - | - | `left == right`, exit |

**2.4 Explanation:**

- Mid = 3: Good version, so first bad is after 3 → `left = 4`
- Mid = 4: Bad version, so first bad is at 4 or before → `right = 4`
- `left == right = 4`, so return 4

**2.5 Return Result:**

We return 4, which is the first bad version.

> **Note:** The key difference from standard binary search is that when we find a bad version, we don't exclude it (set `right = mid` instead of `right = mid - 1`) because it might be the first bad version.

