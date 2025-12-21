from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # If leaf node, check if value equals remaining sum
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursively check left and right subtrees
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining
        )
