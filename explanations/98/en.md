# Problem 98: Validate Binary Search Tree

**Difficulty:** Medium  
**LeetCode Link:** https://leetcode.com/problems/validate-binary-search-tree/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to determine if a binary tree is a valid BST. A valid BST requires that for each node, all values in the left subtree are strictly less than the node's value, and all values in the right subtree are strictly greater than the node's value.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most $10^4$ nodes, and each node value can be in the range $[-2^{31}, 2^{31} - 1]$.
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree, for the recursion stack. In the worst case (skewed tree), this is $O(n)$.
- **Edge Case:** A single node is a valid BST. Also, we must handle the case where node values can be at the integer boundaries.

**1.2 High-level approach:**

The goal is to validate that each node satisfies the BST property. We use a recursive approach that maintains valid ranges (min, max) for each node. As we traverse, we update these bounds based on the current node's value.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each node, check if all nodes in its left subtree are smaller and all nodes in its right subtree are larger. This is $O(n^2)$ time.
- **Optimized Strategy:** Use recursion with bounds checking. Pass down min and max values that define the valid range for each subtree. This is $O(n)$ time.
- **Optimization:** By maintaining bounds as we traverse, we avoid checking all descendants for each node, reducing time complexity from $O(n^2)$ to $O(n)$.

**1.4 Decomposition:**

1. Define a recursive function that takes a node and valid range (min_val, max_val).
2. If the node is None, return True (empty subtree is valid).
3. Check if the current node's value is within the valid range.
4. Recursively validate the left subtree with updated max bound (node.val).
5. Recursively validate the right subtree with updated min bound (node.val).
6. Return True only if both subtrees are valid.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `root = [2, 1, 3]`.

- Tree structure:
```
    2
   / \
  1   3
```
- Initialize with `min_val = -inf` and `max_val = +inf`

**2.2 Start Checking:**

We begin validation from the root node with unbounded range.

**2.3 Trace Walkthrough:**

| Step | Node | min_val | max_val | node.val | Check | Left Result | Right Result | Final Result |
|------|------|---------|---------|----------|-------|-------------|--------------|--------------|
| 1    | 2    | -inf    | +inf    | 2        | -inf < 2 < +inf ✓ | Validate(1, -inf, 2) | Validate(3, 2, +inf) | - |
| 2    | 1    | -inf    | 2       | 1        | -inf < 1 < 2 ✓ | Validate(None) = True | Validate(None) = True | True |
| 3    | 3    | 2       | +inf    | 3        | 2 < 3 < +inf ✓ | Validate(None) = True | Validate(None) = True | True |

**2.4 Increment and Loop:**

For each node, we recursively validate its left and right subtrees with updated bounds. The left subtree gets a new max bound (current node's value), and the right subtree gets a new min bound (current node's value).

**2.5 Return Result:**

All nodes satisfy the BST property, so we return `res = True`.

