class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        # dp[r] stores the minimum sum we've seen with remainder r
        # Initialize with infinity for all remainders except 0
        dp = [float("inf")] * k
        dp[0] = 0  # Base case: sum 0 has remainder 0

        res = 0
        for num in nums:
            res += num
            # If we've seen this remainder before, we can "delete" the subarray
            # by resetting to the minimum sum we've seen with this remainder
            res = min(dp[res % k], res)
            # Update dp with the new minimum for this remainder
            dp[res % k] = min(dp[res % k], res)

        return res
