class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Sum of first n odd numbers = n * n
        # Sum of first n even numbers = n * (n + 1)
        # GCD(n * n, n * (n + 1)) = n * GCD(n, n + 1) = n * 1 = n
        # Since GCD(n, n + 1) = 1 (consecutive integers are coprime)
        return n
