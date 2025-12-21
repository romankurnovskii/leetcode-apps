class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)

        for spell in spells:
            target = (success + spell - 1) // spell
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            res.append(n - left)

        return res
