## Explanation

### Strategy (The "Why")

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. The LCA is the lowest node that has both nodes as descendants.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the BST can be between $2$ and $10^5$.
- **Value Range:** All node values are unique and between $-10^9$ and $10^9$.
- **Time Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Space Complexity:** $O(h)$ - The recursion stack can be as deep as the height of the tree. In the worst case, this is $O(n)$, and in the average case, this is $O(\log n)$.
- **Edge Case:** Both nodes are guaranteed to exist in the BST. The LCA could be one of the nodes itself (if one is an ancestor of the other).

**1.2 High-level approach:**

The goal is to find the lowest common ancestor of two nodes in a BST.

![BST LCA](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

We leverage the BST property: if both nodes are less than the current root, the LCA is in the left subtree. If both are greater, the LCA is in the right subtree. Otherwise, the current root is the LCA.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find paths from root to both nodes, then find the last common node in both paths. This requires storing paths and comparing them.
- **Optimized Strategy (BST Property):** Use the BST property to navigate directly. If both nodes are on the same side of the root, recurse on that side. Otherwise, the root is the LCA.
- **Why it's better:** The BST property allows us to eliminate half of the tree at each step, making this much more efficient than a general binary tree LCA algorithm.

**1.4 Decomposition:**

1. Compare the values of both nodes with the current root.
2. If both nodes are less than the root, the LCA is in the left subtree - recurse left.
3. If both nodes are greater than the root, the LCA is in the right subtree - recurse right.
4. Otherwise (one is less and one is greater, or one equals the root), the current root is the LCA.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[6,2,8,0,4,7,9,null,null,3,5]$, $p = 2$, $q = 8$

The BST structure:
```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```

**2.2 Start Checking:**

We begin at the root node (value 6).

**2.3 Trace Walkthrough:**

| Step | Current Root | p | q | Comparison | Action |
|------|--------------|---|---|------------|--------|
| 1 | 6 | 2 | 8 | $2 < 6$ and $8 > 6$ | Root (6) is LCA |

Since $p = 2 < 6$ and $q = 8 > 6$, they are on opposite sides of the root. Therefore, the root (6) is the LCA.

**2.4 Another Example:**

If $p = 2$ and $q = 4$:
- Step 1: Root = 6, both $2 < 6$ and $4 < 6$, so recurse left
- Step 2: Root = 2, $2 == 2$ and $4 > 2$, so root (2) is LCA

**2.5 Return Result:**

We return the root node (6), which is the LCA.

> **Note:** The BST property makes this problem much simpler than finding LCA in a general binary tree. We don't need to search both subtrees - we can always determine which direction to go.

