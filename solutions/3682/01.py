from typing import List


class Solution:
    def minIndexSum(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {word: i for i, word in enumerate(list1)}
        min_sum = float("inf")
        res = []

        for i, word in enumerate(list2):
            if word in index_map:
                total = i + index_map[word]
                if total < min_sum:
                    min_sum = total
                    res = [word]
                elif total == min_sum:
                    res.append(word)

        return res
