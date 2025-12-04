# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob this node, don't rob this node)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we can't rob children
            rob_this = node.val + left[1] + right[1]
            
            # If we don't rob this node, we can choose to rob or not rob children
            dont_rob_this = max(left) + max(right)
            
            return (rob_this, dont_rob_this)
        
        return max(dfs(root))

