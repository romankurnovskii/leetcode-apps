class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        # Generate largest n-digit number
        max_num = 10**n - 1
        min_num = 10 ** (n - 1)

        # Try from largest to smallest
        for num in range(max_num, min_num - 1, -1):
            num_str = str(num)
            # Check if it's a palindrome
            if num_str == num_str[::-1]:
                # Check if divisible by k
                if num % k == 0:
                    return num_str

        return ""
