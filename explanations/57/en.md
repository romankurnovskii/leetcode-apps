You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i^th` interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` *after the insertion*.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

**Example 1:**

```sh
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**

```sh
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**Constraints:**

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in **ascending** order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Explanation

### Strategy

This is an **array manipulation problem** that requires inserting a new interval into a sorted list of non-overlapping intervals. The key insight is to process intervals in three phases: before overlap, during overlap, and after overlap.

**Key observations:**
- Intervals are already sorted by start time
- We need to find where the new interval fits
- We may need to merge multiple overlapping intervals
- Process intervals in three phases based on overlap with new interval

**High-level approach:**
1. **Add intervals before overlap**: Add all intervals that end before new interval starts
2. **Merge overlapping intervals**: Find all intervals that overlap with new interval
3. **Add merged interval**: Add the final merged interval
4. **Add remaining intervals**: Add all intervals that start after new interval ends

### Steps

Let's break down the solution step by step:

**Step 1: Initialize result list**
- Create empty result list: `result = []`

**Step 2: Add intervals before overlap**
- Add all intervals where `interval[1] < newInterval[0]`

**Step 3: Merge overlapping intervals**
- Find all intervals that overlap with new interval
- Update new interval boundaries: `start = min(start, interval[0])`, `end = max(end, interval[1])`

**Step 4: Add merged interval**
- Add the final merged interval to result

**Step 5: Add remaining intervals**
- Add all intervals where `interval[0] > newInterval[1]`

**Example walkthrough:**
Let's trace through the second example:

```sh
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

Step 1: Add intervals before overlap
result = [[1,2]] (3,5 overlaps, so stop)

Step 2: Merge overlapping intervals
Overlap with [3,5]: newInterval = [min(4,3), max(8,5)] = [3,8]
Overlap with [6,7]: newInterval = [min(3,6), max(8,7)] = [3,8]
Overlap with [8,10]: newInterval = [min(3,8), max(8,10)] = [3,10]

Step 3: Add merged interval
result = [[1,2],[3,10]]

Step 4: Add remaining intervals
result = [[1,2],[3,10],[12,16]]

Result: [[1,2],[3,10],[12,16]]
```

> **Note:** The key insight is to process intervals in three phases. This approach is efficient because we only need to traverse the array once, and we can determine which phase each interval belongs to by comparing its boundaries with the new interval.

**Time Complexity:** O(n) - we visit each interval at most once  
**Space Complexity:** O(n) - to store the result 