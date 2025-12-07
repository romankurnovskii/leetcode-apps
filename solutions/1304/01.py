class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        
        # For even n: add pairs of positive and negative numbers
        # For odd n: add pairs plus 0
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        
        # If n is odd, add 0
        if n % 2 == 1:
            res.append(0)
        
        return res

