class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if op == "++X" or op == "X++":
                res += 1
            else:  # "--X" or "X--"
                res -= 1
        return res
