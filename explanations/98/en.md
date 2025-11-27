## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to determine if it is a valid binary search tree (BST). A BST is valid if for every node, all nodes in its left subtree are less than it, and all nodes in its right subtree are greater than it.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Edge Case:** An empty tree is a valid BST. A tree with only one node is a valid BST.

**1.2 High-level approach:**

The goal is to validate that a binary tree satisfies the BST property.

We use recursion with range validation. For each node, we check if its value is within the valid range (min_val, max_val). The range is updated as we traverse: left children must be less than the parent, right children must be greater than the parent.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each node, check if all nodes in its left subtree are less and all nodes in its right subtree are greater. This would be $O(n^2)$ time.
- **Optimized Strategy (Range Validation):** Use recursion with min and max bounds. Each node must be within its allowed range. This takes $O(n)$ time.
- **Why it's better:** The range validation approach reduces time complexity from $O(n^2)$ to $O(n)$ by passing down constraints instead of checking all descendants for each node.

**1.4 Decomposition:**

1. Define a recursive function that takes a node and its allowed range (min_val, max_val).
2. If the node is null, return true (base case).
3. Check if the node's value is within the range (strictly greater than min_val and strictly less than max_val).
4. Recursively validate left subtree with range (min_val, node.val).
5. Recursively validate right subtree with range (node.val, max_val).
6. Return true only if all checks pass.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[5,1,4,null,null,3,6]$

The tree structure:
```
    5
   / \
  1   4
     / \
    3   6
```

We initialize:
- Call `validate(root, -∞, +∞)`

**2.2 Start Validation:**

We begin validating from the root.

**2.3 Trace Walkthrough:**

| Node | min_val | max_val | node.val | Check | Result |
|------|---------|---------|----------|-------|--------|
| 5 | -∞ | +∞ | 5 | $-∞ < 5 < +∞$ | ✓ |
| 1 | -∞ | 5 | 1 | $-∞ < 1 < 5$ | ✓ |
| 4 | 5 | +∞ | 4 | $5 < 4 < +∞$ | ✗ |

**2.4 Explanation:**

- Root (5): Valid, within range (-∞, +∞)
- Left child (1): Valid, within range (-∞, 5)
- Right child (4): Invalid! It should be greater than 5, but 4 < 5

**2.5 Return Result:**

We return `False` because node 4 violates the BST property (it's in the right subtree of 5 but is less than 5).

> **Note:** The key insight is to pass down the allowed range for each node. A node's value must be strictly within its range, and we update the range for children: left children get (min_val, node.val) and right children get (node.val, max_val).

