## Explanation

### Strategy (The "Why")

Given an array of intervals where `intervals[i] = [start_i, end_i]`, we need to return the minimum number of intervals to remove so that the remaining intervals are non-overlapping.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of intervals $N$ can be up to $10^5$.
- **Value Range:** Start and end values can be between $-5 \times 10^4$ and $5 \times 10^4$.
- **Time Complexity:** $O(n \log n)$ - We sort the intervals by end time, which takes $O(n \log n)$ time. Then we iterate through the sorted intervals once in $O(n)$ time.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables. The sorting is done in-place (or uses $O(\log n)$ space for the sort algorithm).
- **Edge Case:** If there are no intervals or only one interval, we return 0. If all intervals are non-overlapping, we return 0.

**1.2 High-level approach:**

The goal is to find the minimum number of intervals to remove so that no two intervals overlap.

![Interval Overlap Example](https://assets.leetcode.com/uploads/2021/07/12/intervals.jpg)

The key insight is to use a greedy approach: sort intervals by their end time, and always keep the interval that ends earliest when there's an overlap. This maximizes the space available for future intervals.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of intervals to keep, check which combinations are non-overlapping, and find the one that requires removing the fewest intervals. This would be exponential time $O(2^n)$.
- **Optimized Strategy (Greedy):** Sort intervals by end time. Iterate through them, keeping an interval if it doesn't overlap with the last kept interval. This greedy choice (keeping the interval that ends earliest) is optimal.
- **Why it's better:** The greedy approach reduces the problem from exponential time to $O(n \log n)$ time, which is much more efficient. The key insight is that if we want to maximize the number of intervals we can keep, we should always prefer intervals that end earlier, leaving more room for future intervals.

**1.4 Decomposition:**

1. Sort all intervals by their end time (ascending order).
2. Initialize a counter for removed intervals and track the end time of the last kept interval.
3. Iterate through the sorted intervals.
4. For each interval, check if it overlaps with the last kept interval (if its start is less than the last kept interval's end).
5. If there's no overlap, keep the interval and update the last end time.
6. If there's an overlap, remove the current interval (increment the counter).
7. Return the count of removed intervals.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $intervals = [[1,2],[2,3],[3,4],[1,3]]$

First, we sort intervals by end time:
- Sorted: $[[1,2], [2,3], [1,3], [3,4]]$
  - $[1,2]$ ends at 2
  - $[2,3]$ ends at 3
  - $[1,3]$ ends at 3
  - $[3,4]$ ends at 4

We initialize:
- `res = 0` (count of intervals to remove)
- `last_end = -\infty` (end time of last kept interval)

**2.2 Start Checking:**

We begin with the first interval $[1,2]$.

**2.3 Trace Walkthrough:**

| Interval | Start | End | Last End | Overlap? | Action | Res | Last End After |
|----------|-------|-----|----------|----------|--------|-----|----------------|
| $[1,2]$ | 1 | 2 | $-\infty$ | No ($1 \geq -\infty$) | Keep | 0 | 2 |
| $[2,3]$ | 2 | 3 | 2 | No ($2 \geq 2$) | Keep | 0 | 3 |
| $[1,3]$ | 1 | 3 | 3 | Yes ($1 < 3$) | Remove | 1 | 3 |
| $[3,4]$ | 3 | 4 | 3 | No ($3 \geq 3$) | Keep | 1 | 4 |

**2.4 Increment and Loop:**

After processing all intervals:
- We kept: $[1,2]$, $[2,3]$, $[3,4]$
- We removed: $[1,3]$
- Total removed: 1

**2.5 Return Result:**

We return `res = 1`, which is the minimum number of intervals to remove.

> **Note:** The greedy strategy works because if we have two overlapping intervals, we should always keep the one that ends earlier. This leaves more room for future intervals and maximizes the number of intervals we can keep.


