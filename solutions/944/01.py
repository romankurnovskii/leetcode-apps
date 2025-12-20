class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        
        # Check each column
        for col in range(m):
            # Check if column is sorted
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    res += 1
                    break
        
        return res

