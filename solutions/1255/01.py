class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        # Count available letters
        count = [0] * 26
        for letter in letters:
            count[ord(letter) - ord("a")] += 1

        def backtrack(index: int) -> int:
            if index == len(words):
                return 0

            # Option 1: Skip current word
            max_score = backtrack(index + 1)

            # Option 2: Try to use current word
            word = words[index]
            word_score = 0
            can_use = True

            # Check if we can form this word
            for char in word:
                idx = ord(char) - ord("a")
                count[idx] -= 1
                word_score += score[idx]
                if count[idx] < 0:
                    can_use = False

            # If we can use this word, recurse and add its score
            if can_use:
                max_score = max(max_score, word_score + backtrack(index + 1))

            # Backtrack: restore letter counts
            for char in word:
                count[ord(char) - ord("a")] += 1

            return max_score

        return backtrack(0)
