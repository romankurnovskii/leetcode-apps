class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        # Precompute binary palindromes up to 5000
        def is_binary_palindrome(n):
            binary = bin(n)[2:]
            return binary == binary[::-1]
        
        # Generate all binary palindromes
        palindromes = []
        for i in range(1, 5001):
            if is_binary_palindrome(i):
                palindromes.append(i)
        
        res = []
        for num in nums:
            # Find closest palindrome
            min_ops = float('inf')
            for pal in palindromes:
                ops = abs(num - pal)
                min_ops = min(min_ops, ops)
            res.append(min_ops)
        
        return res
