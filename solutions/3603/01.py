def minCost(m: int, n: int, waitCost: List[List[int]]) -> int:
    # Use a simple recursive DP with memoization for clarity
    from functools import lru_cache

    INF = 10**15

    @lru_cache(maxsize=None)
    def dp(i, j, parity):
        # Base case: reached bottom-right
        if i == m - 1 and j == n - 1:
            return 0
        # Out of bounds
        if i < 0 or i >= m or j < 0 or j >= n:
            return INF
        res = INF
        if parity == 1:  # Move step
            # Move down
            res = min(res, (i + 2) * (j + 1) + dp(i + 1, j, 0))
            # Move right
            res = min(res, (i + 1) * (j + 2) + dp(i, j + 1, 0))
        else:  # Wait step
            res = min(res, waitCost[i][j] + dp(i, j, 1))
        return res

    # Start at (0,0) with move step (parity=1), pay entry cost 1
    return 1 + dp(0, 0, 1)
