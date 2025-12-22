class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # dp[i] = length of longest valid subsequence ending at column i
        # A valid subsequence means columns that can be kept such that
        # all rows remain sorted
        dp = [1] * m
        
        for i in range(1, m):
            for j in range(i):
                # Check if column i can come after column j
                # For column i to come after j, all rows must satisfy:
                # strs[k][j] <= strs[k][i] for all k
                valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break
                
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The answer is total columns minus the longest valid subsequence
        res = m - max(dp)
        return res

