from collections import Counter


def equalPairs(grid):
    n = len(grid)
    row_counts = Counter(tuple(row) for row in grid)
    col_counts = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
    return sum(row_counts[row] * col_counts[row] for row in row_counts)
