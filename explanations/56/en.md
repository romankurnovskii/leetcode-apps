# 56. Merge Intervals

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/merge-intervals/

## Problem Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

**Example 1:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

**Example 2:**
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Constraints:**
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Explanation

### Strategy

This is a **sorting and greedy problem** that requires merging overlapping intervals. The key insight is to sort the intervals by start time and then merge them in a single pass.

**Key observations:**
- We need to sort intervals by start time to process them in order
- If current interval overlaps with previous, merge them
- If no overlap, add current interval to result
- Two intervals overlap if current start <= previous end

**High-level approach:**
1. **Sort intervals**: Sort by start time to process in order
2. **Initialize result**: Start with first interval
3. **Iterate through intervals**: For each interval, check for overlap
4. **Merge or add**: If overlap, merge; if not, add to result

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If intervals is empty, return empty list

**Step 2: Sort intervals**
- Sort by start time: `intervals.sort(key=lambda x: x[0])`

**Step 3: Initialize result**
- Start with first interval: `result = [intervals[0]]`

**Step 4: Iterate through intervals**
For each interval starting from second:
- Check if current interval overlaps with last in result
- If overlap: merge by updating end time
- If no overlap: add current interval to result

**Example walkthrough:**
Let's trace through the first example:

```
intervals = [[1,3],[2,6],[8,10],[15,18]]

Step 1: Sort intervals
intervals = [[1,3],[2,6],[8,10],[15,18]] (already sorted)

Step 2: Initialize result
result = [[1,3]]

Step 3: Process [2,6]
Overlap? Yes (2 <= 3)
Merge: [1, max(3,6)] = [1,6]
result = [[1,6]]

Step 4: Process [8,10]
Overlap? No (8 > 6)
Add to result: result = [[1,6],[8,10]]

Step 5: Process [15,18]
Overlap? No (15 > 10)
Add to result: result = [[1,6],[8,10],[15,18]]

Result: [[1,6],[8,10],[15,18]]
```

> **Note:** The key insight is that after sorting by start time, we only need to check if the current interval overlaps with the last interval in our result. This works because all previous intervals are already merged and non-overlapping.

### Solution

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Handle edge case
        if not intervals:
            return []
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize result with first interval
        result = [intervals[0]]
        
        # Iterate through remaining intervals
        for interval in intervals[1:]:
            # Check if current interval overlaps with last in result
            if interval[0] <= result[-1][1]:
                # Merge intervals by updating end time
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                # No overlap, add current interval to result
                result.append(interval)
        
        # Return merged intervals
        return result
```

**Time Complexity:** O(n log n) - sorting takes O(n log n), merging takes O(n)  
**Space Complexity:** O(n) - to store the result 