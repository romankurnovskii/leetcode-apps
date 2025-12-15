class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        # Extract and sort vowels
        vowel_list = [char for char in s if char in vowels]
        vowel_list.sort()

        # Build result
        res = []
        vowel_idx = 0
        for char in s:
            if char in vowels:
                res.append(vowel_list[vowel_idx])
                vowel_idx += 1
            else:
                res.append(char)

        return "".join(res)
