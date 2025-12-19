class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        seen = {(0, 0)}
        x = y = 0
        
        # Sliding window: simulate removing each substring of length k
        # Start by processing characters from k onwards
        for i in range(k, len(s)):
            # Add effect of new character at position i
            if s[i] == 'U':
                y += 1
            elif s[i] == 'D':
                y -= 1
            elif s[i] == 'L':
                x -= 1
            elif s[i] == 'R':
                x += 1
            
            # Remove effect of character at position i - k (leaving the window)
            if s[i - k] == 'U':
                y -= 1
            elif s[i - k] == 'D':
                y += 1
            elif s[i - k] == 'L':
                x += 1
            elif s[i - k] == 'R':
                x -= 1
            
            seen.add((x, y))
        
        return len(seen)

