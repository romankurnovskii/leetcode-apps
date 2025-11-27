from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Original color at starting position
        original_color = image[sr][sc]
        
        # If original color is same as new color, no change needed
        if original_color == color:
            return image
        
        m, n = len(image), len(image[0])
        
        def dfs(r, c):
            # Check bounds and if pixel has original color
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original_color:
                return
            
            # Change color
            image[r][c] = color
            
            # Recursively fill adjacent pixels (4-directional)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        # Start flood fill from starting position
        dfs(sr, sc)
        
        return image

