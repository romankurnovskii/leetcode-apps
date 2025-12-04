class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        
        n = len(matrix)
        # Min heap: (value, row, col)
        heap = []
        
        # Add first element of each row to heap
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        
        # Pop k-1 times to get kth smallest
        for _ in range(k - 1):
            val, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        
        # The kth smallest is at the top
        return heap[0][0]

