class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        if not words:
            return ""
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        first_vowel_count = sum(1 for c in words[0] if c in vowels)
        
        res = [words[0]]
        for word in words[1:]:
            vowel_count = sum(1 for c in word if c in vowels)
            if vowel_count == first_vowel_count:
                res.append(word[::-1])
            else:
                res.append(word)
        
        return ' '.join(res)

