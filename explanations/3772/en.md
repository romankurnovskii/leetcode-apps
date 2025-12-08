## Explanation

### Strategy (The "Why")

**Restate the problem:** For each node i, we need to find the maximum score among all connected subgraphs that contain node i. The score is the number of good nodes minus the number of bad nodes.

**1.1 Constraints & Complexity:**
- Input size: `2 <= n <= 10^5`
- **Time Complexity:** O(n²) for naive approach, can be optimized with tree DP
- **Space Complexity:** O(n) for the tree and DP arrays
- **Edge Case:** If all nodes are bad, the best score for each node might be -1

**1.2 High-level approach:**
We use tree dynamic programming with rerooting. For each node as root, we perform DFS to find the maximum score of connected subgraphs containing that root.

![Tree DP visualization](https://assets.leetcode.com/static_assets/others/tree-dp-rerooting.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each node, try all possible connected subgraphs, which is exponential
- **Optimized Strategy:** Use tree DP where for each root, we calculate the best subtree score, achieving O(n²) time
- **Emphasize the optimization:** Tree structure allows efficient calculation of subtree scores

**1.4 Decomposition:**
1. Build the tree from edges
2. For each node as root, perform DFS
3. During DFS, calculate the maximum score of connected subgraph containing the root
4. Include child subtrees only if they improve the total score
5. Return the array of maximum scores for each node

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 3`, `edges = [[0,1],[1,2]]`, `good = [1,0,1]`
- Tree: 0-1-2
- Node scores: 0→+1, 1→-1, 2→+1

**2.2 Start DFS:**
We perform DFS for each node as root.

**2.3 Trace Walkthrough:**

| Root | DFS Path | Subgraph | Good | Bad | Score | Max |
|------|----------|----------|------|-----|-------|-----|
| 0 | 0→1→2 | {0,1,2} | 2 | 1 | 1 | 1 |
| 1 | 1→0, 1→2 | {0,1,2} | 2 | 1 | 1 | 1 |
| 2 | 2→1→0 | {0,1,2} | 2 | 1 | 1 | 1 |

**2.4 Increment and Loop:**
After processing all roots, we have maximum scores for each node.

**2.5 Return Result:**
The result array is `[1, 1, 1]`, representing the maximum score for each node.
