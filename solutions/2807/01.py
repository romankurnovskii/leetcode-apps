# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        current = head
        while current and current.next:
            # Calculate GCD of current and next node values
            gcd_value = gcd(current.val, current.next.val)
            
            # Create new node with GCD value
            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            
            # Move to the node after the inserted node
            current = new_node.next
        
        return head

