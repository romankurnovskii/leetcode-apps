## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to flip a binary tree upside down, where the original leftmost node becomes the new root, and the original root becomes the rightmost leaf. The transformation follows a specific pattern where left children become parents and right children become left children.

**1.1 Constraints & Complexity:**
- Input size: The tree can have up to O(n) nodes where n is the number of nodes
- **Time Complexity:** O(n) where n is the number of nodes - we visit each node exactly once
- **Space Complexity:** O(h) where h is the height of the tree - the recursion stack depth equals the tree height
- **Edge Case:** If the tree is empty or has no left child, return the root as-is

**1.2 High-level approach:**
We use recursion to traverse to the leftmost node, which becomes the new root. During the backtracking phase, we reassign pointers to transform the tree structure according to the upside-down pattern.

![Binary tree upside down transformation](https://assets.leetcode.com/static_assets/others/binary-tree-upside-down.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Create a new tree by copying nodes and reassigning pointers iteratively. This requires O(n) extra space.
- **Optimized Strategy:** Use recursion to transform the tree in-place by reassigning pointers during backtracking. This uses O(h) space for recursion.
- **Why it's better:** We modify the tree in-place without creating new nodes, making it more memory efficient.

**1.4 Decomposition:**
1. Recursively traverse to the leftmost node, which will become the new root
2. During backtracking, reassign the current node's left child's left pointer to the current node's right child
3. Reassign the current node's left child's right pointer to the current node itself
4. Set the current node's left and right pointers to None to break old connections
5. Return the new root (leftmost node) from the deepest recursion

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example tree with nodes [1,2,3,4,5]:
- Root: 1, left: 2, right: 3
- Node 2: left: 4, right: 5
- After transformation, node 4 becomes the new root

**2.2 Start Processing:**
We begin recursive traversal starting from the root, always going left first.

**2.3 Trace Walkthrough:**

| Node | Has Left? | Action | New Root | Transformations |
|------|-----------|--------|----------|------------------|
| 1 | Yes | Go left to 2 | - | - |
| 2 | Yes | Go left to 4 | - | - |
| 4 | No | Return 4 | 4 | - |
| 2 | - | Backtrack | 4 | 4.left = 5, 4.right = 2, 2.left = None, 2.right = None |
| 1 | - | Backtrack | 4 | 2.left = 3, 2.right = 1, 1.left = None, 1.right = None |

**2.4 Increment and Loop:**
The recursion naturally handles the traversal. We continue until we reach a node with no left child.

**2.5 Return Result:**
Return the new root (node 4), which is the leftmost node from the original tree. The tree is now upside down with all pointers correctly reassigned.

