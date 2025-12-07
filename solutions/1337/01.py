class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Calculate strength (number of soldiers) for each row
        strengths = []
        for i, row in enumerate(mat):
            # Count soldiers (1s) in the row
            strength = sum(row)
            strengths.append((strength, i))
        
        # Sort by strength, then by index
        strengths.sort()
        
        # Return first k indices
        res = [idx for _, idx in strengths[:k]]
        return res

