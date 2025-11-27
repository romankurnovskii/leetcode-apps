## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to return the inorder traversal of its nodes' values.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $100$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$.
- **Edge Case:** If the tree is empty, return an empty list.

**1.2 High-level approach:**

The goal is to traverse the tree in inorder: left subtree, root, right subtree.

We use recursion to traverse the tree. For each node, we recursively traverse the left subtree, visit the node, then recursively traverse the right subtree.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree.
- **Optimized Strategy (Recursion):** Use recursion to naturally follow the inorder traversal order. This is the standard and efficient approach.
- **Why it's better:** Recursion naturally follows the tree structure and implements inorder traversal elegantly.

**1.4 Decomposition:**

1. Define a recursive function that takes a node.
2. If the node is null, return (base case).
3. Recursively traverse the left subtree.
4. Visit the current node (add its value to results).
5. Recursively traverse the right subtree.

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

| Step | Node | Action | res After |
|------|------|--------|-----------|
| 1 | 1 | Go left (null) | [] |
| 2 | 1 | Visit 1 | [1] |
| 3 | 2 | Go left (3) | [1] |
| 4 | 3 | Go left (null) | [1] |
| 5 | 3 | Visit 3 | [1, 3] |
| 6 | 3 | Go right (null) | [1, 3] |
| 7 | 2 | Visit 2 | [1, 3, 2] |
| 8 | 2 | Go right (null) | [1, 3, 2] |

**2.4 Final Result:**

After traversal: `res = [1, 3, 2]`

**2.5 Return Result:**

We return `[1, 3, 2]`, which is the inorder traversal.

> **Note:** The key is to follow the inorder order: left subtree first, then root, then right subtree. Recursion naturally implements this order.

