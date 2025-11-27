## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to check whether it is a mirror of itself (symmetric around its center).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $1000$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$.
- **Edge Case:** An empty tree is symmetric. A tree with only one node is symmetric.

**1.2 High-level approach:**

The goal is to determine if a binary tree is symmetric (mirror of itself).

We use recursion to check if the left and right subtrees are mirrors of each other. Two trees are mirrors if their roots have the same value, and the left subtree of one is a mirror of the right subtree of the other, and vice versa.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must check the mirror property.
- **Optimized Strategy (Recursion):** Use recursion to check if left and right subtrees are mirrors. This is the standard and efficient approach.
- **Why it's better:** Recursion naturally checks the mirror property by comparing corresponding nodes in the left and right subtrees.

**1.4 Decomposition:**

1. Define a helper function that checks if two trees are mirrors.
2. Two trees are mirrors if:
   - Both are null (base case: true).
   - One is null and the other is not (false).
   - Both roots have the same value, and:
     - Left subtree of first is mirror of right subtree of second.
     - Right subtree of first is mirror of left subtree of second.
3. Check if root's left and right subtrees are mirrors.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,2,2,3,4,4,3]$

The tree structure:
```
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

We initialize:
- Call `is_mirror(root.left, root.right)`

**2.2 Start Checking:**

We begin checking if left and right subtrees are mirrors.

**2.3 Trace Walkthrough:**

| left | right | left.val | right.val | Check | Result |
|------|-------|----------|-----------|-------|--------|
| 2 | 2 | 2 | 2 | Equal ✓ | Check children |
| 3 | 3 | 3 | 3 | Equal ✓ | Both null ✓ |
| 4 | 4 | 4 | 4 | Equal ✓ | Both null ✓ |
| 4 | 4 | 4 | 4 | Equal ✓ | Both null ✓ |
| 3 | 3 | 3 | 3 | Equal ✓ | Both null ✓ |

**2.4 Explanation:**

- Root's left (2) and right (2) have same value ✓
- Left's left (3) and right's right (3) are mirrors ✓
- Left's right (4) and right's left (4) are mirrors ✓

**2.5 Return Result:**

We return `True` because the tree is symmetric.

> **Note:** The key insight is that a tree is symmetric if its left and right subtrees are mirrors. Two trees are mirrors if their roots match and the left of one mirrors the right of the other (and vice versa).

