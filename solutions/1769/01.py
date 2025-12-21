from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        # For each position, calculate operations needed
        for i in range(n):
            operations = 0
            for j in range(n):
                if boxes[j] == "1":
                    operations += abs(i - j)
            res[i] = operations

        return res
