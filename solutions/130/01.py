class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            # Mark 'O' on border and connected to border as 'E' (escape)
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
                return

            board[i][j] = "E"
            # Check all 4 directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Mark all border 'O's and their connections as 'E'
        for i in range(m):
            dfs(i, 0)  # Left border
            dfs(i, n - 1)  # Right border

        for j in range(n):
            dfs(0, j)  # Top border
            dfs(m - 1, j)  # Bottom border

        # Convert remaining 'O' to 'X' and 'E' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
