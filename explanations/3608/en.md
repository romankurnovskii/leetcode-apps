## 3608. Minimum Time for K Connected Components (Medium)

https://leetcode.com/problems/minimum-time-for-k-connected-components

## Description

You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [u_i, v_i, time_i] indicates an undirected edge between nodes u_i and v_i that can be removed at time_i.

You are also given an integer k.

Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t, the graph contains at least k connected components.

Return the minimum time t.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

## Examples

**Example 1**

    Input: n = 2, edges = [[0,1,3]], k = 2
    Output: 3
    Explanation:
    - Initially, there is one connected component {0, 1}.
    - At time = 1 or 2, the graph remains unchanged.
    - At time = 3, edge [0, 1] is removed, resulting in k = 2 connected components {0}, {1}. Thus, the answer is 3.

**Example 2**

    Input: n = 3, edges = [[0,1,2],[1,2,4]], k = 3
    Output: 4
    Explanation:
    - Initially, there is one connected component {0, 1, 2}.
    - At time = 2, edge [0, 1] is removed, resulting in two connected components {0}, {1, 2}.
    - At time = 4, edge [1, 2] is removed, resulting in k = 3 connected components {0}, {1}, {2}. Thus, the answer is 4.

**Example 3**

    Input: n = 3, edges = [[0,2,5]], k = 2
    Output: 0
    Explanation:
    - Since there are already k = 2 disconnected components {1}, {0, 2}, no edge removal is needed. Thus, the answer is 0.

## Constraints

```
- 1 <= n <= 10^5
- 0 <= edges.length <= 10^5
- edges[i] = [u_i, v_i, time_i]
- 0 <= u_i, v_i < n
- u_i != v_i
- 1 <= time_i <= 10^9
- 1 <= k <= n
- There are no duplicate edges.
```

## Explanation

### Strategy

Let's restate the problem:
- You have a graph with n nodes and edges, each edge can be removed at a certain time.
- You want to find the minimum time t such that, after removing all edges with time <= t, the graph has at least k connected components.

**Type:** Graph, Binary Search, Union-Find (DSU)

**What is given:**
- n: number of nodes
- edges: list of [u, v, time] edges
- k: required number of connected components

**What is asked:**
- The minimum time t so that after removing all edges with time <= t, the graph has at least k connected components.

**Constraints/Edge Cases:**
- The graph may already have at least k components at the start.
- There may be no edges.
- n and edges can be large (up to 1e5).

**High-level plan:**
- Use binary search on t (the time threshold).
- For each candidate t, use union-find to count the number of connected components after removing all edges with time <= t.
- The answer is the smallest t for which the number of components is at least k.

### Steps

1. **Binary Search:**
   - Sort all unique edge times and use binary search to find the smallest t such that the number of connected components is at least k after removing all edges with time <= t.
2. **Union-Find (DSU):**
   - For each candidate t, use union-find to connect all nodes with edges having time > t, then count the number of connected components.
3. **Edge Cases:**
   - If the initial graph already has at least k components, return 0.
   - If there are no edges, return 0 if k <= n, else -1.

#### Example Walkthrough

Suppose n = 3, edges = [[0,1,2],[1,2,4]], k = 3:
- Try t = 2: Remove edge [0,1]. The graph has two components: {0}, {1,2}.
- Try t = 4: Remove both edges. The graph has three components: {0}, {1}, {2}.
- The minimum t is 4.

### Solution

```python
from typing import List

def count_components(n, edges_by_time, t):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px
    for u, v, time in edges_by_time:
        if time > t:
            union(u, v)
    comps = set(find(i) for i in range(n))
    return len(comps)

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if k == n:
            return 0
        if not edges:
            return 0 if k <= n else -1
        edges_by_time = sorted(edges, key=lambda x: x[2])
        lo, hi = 0, max(e[2] for e in edges)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            comps = count_components(n, edges_by_time, mid)
            if comps >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

**Time Complexity:** O(E log T), where E is the number of edges and T is the range of possible times (up to 1e9). Each binary search step requires a union-find pass over all edges.

**Space Complexity:** O(N), for the union-find parent array.

