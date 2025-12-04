from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build graph: graph[a][b] = value means a / b = value
        graph = defaultdict(dict)
        
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                node, value = queue.popleft()
                
                if node == end:
                    return value
                
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, value * weight))
            
            return -1.0
        
        res = []
        for a, b in queries:
            res.append(bfs(a, b))
        
        return res

