# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Node has two children
                # Find the minimum value in right subtree
                min_node = self.findMin(root.right)
                # Replace root's value with min value
                root.val = min_node.val
                # Delete the min node from right subtree
                root.right = self.deleteNode(root.right, min_node.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
