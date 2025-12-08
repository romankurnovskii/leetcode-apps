class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        # Iterate over all possible pairs (a, b)
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # Calculate c^2 = a^2 + b^2
                c_squared = a * a + b * b
                c = int(c_squared**0.5)

                # Check if c is a perfect square and within range
                if c * c == c_squared and 1 <= c <= n:
                    res += 1

        return res
