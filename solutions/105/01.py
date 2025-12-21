# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Create a map for O(1) lookup of inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            # Root is the first element in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find root position in inorder
            root_idx = inorder_map[root_val]

            # Calculate sizes of left and right subtrees
            left_size = root_idx - in_start

            # Recursively build left and right subtrees
            root.left = build(
                pre_start + 1, pre_start + left_size, in_start, root_idx - 1
            )
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
