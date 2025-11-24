class Solution:
    def __init__(self):
        # We precompute the values up to 100,000 (limit from problem constraints)
        MAX_N = 100000
        self.prefix = [0] * (MAX_N + 1)

        running_total = 0

        for i in range(MAX_N + 1):
            waviness = 0
            s = str(i)

            # Only numbers with 3 or more digits can have waviness
            if len(s) >= 3:
                for j in range(1, len(s) - 1):
                    prev_d = int(s[j-1])
                    curr_d = int(s[j])
                    next_d = int(s[j+1])

                    # Check for Peak (prev < curr > next)
                    if prev_d < curr_d and curr_d > next_d:
                        waviness += 1
                    # Check for Valley (prev > curr < next)
                    elif prev_d > curr_d and curr_d < next_d:
                        waviness += 1

            running_total += waviness
            self.prefix[i] = running_total

    def totalWaviness(self, num1: int, num2: int) -> int:
        # Standard prefix sum range query formula:
        # Sum(L, R) = Prefix[R] - Prefix[L-1]

        upper = self.prefix[num2]
        lower = self.prefix[num1 - 1] if num1 > 0 else 0

        res = upper - lower
        return res

