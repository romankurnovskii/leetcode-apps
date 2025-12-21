class Solution:
    def totalNQueens(self, n: int) -> int:
        # Track which columns, diagonals, and anti-diagonals are occupied
        cols = set()
        diag1 = set()  # row - col (constant for same diagonal)
        diag2 = set()  # row + col (constant for same anti-diagonal)

        res = 0

        def backtrack(row):
            nonlocal res
            # Base case: all rows have been placed
            if row == n:
                res += 1
                return

            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if this position is under attack
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place the queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack: remove the queen
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res
