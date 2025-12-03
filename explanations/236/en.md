## Explanation

### Strategy (The "Why")

The problem asks us to find the lowest common ancestor (LCA) of two nodes in a binary tree. The LCA is the deepest node that has both nodes as descendants (a node can be a descendant of itself).

**1.1 Constraints & Complexity:**

- **Input Constraints:** The tree has $2 \leq n \leq 10^5$ nodes with unique values in $[-10^9, 10^9]$.
- **Time Complexity:** $O(n)$ - We may need to visit all nodes in the worst case.
- **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
- **Edge Case:** If one node is an ancestor of the other, return that ancestor node.

**1.2 High-level approach:**

The goal is to find the deepest node that is an ancestor of both target nodes. We use recursive DFS: if we find both nodes in a subtree, the current root is the LCA.

![Binary Tree LCA](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find paths to both nodes, then find the last common node in both paths. This requires storing paths and takes $O(n)$ time and $O(n)$ space.
- **Optimized (Recursive DFS):** Recursively search both subtrees. If both subtrees return non-null, the current root is the LCA. This takes $O(n)$ time and $O(h)$ space.
- **Emphasize the optimization:** The recursive approach finds the LCA in a single pass without storing paths, making it more space-efficient.

**1.4 Decomposition:**

1. **Base Case:** If root is `None` or equals `p` or `q`, return root.
2. **Recursive Search:** Recursively search left and right subtrees for `p` and `q`.
3. **Combine Results:** If both subtrees return non-null, root is the LCA. Otherwise, return whichever subtree found a node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 1`.

**2.2 Start Searching:**

Begin at root node `3`.

**2.3 Trace Walkthrough:**

| Node | Left Result | Right Result | Action |
|------|-------------|--------------|---------|
| 3 | Search left (5) | Search right (1) | Both found → Return 3 |
| 5 | Search left (6) | Search right (2) | Found p → Return 5 |
| 1 | Search left (0) | Search right (8) | Found q → Return 1 |

**2.4 Recursive Unwinding:**

- Node `5` returns itself (found `p`).
- Node `1` returns itself (found `q`).
- Node `3` receives both results, so it's the LCA.

**2.5 Return Result:**

The function returns node `3`, which is the LCA of nodes `5` and `1`.

> **Note:** The key insight is that if both left and right subtrees return non-null, the current root must be the LCA. If only one subtree returns non-null, that subtree contains the LCA.

