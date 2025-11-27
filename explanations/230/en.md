# Problem 230: Kth Smallest Element in a BST

**Difficulty:** Medium  
**LeetCode Link:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the kth smallest element (1-indexed) in a Binary Search Tree. In a BST, all values in the left subtree are smaller than the root, and all values in the right subtree are larger.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most $10^4$ nodes, and $1 \leq k \leq n$.
- **Time Complexity:** $O(h + k)$ where $h$ is the height of the tree. In the worst case (skewed tree), this is $O(n + k) = O(n)$. We traverse until we find the kth element.
- **Space Complexity:** $O(h)$ for the recursion stack, which is $O(n)$ in the worst case for a skewed tree.
- **Edge Case:** If $k = 1$, we return the leftmost (smallest) node in the tree.

**1.2 High-level approach:**

The goal is to find the kth smallest element efficiently. Since in-order traversal of a BST visits nodes in sorted order, we can use in-order traversal and stop when we've visited k nodes.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Do a complete in-order traversal, store all values in an array, then return the kth element. This is $O(n)$ time and $O(n)$ space.
- **Optimized Strategy:** Use in-order traversal but stop early when we reach the kth element. This is $O(h + k)$ time and $O(h)$ space.
- **Optimization:** By stopping early, we avoid storing all elements and can terminate as soon as we find the kth smallest element, potentially saving time and space.

**1.4 Decomposition:**

1. Initialize a counter to track how many nodes we've visited.
2. Perform in-order traversal (left, root, right).
3. For each node visited in order, increment the counter.
4. When the counter reaches k, record the current node's value and return.
5. If we haven't found the kth element yet, continue the traversal.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `root = [3, 1, 4, null, 2]`, `k = 1`.

- Tree structure:
```
    3
   / \
  1   4
   \
    2
```
- Initialize `count = 0` and `res = None`

**2.2 Start Checking:**

We begin in-order traversal from the root, always going left first to find the smallest elements.

**2.3 Trace Walkthrough:**

| Step | Current Node | Action | count | res | Next Action |
|------|--------------|--------|-------|-----|-------------|
| 1    | 3            | Go left to 1 | 0 | None | Continue left |
| 2    | 1            | Go left (null) | 0 | None | Process node 1 |
| 3    | 1            | Process: count++ | 1 | 1 | Check if count == k |
| 4    | 1            | count == 1, set res = 1 | 1 | 1 | Return (found!) |

**2.4 Increment and Loop:**

The in-order traversal follows the pattern: visit left subtree, process current node (increment count), then visit right subtree. We stop as soon as count equals k.

**2.5 Return Result:**

When count reaches k (1 in this case), we found the 1st smallest element which is 1, so we return `res = 1`.

