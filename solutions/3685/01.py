class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        
        # Sort in ascending order
        sorted_nums = sorted(nums)
        
        # Precompute subset-sum DP for all elements
        # dp[i][j] = can we achieve sum j using first i elements
        dp = [[False] * (k + 1) for _ in range(n + 1)]
        
        # Base case: sum 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if sorted_nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - sorted_nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        res = []
        # For each cap value x from 1 to n
        for x in range(1, n + 1):
            # Find first index where element > x
            ind = n
            for i in range(n):
                if sorted_nums[i] > x:
                    ind = i
                    break
            
            # If no element > x, use original array result
            if ind == n:
                res.append(dp[n][k])
            else:
                # Elements from ind to n-1 will be capped to x
                sz = n - ind  # Number of elements that become x
                
                # Check if we can form sum k
                found = False
                for j in range(k + 1):
                    if dp[ind][j]:  # Can form sum j with first ind elements
                        remainder = k - j
                        if remainder % x == 0:
                            multiple = remainder // x
                            if multiple <= sz:  # We have enough x's
                                found = True
                                break
                res.append(found)
        
        return res

