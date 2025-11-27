from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        digit_to_letters = {
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
        
        def backtrack(index, current_combination):
            # Base case: if we've processed all digits
            if index == len(digits):
                res.append(current_combination)
                return
            
            # Get letters for current digit
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            
            # Try each letter for current digit
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return res

