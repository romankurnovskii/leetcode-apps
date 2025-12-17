class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # res[j] - best profit after completing j transactions
        res = [0] * (k + 1)
        # bought[j] - best profit if holding a "bought" position in j-th transaction
        # (bought normally, waiting to sell)
        bought = [-float('inf')] * k
        # sold[j] - best profit if holding a "short sold" position in j-th transaction
        # (sold short, waiting to buy back)
        sold = [0] * k
        
        for price in prices:
            # Process from k down to 1 to avoid using updated values
            for j in range(k, 0, -1):
                # Complete a transaction:
                # - Complete normal: sell at current price (bought[j-1] + price)
                # - Complete short: buy back at current price (sold[j-1] - price)
                res[j] = max(res[j], bought[j - 1] + price, sold[j - 1] - price)
                
                # Start a new transaction:
                # - Start normal: buy at current price (res[j-1] - price)
                bought[j - 1] = max(bought[j - 1], res[j - 1] - price)
                # - Start short: sell at current price (res[j-1] + price)
                sold[j - 1] = max(sold[j - 1], res[j - 1] + price)
        
        return max(res)

