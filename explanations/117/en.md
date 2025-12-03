## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $0 \leq n \leq 6000$ nodes, with values in $[-100, 100]$.
* **Time Complexity:** $O(n)$ - We visit each node exactly once using BFS.
* **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level.
* **Edge Case:** An empty tree returns `None`. A single-node tree has no next pointers to set.

**1.2 High-level approach**

The goal is to connect each node's `next` pointer to its next right node at the same level. We use level-order traversal (BFS) to process nodes level by level, connecting them as we go.

![Next pointer connection showing how nodes are connected level by level]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Store nodes by level in separate arrays, then connect them. This uses $O(n)$ extra space for level arrays.
* **Optimized (BFS with Queue):** Use a queue to process nodes level by level. Connect nodes within the same level as we process them. This uses $O(n)$ space for the queue, which is necessary for BFS.

**1.4 Decomposition**

1. **Level-Order Traversal:** Use BFS to process nodes level by level.
2. **Track Level Size:** Process exactly `level_size` nodes at each iteration.
3. **Connect Nodes:** For each node in a level, set `prev.next = node` (except the first node).
4. **Update Queue:** Add children to queue for next level.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [1,2,3,4,5,null,7]$.

We initialize:
* `queue = deque([1])` (root node)
* `prev = None` (previous node in current level)

**2.2 Start Processing**

We process level 0 (root).

**2.3 Trace Walkthrough**

| Level | Queue Before | Level Size | Process | prev | Queue After | Next Pointers |
|-------|--------------|------------|---------|------|-------------|---------------|
| 0 | [1] | 1 | 1 | None | [2,3] | 1.next = None |
| 1 | [2,3] | 2 | 2 | None | [3,4,5] | 2.next = None |
| 1 | [3,4,5] | - | 3 | 2 | [4,5,7] | 2.next = 3, 3.next = None |
| 2 | [4,5,7] | 3 | 4 | None | [5,7] | 4.next = None |
| 2 | [5,7] | - | 5 | 4 | [7] | 4.next = 5, 5.next = None |
| 2 | [7] | - | 7 | 5 | [] | 5.next = 7, 7.next = None |

**2.4 Level Processing**

For each level:
1. Get `level_size = len(queue)`
2. Initialize `prev = None`
3. For `level_size` iterations:
   - Pop node from queue
   - If `prev` exists, set `prev.next = node`
   - Update `prev = node`
   - Add children to queue

**2.5 Return Result**

After processing, all nodes have their `next` pointers set correctly:
- Level 0: `1.next = None`
- Level 1: `2.next = 3`, `3.next = None`
- Level 2: `4.next = 5`, `5.next = 7`, `7.next = None`

