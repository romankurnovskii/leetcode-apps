# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next:
            return None

        # Phase 1: Find the meeting point
        slow = head
        fast = head

        # Find meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If pointers meet, cycle detected
            if slow == fast:
                break
        else:
            # No cycle found
            return None

        # Phase 2: Find the cycle start
        slow = head

        # Move both pointers one step at a time
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Return the cycle start
        return slow
