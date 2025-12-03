## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $1 \leq n \leq 1000$ nodes, with values in $[0, 9]$, and depth at most 10.
* **Time Complexity:** $O(n)$ - We visit each node exactly once during DFS traversal.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. Given depth ≤ 10, this is effectively $O(1)$.
* **Edge Case:** A single-node tree returns the node's value. All nodes have digit values (0-9).

**1.2 High-level approach**

The goal is to sum all numbers formed by root-to-leaf paths. Each path represents a number where digits are concatenated. We use DFS to traverse all paths, building numbers as we go, and sum them when we reach leaves.

![Root-to-leaf number visualization showing how paths form numbers]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Collect all root-to-leaf paths, convert each to a number, then sum. This requires storing all paths, using $O(n \times h)$ space.
* **Optimized (DFS with Running Sum):** Build numbers incrementally during traversal. When reaching a leaf, add the number to the total. This uses $O(h)$ space for recursion stack.

**1.4 Decomposition**

1. **DFS Traversal:** Recursively visit each node.
2. **Build Number:** For each node, update the running number: $current = current \times 10 + node.val$.
3. **Leaf Check:** If node is a leaf, add the number to the result.
4. **Recursive Calls:** Process left and right subtrees with updated number.
5. **Return Sum:** Return the total sum of all root-to-leaf numbers.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [1,2,3]$.

We initialize:
* `res = 0` (accumulator for sum)
* `current_sum = 0` (running number being built)

**2.2 Start Processing**

We call `dfs(root, 0)`.

**2.3 Trace Walkthrough**

| Node | current_sum (before) | current_sum (after) | Is Leaf? | Action | res |
|------|----------------------|---------------------|----------|--------|-----|
| 1 | 0 | 1 | No | Continue | 0 |
| 2 (left) | 1 | 12 | Yes | Add 12 | 12 |
| 3 (right) | 1 | 13 | Yes | Add 13 | 25 |

**2.4 Recursive Processing**

For each node:
1. If `not node`, return (base case)
2. Update: `current_sum = current_sum * 10 + node.val`
3. If leaf (`not node.left and not node.right`):
   - Add to result: `res += current_sum`
   - Return
4. Recursively process: `dfs(node.left, current_sum)` and `dfs(node.right, current_sum)`

**2.5 Return Result**

After processing all paths:
- Path $1 \to 2$: number = 12
- Path $1 \to 3$: number = 13
- Sum: $12 + 13 = 25$

The function returns `res = 25`.

