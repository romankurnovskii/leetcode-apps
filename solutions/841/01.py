from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(room):
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    dfs(key)

        # Start from room 0
        dfs(0)

        # Check if all rooms are visited
        return all(visited)
