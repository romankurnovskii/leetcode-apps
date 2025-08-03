# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        # If pointers meet, there's a cycle
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    # If we reach here, there's no cycle
    return False
