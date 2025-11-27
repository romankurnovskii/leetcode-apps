class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count characters in t
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        # Sliding window
        left = 0
        right = 0
        window = {}
        valid = 0  # Number of characters that satisfy the requirement
        start = 0
        min_len = float('inf')
        
        while right < len(s):
            # Expand window
            char = s[right]
            right += 1
            
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1
            
            # Shrink window
            while valid == len(need):
                # Update minimum window
                if right - left < min_len:
                    start = left
                    min_len = right - left
                
                # Remove left character
                left_char = s[left]
                left += 1
                
                if left_char in need:
                    if window[left_char] == need[left_char]:
                        valid -= 1
                    window[left_char] -= 1
        
        return "" if min_len == float('inf') else s[start:start + min_len]

