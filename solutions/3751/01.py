class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(num: int) -> int:
            # Convert number to string to access digits
            s = str(num)

            # Numbers with fewer than 3 digits have waviness 0
            if len(s) < 3:
                return 0

            waviness = 0
            # Check each middle digit (not first or last)
            for i in range(1, len(s) - 1):
                digit = int(s[i])
                left = int(s[i - 1])
                right = int(s[i + 1])

                # Check if it's a peak (strictly greater than both neighbors)
                if digit > left and digit > right:
                    waviness += 1
                # Check if it's a valley (strictly less than both neighbors)
                elif digit < left and digit < right:
                    waviness += 1

            return waviness

        # Sum waviness for all numbers in the range
        total = 0
        for num in range(num1, num2 + 1):
            total += get_waviness(num)

        return total
