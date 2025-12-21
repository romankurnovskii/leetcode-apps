from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(current_permutation, remaining):
            if not remaining:
                res.append(current_permutation[:])
                return

            for i in range(len(remaining)):
                # Choose
                current_permutation.append(remaining[i])
                # Explore
                backtrack(current_permutation, remaining[:i] + remaining[i + 1 :])
                # Unchoose
                current_permutation.pop()

        backtrack([], nums)
        return res
