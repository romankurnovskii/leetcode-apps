from typing import List


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute cost to make substring palindrome
        def cost_to_palindrome(left, right):
            cost = 0
            while left < right:
                if s[left] != s[right]:
                    cost += 1
                left += 1
                right -= 1
            return cost

        # Memoization
        from functools import lru_cache

        @lru_cache(None)
        def dp(pos, cuts_left):
            if cuts_left == 1:
                return cost_to_palindrome(pos, n - 1)

            if pos >= n:
                return float("inf")

            res = float("inf")
            for i in range(pos, n - cuts_left + 1):
                cost = cost_to_palindrome(pos, i)
                res = min(res, cost + dp(i + 1, cuts_left - 1))

            return res

        res = dp(0, k)
        return res
