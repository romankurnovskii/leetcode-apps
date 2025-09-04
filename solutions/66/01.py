def plusOne(digits: List[int]) -> List[int]:
    # Start from the last digit
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1

        if digits[i] < 10:
            return digits

        digits[i] = 0

    # If we reach here, all digits were 9
    # Add new digit at the beginning
    return [1] + digits
