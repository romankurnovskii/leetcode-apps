from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node, current_sum):
            nonlocal res
            if not node:
                return
            
            # Update current number
            current_sum = current_sum * 10 + node.val
            
            # If leaf node, add to result
            if not node.left and not node.right:
                res += current_sum
                return
            
            # Recursively process left and right subtrees
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        
        dfs(root, 0)
        return res

