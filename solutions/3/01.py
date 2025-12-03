class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use sliding window with hash set to track characters
        char_set = set()
        left = 0
        res = 0
        
        for right in range(len(s)):
            # If character already in window, shrink from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character and update max length
            char_set.add(s[right])
            res = max(res, right - left + 1)
        
        return res

