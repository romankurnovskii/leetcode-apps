## Explanation

### Strategy (The "Why")

Given an $n \times n$ adjacency matrix `isConnected` representing cities, where `isConnected[i][j] = 1` means city $i$ and city $j$ are directly connected, we need to find the total number of provinces. A province is a group of directly or indirectly connected cities.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of cities $n$ can be up to $200$.
- **Value Range:** Matrix values are 0 or 1. The matrix is symmetric (undirected graph).
- **Time Complexity:** $O(n^2)$ - We visit each city once, and for each city, we check all $n$ cities to find neighbors. In the worst case, we explore all $n^2$ connections.
- **Space Complexity:** $O(n)$ - We use a visited array of size $n$, and the recursion stack can be at most $O(n)$ deep.
- **Edge Case:** If there are no cities, return 0. If all cities are isolated (no connections), there are $n$ provinces.

**1.2 High-level approach:**

The goal is to find the number of connected components in an undirected graph.

![Number of Provinces](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

We use DFS (depth-first search) to explore each connected component. Each time we start a new DFS from an unvisited city, we've found a new province.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the graph to find connected components.
- **Optimized Strategy (DFS):** Use DFS to explore each connected component. Mark cities as visited to avoid revisiting them. Each unvisited city we encounter represents a new province.
- **Why it's better:** DFS efficiently explores each connected component. We visit each city and each connection at most once, giving us optimal time complexity.

**1.4 Decomposition:**

1. Initialize a visited array to track which cities have been explored.
2. Initialize a counter for provinces.
3. For each city, if it hasn't been visited, increment the province counter and start DFS from that city.
4. In the DFS function, mark the current city as visited and recursively visit all its connected neighbors.
5. Return the total number of provinces.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $isConnected = [[1,1,0],[1,1,0],[0,0,1]]$

The adjacency matrix:
```
City 0: [1, 1, 0]  (connected to 0 and 1)
City 1: [1, 1, 0]  (connected to 0 and 1)
City 2: [0, 0, 1]  (connected only to 2)
```

We initialize:
- `visited = [False, False, False]`
- `res = 0`

**2.2 Start Exploring:**

We begin checking cities from index 0.

**2.3 Trace Walkthrough:**

| Step | Current City | Visited? | Action | DFS Exploration |
|------|--------------|----------|--------|----------------|
| 1 | 0 | No | Start new province, DFS(0) | Mark 0, visit 1 |
| 2 | 1 | No (in DFS) | Continue DFS(1) | Mark 1, check neighbors (0 already visited) |
| 3 | 2 | No | Start new province, DFS(2) | Mark 2, no unvisited neighbors |

Detailed DFS from city 0:
- Mark city 0 as visited
- Check city 1: `isConnected[0][1] = 1` and city 1 not visited → DFS(1)
  - Mark city 1 as visited
  - Check city 0: already visited → skip
  - Check city 2: `isConnected[1][2] = 0` → skip
- Check city 2: `isConnected[0][2] = 0` → skip

DFS from city 2:
- Mark city 2 as visited
- Check neighbors: all either not connected or already visited

**2.4 Provinces Found:**

- Province 1: Cities 0 and 1 (connected)
- Province 2: City 2 (isolated)

**2.5 Return Result:**

We return `res = 2`, which is the total number of provinces.

> **Note:** The key insight is that each time we encounter an unvisited city, it must be part of a new province. DFS ensures we explore the entire connected component before moving to the next city.

