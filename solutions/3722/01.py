class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        res = s  # Start with original string
        
        # Try reversing first k characters for k from 1 to n
        for k in range(1, n + 1):
            # Reverse first k characters
            reversed_str = s[:k][::-1] + s[k:]
            if reversed_str < res:
                res = reversed_str
        
        # Try reversing last k characters for k from 1 to n
        for k in range(1, n + 1):
            # Reverse last k characters
            reversed_str = s[:n-k] + s[n-k:][::-1]
            if reversed_str < res:
                res = reversed_str
        
        return res

