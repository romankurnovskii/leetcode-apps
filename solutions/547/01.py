from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        res = 0

        def dfs(city):
            # Mark current city as visited
            visited[city] = True

            # Check all other cities
            for neighbor in range(n):
                # If connected and not visited, visit it
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        # Try to start DFS from each city
        for i in range(n):
            if not visited[i]:
                # New province found
                res += 1
                dfs(i)

        return res
