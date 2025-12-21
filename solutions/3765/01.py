class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        s = str(num)
        n = len(s)

        # Check all prefixes
        for i in range(1, n + 1):
            prefix = int(s[:i])
            if not is_prime(prefix):
                return False

        # Check all suffixes
        for i in range(n):
            suffix = int(s[i:])
            if not is_prime(suffix):
                return False

        return True
