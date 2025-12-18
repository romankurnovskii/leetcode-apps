class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        total = sum(balance)
        
        # If total is negative, impossible
        if total < 0:
            return -1
        
        # Find the index with negative balance
        neg_idx = None
        for i in range(n):
            if balance[i] < 0:
                neg_idx = i
                break
        
        # If no negative balance, already balanced
        if neg_idx is None:
            return 0
        
        # We need to transfer balance to neg_idx
        # Greedily use nearest positive balances
        res = 0
        neg_amount = abs(balance[neg_idx])
        
        # Create list of (distance, index, amount) for positive balances
        positives = []
        for i in range(n):
            if balance[i] > 0:
                # Calculate distance (circular)
                dist = min(abs(i - neg_idx), n - abs(i - neg_idx))
                positives.append((dist, i, balance[i]))
        
        # Sort by distance
        positives.sort()
        
        # Greedily transfer from nearest positives
        remaining = neg_amount
        for dist, idx, amount in positives:
            if remaining <= 0:
                break
            transfer = min(remaining, amount)
            res += transfer * dist
            remaining -= transfer
        
        return res
