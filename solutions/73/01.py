def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    if not matrix or not matrix[0]:
        return
    
    m, n = len(matrix), len(matrix[0])
    
    # Use first row and column as markers
    # We need to handle them separately since they're used as markers
    first_row_has_zero = False
    first_col_has_zero = False
    
    # Check if first row has any zeros
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break
    
    # Check if first column has any zeros
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break
    
    # Use first row and column as markers for other elements
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark row i
                matrix[0][j] = 0  # Mark column j
    
    # Set rows to zero based on markers (excluding first row)
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
    
    # Set columns to zero based on markers (excluding first column)
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0
    
    # Handle first row
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    # Handle first column
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
