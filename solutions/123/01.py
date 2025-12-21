from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State machine: buy1, sell1, buy2, sell2
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0

        for price in prices:
            # First transaction
            buy1 = max(buy1, -price)  # Buy at lowest price
            sell1 = max(sell1, buy1 + price)  # Sell at highest profit

            # Second transaction (using profit from first)
            buy2 = max(buy2, sell1 - price)  # Buy at lowest price after first sell
            sell2 = max(sell2, buy2 + price)  # Sell at highest profit

        return sell2
