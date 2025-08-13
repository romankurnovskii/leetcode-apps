def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:  # edge case
        return []

    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for interval in intervals[1:]:  # remaining
        # Check if current interval overlaps with last in result
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)

    return result
