# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # Create a map for O(1) lookup of inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None
            
            # Root is the last element in postorder
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # Find root position in inorder
            root_idx = inorder_map[root_val]
            
            # Calculate sizes of left and right subtrees
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(in_start, root_idx - 1, post_start, post_start + left_size - 1)
            root.right = build(root_idx + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)

