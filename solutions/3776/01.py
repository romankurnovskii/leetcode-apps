class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        total = sum(balance)
        
        # If total is negative, impossible
        if total < 0:
            return -1
        
        # Find the negative index
        neg_idx = -1
        for i in range(n):
            if balance[i] < 0:
                neg_idx = i
                break
        
        # If no negative, already balanced
        if neg_idx == -1:
            return 0
        
        res = 0
        # Greedily transfer from nearest positive neighbors
        # We need to move abs(balance[neg_idx]) units to neg_idx
        
        needed = abs(balance[neg_idx])
        
        # Try both directions and take minimum
        # Actually, we need to find the optimal way to transfer
        
        # Sort positive indices by distance from negative index
        positives = []
        for i in range(n):
            if balance[i] > 0:
                # Calculate circular distance
                dist1 = (i - neg_idx) % n
                dist2 = (neg_idx - i) % n
                dist = min(dist1, dist2)
                positives.append((dist, i, balance[i]))
        
        positives.sort()
        
        # Greedily use closest positives
        for dist, idx, amount in positives:
            if needed <= 0:
                break
            transfer = min(needed, amount)
            res += transfer * dist
            needed -= transfer
        
        return res if needed <= 0 else -1

