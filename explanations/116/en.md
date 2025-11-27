## Explanation

### Strategy (The "Why")

Given a perfect binary tree, we need to populate each node's `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be up to $2^{12} - 1$ (perfect binary tree).
- **Value Range:** Node values are between $-1000$ and $1000$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space, not counting the recursion stack. The `next` pointers are part of the output.
- **Edge Case:** If the tree is empty, return null. For a perfect binary tree, all levels are completely filled.

**1.2 High-level approach:**

The goal is to connect nodes at the same level using the `next` pointer.

![Next Right Pointers](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

We use level-order traversal, but instead of using a queue, we leverage the `next` pointers we've already set. We process level by level, connecting children as we go.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use BFS with a queue to process each level, then connect nodes at the same level. This takes $O(n)$ time and $O(n)$ space for the queue.
- **Optimized Strategy (Level-by-level):** Process level by level using the `next` pointers. For each node, connect its left child to right child, and right child to next node's left child. This takes $O(n)$ time and $O(1)$ extra space.
- **Why it's better:** The optimized approach uses $O(1)$ extra space instead of $O(n)$ for a queue, by leveraging the tree structure and `next` pointers we're building.

**1.4 Decomposition:**

1. Start from the root level (which has no `next` pointers to set).
2. For each level, iterate through nodes using the `next` pointers.
3. For each node, connect its left child to its right child.
4. If the node has a `next` pointer, connect its right child to the `next` node's left child.
5. Move to the next level by following the leftmost node's left child.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,2,3,4,5,6,7]$

The tree structure:
```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

**2.2 Start Connecting:**

We begin at the root level.

**2.3 Trace Walkthrough:**

**Level 1 (root):**
- Node 1: No connections needed at root level

**Level 2:**
- Node 2: Connect 2.left (4) → 2.right (5)
- Node 2: Connect 2.right (5) → 2.next.left (6) [since 2.next = 3]
- Node 3: Connect 3.left (6) → 3.right (7)

**2.4 Final Connections:**

After processing:
- Level 1: 1 → NULL
- Level 2: 2 → 3 → NULL
- Level 3: 4 → 5 → 6 → 7 → NULL

**2.5 Return Result:**

We return the root with all `next` pointers properly set.

> **Note:** The key insight is that we can use the `next` pointers we've already set to traverse the current level, eliminating the need for a queue. This makes the space complexity $O(1)$.

