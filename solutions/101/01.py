# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        def is_mirror(left, right):
            # Both are None
            if not left and not right:
                return True
            # One is None
            if not left or not right:
                return False
            # Values must match and subtrees must be mirrors
            return (left.val == right.val and 
                    is_mirror(left.left, right.right) and 
                    is_mirror(left.right, right.left))
        
        if not root:
            return True
        
        return is_mirror(root.left, root.right)

