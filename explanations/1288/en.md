## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Array length is between 1 and 1000, and interval values are between 0 and 10^5.
- **Time Complexity:** O(n log n) - We sort the intervals, which dominates the time complexity.
- **Space Complexity:** O(1) - We only use a few variables, excluding the input array.
- **Edge Case:** If there's only one interval, return 1.

**1.2 High-level approach:**
The goal is to count intervals that are not covered by any other interval. An interval [a,b) is covered by [c,d) if c <= a and b <= d. We sort intervals by start (ascending) and end (descending), then track the maximum end seen so far.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each interval, check if it's covered by any other interval. This takes O(n^2) time.
- **Optimized Strategy (Sorting):** Sort intervals by start, then by end (descending). If an interval's end is greater than the maximum end seen so far, it's not covered. This takes O(n log n) time.
- **Emphasize the optimization:** Sorting allows us to process intervals in one pass, reducing time complexity from O(n^2) to O(n log n).

**1.4 Decomposition:**
1. Sort intervals by start (ascending), then by end (descending) for same starts.
2. Initialize max_end = -1 and result counter = 0.
3. For each interval, if its end > max_end, it's not covered, so increment counter and update max_end.
4. Return the counter.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `intervals = [[1,4],[3,6],[2,8]]`

After sorting: `[[1,4],[2,8],[3,6]]` (sorted by start, then end descending)

Initialize:
- `max_end = -1`
- `res = 0`

**2.2 Start Checking:**
We iterate through sorted intervals.

**2.3 Trace Walkthrough:**

| Interval | Start | End | End > max_end? | Action | max_end | res |
|----------|-------|-----|----------------|--------|---------|-----|
| [1,4] | 1 | 4 | Yes (4 > -1) | Count, update | 4 | 1 |
| [2,8] | 2 | 8 | Yes (8 > 4) | Count, update | 8 | 2 |
| [3,6] | 3 | 6 | No (6 <= 8) | Skip | 8 | 2 |

**2.4 Return Result:**
The result is 2, meaning [1,4] and [2,8] are not covered, while [3,6] is covered by [2,8].

