class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        def backtrack(count):
            res = 0
            for char in count:
                if count[char] > 0:
                    res += 1  # Count this sequence
                    count[char] -= 1
                    res += backtrack(count)
                    count[char] += 1
            return res
        
        count = Counter(tiles)
        return backtrack(count)
