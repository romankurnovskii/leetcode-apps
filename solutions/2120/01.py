from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        res = []
        
        # Direction mapping
        directions = {
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        
        for i in range(m):
            row, col = startPos[0], startPos[1]
            count = 0
            
            for j in range(i, m):
                dr, dc = directions[s[j]]
                new_row, new_col = row + dr, col + dc
                
                # Check if next move is valid
                if 0 <= new_row < n and 0 <= new_col < n:
                    row, col = new_row, new_col
                    count += 1
                else:
                    break
            
            res.append(count)
        
        return res
