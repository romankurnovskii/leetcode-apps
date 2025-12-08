class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Try all possible first operation scores
        possible_scores = [
            nums[0] + nums[1],  # first two
            nums[-1] + nums[-2],  # last two
            nums[0] + nums[-1],  # first and last
        ]

        res = 0

        for target_score in possible_scores:
            # DP: dp[l][r] = max operations on subarray nums[l:r+1]
            from functools import lru_cache

            @lru_cache(maxsize=None)
            def dp(l, r):
                if r - l < 1:  # Need at least 2 elements
                    return 0

                max_ops = 0

                # Try first two
                if l + 1 <= r and nums[l] + nums[l + 1] == target_score:
                    max_ops = max(max_ops, 1 + dp(l + 2, r))

                # Try last two
                if l <= r - 1 and nums[r - 1] + nums[r] == target_score:
                    max_ops = max(max_ops, 1 + dp(l, r - 2))

                # Try first and last
                if l < r and nums[l] + nums[r] == target_score:
                    max_ops = max(max_ops, 1 + dp(l + 1, r - 1))

                return max_ops

            res = max(res, dp(0, n - 1))

        return res
