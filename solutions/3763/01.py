from typing import List


class Solution:
    def maxSum(self, nums: List[int], threshold: int) -> int:
        import heapq

        heap = []
        res = 0

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > threshold:
                heapq.heappop(heap)

            if len(heap) == threshold:
                res = max(res, sum(heap))

        return res
