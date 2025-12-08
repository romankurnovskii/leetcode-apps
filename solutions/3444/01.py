class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        # Try each possible value for (sub[0] + sub[1]) % k
        for val in range(k):
            # dp[i] = max length of subsequence ending with element x where x % k == i
            dp = [0] * k

            for num in nums:
                r = num % k
                # The previous element should satisfy: (prev + num) % k == val
                # So: prev % k == (val - r + k) % k
                prev_r = (val - r + k) % k

                # Update dp[r] with dp[prev_r] + 1
                new_len = dp[prev_r] + 1
                dp[r] = max(dp[r], new_len)
                res = max(res, new_len)

        return res
