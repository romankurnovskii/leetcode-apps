class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        
        # Start with all tasks using technique1
        total = sum(technique1)
        
        # Calculate deltas: switching from technique1 to technique2
        deltas = [technique2[i] - technique1[i] for i in range(n)]
        
        # Sort deltas in descending order
        deltas.sort(reverse=True)
        
        res = total
        
        # We need at least k tasks using technique1
        # So we can switch at most (n - k) tasks to technique2
        # Apply the largest positive deltas
        for i in range(n - k):
            total += deltas[i]
            res = max(res, total)
        
        return res
