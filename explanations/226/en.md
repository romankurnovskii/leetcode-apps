## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The tree has 0 to 100 nodes, and node values range from -100 to 100.
- **Time Complexity:** O(n) where n is the number of nodes. We visit each node once.
- **Space Complexity:** O(h) where h is the height of the tree for the recursion stack. In worst case (skewed tree), this is O(n).
- **Edge Case:** If the root is None, return None.

**1.2 High-level approach:**
The goal is to invert a binary tree by swapping left and right children at every node. We use recursion to process each node.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same recursive approach - there's no significantly different brute force method for this problem.
- **Optimized Strategy:** Use recursion to swap children at each node, then recursively invert the subtrees.
- **Why optimized is better:** This is the natural and most efficient approach for tree problems.

**1.4 Decomposition:**
1. If the node is None, return None (base case).
2. Swap the left and right children of the current node.
3. Recursively invert the left subtree.
4. Recursively invert the right subtree.
5. Return the root.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Example tree: `[4,2,7,1,3,6,9]`

```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

**2.2 Start Checking:**
Start from the root and recursively process each node.

**2.3 Trace Walkthrough:**

| Node | Before Swap | After Swap | Left Child | Right Child |
|------|------------|------------|------------|--------------|
| 4 | left=2, right=7 | left=7, right=2 | Invert 7 | Invert 2 |
| 7 | left=6, right=9 | left=9, right=6 | Invert 9 | Invert 6 |
| 2 | left=1, right=3 | left=3, right=1 | Invert 3 | Invert 1 |

**2.4 Increment and Loop:**
For each node:
- Swap: `root.left, root.right = root.right, root.left`
- Recursively invert: `self.invertTree(root.left)`, `self.invertTree(root.right)`

**2.5 Return Result:**
After inversion:
```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

Return the root node.

