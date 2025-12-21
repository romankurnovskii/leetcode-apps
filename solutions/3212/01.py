class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        # Convert to numeric values: X=1, Y=-1, .=0
        # Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == "X":
                    val = 1
                elif grid[i][j] == "Y":
                    val = -1

                prefix[i + 1][j + 1] = (
                    val + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
                )

        res = 0
        # Check all submatrices starting from (0,0)
        for i in range(m):
            for j in range(n):
                # Check if this submatrix contains at least one X
                has_x = False
                for x in range(i + 1):
                    for y in range(j + 1):
                        if grid[x][y] == "X":
                            has_x = True
                            break
                    if has_x:
                        break

                if not has_x:
                    continue

                # Calculate sum of submatrix from (0,0) to (i,j)
                # Using prefix sum: sum = prefix[i+1][j+1]
                if prefix[i + 1][j + 1] == 0:
                    res += 1

        return res
