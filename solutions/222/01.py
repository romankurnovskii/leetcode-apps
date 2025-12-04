from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Get left and right heights
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        if left_height == right_height:
            # Left subtree is full, right subtree may not be
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is full, left subtree may not be
            return (1 << right_height) + self.countNodes(root.left)
    
    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

