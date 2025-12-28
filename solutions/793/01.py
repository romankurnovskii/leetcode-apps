class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def numOfTrailingZeros(x: int) -> int:
            """Count trailing zeros in x!"""
            res = 0
            while x > 0:
                x //= 5
                res += x
            return res

        def binarySearch(target: int) -> int:
            """Find the largest x such that numOfTrailingZeros(x) <= target"""
            left, right = 0, 5 * (target + 1)
            while left <= right:
                mid = left + (right - left) // 2
                zeros = numOfTrailingZeros(mid)
                if zeros <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        # The answer is either 0 or 5
        # Find the range of x values where trailing zeros = k
        return binarySearch(k) - binarySearch(k - 1)
