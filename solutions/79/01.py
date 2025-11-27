from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(row, col, index):
            # Base case: found the word
            if index == len(word):
                return True
            
            # Check bounds and if current cell matches
            if (row < 0 or row >= m or col < 0 or col >= n or 
                board[row][col] != word[index]):
                return False
            
            # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = '#'
            
            # Explore 4 directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                if dfs(row + dr, col + dc, index + 1):
                    return True
            
            # Backtrack: restore cell
            board[row][col] = temp
            return False
        
        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False

