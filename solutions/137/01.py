class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  # Bits that appear once
        twos = 0  # Bits that appear twice
        
        for num in nums:
            # Update ones: bits that appear once (not in twos)
            ones = (ones ^ num) & ~twos
            # Update twos: bits that appear twice (in ones)
            twos = (twos ^ num) & ~ones
        
        return ones

