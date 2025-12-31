from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        # For each middle soldier j, count:
        # - soldiers before j with rating < rating[j] (for increasing)
        # - soldiers before j with rating > rating[j] (for decreasing)
        # - soldiers after j with rating > rating[j] (for increasing)
        # - soldiers after j with rating < rating[j] (for decreasing)

        for j in range(1, n - 1):
            left_smaller = sum(1 for i in range(j) if rating[i] < rating[j])
            left_larger = sum(1 for i in range(j) if rating[i] > rating[j])
            right_larger = sum(1 for k in range(j + 1, n) if rating[k] > rating[j])
            right_smaller = sum(1 for k in range(j + 1, n) if rating[k] < rating[j])

            # Increasing: left_smaller * right_larger
            # Decreasing: left_larger * right_smaller
            res += left_smaller * right_larger + left_larger * right_smaller

        return res
