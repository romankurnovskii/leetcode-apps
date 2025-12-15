from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        res = 0
        
        def backtrack():
            nonlocal res
            for char in count:
                if count[char] > 0:
                    # Use this character
                    count[char] -= 1
                    res += 1
                    backtrack()
                    # Backtrack
                    count[char] += 1
        
        backtrack()
        return res
