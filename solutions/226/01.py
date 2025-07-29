from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Base case: If the node is null, there's nothing to do.
    if not root:
        return None
        
    root.left, root.right = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root