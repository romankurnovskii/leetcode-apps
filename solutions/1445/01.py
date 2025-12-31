from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        # First pass: calculate total sum
        def get_sum(node):
            if not node:
                return 0
            return node.val + get_sum(node.left) + get_sum(node.right)

        total_sum = get_sum(root)
        res = 0

        # Second pass: find maximum product
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum

            # Try removing edge to left or right subtree
            if left_sum > 0:
                product = (total_sum - left_sum) * left_sum
                res = max(res, product)

            if right_sum > 0:
                product = (total_sum - right_sum) * right_sum
                res = max(res, product)

            return subtree_sum

        dfs(root)
        return res % MOD
