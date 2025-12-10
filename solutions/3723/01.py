class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if it's possible: max sum for num digits is 9 * num
        if sum > 9 * num:
            return ""

        # Check if it's possible: min sum for num digits is 1 (if num >= 1)
        if sum < 1:
            return ""

        # Greedy: fill leftmost digits with 9s first to maximize sum of squares
        # Then fill remaining with what's needed
        res = []
        remaining_sum = sum

        # Fill as many 9s as possible
        for i in range(num):
            if remaining_sum >= 9:
                res.append("9")
                remaining_sum -= 9
            else:
                res.append(str(remaining_sum))
                remaining_sum = 0

        # If we still have remaining sum, it's impossible
        if remaining_sum > 0:
            return ""

        # Return the maximum number (already sorted descending)
        return "".join(res)
