## Explanation

### Strategy

**Constraints & Edge Cases**

* **Graph Size:** The DAG has 2-15 nodes labeled 0 to n-1. The graph is guaranteed to be acyclic and connected from node 0 to node n-1.
* **Time Complexity:** We use DFS to explore all paths. In worst case, there can be exponential number of paths, but with n ≤ 15, this is manageable. **Time Complexity: O(2^n)** in worst case, **Space Complexity: O(n)** for recursion stack and path storage.
* **Edge Case:** If there's only one path from 0 to n-1, we return that single path.

**High-level approach**

The problem asks us to find all paths from node 0 to node n-1 in a directed acyclic graph. We use depth-first search to explore all possible paths.

**Brute force vs. optimized strategy**

* **Brute Force:** This is essentially what we do - explore all paths. Since the graph is acyclic, we don't need to worry about cycles, making DFS straightforward.
* **Optimized:** Use DFS with backtracking. When we reach node n-1, we save the current path. We backtrack to explore other paths.

**Decomposition**

1. **DFS Traversal:** Start from node 0, recursively visit all neighbors.
2. **Path Tracking:** Maintain current path as we traverse.
3. **Result Collection:** When we reach node n-1, add the current path to results.
4. **Backtracking:** Remove current node from path before returning to explore other paths.

### Steps

1. **Initialization & Example Setup**
   Let's use `graph = [[1,2],[3],[3],[]]` as our example.
   - Initialize `res = []` to store all paths.
   - Start DFS from node 0 with path `[0]`.

2. **DFS Function**
   The `dfs(node, path)` function:
   - If `node == n - 1`, we found a path → append `path[:]` to `res`.
   - For each neighbor in `graph[node]`:
     - Add neighbor to path.
     - Recursively call `dfs(neighbor, path)`.
     - Remove neighbor from path (backtrack).

3. **Trace Walkthrough**

Starting from node 0:

| Step | Current Node | Path | Neighbors | Action |
|------|--------------|------|-----------|--------|
| 1    | 0            | [0]  | [1,2]     | Go to 1 |
| 2    | 1            | [0,1]| [3]       | Go to 3 |
| 3    | 3            | [0,1,3] | []    | Found path! Add [0,1,3] |
| 4    | 1            | [0,1]| [3]       | Backtrack, return |
| 5    | 0            | [0]  | [1,2]     | Go to 2 |
| 6    | 2            | [0,2]| [3]       | Go to 3 |
| 7    | 3            | [0,2,3] | []    | Found path! Add [0,2,3] |

4. **Backtracking**
   After exploring a path, we remove the last node to try other branches:
   - After finding [0,1,3], remove 3, then remove 1.
   - Now we can explore path through node 2.

5. **Return Result**
   Return `res = [[0,1,3], [0,2,3]]`.
