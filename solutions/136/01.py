class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize result
        result = 0

        # XOR all numbers in the array
        for num in nums:
            result ^= num

        # Return the single number
        return result
