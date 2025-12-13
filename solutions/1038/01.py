# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        
        def reverse_inorder(node):
            nonlocal total
            if node:
                # Traverse right first (largest values)
                reverse_inorder(node.right)
                
                # Update current node value
                total += node.val
                node.val = total
                
                # Traverse left (smaller values)
                reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root

