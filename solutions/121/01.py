def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        potential_profit = price - min_price
        max_profit = max(max_profit, potential_profit)

    return max_profit
