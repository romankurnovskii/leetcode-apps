class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        
        # Count frequency of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        length = 0
        has_odd = False
        
        # For each character count
        for count in char_count.values():
            # Add even pairs
            length += (count // 2) * 2
            # Check if there's an odd count (for center character)
            if count % 2 == 1:
                has_odd = True
        
        # Add 1 for center character if we have any odd counts
        if has_odd:
            length += 1
        
        return length

