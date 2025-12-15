class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Find team that beats all others (row has all 1s except diagonal)
        for i in range(n):
            is_champion = True
            for j in range(n):
                if i != j and grid[i][j] == 0:
                    is_champion = False
                    break
            if is_champion:
                return i

        return -1
