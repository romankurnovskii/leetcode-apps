class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        from functools import lru_cache

        rows = len(grid)
        cols = len(grid[0])

        # Get all unique values and sort in descending order
        value_set = set([grid[r][c] for r in range(rows) for c in range(cols)])
        value_list = sorted(list(value_set), reverse=True)

        # Map each value to the list of row indexes containing it
        val_to_rows = defaultdict(list)
        for value in value_list:
            val_to_rows[value] = [r for r in range(rows) if value in grid[r]]

        # DFS with memoization (don't include score in key)
        @lru_cache(maxsize=None)
        def dfs(row_set, value_idx):
            if value_idx == len(value_list):
                return 0

            value = value_list[value_idx]
            score_list = []

            # Try selecting this value from each available row
            for row in val_to_rows[value]:
                if row not in row_set:
                    new_row_set = row_set | frozenset([row])
                    score_list.append(value + dfs(new_row_set, value_idx + 1))

            # Also try skipping this value
            score_list.append(dfs(row_set, value_idx + 1))

            return max(score_list) if score_list else 0

        return dfs(frozenset(), 0)
