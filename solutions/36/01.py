class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create sets to track seen numbers in each row, column, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                cell = board[i][j]

                # Skip empty cells
                if cell == ".":
                    continue

                # Calculate which 3x3 box this cell belongs to
                box_index = (i // 3) * 3 + (j // 3)

                # Check if this number is already seen in row, column, or box
                if cell in rows[i] or cell in cols[j] or cell in boxes[box_index]:
                    return False

                # Add the number to all three tracking sets
                rows[i].add(cell)
                cols[j].add(cell)
                boxes[box_index].add(cell)

        # If we complete the entire board without finding duplicates, it's valid
        return True
