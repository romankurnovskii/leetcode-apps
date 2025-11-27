from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the rightmost digit
        for i in range(len(digits) - 1, -1, -1):
            # If digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set to 0 and continue (carry over)
            digits[i] = 0
        
        # If we reach here, all digits were 9, need to add 1 at the beginning
        return [1] + digits
