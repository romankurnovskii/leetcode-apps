class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            remainder = num % 3
            if remainder != 0:
                # We can either add (3 - remainder) or subtract remainder
                # Choose the minimum operations (always 1)
                res += 1
        return res
