class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Memoization cache for power values
        memo = {}

        def get_power(x: int) -> int:
            if x == 1:
                return 0
            if x in memo:
                return memo[x]

            # Collatz sequence: if even, divide by 2; if odd, 3*x+1
            if x % 2 == 0:
                steps = 1 + get_power(x // 2)
            else:
                steps = 1 + get_power(3 * x + 1)

            memo[x] = steps
            return steps

        # Calculate power for each number in range [lo, hi]
        numbers_with_power = []
        for num in range(lo, hi + 1):
            power = get_power(num)
            numbers_with_power.append((power, num))

        # Sort by power (ascending), then by number (ascending) if powers are equal
        numbers_with_power.sort()

        # Return the k-th element (1-indexed, so k-1)
        return numbers_with_power[k - 1][1]
