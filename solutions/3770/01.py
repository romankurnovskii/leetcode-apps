class Solution:
    def largestPrime(self, n: int) -> int:
        # Sieve of Eratosthenes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        # Get all primes
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        
        # Compute consecutive prime sums starting from 2
        res = 0
        for start in range(len(primes)):
            current_sum = 0
            for end in range(start, len(primes)):
                current_sum += primes[end]
                if current_sum > n:
                    break
                # Check if sum is prime and <= n
                if current_sum <= n and is_prime[current_sum]:
                    res = max(res, current_sum)
        
        return res
