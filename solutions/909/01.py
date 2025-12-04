from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_position(square):
            # Convert square number to row, col
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:  # Odd rows are reversed
                col = n - 1 - col
            row = n - 1 - row  # Board is bottom-up
            return row, col
        
        queue = deque([(1, 0)])  # (square, moves)
        visited = {1}
        
        while queue:
            square, moves = queue.popleft()
            
            if square == n * n:
                return moves
            
            # Try all 6 possible moves
            for next_square in range(square + 1, min(square + 7, n * n + 1)):
                row, col = get_position(next_square)
                
                # Check if there's a snake or ladder
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1

