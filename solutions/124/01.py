from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            # Get max path sum from left and right subtrees
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            # Update global maximum (path through current node)
            res = max(res, node.val + left_sum + right_sum)

            # Return max path sum that can be extended upward
            return node.val + max(left_sum, right_sum)

        dfs(root)
        return res
