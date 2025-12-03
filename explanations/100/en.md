## Explanation

### Strategy (The "Why")

The problem asks us to determine if two binary trees are structurally identical and have the same node values.

**1.1 Constraints & Complexity:**

- **Input Constraints:** Both trees have at most 100 nodes, and node values are in the range $[-10^4, 10^4]$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once, where $n$ is the minimum number of nodes in the two trees.
- **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In the worst case (skewed tree), $h = n$, giving $O(n)$ space.
- **Edge Case:** Both trees are empty (both roots are `None`), which should return `True`.

**1.2 High-level approach:**

The goal is to check if two trees have the same structure and values by comparing them node by node recursively. We compare the root values, then recursively check left and right subtrees.

![Binary tree comparison](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert both trees to arrays using traversal, then compare arrays. This requires $O(n)$ time and $O(n)$ space for storing both arrays.
- **Optimized (Recursive Comparison):** Compare nodes directly during traversal without storing intermediate results. This uses $O(n)$ time but only $O(h)$ space for the recursion stack.
- **Emphasize the optimization:** By comparing nodes directly during traversal, we can short-circuit early if we find a mismatch, potentially avoiding full tree traversal.

**1.4 Decomposition:**

1. **Base Cases:** If both nodes are `None`, return `True`. If only one is `None`, return `False`.
2. **Value Comparison:** Check if the current nodes have the same value.
3. **Recursive Check:** Recursively check if left subtrees match and right subtrees match.
4. **Combine Results:** Return `True` only if values match and both subtrees match.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `p = [1,2,3]`, `q = [1,2,3]`.

Both trees have the same structure and values.

**2.2 Start Comparison:**

We begin at the root nodes of both trees.

**2.3 Trace Walkthrough:**

| Node Pair | p.val | q.val | Match? | Left Check | Right Check | Result |
|-----------|-------|-------|--------|------------|-------------|--------|
| Root (1, 1) | 1 | 1 | Yes | Check (2, 2) | Check (3, 3) | Continue |
| Left (2, 2) | 2 | 2 | Yes | Check (None, None) | Check (None, None) | True |
| Right (3, 3) | 3 | 3 | Yes | Check (None, None) | Check (None, None) | True |

**2.4 Recursive Unwinding:**

- Both left subtrees (2, 2) match: both have value 2 and no children.
- Both right subtrees (3, 3) match: both have value 3 and no children.
- Root nodes (1, 1) match.

**2.5 Return Result:**

Since all nodes match in structure and value, the function returns `True`.

> **Note:** The algorithm short-circuits: if any node comparison fails, the entire function returns `False` immediately without checking remaining nodes.

