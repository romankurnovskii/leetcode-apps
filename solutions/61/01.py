# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Handle edge cases
    if not head or not head.next or k == 0:
        return head

    # Find the length of the list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next

    # Normalize k
    k = k % length
    if k == 0:
        return head

    new_head_pos = length - k

    # Find the node before the new head
    current = head
    for _ in range(new_head_pos - 1):
        current = current.next

    # Break the list and reconnect
    new_head = current.next
    current.next = None

    # Connect the end to the original head
    last_node = new_head
    while last_node.next:
        last_node = last_node.next
    last_node.next = head

    return new_head
