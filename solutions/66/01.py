class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # Add one to current digit
            digits[i] += 1

            # If digit is less than 10, no carry needed
            if digits[i] < 10:
                return digits

            # Handle carry: set current digit to 0
            digits[i] = 0

        # If we reach here, all digits were 9
        # Add new digit at the beginning
        return [1] + digits
