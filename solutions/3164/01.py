class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        res = 0

        # Check each possible starting position
        for i in range(n - m):
            match = True
            # Check if subarray starting at i matches pattern
            for k in range(m):
                if pattern[k] == 1:
                    if nums[i + k + 1] <= nums[i + k]:
                        match = False
                        break
                elif pattern[k] == 0:
                    if nums[i + k + 1] != nums[i + k]:
                        match = False
                        break
                else:  # pattern[k] == -1
                    if nums[i + k + 1] >= nums[i + k]:
                        match = False
                        break

            if match:
                res += 1

        return res
