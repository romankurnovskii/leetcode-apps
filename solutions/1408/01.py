from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words_set = set(words)

        for word in words:
            for other in words_set:
                if word != other and word in other:
                    res.append(word)
                    break

        return res
