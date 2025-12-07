class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path, remaining):
            if len(path) == k and remaining == 0:
                res.append(path[:])
                return
            
            if len(path) >= k or remaining < 0:
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()
        
        backtrack(1, [], n)
        return res

