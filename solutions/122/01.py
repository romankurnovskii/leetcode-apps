class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Handle edge case
        if not prices:
            return 0

        # Initialize profit
        profit = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(prices)):
            # Calculate the difference between current and previous price
            difference = prices[i] - prices[i - 1]

            # If the difference is positive, add it to profit
            if difference > 0:
                profit += difference

        # Return the total profit
        return profit
