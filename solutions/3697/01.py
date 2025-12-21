from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        # Convert to string to access digits
        s = str(n)
        components = []

        # Process each digit from right to left (ones place to highest place)
        # We'll build components and then reverse to get descending order
        for i in range(len(s) - 1, -1, -1):
            digit = int(s[i])
            if digit != 0:
                # Calculate the power of 10 for this position
                # Position 0 (rightmost) = 10^0, position 1 = 10^1, etc.
                power = len(s) - 1 - i
                component = digit * (10**power)
                components.append(component)

        # Return in descending order (largest to smallest)
        return components[::-1]
