class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        # Use iterative approach
        prev3 = 0  # T(0)
        prev2 = 1  # T(1)
        prev1 = 1  # T(2)

        for i in range(3, n + 1):
            current = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = current

        return prev1
