from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        
        def backtrack(index, current):
            # Base case: if we've processed all digits
            if index == len(digits):
                res.append(current)
                return
            
            # Get letters for current digit
            letters = digit_map[digits[index]]
            
            # Try each letter
            for letter in letters:
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return res

