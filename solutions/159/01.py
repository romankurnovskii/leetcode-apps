from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        char_count = defaultdict(int)
        
        while right < len(s):
            char_count[s[right]] += 1
            
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res

