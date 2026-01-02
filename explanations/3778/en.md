## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a weighted graph with n nodes and edges, we need to find the minimum distance from node 1 to node n, excluding the edge with the maximum weight.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes n can be up to 10^4, and the number of edges can be up to 10^4.
- **Time Complexity:** O(E log V) - we use Dijkstra's algorithm which is O(E log V) where E is the number of edges and V is the number of vertices.
- **Space Complexity:** O(V + E) - we need to store the graph and distance array.
- **Edge Case:** If excluding the maximum edge makes the graph disconnected, return -1. If there's only one path and it uses the maximum edge, we need to find an alternative.

**1.2 High-level approach:**

The goal is to find the maximum weight edge first, then run Dijkstra's algorithm while excluding that edge to find the shortest path.

![Graph pathfinding visualization](https://assets.leetcode.com/static_assets/others/graph-path.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try removing each edge and run Dijkstra for each. This is O(E^2 log V) which is inefficient.
- **Optimized Strategy:** Identify the maximum weight edge first, then run Dijkstra once excluding only that edge. This is O(E log V) time.
- **Optimization:** By identifying the maximum edge first and excluding only it, we avoid multiple Dijkstra runs and solve efficiently.

**1.4 Decomposition:**

1. Build the graph from the given edges.
2. Find the edge with maximum weight.
3. Run Dijkstra's algorithm excluding the maximum weight edge.
4. Return the shortest distance from node 1 to node n, or -1 if unreachable.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `edges = [[1,2,3], [2,3,5], [1,3,7]]`, `n = 3`

- Graph: `{1: [(2,3), (3,7)], 2: [(1,3), (3,5)], 3: [(1,7), (2,5)]}`
- Maximum edge: `(1, 3)` with weight `7`
- Result variable: `res = -1`

**2.2 Start Checking:**

We run Dijkstra excluding the maximum edge (1, 3).

**2.3 Trace Walkthrough:**

| Step | Node | Distance | Action |
| ---- | ---- | -------- | ------ |
| 1    | 1    | 0        | Start |
| 2    | 2    | 3        | Via edge (1,2) |
| 3    | 3    | 8        | Via path 1->2->3 (3+5=8) |

**2.4 Increment and Loop:**

Dijkstra's algorithm processes nodes in order of increasing distance until reaching node n.

**2.5 Return Result:**

The result is `8`, which is the minimum distance from node 1 to node 3 excluding the maximum edge (1,3) with weight 7.

