class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Generate Fibonacci numbers up to k
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        res = 0
        idx = len(fib) - 1

        while k > 0:
            if fib[idx] <= k:
                k -= fib[idx]
                res += 1
            idx -= 1

        return res
