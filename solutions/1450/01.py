from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort(key=lambda x: x[0])

        res = 0
        day = 1
        i = 0
        heap = []  # Min heap of end days

        while i < len(events) or heap:
            # Add all events that start today
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # Remove events that have already ended
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # Attend the event that ends earliest
            if heap:
                heapq.heappop(heap)
                res += 1

            day += 1

        return res
