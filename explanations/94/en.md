## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to return the inorder traversal of its nodes' values.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $100$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Edge Case:** If the tree is empty, return an empty list. If the tree has only one node, return that node's value.

**1.2 High-level approach:**

The goal is to traverse the tree in inorder (left, root, right) order.

We use recursion to implement inorder traversal. We recursively traverse the left subtree, visit the root, then recursively traverse the right subtree.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree.
- **Optimized Strategy (Recursion):** Use recursion to naturally implement inorder traversal. This is the standard and efficient approach.
- **Why it's better:** Recursion naturally follows the tree structure and implements inorder traversal efficiently. An iterative approach using a stack is also possible but more complex.

**1.4 Decomposition:**

1. Define a recursive function that takes a node.
2. Base case: if node is null, return.
3. Recursively traverse left subtree.
4. Visit current node (add value to result).
5. Recursively traverse right subtree.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,null,2,3]$

The tree structure:
```
    1
     \
      2
     /
    3
```

We initialize:
- `res = []`

**2.2 Start Traversal:**

We begin from the root.

**2.3 Trace Walkthrough:**

| Node | Action | res After |
|------|--------|-----------|
| 1 | Go left (null) | [] |
| 1 | Visit 1 | [1] |
| 1 | Go right (2) | [1] |
| 2 | Go left (3) | [1] |
| 3 | Go left (null) | [1] |
| 3 | Visit 3 | [1,3] |
| 3 | Go right (null) | [1,3] |
| 2 | Visit 2 | [1,3,2] |
| 2 | Go right (null) | [1,3,2] |

**2.4 Final Result:**

After traversal: `res = [1,3,2]`

**2.5 Return Result:**

We return `[1,3,2]`, which is the inorder traversal.

> **Note:** The key is to follow the inorder order: left subtree first, then root, then right subtree. Recursion naturally implements this by processing the left subtree before the root, and the root before the right subtree.

