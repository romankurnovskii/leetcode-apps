class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        exchange = numExchange

        # Drink all initial bottles
        res += numBottles
        empty = numBottles

        # Continue exchanging while possible
        while empty >= exchange:
            # Exchange empty bottles for one full bottle
            empty -= exchange
            exchange += 1
            res += 1
            empty += 1

        return res
