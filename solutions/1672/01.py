class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0

        # Calculate wealth for each customer (sum of all accounts)
        for customer in accounts:
            wealth = sum(customer)
            res = max(res, wealth)

        return res
