from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        res = []
        current_sum = 0

        for num in nums:
            res.append(num)
            current_sum += num
            if current_sum > total - current_sum:
                break

        return res
