class Solution:
    def minOperations(self, n: int) -> int:
        # The array is [1, 3, 5, ..., 2*n-1]
        # Target value is the average: (1 + 2*n-1) / 2 = n
        # For each element at index i, value is 2*i + 1
        # Operations needed to make it equal to n: |(2*i + 1) - n|
        # But we only need to count half since we can pair operations
        
        res = 0
        for i in range(n // 2):
            target = n
            current = 2 * i + 1
            res += target - current
        
        return res
