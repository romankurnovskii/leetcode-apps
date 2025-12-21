class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k >= n/2, we can make as many transactions as we want
        # This becomes the "unlimited transactions" problem
        if k >= n // 2:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        # DP: buy[i][j] = max profit with at most i transactions, holding stock after j-th day
        # sell[i][j] = max profit with at most i transactions, not holding stock after j-th day
        buy = [-float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            # Update for each transaction count from k down to 1
            for i in range(k, 0, -1):
                # Either keep holding or buy today
                buy[i] = max(buy[i], sell[i - 1] - price)
                # Either keep not holding or sell today
                sell[i] = max(sell[i], buy[i] + price)

        return sell[k]
