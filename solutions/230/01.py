# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use in-order traversal to get elements in sorted order
        # Count nodes as we traverse
        count = 0
        res = None
        
        def inorder(node):
            nonlocal count, res
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            count += 1
            if count == k:
                res = node.val
                return
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return res

