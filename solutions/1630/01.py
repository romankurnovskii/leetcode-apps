from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        
        for i in range(len(l)):
            # Extract subarray
            subarray = nums[l[i]:r[i] + 1]
            
            # Sort the subarray
            sorted_sub = sorted(subarray)
            
            # Check if it's arithmetic
            if len(sorted_sub) <= 1:
                res.append(True)
            else:
                diff = sorted_sub[1] - sorted_sub[0]
                is_arithmetic = True
                for j in range(2, len(sorted_sub)):
                    if sorted_sub[j] - sorted_sub[j - 1] != diff:
                        is_arithmetic = False
                        break
                res.append(is_arithmetic)
        
        return res
