class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # Extract vowels and sort them
        vowel_list = [c for c in s if c in vowels]
        vowel_list.sort()
        
        # Build result
        res = []
        vowel_idx = 0
        for c in s:
            if c in vowels:
                res.append(vowel_list[vowel_idx])
                vowel_idx += 1
            else:
                res.append(c)
        
        return ''.join(res)
