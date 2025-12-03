# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a linked list segment
        def reverse_segment(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Count nodes to check if we have enough for a group
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            # Reverse the first k nodes
            reversed_head = reverse_segment(head, curr)
            # Recursively reverse the rest
            head.next = self.reverseKGroup(curr, k)
            return reversed_head
        
        # Not enough nodes, return as is
        return head

