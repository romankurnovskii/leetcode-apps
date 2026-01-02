from typing import List


class Solution:
    def maxTransactions(self, transactions: List[List[int]]) -> int:
        transactions.sort(key=lambda x: x[1])

        balance = 0
        res = 0

        for amount, time in transactions:
            if balance + amount >= 0:
                balance += amount
                res += 1

        return res
