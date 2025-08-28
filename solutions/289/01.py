def gameOfLife(board):
    """
    Update the board to the next generation of Conway's Game of Life.
    This is done in-place using O(1) space.
    
    Args:
        board: List[List[int]] - The board to update in-place
        
    Returns:
        None - Modifies the board in-place
    """
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    
    # First pass: mark cells with their next state using special values
    # 2 = currently live, will die (live→dead)
    # 3 = currently dead, will live (dead→live)
    for i in range(m):
        for j in range(n):
            live_neighbors = countLiveNeighbors(board, i, j, m, n)
            
            if board[i][j] == 1:  # Currently live
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 2  # Mark as live→dead
            else:  # Currently dead
                if live_neighbors == 3:
                    board[i][j] = 3  # Mark as dead→live
    
    # Second pass: convert special values to final states
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0  # Convert live→dead to dead
            elif board[i][j] == 3:
                board[i][j] = 1  # Convert dead→live to live


def countLiveNeighbors(board, i, j, m, n):
    """
    Count the number of live neighbors for a given cell.
    
    Args:
        board: List[List[int]] - The game board
        i, j: int - Row and column indices of the cell
        m, n: int - Dimensions of the board
        
    Returns:
        int - Number of live neighbors
    """
    count = 0
    
    # Check all 8 neighbors
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:  # Skip the cell itself
                continue
            
            ni, nj = i + di, j + dj
            
            # Check bounds
            if 0 <= ni < m and 0 <= nj < n:
                # Count live cells (including those marked as live→dead)
                if board[ni][nj] == 1 or board[ni][nj] == 2:
                    count += 1
    
    return count
