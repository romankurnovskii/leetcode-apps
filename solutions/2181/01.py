# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Skip the first zero
        current = head.next
        dummy = ListNode(0)
        tail = dummy

        while current:
            # Sum values until we hit the next zero
            total = 0
            while current and current.val != 0:
                total += current.val
                current = current.next

            # Create new node with the sum
            if total > 0:
                tail.next = ListNode(total)
                tail = tail.next

            # Move past the zero
            if current:
                current = current.next

        return dummy.next
