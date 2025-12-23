class Solution:
    def minOperations(self, s: str) -> int:
        """
        Minimum operations to make all characters 'a'.
        One operation shifts all occurrences of a chosen character forward by 1 (circular).
        The minimum ops equals the maximum distance any char needs to reach 'a'.
        """
        max_dist = 0
        for c in s:
            dist = (26 - (ord(c) - ord("a"))) % 26  # distance to 'a'
            max_dist = max(max_dist, dist)
        return max_dist
