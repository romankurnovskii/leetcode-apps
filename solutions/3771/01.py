class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        
        # Prefix sums for damage
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + damage[i]
        
        # For each room j, count how many starting positions i <= j
        # would result in earning a point at room j
        # Condition: hp - (prefix[j+1] - prefix[i]) >= requirement[j]
        # => hp - prefix[j+1] + prefix[i] >= requirement[j]
        # => prefix[i] >= requirement[j] - hp + prefix[j+1]
        
        res = 0
        import bisect
        for j in range(n):
            threshold = requirement[j] - hp + prefix[j + 1]
            # Use binary search to find first index where prefix[i] >= threshold
            # Since prefix is non-decreasing, we can use bisect_left
            idx = bisect.bisect_left(prefix, threshold, hi=j + 1)
            # All indices from idx to j (inclusive) satisfy the condition
            res += max(0, j + 1 - idx)
        
        return res
