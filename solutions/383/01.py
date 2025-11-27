class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count characters in magazine
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Check if we can construct ransomNote
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True

