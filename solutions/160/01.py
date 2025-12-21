# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # Two pointer approach: traverse both lists
        # When one pointer reaches end, switch to other list
        # This way both pointers will meet at intersection (if exists)
        # or both will be None (if no intersection)

        p1, p2 = headA, headB

        while p1 != p2:
            # If p1 reaches end, switch to headB
            p1 = p1.next if p1 else headB
            # If p2 reaches end, switch to headA
            p2 = p2.next if p2 else headA

        return p1
