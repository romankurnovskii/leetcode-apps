# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous and current pointers
        prev = None
        current = head
        
        # Iterate through the list, reversing links
        while current:
            # Store the next node before we break the link
            next_node = current.next
            # Reverse the link: point current to previous
            current.next = prev
            # Move pointers forward
            prev = current
            current = next_node
        
        # prev now points to the new head
        res = prev
        return res

