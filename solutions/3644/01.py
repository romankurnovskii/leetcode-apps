class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Take bitwise AND of all misplaced numbers
        mask = (1 << 30) - 1  # All bits set
        for i, val in enumerate(nums):
            if val != i:
                mask &= val
        # If mask unchanged (no mismatches), return 0
        return 0 if mask == (1 << 30) - 1 else mask
