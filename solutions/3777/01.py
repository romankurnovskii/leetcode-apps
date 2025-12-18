class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    def add(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Convert string to 0-1 array (A=0, B=1)
        A = [ord(c) - ord('A') for c in s]
        
        # Initialize Fenwick Tree
        bit = FenwickTree(n)
        # Mark violations (adjacent identical characters)
        for i in range(n - 1):
            if A[i] == A[i + 1]:
                bit.add(i + 1, 1)
        
        res = []
        for q in queries:
            if q[0] == 1:
                # Flip operation
                i = q[1]
                A[i] ^= 1  # Flip the bit
                
                # Update violations at position i and i+1
                if i > 0:
                    # Check violation with left neighbor
                    bit.add(i, 1 if A[i] == A[i - 1] else -1)
                if i < n - 1:
                    # Check violation with right neighbor
                    bit.add(i + 1, 1 if A[i] == A[i + 1] else -1)
            else:
                # Query operation: count violations in range [l, r]
                # Number of violations = minimum deletions needed
                res.append(bit.query(q[2]) - bit.query(q[1]))
        
        return res
