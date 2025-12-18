class Solution:
    def reverseWords(self, s: str) -> str:
        def count_vowels(word):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return sum(1 for char in word if char in vowels)
        
        words = s.split()
        if not words:
            return s
        
        # Count vowels in first word
        first_vowel_count = count_vowels(words[0])
        
        # Process remaining words
        res = [words[0]]
        for i in range(1, len(words)):
            word = words[i]
            vowel_count = count_vowels(word)
            if vowel_count == first_vowel_count:
                # Reverse the word
                res.append(word[::-1])
            else:
                res.append(word)
        
        return ' '.join(res)
