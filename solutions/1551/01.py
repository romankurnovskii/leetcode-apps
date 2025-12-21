class Solution:
    def minOperations(self, n: int) -> int:
        # Target value is the average
        target = n

        # Calculate operations needed
        res = 0
        for i in range(n):
            current = 2 * i + 1
            if current < target:
                res += target - current
            else:
                break

        return res
