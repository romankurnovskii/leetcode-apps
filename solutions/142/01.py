# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    # Phase 1: Find the meeting point
    slow = head
    fast = head

    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    # Phase 2: Find the cycle start
    slow = head

    # Move both pointers one step at a time
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
