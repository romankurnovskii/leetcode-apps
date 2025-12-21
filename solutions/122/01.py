def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    profit = 0

    for i in range(1, len(prices)):
        # Calculate the difference between current and previous price
        difference = prices[i] - prices[i - 1]

        if difference > 0:
            profit += difference

    return profit
