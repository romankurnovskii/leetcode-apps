from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # pref[i] = length of longest non-decreasing subarray ending at index i
        pref = [1] * n
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                pref[i] = pref[i - 1] + 1
            else:
                pref[i] = 1

        # suff[i] = length of longest non-decreasing subarray starting at index i
        suff = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                suff[i] = suff[i + 1] + 1
            else:
                suff[i] = 1

        # Initial maximum: longest without replacement
        result = max(max(pref), max(suff))

        # Try replacing each element
        for i in range(n):
            if i > 0 and i < n - 1:
                # Case 1: Bridge prefix and suffix if possible
                # When bridging, we replace nums[i] with a value between nums[i-1] and nums[i+1]
                # The combined subarray includes the replaced element, so length is pref[i-1] + 1 + suff[i+1]
                if nums[i - 1] <= nums[i + 1]:
                    combined = pref[i - 1] + 1 + suff[i + 1]
                    result = max(result, combined)
                # Case 2: Extend prefix ending at i-1
                # Set nums[i] >= nums[i-1] to extend prefix
                result = max(result, pref[i - 1] + 1)
                # Case 3: Extend suffix starting at i+1
                # Set nums[i] <= nums[i+1] to extend suffix
                result = max(result, 1 + suff[i + 1])
            elif i == 0:
                # Replace first element: can extend suffix starting at i+1
                if i < n - 1:
                    result = max(result, 1 + suff[i + 1])
            elif i == n - 1:
                # Replace last element: can extend prefix ending at i-1
                if i > 0:
                    result = max(result, pref[i - 1] + 1)

        return result
