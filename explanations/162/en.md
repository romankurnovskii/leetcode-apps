## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 1000$ elements. Values are in the range $[-2^{31}, 2^{31} - 1]$. Adjacent elements are guaranteed to be different.
- **Time Complexity:** $O(\log n)$ where $n$ is the array length. We use binary search.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space.
- **Edge Case:** If the array has one element, return index 0. If the array is strictly increasing, return the last index. If strictly decreasing, return index 0.

**1.2 High-level approach:**

The goal is to find a peak element (greater than both neighbors) in $O(\log n)$ time. We use binary search. The key insight is that if `nums[mid] > nums[mid+1]`, there must be a peak in the left half (including mid). Otherwise, there's a peak in the right half.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Scan the array and check each element with its neighbors. This is $O(n)$ time.
- **Optimized Strategy:** Use binary search. Compare `nums[mid]` with `nums[mid+1]` to determine which half contains a peak. This is $O(\log n)$ time.
- **Why optimized is better:** Binary search reduces time complexity from $O(n)$ to $O(\log n)$ by eliminating half of the search space at each step.

**1.4 Decomposition:**

1. Initialize `left = 0` and `right = n - 1`.
2. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] > nums[mid + 1]`, peak is in left half: `right = mid`.
   - Otherwise, peak is in right half: `left = mid + 1`.
3. Return `left` (which equals `right` when loop ends).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1,2,3,1]`

We initialize:
- `left = 0`
- `right = 3`

**2.2 Start Checking:**

We perform binary search to find a peak element.

**2.3 Trace Walkthrough:**

| Iteration | left | right | mid | nums[mid] | nums[mid+1] | Comparison | Action |
|-----------|------|-------|-----|------------|-------------|------------|--------|
| 1 | 0 | 3 | 1 | 2 | 3 | 2 < 3 | left = 2 |
| 2 | 2 | 3 | 2 | 3 | 1 | 3 > 1 | right = 2 |
| 3 | 2 | 2 | - | - | - | left == right | Return 2 |

**2.4 Increment and Loop:**

The binary search logic:
- If `nums[mid] > nums[mid + 1]`: The peak is at `mid` or to the left, so `right = mid`.
- Otherwise: The peak is to the right, so `left = mid + 1`.

This works because:
- If we're on a downward slope (`nums[mid] > nums[mid+1]`), there must be a peak to the left (or `mid` itself if it's greater than its left neighbor).
- If we're on an upward slope (`nums[mid] < nums[mid+1]`), there must be a peak to the right.

**2.5 Return Result:**

When `left == right`, we've found a peak. In our example, `left = 2`, and `nums[2] = 3` is indeed a peak (greater than both `nums[1] = 2` and `nums[3] = 1`). We return `2`.

