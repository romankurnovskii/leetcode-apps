from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Find all nodes that have no incoming edges
        has_incoming = [False] * n
        
        for from_node, to_node in edges:
            has_incoming[to_node] = True
        
        # Return all nodes without incoming edges
        res = []
        for i in range(n):
            if not has_incoming[i]:
                res.append(i)
        
        return res

