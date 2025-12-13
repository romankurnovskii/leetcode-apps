from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []
        seen_a = set()
        seen_b = set()
        
        for i in range(n):
            # Add current elements to sets
            seen_a.add(A[i])
            seen_b.add(B[i])
            
            # Count common elements
            common = len(seen_a & seen_b)
            res.append(common)
        
        return res

