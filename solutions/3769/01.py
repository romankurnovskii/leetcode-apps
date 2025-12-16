class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def binary_reflection(n):
            # Convert to binary, reverse, convert back
            binary = bin(n)[2:]  # Remove '0b' prefix
            reversed_binary = binary[::-1]
            return int(reversed_binary, 2)
        
        return sorted(nums, key=lambda x: (binary_reflection(x), x))
