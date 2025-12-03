class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Since we're using squares, the sign of original numbers doesn't matter
        # We want to maximize: arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...
        # This means we want large squares at even indices and small squares at odd indices
        
        # Sort numbers by absolute value (squares are same for positive/negative)
        nums_sorted = sorted([abs(x) for x in nums], reverse=True)
        
        n = len(nums_sorted)
        res = 0
        
        # Assign largest numbers to even indices (positive contribution)
        # and smallest numbers to odd indices (negative contribution)
        for i in range(n):
            if i % 2 == 0:
                # Even index: add square
                res += nums_sorted[i] * nums_sorted[i]
            else:
                # Odd index: subtract square
                res -= nums_sorted[i] * nums_sorted[i]
        
        return res

