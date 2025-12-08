class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Calculate XOR of all elements
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Count different bits between xor_all and k
        diff = xor_all ^ k
        res = bin(diff).count("1")
        return res
