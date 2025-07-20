## 3607. Power Grid Maintenance [Medium]

https://leetcode.com/problems/power-grid-maintenance

## Description

You are given an integer `c` representing `c` power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing).

These stations are interconnected via `n` **bidirectional** cables, represented by a 2D array `connections`, where each element `connections[i] = [u_i, v_i]` indicates a connection between station `u_i` and station `v_i`. Stations that are directly or indirectly connected form a **power grid**.

Initially, **all** stations are online (operational).

You are also given a 2D array `queries`, where each query is one of the following two types:

- `[1, x]`: A maintenance check is requested for station `x`. If station `x` is online, it resolves the check by itself. If station `x` is offline, the check is resolved by the operational station with the smallest `id` in the same **power grid** as `x`. If **no** operational station exists in that grid, return -1.
- `[2, x]`: Station `x` goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type `[1, x]` in the **order** they appear.

**Note:** The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

**Examples**

**Example 1:**

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:
- Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
- Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
- Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
- Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
- Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
- Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.

**Example 2:**

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:
- There are no connections, so each station is its own isolated grid.
- Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
- Query [2,1]: Station 1 goes offline.
- Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.

**Constraints**
```text
1 <= c <= 10^5
0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)
connections[i].length == 2
1 <= u_i, v_i <= c
u_i != v_i
1 <= queries.length <= 2 * 10^5
queries[i].length == 2
queries[i][0] is either 1 or 2.
1 <= queries[i][1] <= c
```

## Explanation

### Strategy

Let's restate the problem:
- We have a set of power stations connected by cables, forming one or more power grids (connected components).
- Each station can go offline, but the grid structure does not change.
- For a maintenance check, if the station is online, it handles the check; if offline, the smallest online station in the same grid handles it (or -1 if none).

**Type:** Graph, Union Find, Heap, DFS, Ordered Set

**What is being asked?**
- Efficiently answer queries about which station can handle a maintenance check, considering online/offline status and grid structure.

**What is given?**
- Number of stations, connections, and a list of queries.

**Constraints/Edge Cases:**
- Up to 10^5 stations and 2*10^5 queries.
- Stations can go offline, but the grid structure is static.

**High-Level Plan:**
- Precompute connected components (power grids) using DFS or Union Find (DSU).
- For each component, maintain a data structure (set, heap, or sorted list) of online stations.
- For type 1 queries, if the station is online, return it; otherwise, return the smallest online station in its component, or -1 if none.
- For type 2 queries, mark the station as offline (remove from set/heap/list or mark in a boolean array).

### Steps

1. **Build the graph and find connected components:**
   - Use DFS or DSU to assign each station a component ID.
2. **For each component, track online stations:**
   - Use a set, heap, or sorted list for fast lookup of the smallest online station.
3. **Process queries:**
   - For `[1, x]`, if `x` is online, return `x`; else, return the smallest online station in the same component, or -1 if none.
   - For `[2, x]`, mark `x` as offline.

**Example Walkthrough:**

Suppose c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

- All stations are online and form a single grid.
- [1,3]: 3 is online → return 3
- [2,1]: 1 goes offline
- [1,1]: 1 is offline, smallest online in grid is 2 → return 2
- [2,2]: 2 goes offline
- [1,2]: 2 is offline, smallest online in grid is 3 → return 3

> **Note:** The grid structure is static; only online/offline status changes.

