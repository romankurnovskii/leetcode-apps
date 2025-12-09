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
            # Use binary search to find closest palindrome
            import bisect
            idx = bisect.bisect_left(palindromes, num)
            
            min_ops = float('inf')
            # Check the palindrome at idx (if exists)
            if idx < len(palindromes):
                min_ops = min(min_ops, abs(num - palindromes[idx]))
            # Check the palindrome before idx (if exists)
            if idx > 0:
                min_ops = min(min_ops, abs(num - palindromes[idx - 1]))
            
            res.append(min_ops)
        
        return res
