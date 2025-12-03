## Explanation

### Strategy (The "Why")

The problem asks us to construct a binary tree from its inorder and postorder traversal arrays.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 3000$, values in $[-3000, 3000]$, all values are unique.
- **Time Complexity:** $O(n)$ - We visit each node once. The hash map lookup is $O(1)$.
- **Space Complexity:** $O(n)$ - Hash map for inorder indices takes $O(n)$, recursion stack takes $O(h)$.
- **Edge Case:** Empty arrays return `None`.

**1.2 High-level approach:**

The goal is to reconstruct the tree using the property that in postorder, the root comes last, and in inorder, the root separates left and right subtrees.

![Tree Construction](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each root, search for it in inorder array linearly. This takes $O(n^2)$ time.
- **Optimized (Hash Map):** Use a hash map to store inorder indices for $O(1)$ lookup. This takes $O(n)$ time.
- **Emphasize the optimization:** The hash map reduces the time complexity from $O(n^2)$ to $O(n)$ by eliminating linear searches.

**1.4 Decomposition:**

1. **Build Hash Map:** Create a map from values to their inorder indices.
2. **Recursive Build:** Use postorder to get root (last element), use inorder to split left/right subtrees.
3. **Calculate Ranges:** Determine inorder and postorder ranges for left and right subtrees.
4. **Return Root:** Build and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `inorder = [9,3,15,20,7]`, `postorder = [9,15,7,20,3]`.

Hash map: `{9:0, 3:1, 15:2, 20:3, 7:4}`

**2.2 Start Building:**

Root is `postorder[4] = 3`. Find its position in inorder: `inorder[1] = 3`.

**2.3 Trace Walkthrough:**

| Root | Inorder Range | Postorder Range | Left Size | Left Subtree | Right Subtree |
|------|---------------|-----------------|-----------|--------------|---------------|
| 3 | [0:4] | [0:4] | 1 | in[0:0], post[0:0] | in[2:4], post[1:3] |
| 9 | [0:0] | [0:0] | 0 | None | None |
| 20 | [2:4] | [1:3] | 1 | in[2:2], post[1:1] | in[3:4], post[2:2] |
| 15 | [2:2] | [1:1] | 0 | None | None |
| 7 | [3:4] | [2:2] | 0 | None | None |

**2.4 Complete Construction:**

Tree structure: `3` (root) with left child `9` and right child `20`. `20` has left child `15` and right child `7`.

**2.5 Return Result:**

The function returns the root node of the constructed tree.

> **Note:** Similar to problem 105, but here the root is the last element in postorder instead of the first in preorder.

