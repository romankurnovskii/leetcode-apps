class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the left boundary: first index where order breaks
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:
            return 0  # Already sorted

        # Find the right boundary: last index where order breaks
        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        # Find min and max in the unsorted subarray
        sub_min = min(nums[left : right + 1])
        sub_max = max(nums[left : right + 1])

        # Extend left boundary
        while left > 0 and nums[left - 1] > sub_min:
            left -= 1

        # Extend right boundary
        while right < n - 1 and nums[right + 1] < sub_max:
            right += 1

        return right - left + 1
