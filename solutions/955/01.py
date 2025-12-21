class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        # Track which pairs of strings are already sorted
        sorted_pairs = [False] * (n - 1)
        
        for j in range(m):
            # Check if this column breaks any unsorted pair
            should_delete = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][j] > strs[i + 1][j]:
                    res += 1
                    should_delete = True
                    break
            
            # If we keep this column, update sorted status
            if not should_delete:
                for i in range(n - 1):
                    if strs[i][j] < strs[i + 1][j]:
                        sorted_pairs[i] = True
        
        return res

