# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root, val: int):
        # If tree is empty, create new node
        if not root:
            return TreeNode(val)
        
        # If val is less than root, insert into left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If val is greater than root, insert into right subtree
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root

