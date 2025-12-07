class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        sold = 0
        
        for i in range(1, len(prices)):
            hold = max(hold, sold - prices[i])
            sold = max(sold, hold + prices[i] - fee)
        
        return sold

