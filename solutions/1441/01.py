class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        idx = 0

        for i in range(1, n + 1):
            if idx >= len(target):
                break

            res.append("Push")

            if i == target[idx]:
                idx += 1
            else:
                res.append("Pop")

        return res
