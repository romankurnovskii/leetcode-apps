from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        from collections import Counter

        # Count available letters
        letter_count = Counter(letters)

        # Calculate score for each word
        def word_score(word):
            return sum(score[ord(c) - ord("a")] for c in word)

        # Check if word can be formed with available letters
        def can_form(word, available):
            word_count = Counter(word)
            for char, count in word_count.items():
                if available[char] < count:
                    return False
            return True

        # Use word and update available letters
        def use_word(word, available):
            word_count = Counter(word)
            for char, count in word_count.items():
                available[char] -= count

        # Restore available letters
        def restore_word(word, available):
            word_count = Counter(word)
            for char, count in word_count.items():
                available[char] += count

        # Backtracking
        def backtrack(idx, available):
            if idx == len(words):
                return 0

            # Option 1: Skip current word
            res = backtrack(idx + 1, available)

            # Option 2: Use current word if possible
            word = words[idx]
            if can_form(word, available):
                use_word(word, available)
                res = max(res, word_score(word) + backtrack(idx + 1, available))
                restore_word(word, available)

            return res

        res = backtrack(0, letter_count)
        return res
