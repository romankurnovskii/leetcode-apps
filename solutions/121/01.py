class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Handle edge case
        if not prices:
            return 0

        # Initialize variables
        min_price = prices[0]
        max_profit = 0

        # Iterate through the array starting from the second element
        for price in prices[1:]:
            # Update minimum price if current price is lower
            min_price = min(min_price, price)

            # Calculate potential profit and update maximum profit
            potential_profit = price - min_price
            max_profit = max(max_profit, potential_profit)

        # Return the maximum profit
        return max_profit
