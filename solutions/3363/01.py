class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        A = [row[:] for row in fruits]  # Make a copy to avoid modifying input

        # Set inaccessible cells to 0
        for i in range(n):
            for j in range(n):
                if i < j < n - 1 - i:
                    A[i][j] = 0
                if j < i < n - 1 - j:
                    A[i][j] = 0

        # First child goes along the diagonal
        res = sum(A[i][i] for i in range(n))

        # Second child: from (0, n-1) to (n-1, n-1)
        for i in range(1, n):
            for j in range(i + 1, n):
                A[i][j] += max(
                    A[i - 1][j - 1],
                    A[i - 1][j],
                    A[i - 1][j + 1] if j + 1 < n else 0,
                )

        # Third child: from (n-1, 0) to (n-1, n-1)
        for j in range(1, n):
            for i in range(j + 1, n):
                A[i][j] += max(
                    A[i - 1][j - 1],
                    A[i][j - 1],
                    A[i + 1][j - 1] if i + 1 < n else 0,
                )

        # Add the fruits from the two paths just before the destination
        return res + A[n - 1][n - 2] + A[n - 2][n - 1]
