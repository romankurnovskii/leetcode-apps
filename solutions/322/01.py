class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic programming: dp[i] = minimum coins needed for amount i
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        res = dp[amount] if dp[amount] != float("inf") else -1
        return res
