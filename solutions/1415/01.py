class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(path):
            if len(path) == n:
                res.append("".join(path))
                return

            for char in ["a", "b", "c"]:
                if not path or path[-1] != char:
                    path.append(char)
                    backtrack(path)
                    path.pop()
                    if len(res) >= k:
                        return

        res = []
        backtrack([])

        if len(res) < k:
            return ""

        return res[k - 1]
