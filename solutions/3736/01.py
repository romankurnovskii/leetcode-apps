from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Find the maximum value in the array
        max_val = max(nums)

        # Calculate the total moves needed
        # For each element, we need to increase it by (max_val - element) to reach max_val
        total_moves = 0
        for num in nums:
            total_moves += max_val - num

        return total_moves
