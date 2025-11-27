## Explanation

### Strategy (The "Why")

Given the root of a binary search tree and a key, we need to delete the node with the given key and return the root of the BST.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-10^5$ and $10^5$.
- **Time Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Space Complexity:** $O(h)$ - The recursion stack can be as deep as the height of the tree.
- **Edge Case:** If the key doesn't exist, return the original tree. If the node to delete has no children, simply remove it.

**1.2 High-level approach:**

The goal is to delete a node from a BST while maintaining the BST property.

We use recursion to find the node. If found, we handle three cases: no children, one child, or two children. For two children, we replace the node's value with the minimum value from its right subtree, then delete that minimum node.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must maintain the BST structure.
- **Optimized Strategy (Recursion):** Use recursion to find and delete the node, handling each case appropriately. This is the standard and efficient approach.
- **Why it's better:** The recursive approach naturally handles the tree structure and maintains BST properties efficiently.

**1.4 Decomposition:**

1. If root is null, return null.
2. If key is less than root.val, recursively delete from left subtree.
3. If key is greater than root.val, recursively delete from right subtree.
4. If key equals root.val:
   - If no left child, return right child.
   - If no right child, return left child.
   - If two children, find minimum in right subtree, replace root's value, and delete the minimum node.
5. Return the root.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[5,3,6,2,4,null,7]$, key = 3

The tree structure:
```
    5
   / \
  3   6
 / \   \
2   4   7
```

**2.2 Start Searching:**

We search for the node with key = 3.

**2.3 Trace Walkthrough:**

| Step | Current Node | Key Comparison | Action |
|------|--------------|----------------|--------|
| 1 | 5 | 3 < 5 | Go left |
| 2 | 3 | 3 == 3 | Found! Delete node 3 |

**Deleting node 3:**
- Node 3 has two children (2 and 4)
- Find minimum in right subtree: min(4) = 4
- Replace node 3's value with 4
- Delete node 4 from right subtree (node 4 has no children, so simply remove it)

**2.4 Final Tree:**

After deletion:
```
    5
   / \
  4   6
 /     \
2       7
```

**2.5 Return Result:**

We return the root of the modified tree.

> **Note:** The key insight is that when deleting a node with two children, we can replace it with the minimum node from its right subtree (or maximum from left subtree). This maintains the BST property because the minimum in the right subtree is greater than all left children and less than all other right children.

