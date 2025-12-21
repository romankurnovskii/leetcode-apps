class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        if not words:
            return ""

        # Count vowels in the first word
        first_word_vowels = sum(1 for c in words[0] if c in "aeiou")

        # Process remaining words
        res = [words[0]]

        for word in words[1:]:
            # Count vowels in current word
            vowel_count = sum(1 for c in word if c in "aeiou")

            # If vowel count matches first word, reverse it
            if vowel_count == first_word_vowels:
                res.append(word[::-1])
            else:
                res.append(word)

        return " ".join(res)
