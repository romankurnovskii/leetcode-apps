class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # Start with array of all 1s
        arr = [1] * n
        
        # Apply prefix sum k times
        for _ in range(k):
            for i in range(1, n):
                arr[i] = (arr[i] + arr[i - 1]) % MOD
        
        return arr[n - 1]

