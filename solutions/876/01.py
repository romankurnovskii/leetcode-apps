# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use two pointers: slow and fast
        # Slow moves one step at a time, fast moves two steps
        # When fast reaches the end, slow will be at the middle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Slow is now at the middle node
        res = slow
        return res

