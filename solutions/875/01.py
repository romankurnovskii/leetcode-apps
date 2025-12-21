class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
