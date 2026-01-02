from typing import List


class Solution:
    def calculateLateFee(self, books: List[int], days: int) -> int:
        res = 0

        for book in books:
            if book > days:
                res += book - days

        return res
