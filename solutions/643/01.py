from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate sum of first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
