class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = 0

        # Greedy: flip from left to right
        while i < n:
            if nums[i] == 0:
                # Need to flip this position
                if i + 2 < n:
                    # Flip 3 consecutive elements
                    nums[i] ^= 1
                    nums[i + 1] ^= 1
                    nums[i + 2] ^= 1
                    res += 1
                else:
                    # Cannot flip, impossible
                    return -1
            i += 1

        # Check if all are 1
        if all(num == 1 for num in nums):
            return res
        else:
            return -1
