def setZeroes(matrix):
    """
    Set entire rows and columns to zero if they contain a zero element.
    This is done in-place using O(1) space.
    
    Args:
        matrix: List[List[int]] - The matrix to modify in-place
        
    Returns:
        None - Modifies the matrix in-place
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
