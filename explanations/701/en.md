## Explanation

### Strategy (The "Why")

Given the root node of a binary search tree (BST) and a value to insert, we need to insert the value into the BST and return the root node of the BST after insertion.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the BST can be up to $10^4$.
- **Value Range:** Values are between $-10^8$ and $10^8$.
- **Time Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Space Complexity:** $O(h)$ - The recursion stack can be as deep as the height of the tree. In the worst case, this is $O(n)$, and in the average case, this is $O(\log n)$.
- **Edge Case:** If the tree is empty (root is null), we create a new node with the given value and return it.

**1.2 High-level approach:**

The goal is to insert a new value into a BST while maintaining the BST property: all values in the left subtree are less than the root, and all values in the right subtree are greater than the root.

![BST Insertion](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

We use the BST property to navigate to the correct insertion point: if the value is less than the current node, go left; if greater, go right. When we reach a null position, that's where we insert the new node.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach for BST insertion. We must use the BST property to find the correct position.
- **Optimized Strategy (Recursive):** Recursively traverse the tree using the BST property. When we find a null position, create and return a new node. This naturally maintains the BST structure.
- **Why it's better:** The recursive approach is clean and intuitive. It leverages the BST property efficiently, ensuring we only traverse one path from root to leaf.

**1.4 Decomposition:**

1. Check if the current node is null. If so, create a new node with the value and return it.
2. Compare the value to insert with the current node's value.
3. If the value is less than the current node's value, recursively insert into the left subtree.
4. If the value is greater than or equal to the current node's value, recursively insert into the right subtree.
5. Return the current node (which may have been modified with a new child).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[4,2,7,1,3]$, $val = 5$

The BST structure:
```
      4
     / \
    2   7
   / \
  1   3
```

We need to insert value 5.

**2.2 Start Traversing:**

We begin at the root node (value 4).

**2.3 Trace Walkthrough:**

| Step | Current Node | Value to Insert | Comparison | Action |
|------|--------------|-----------------|------------|--------|
| 1 | 4 | 5 | $5 > 4$ | Go to right child (7) |
| 2 | 7 | 5 | $5 < 7$ | Go to left child (null) |
| 3 | null | 5 | - | Create new node with value 5 |

After insertion:
```
      4
     / \
    2   7
   / \ /
  1  3 5
```

**2.4 Return Result:**

The new node is created and linked as the left child of node 7. The root node (4) is returned.

> **Note:** The BST property ensures that we always know which direction to go. We never need to backtrack or check multiple paths.

