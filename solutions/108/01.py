from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None
            
            # Choose middle element as root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)

