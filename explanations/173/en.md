## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^5$ nodes. Node values are in the range $[0, 10^6]$. At most $10^5$ calls to `next()` and `hasNext()`.
- **Time Complexity:** 
  - `__init__`: $O(h)$ where $h$ is the height of the tree (we push left nodes).
  - `next()`: Amortized $O(1)$ per call.
  - `hasNext()`: $O(1)$.
- **Space Complexity:** $O(h)$ for the stack storing nodes along the path to the leftmost node.
- **Edge Case:** If the tree has only one node, the stack contains that node initially.

**1.2 High-level approach:**

The goal is to implement an iterator that returns nodes in in-order traversal (left, root, right) order. We use a stack to simulate the in-order traversal. Initially, we push all left nodes. When `next()` is called, we pop a node, push its right subtree's left nodes, and return the node's value.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Perform full in-order traversal, store all values in a list, then iterate through the list. This requires $O(n)$ space and doesn't meet the $O(h)$ space requirement.
- **Optimized Strategy:** Use a stack to maintain only the nodes needed for the current path. Push left nodes initially, and when popping, push left nodes of the right child. This uses $O(h)$ space.
- **Why optimized is better:** The optimized approach meets the $O(h)$ space requirement and provides amortized $O(1)$ time for `next()`.

**1.4 Decomposition:**

1. In `__init__`, push all left nodes starting from the root.
2. In `next()`, pop a node from the stack, push all left nodes of its right child, and return the node's value.
3. In `hasNext()`, check if the stack is non-empty.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `root = [7, 3, 15, null, null, 9, 20]`

The tree structure:
```
      7
     / \
    3   15
       /  \
      9    20
```

We initialize `stack = []` and call `_push_left(root)`.

**2.2 Start Checking:**

The `_push_left` function pushes all left nodes: 7, then 3. So `stack = [7, 3]` (top is 3).

**2.3 Trace Walkthrough:**

| Operation | Stack before | Action | Stack after | Return |
|-----------|--------------|--------|-------------|--------|
| __init__ | [] | Push left: 7, 3 | [7, 3] | - |
| next() | [7, 3] | Pop 3, push left of 3.right (none) | [7] | 3 |
| next() | [7] | Pop 7, push left of 7.right: 15, 9 | [15, 9] | 7 |
| hasNext() | [15, 9] | Check stack non-empty | [15, 9] | True |
| next() | [15, 9] | Pop 9, push left of 9.right (none) | [15] | 9 |
| next() | [15] | Pop 15, push left of 15.right: 20 | [20] | 15 |
| next() | [20] | Pop 20, push left of 20.right (none) | [] | 20 |
| hasNext() | [] | Check stack empty | [] | False |

**2.4 Increment and Loop:**

- **`_push_left(node)`**: While `node` is not None, push `node` to stack and move to `node.left`.
- **`next()`**: 
  - Pop a node from the stack.
  - Call `_push_left(node.right)` to push all left nodes of the right subtree.
  - Return the popped node's value.

**2.5 Return Result:**

The iterator returns values in in-order order: 3, 7, 9, 15, 20. Each call to `next()` returns the next value, and `hasNext()` correctly indicates when more values are available.

