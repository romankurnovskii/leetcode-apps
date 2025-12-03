class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        # Create rows to store characters
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Distribute characters into rows
        for char in s:
            rows[current_row] += char
            
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to next row
            current_row += 1 if going_down else -1
        
        # Concatenate all rows
        res = "".join(rows)
        return res

