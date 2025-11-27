## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to find the longest ZigZag path. A ZigZag path is defined as alternating between going left and right. The path length is the number of nodes visited minus 1 (number of edges).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $5 \times 10^4$.
- **Value Range:** Node values are between $1$ and $10^5$.
- **Time Complexity:** $O(n)$ - We visit each node at most a constant number of times.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$.
- **Edge Case:** If the tree has only one node, return 0 (no edges). If the tree has no left or right children, return 0.

**1.2 High-level approach:**

The goal is to find the longest path that alternates between left and right directions.

We use DFS to explore all possible ZigZag paths. For each node, we track the direction we came from (left or right) and the current path length. We can either continue the current path or start a new path.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths and find the longest ZigZag one. This would be exponential.
- **Optimized Strategy (DFS):** Use DFS to explore paths, tracking direction and length. This takes $O(n)$ time.
- **Why it's better:** The DFS approach efficiently explores all paths in a single traversal, avoiding the need to generate all possible paths explicitly.

**1.4 Decomposition:**

1. Start DFS from root's left and right children (if they exist).
2. For each node, track the direction we came from (is_left) and current path length.
3. If coming from left, go right (extend path) or go left (start new path).
4. If coming from right, go left (extend path) or go right (start new path).
5. Update the maximum path length seen.
6. Return the maximum path length.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]$

We initialize:
- `res = 0`

**2.2 Start DFS:**

We begin DFS from root's children.

**2.3 Trace Walkthrough:**

Starting from root:
- Go left: DFS(root.left, is_left=True, length=1)
- Go right: DFS(root.right, is_left=False, length=1)

For each path:
- If coming from left and node has right child: extend path (length+1)
- If coming from left and node has left child: start new path (length=1)
- Similar logic for coming from right

**2.4 Explanation:**

The algorithm explores all possible ZigZag paths:
- Path 1: root → right → left → right → ... (extending)
- Path 2: root → right → right → left → ... (restarting)

We track the maximum length found.

**2.5 Return Result:**

We return the maximum ZigZag path length found.

> **Note:** The key insight is that at each node, we can either continue the current ZigZag path (if going in the opposite direction) or start a new path (if going in the same direction). We need to explore both possibilities to find the maximum.

