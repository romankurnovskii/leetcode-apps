from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If no decreasing element found, reverse the entire array
        if i < 0:
            nums.reverse()
            return

        # Step 2: Find the smallest element on the right that is larger than nums[i]
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray from i+1 to the end
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
