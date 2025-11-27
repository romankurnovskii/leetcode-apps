from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        res = 0
        
        # Use two heaps for left and right candidates
        left_heap = []
        right_heap = []
        
        left_idx = 0
        right_idx = n - 1
        
        # Initialize heaps with first and last candidates
        for _ in range(candidates):
            if left_idx <= right_idx:
                heapq.heappush(left_heap, costs[left_idx])
                left_idx += 1
            if left_idx <= right_idx:
                heapq.heappush(right_heap, costs[right_idx])
                right_idx -= 1
        
        # Hire k workers
        for _ in range(k):
            # Choose the minimum from left or right heap
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                res += heapq.heappop(left_heap)
                # Add next candidate from left if available
                if left_idx <= right_idx:
                    heapq.heappush(left_heap, costs[left_idx])
                    left_idx += 1
            else:
                res += heapq.heappop(right_heap)
                # Add next candidate from right if available
                if left_idx <= right_idx:
                    heapq.heappush(right_heap, costs[right_idx])
                    right_idx -= 1
        
        return res

