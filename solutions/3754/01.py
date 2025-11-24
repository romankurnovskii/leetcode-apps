class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)

        # Filter out '0's
        non_zeros = [c for c in s if c != "0"]

        # Edge case: if n was 0, list is empty
        if not non_zeros:
            return 0

        # Reconstruct the number from non-zero digits
        x = int("".join(non_zeros))

        # Calculate sum of digits
        digit_sum = sum(int(c) for c in non_zeros)

        res = x * digit_sum
        return res

