class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        
        # Find the index with negative balance
        j = -1
        for i, b in enumerate(balance):
            if b < 0:
                j = i
                break
        
        # If all balances are non-negative, return 0
        if j < 0:
            return 0
        
        # If total sum is negative, impossible
        if sum(balance) < 0:
            return -1
        
        # Work with a copy to avoid modifying input
        A = balance[:]
        res = 0
        d = 0
        
        # Expand outward from negative index
        while A[j] < 0:
            d += 1
            # Get storage from neighbors at distance d
            storage = A[(j + d) % n] + A[(j - d) % n]
            transfer = min(-A[j], storage)
            res += transfer * d
            A[j] += storage
        
        return res
