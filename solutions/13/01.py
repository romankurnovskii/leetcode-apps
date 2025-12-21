class Solution:
    def romanToInt(self, s: str) -> int:
        # Map of Roman symbols to values
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        prev_value = 0

        # Process from right to left
        for i in range(len(s) - 1, -1, -1):
            current_value = roman_map[s[i]]

            # If current value is less than previous, subtract it
            # Otherwise, add it
            if current_value < prev_value:
                res -= current_value
            else:
                res += current_value

            prev_value = current_value

        return res
