# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        # Start with the root node
        leftmost = root

        # While we have a level to process
        while leftmost.left:
            # Current node in the current level
            current = leftmost

            # Iterate through the current level
            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to next node's left child (if exists)
                if current.next:
                    current.right.next = current.next.left

                # Move to next node in the same level
                current = current.next

            # Move to the next level
            leftmost = leftmost.left

        return root
