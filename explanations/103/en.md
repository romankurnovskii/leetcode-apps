## Explanation

### Strategy (The "Why")

The problem asks us to return the zigzag level order traversal of a binary tree: left-to-right for even levels, right-to-left for odd levels.

**1.1 Constraints & Complexity:**

- **Input Constraints:** The tree has $0 \leq n \leq 2000$ nodes with values in $[-100, 100]$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level.
- **Edge Case:** Empty tree returns empty list.

**1.2 High-level approach:**

The goal is to traverse the tree level by level, alternating the direction at each level. We use BFS with a flag to track direction.

![Zigzag Traversal](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Do regular level-order traversal, then reverse every other level. This takes $O(n)$ time and $O(n)$ space.
- **Optimized (BFS with Direction Flag):** Use BFS and reverse the level list when needed based on a flag. This takes $O(n)$ time and $O(n)$ space.
- **Emphasize the optimization:** While complexity is the same, the direction flag approach is cleaner and more efficient than reversing after collection.

**1.4 Decomposition:**

1. **BFS Traversal:** Use a queue to process nodes level by level.
2. **Track Direction:** Use a boolean flag to alternate between left-to-right and right-to-left.
3. **Reverse When Needed:** For odd levels (right-to-left), reverse the level list before adding to result.
4. **Return Result:** Return the list of levels.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [3,9,20,null,null,15,7]`.

Initialize: `queue = [3]`, `left_to_right = True`, `res = []`

**2.2 Start Processing:**

Process level 0 (root).

**2.3 Trace Walkthrough:**

| Level | Queue Before | Level Values | Direction | After Reverse | Result |
|-------|--------------|--------------|-----------|---------------|--------|
| 0 | [3] | [3] | L→R | [3] | [[3]] |
| 1 | [9, 20] | [9, 20] | R→L | [20, 9] | [[3], [20, 9]] |
| 2 | [15, 7] | [15, 7] | L→R | [15, 7] | [[3], [20, 9], [15, 7]] |

**2.4 Complete Traversal:**

All levels processed: Level 0 (L→R), Level 1 (R→L), Level 2 (L→R).

**2.5 Return Result:**

The function returns `[[3], [20, 9], [15, 7]]`.

> **Note:** The direction alternates at each level: even levels (0, 2, ...) are left-to-right, odd levels (1, 3, ...) are right-to-left.

