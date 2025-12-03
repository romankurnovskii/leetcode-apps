"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to map original nodes to cloned nodes
        node_map = {}
        
        def clone(node):
            # If already cloned, return the clone
            if node in node_map:
                return node_map[node]
            
            # Create a new node
            clone_node = Node(node.val)
            node_map[node] = clone_node
            
            # Clone all neighbors
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            
            return clone_node
        
        return clone(node)

