# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root) -> int:
        res = 0
        
        def dfs(node, is_left, length):
            nonlocal res
            if not node:
                return
            
            res = max(res, length)
            
            if is_left:
                # Coming from left, go right
                dfs(node.right, False, length + 1)
                # Or start new path going left
                dfs(node.left, True, 1)
            else:
                # Coming from right, go left
                dfs(node.left, True, length + 1)
                # Or start new path going right
                dfs(node.right, False, 1)
        
        if root:
            dfs(root.left, True, 1)
            dfs(root.right, False, 1)
        
        return res

