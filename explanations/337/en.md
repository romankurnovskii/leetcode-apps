## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The tree has at most 10^4 nodes, and each node value is between 0 and 10^4.
- **Time Complexity:** O(n) - We visit each node exactly once, where n is the number of nodes.
- **Space Complexity:** O(h) - The recursion stack depth is at most the height h of the tree. In the worst case (skewed tree), h = n, giving O(n) space.
- **Edge Case:** If the tree is empty (root is None), return 0.

**1.2 High-level approach:**
The goal is to find the maximum amount of money we can rob from a binary tree without robbing two directly connected nodes. We use dynamic programming with a post-order traversal, where for each node we calculate two values: the maximum if we rob this node, and the maximum if we don't rob this node.

![House Robber III tree](https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible combinations of robbing/not robbing each node, checking constraints. This would be exponential time O(2^n).
- **Optimized Strategy (DP with DFS):** For each node, calculate the maximum profit for two cases: robbing this node (can't rob children) and not robbing this node (can rob children). This takes O(n) time.
- **Emphasize the optimization:** By storing both possibilities at each node, we avoid recalculating subproblems and reduce time complexity from exponential to linear.

**1.4 Decomposition:**
1. Perform a post-order traversal of the tree.
2. For each node, return a tuple: (rob_this, dont_rob_this).
3. If we rob this node, we can't rob its children, so we take children's "don't rob" values.
4. If we don't rob this node, we can choose the maximum from each child's two options.
5. Return the maximum of the root's two options.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `root = [3,2,3,null,3,null,1]`

Initialize:
- Start DFS from root node with value 3.

**2.2 Start Processing:**
We traverse the tree using post-order DFS (process children before parent).

**2.3 Trace Walkthrough:**

| Node | Left Child Result | Right Child Result | Rob This | Don't Rob This | Max |
|------|-------------------|-------------------|----------|----------------|-----|
| 1 (leaf) | (0,0) | (0,0) | 1 + 0 + 0 = 1 | 0 + 0 = 0 | 1 |
| 3 (leaf) | (0,0) | (0,0) | 3 + 0 + 0 = 3 | 0 + 0 = 0 | 3 |
| 2 | (0,0) | (3,0) | 2 + 0 + 0 = 2 | 0 + 3 = 3 | 3 |
| 3 (root) | (2,3) | (1,0) | 3 + 3 + 0 = 6 | 3 + 1 = 4 | 7 |

**2.4 Return Result:**
The final result is max(rob_root, dont_rob_root) = max(6, 4) = 7.

