import heapq

class MedianFinder:
    def __init__(self):
        # max_heap for smaller half, min_heap for larger half
        self.max_heap = []  # Use negative values for max heap
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])

