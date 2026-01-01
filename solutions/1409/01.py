from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))
        res = []

        for q in queries:
            idx = p.index(q)
            res.append(idx)
            p.pop(idx)
            p.insert(0, q)

        return res
