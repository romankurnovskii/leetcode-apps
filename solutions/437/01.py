# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        prefix_sums = {}
        
        def dfs(node, current_sum):
            nonlocal res, prefix_sums
            if not node:
                return
            
            current_sum += node.val
            if current_sum == targetSum:
                res += 1
            
            res += prefix_sums.get(current_sum - targetSum, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            prefix_sums[current_sum] -= 1
        
        dfs(root, 0)
        return res

