class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def binary_reflection(n):
            # Convert to binary, reverse, convert back to int
            binary = bin(n)[2:]  # Remove '0b' prefix
            reversed_binary = binary[::-1]  # Reverse the string
            return int(reversed_binary, 2)  # Convert back to int
        
        # Sort by binary reflection, then by original value if reflection is same
        res = sorted(nums, key=lambda x: (binary_reflection(x), x))
        return res

