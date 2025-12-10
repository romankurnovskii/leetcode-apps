class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(n):
            s = str(n)
            if len(s) < 3:
                return 0

            waviness = 0
            for i in range(1, len(s) - 1):
                # Check if digit at i is a peak or valley
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    waviness += 1  # Peak
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    waviness += 1  # Valley

            return waviness

        res = 0
        for num in range(num1, num2 + 1):
            res += get_waviness(num)

        return res
