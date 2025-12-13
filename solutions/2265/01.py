# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0  # sum, count
            
            # Get subtree info from children
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate current subtree sum and count
            subtree_sum = node.val + left_sum + right_sum
            subtree_count = 1 + left_count + right_count
            
            # Calculate average (integer division)
            avg = subtree_sum // subtree_count
            
            # Check if node value equals average
            if node.val == avg:
                res += 1
            
            return subtree_sum, subtree_count
        
        dfs(root)
        return res

