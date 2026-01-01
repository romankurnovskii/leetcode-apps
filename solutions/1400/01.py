from typing import List


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        from collections import Counter

        count = Counter(s)
        odd_count = sum(1 for v in count.values() if v % 2 == 1)

        return odd_count <= k
