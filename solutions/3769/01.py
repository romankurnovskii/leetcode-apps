from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def binary_reflection(n):
            # Convert to binary, remove '0b' prefix, reverse, convert back to int
            binary = bin(n)[2:]
            reversed_binary = binary[::-1]
            return int(reversed_binary, 2)

        # Sort by binary reflection, then by original value if reflection is equal
        res = sorted(nums, key=lambda x: (binary_reflection(x), x))
        return res

