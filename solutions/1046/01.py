class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        # Use max heap (negate values for min heap)
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Get two heaviest stones
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            # If they're different, add the difference back
            if x != y:
                heapq.heappush(heap, -(y - x))

        # Return last stone weight or 0
        return -heap[0] if heap else 0
