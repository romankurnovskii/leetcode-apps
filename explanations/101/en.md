## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to check whether it is a mirror of itself (i.e., symmetric around its center).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $1000$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$.
- **Edge Case:** An empty tree is symmetric. A tree with only one node is symmetric.

**1.2 High-level approach:**

The goal is to determine if a binary tree is symmetric (mirror of itself).

We use recursion to check if the left and right subtrees are mirrors of each other. Two trees are mirrors if their roots have the same value, and the left subtree of one is a mirror of the right subtree of the other.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must check the mirror property.
- **Optimized Strategy (Recursion):** Use recursion to check if left and right subtrees are mirrors. This is the natural and efficient approach.
- **Why it's better:** Recursion naturally checks the mirror property by comparing corresponding nodes in the left and right subtrees.

**1.4 Decomposition:**

1. Define a helper function that checks if two trees are mirrors.
2. Two trees are mirrors if:
   - Both are null (symmetric).
   - One is null (not symmetric).
   - Both roots have the same value, and left subtree of one is mirror of right subtree of the other.
3. For the main tree, check if left and right subtrees are mirrors.

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

We begin comparing the left and right subtrees.

**2.3 Trace Walkthrough:**

| Step | left | right | left.val == right.val? | Check Subtrees | Result |
|------|------|-------|------------------------|----------------|--------|
| 1 | 2 | 2 | Yes | is_mirror(3,3) and is_mirror(4,4) | Check... |
| 2 | 3 | 3 | Yes | is_mirror(null,null) and is_mirror(null,null) | True |
| 3 | 4 | 4 | Yes | is_mirror(null,null) and is_mirror(null,null) | True |
| 4 | 2 | 2 | Yes | Both subtrees are mirrors | True |

**2.4 Explanation:**

- Root (1): left=2, right=2, values match ✓
- Left subtree of left (3) vs right subtree of right (3): match ✓
- Right subtree of left (4) vs left subtree of right (4): match ✓
- All corresponding nodes match, so the tree is symmetric.

**2.5 Return Result:**

We return `True` because the tree is symmetric.

> **Note:** The key insight is that a tree is symmetric if its left and right subtrees are mirrors. Two trees are mirrors if their roots match and the left of one mirrors the right of the other (and vice versa).

