class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        lsum = 0
        rsum = 0

        # Strictly increasing from left
        while l < n - 1 and nums[l] < nums[l + 1]:
            lsum += nums[l]
            l += 1

        # Strictly decreasing from right
        while r > 0 and nums[r - 1] > nums[r]:
            rsum += nums[r]
            r -= 1

        # Single peak element
        if l == r:
            option1 = abs((lsum + nums[l]) - rsum)
            option2 = abs(lsum - (rsum + nums[l]))
            return min(option1, option2)
        # Flat peak with two equal middle elements
        elif r - l == 1 and nums[l] == nums[r]:
            return abs(lsum - rsum)
        # Invalid mountain
        else:
            return -1
