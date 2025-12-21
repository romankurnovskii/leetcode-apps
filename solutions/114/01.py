from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)

        # Save right subtree
        right = root.right

        # Move left subtree to right
        root.right = root.left
        root.left = None

        # Find the end of the new right subtree and attach saved right
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right
