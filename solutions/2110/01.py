from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        i = 0
        
        while i < n:
            # Find the length of the current smooth descent period
            length = 1
            while i + length < n and prices[i + length] == prices[i + length - 1] - 1:
                length += 1
            
            # Count all subarrays within this period
            # For a period of length k, there are k*(k+1)//2 subarrays
            res += length * (length + 1) // 2
            
            i += length
        
        return res

