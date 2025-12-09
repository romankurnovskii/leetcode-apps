## Explanation

### Strategy (The "Why")

**Restate the problem:** For each node i, we need to find the maximum score among all connected subgraphs that contain node i. The score is the number of good nodes minus the number of bad nodes.

**1.1 Constraints & Complexity:**
- Input size: `2 <= n <= 10^5`
- **Time Complexity:** O(n) using rerooting DP - first DFS computes subtree scores, second DFS reroots in O(n)
- **Space Complexity:** O(n) for the tree and DP arrays
- **Edge Case:** If all nodes are bad, the best score for each node might be -1

**1.2 High-level approach:**
We use tree dynamic programming with efficient rerooting. First, we compute subtree scores from an arbitrary root. Then, we use rerooting to compute answers for all nodes in O(n) time by efficiently transferring parent contributions to children.

![Tree DP visualization](https://assets.leetcode.com/static_assets/others/tree-dp-rerooting.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each node as root, perform DFS separately, which is O(n²)
- **Optimized Strategy:** Use rerooting DP - compute subtree scores once, then efficiently reroot to all nodes in O(n) time
- **Emphasize the optimization:** Rerooting allows us to compute all root answers in O(n) instead of O(n²) by reusing subtree information

**1.4 Decomposition:**
1. Build the tree from edges
2. First DFS: Compute subtree scores from root 0 (down[node] = max score of subtree rooted at node)
3. Second DFS: Reroot efficiently - when moving from parent to child, calculate parent's contribution without child and add it to child's score
4. Use rerooting formula: ans[child] = down[child] + max(0, ans[parent] - max(0, down[child]))
5. Return the array of maximum scores for each node

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 3`, `edges = [[0,1],[1,2]]`, `good = [1,0,1]`
- Tree: 0-1-2
- Node scores: 0→+1, 1→-1, 2→+1

**2.2 First DFS (Compute Subtree Scores):**
We perform DFS from root 0 to compute down[node] = max score of subtree rooted at node.

**2.3 Trace Walkthrough (First DFS):**

| Node | Parent | Children | Node Score | Child Scores | down[node] |
|------|--------|----------|------------|--------------|------------|
| 2 | 1 | None | +1 | - | 1 |
| 1 | 0 | 2 | -1 | down[2]=1 (>0) | -1 + 1 = 0 |
| 0 | -1 | 1 | +1 | down[1]=0 (≤0) | 1 |

**2.4 Second DFS (Rerooting):**
We reroot from parent to child efficiently. For node 0 (root), ans[0] = down[0] = 1.

**2.5 Trace Walkthrough (Rerooting to Node 1):**
- parent_contrib = ans[0] - max(0, down[1]) = 1 - 0 = 1
- ans[1] = down[1] + max(0, 1) = 0 + 1 = 1

**2.6 Trace Walkthrough (Rerooting to Node 2):**
- parent_contrib = ans[1] - max(0, down[2]) = 1 - 1 = 0
- ans[2] = down[2] + max(0, 0) = 1 + 0 = 1

**2.7 Return Result:**
The result array is `[1, 1, 1]`, representing the maximum score for each node when it is the root.
