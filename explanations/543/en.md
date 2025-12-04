## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Tree has between 1 and 10^4 nodes, and node values are between -100 and 100.
- **Time Complexity:** O(n) - We visit each node exactly once during DFS, where n is the number of nodes.
- **Space Complexity:** O(h) - The recursion stack depth is at most the height h of the tree. In the worst case (skewed tree), h = n, giving O(n) space.
- **Edge Case:** If the tree has only one node, the diameter is 0 (no edges).

**1.2 High-level approach:**
The goal is to find the diameter (longest path between any two nodes) of a binary tree. The diameter may or may not pass through the root. We use DFS to calculate the depth of each subtree and track the maximum diameter found so far.

![Diameter of Binary Tree](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each node, find the longest path passing through it by calculating depths of left and right subtrees. This still requires visiting each node once, so it's O(n) but with redundant calculations.
- **Optimized Strategy (DFS with Global Tracking):** Perform a single DFS pass, calculating subtree depths and updating the maximum diameter as we go. This takes O(n) time with a single traversal.
- **Emphasize the optimization:** By tracking the maximum diameter during a single DFS pass, we avoid multiple traversals and redundant calculations.

**1.4 Decomposition:**
1. Perform DFS traversal of the tree.
2. For each node, calculate the depth of its left and right subtrees.
3. The diameter passing through this node is left_depth + right_depth.
4. Update the global maximum diameter if this is larger.
5. Return the depth of the current subtree (1 + max(left_depth, right_depth)).

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `root = [1,2,3,4,5]`

Initialize:
- `res = 0` (global maximum diameter)

**2.2 Start Processing:**
We perform DFS starting from the root.

**2.3 Trace Walkthrough:**

| Node | Left Depth | Right Depth | Diameter Through Node | Max Diameter | Return Depth |
|------|------------|-------------|----------------------|--------------|--------------|
| 4 (leaf) | 0 | 0 | 0 | 0 | 1 |
| 5 (leaf) | 0 | 0 | 0 | 0 | 1 |
| 2 | 1 | 1 | 2 | 2 | 2 |
| 3 (leaf) | 0 | 0 | 0 | 2 | 1 |
| 1 (root) | 2 | 1 | 3 | 3 | 3 |

**2.4 Return Result:**
The maximum diameter found is 3, which is the path [4,2,1,3] or [5,2,1,3].

