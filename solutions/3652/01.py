class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Calculate base profit without modification
        base_profit = sum(strategy[i] * prices[i] for i in range(n))

        # Precompute prefix sums for prices
        price_prefix = [0] * (n + 1)
        for i in range(n):
            price_prefix[i + 1] = price_prefix[i] + prices[i]

        # Precompute prefix sums for strategy * prices (original profit)
        strategy_profit_prefix = [0] * (n + 1)
        for i in range(n):
            strategy_profit_prefix[i + 1] = (
                strategy_profit_prefix[i] + strategy[i] * prices[i]
            )

        res = base_profit

        # Try each possible segment [i, i+k-1]
        for i in range(n - k + 1):
            # Original profit from this segment using prefix sum
            original_segment_profit = (
                strategy_profit_prefix[i + k] - strategy_profit_prefix[i]
            )

            # Modified segment: first k/2 are 0 (hold), last k/2 are 1 (sell)
            # Profit from modified segment = sum of prices in last k/2
            modified_segment_profit = price_prefix[i + k] - price_prefix[i + k // 2]

            # Delta = modified - original
            delta = modified_segment_profit - original_segment_profit

            res = max(res, base_profit + delta)

        return res
