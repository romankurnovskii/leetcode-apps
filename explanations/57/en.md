## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given a sorted array of non-overlapping intervals and a new interval. We need to insert the new interval into the array such that the result remains sorted and all overlapping intervals are merged.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 10^4 intervals, each with start and end values up to 10^5.
- **Time Complexity:** O(n) where n is the number of intervals. We traverse the array once, processing each interval at most once.
- **Space Complexity:** O(n) to store the result array.
- **Edge Case:** If the intervals array is empty, we return an array containing only the new interval.

**1.2 High-level approach:**

The goal is to process intervals in three phases: add intervals that come before the new interval, merge all intervals that overlap with the new interval, and add the remaining intervals that come after.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Insert the new interval, sort the entire array, then merge overlapping intervals. This would be O(n log n) time due to sorting.
- **Optimized Strategy:** Since intervals are already sorted, we can process them in a single pass: add intervals before overlap, merge overlapping ones, then add remaining intervals. This is O(n) time.
- **Optimization:** By leveraging the fact that intervals are already sorted, we avoid the need for sorting and can process everything in one pass, making the solution more efficient.

**1.4 Decomposition:**

1. Add all intervals that end before the new interval starts (no overlap).
2. Merge all intervals that overlap with the new interval by updating the start and end boundaries.
3. Add the merged interval to the result.
4. Add all remaining intervals that start after the merged interval ends.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`

- Result array: `res = []`
- Index `i = 0`
- New interval boundaries: `start = 4`, `end = 8`

**2.2 Start Processing:**

We begin processing intervals from left to right, checking each interval's relationship with the new interval.

**2.3 Trace Walkthrough:**

| Step | i | Interval | Condition | Action | res | start, end |
| ---- | - | -------- | --------- | ------ | --- | ---------- |
| 1    | 0 | [1,2] | 2 < 4 (ends before) | Add to res | `[[1,2]]` | 4, 8 |
| 2    | 1 | [3,5] | 3 <= 8 (overlaps) | Merge: start=min(4,3)=3, end=max(8,5)=8 | `[[1,2]]` | 3, 8 |
| 3    | 2 | [6,7] | 6 <= 8 (overlaps) | Merge: start=min(3,6)=3, end=max(8,7)=8 | `[[1,2]]` | 3, 8 |
| 4    | 3 | [8,10] | 8 <= 8 (overlaps) | Merge: start=min(3,8)=3, end=max(8,10)=10 | `[[1,2]]` | 3, 10 |
| 5    | 4 | [12,16] | 12 > 10 (starts after) | Add merged [3,10], then add [12,16] | `[[1,2],[3,10],[12,16]]` | - |

**2.4 Increment and Loop:**

After processing each interval, we increment the index `i` and continue until all intervals are processed.

**2.5 Return Result:**

The result is `[[1,2],[3,10],[12,16]]`, where the new interval [4,8] has been merged with overlapping intervals [3,5], [6,7], and [8,10] to form [3,10].
