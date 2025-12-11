from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate XOR of entire array
        total_xor = 0
        for num in nums:
            total_xor ^= num

        # If total XOR is non-zero, entire array is valid
        if total_xor != 0:
            return n

        # If total XOR is zero, we need to remove at least one element
        # Try removing each element and check if XOR becomes non-zero
        for i in range(n):
            # XOR without nums[i]
            xor_without = total_xor ^ nums[i]
            if xor_without != 0:
                return n - 1

        # If all elements are 0, return 0
        return 0
