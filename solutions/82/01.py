# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr and curr.next:
            # If we find duplicates
            if curr.val == curr.next.val:
                # Skip all nodes with the same value
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                # Link prev to the node after duplicates
                prev.next = curr
            else:
                # No duplicates, move both pointers
                prev = curr
                curr = curr.next
        
        return dummy.next

