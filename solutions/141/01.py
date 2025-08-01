# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Handle edge cases
        if not head or not head.next:
            return False

        # Initialize two pointers
        slow = head
        fast = head.next

        # Move pointers until they meet or reach end
        while fast and fast.next:
            # If pointers meet, there's a cycle
            if slow == fast:
                return True

            # Move slow pointer one step
            slow = slow.next

            # Move fast pointer two steps
            fast = fast.next.next

        # If we reach here, there's no cycle
        return False
