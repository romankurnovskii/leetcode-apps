# Problem 105: Construct Binary Tree from Preorder and Inorder Traversal
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Explanation

### Strategy (The "Why")

The problem asks us to construct a binary tree from its preorder and inorder traversal arrays.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 3000$, values in $[-3000, 3000]$, all values are unique.
- **Time Complexity:** $O(n)$ - We visit each node once. The hash map lookup is $O(1)$.
- **Space Complexity:** $O(n)$ - Hash map for inorder indices takes $O(n)$, recursion stack takes $O(h)$ where $h$ is tree height.
- **Edge Case:** Empty arrays return `None`.

**1.2 High-level approach:**

The goal is to reconstruct the tree using the property that in preorder, the root comes first, and in inorder, the root separates left and right subtrees.

![Tree Construction](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each root, search for it in inorder array linearly. This takes $O(n^2)$ time.
- **Optimized (Hash Map):** Use a hash map to store inorder indices for $O(1)$ lookup. This takes $O(n)$ time.
- **Emphasize the optimization:** The hash map reduces the time complexity from $O(n^2)$ to $O(n)$ by eliminating linear searches.

**1.4 Decomposition:**

1. **Build Hash Map:** Create a map from values to their inorder indices.
2. **Recursive Build:** Use preorder to get root, use inorder to split left/right subtrees.
3. **Calculate Ranges:** Determine preorder and inorder ranges for left and right subtrees.
4. **Return Root:** Build and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`.

Hash map: `{9:0, 3:1, 15:2, 20:3, 7:4}`

**2.2 Start Building:**

Root is `preorder[0] = 3`. Find its position in inorder: `inorder[1] = 3`.

**2.3 Trace Walkthrough:**

| Root | Preorder Range | Inorder Range | Left Size | Left Subtree | Right Subtree |
|------|----------------|---------------|-----------|--------------|---------------|
| 3 | [0:4] | [0:4] | 1 | pre[1:2], in[0:0] | pre[2:5], in[2:4] |
| 9 | [1:2] | [0:0] | 0 | None | None |
| 20 | [2:5] | [2:4] | 1 | pre[3:4], in[2:2] | pre[4:5], in[3:4] |
| 15 | [3:4] | [2:2] | 0 | None | None |
| 7 | [4:5] | [3:4] | 0 | None | None |

**2.4 Complete Construction:**

Tree structure: `3` (root) with left child `9` and right child `20`. `20` has left child `15` and right child `7`.

**2.5 Return Result:**

The function returns the root node of the constructed tree.

> **Note:** The key insight is that preorder gives us the root, and inorder tells us how many nodes are in the left subtree, allowing us to split the preorder array correctly.

