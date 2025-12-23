class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Flatten grid horizontally (row by row)
        hor = ""
        for arr in grid:
            hor += "".join(arr)
        
        # Find all horizontal pattern matches
        res1 = set()
        x = len(pattern)
        for i in range(len(hor) - x + 1):
            if hor[i:i+x] == pattern:
                for j in range(i, i + x):
                    row = j // n
                    col = j % n
                    res1.add((row, col))
        
        if len(res1) == 0:
            return 0
        
        # Flatten grid vertically (column by column)
        var = ""
        for j in range(n):
            for i in range(m):
                var += grid[i][j]
        
        # Find all vertical pattern matches
        res2 = set()
        for i in range(len(var) - x + 1):
            if var[i:i+x] == pattern:
                for j in range(i, i + x):
                    row = j % m
                    col = j // m
                    res2.add((row, col))
        
        # Count cells that are in both horizontal and vertical matches
        res = res1.intersection(res2)
        
        return len(res)

