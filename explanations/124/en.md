## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $1 \leq n \leq 3 \times 10^4$ nodes, with values in $[-1000, 1000]$.
* **Time Complexity:** $O(n)$ - We visit each node exactly once during DFS traversal.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
* **Edge Case:** A single-node tree returns the node's value. All negative values require careful handling (we use `max(0, ...)` to avoid negative contributions).

**1.2 High-level approach**

The goal is to find the maximum path sum in a binary tree, where a path can start and end at any nodes (not necessarily root or leaf). We use DFS to calculate the maximum path sum that can be extended upward from each node, while tracking the global maximum.

![Maximum path sum visualization showing paths that can go through any node]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible paths in the tree. This is exponential in complexity.
* **Optimized (DFS with Global Tracking):** For each node, calculate the maximum path sum that can be extended upward (for parent) and the maximum path sum through the node (for global maximum). This achieves $O(n)$ time.

**1.4 Decomposition**

1. **DFS Traversal:** Recursively visit each node.
2. **Calculate Contributions:** For each node, get maximum contributions from left and right subtrees (non-negative only).
3. **Update Global Maximum:** Calculate path sum through current node and update global maximum.
4. **Return Upward Contribution:** Return the maximum path sum that can be extended to parent.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [-10,9,20,null,null,15,7]$.

We initialize:
* `res = -inf` (global maximum path sum)
* Start DFS from root node (-10)

**2.2 Start Processing**

We call `dfs(root)`.

**2.3 Trace Walkthrough**

| Node | left_sum | right_sum | Path Through Node | Return Value | res (after) |
|------|----------|-----------|-------------------|--------------|-------------|
| -10 | max(0, dfs(9)) | max(0, dfs(20)) | -10 + 0 + 0 = -10 | -10 + max(0,0) = -10 | -10 |
| 9 | 0 | 0 | 9 + 0 + 0 = 9 | 9 + 0 = 9 | 9 |
| 20 | max(0, dfs(15)) | max(0, dfs(7)) | 20 + 15 + 7 = 42 | 20 + max(15,7) = 35 | 42 |
| 15 | 0 | 0 | 15 + 0 + 0 = 15 | 15 + 0 = 15 | 42 |
| 7 | 0 | 0 | 7 + 0 + 0 = 7 | 7 + 0 = 7 | 42 |

**2.4 Recursive Processing**

For each node:
1. If `not node`, return 0 (base case)
2. Recursively get `left_sum = max(0, dfs(node.left))` (non-negative only)
3. Recursively get `right_sum = max(0, dfs(node.right))` (non-negative only)
4. Update global: `res = max(res, node.val + left_sum + right_sum)`
5. Return: `node.val + max(left_sum, right_sum)` (for parent)

**2.5 Return Result**

After processing all nodes, `res = 42`, which is the maximum path sum from the path $15 \to 20 \to 7$.

> **Note:** We use `max(0, ...)` to ensure we only consider positive contributions from subtrees. If a subtree contributes negatively, we ignore it (treat as 0).

