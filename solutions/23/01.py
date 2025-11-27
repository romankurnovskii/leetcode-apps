# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Create a min heap
        heap = []
        
        # Add first node from each list to heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Create dummy node
        dummy = ListNode(0)
        current = dummy
        
        # Merge lists
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # Add next node from the same list if it exists
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next

