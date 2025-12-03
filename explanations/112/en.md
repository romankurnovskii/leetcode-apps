## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $0 \leq n \leq 5000$ nodes, with values in $[-1000, 1000]$.
* **Time Complexity:** $O(n)$ - We visit each node at most once in the worst case.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
* **Edge Case:** An empty tree returns `False`. A single-node tree returns `True` if the node value equals `targetSum`.

**1.2 High-level approach**

The goal is to check if there exists a root-to-leaf path where the sum of node values equals `targetSum`. We traverse the tree recursively, subtracting each node's value from the remaining sum, and check if we reach a leaf with the correct sum.

![Path sum visualization showing root-to-leaf paths and their sums]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Find all root-to-leaf paths, calculate their sums, then check if any equals `targetSum`. This requires storing all paths, using $O(n \times h)$ space.
* **Optimized (Recursive DFS):** Traverse the tree and check the sum incrementally. If we find a valid path, return immediately. This uses $O(h)$ space for recursion stack.

**1.4 Decomposition**

1. **Base Case:** If node is `None`, return `False`.
2. **Leaf Check:** If node is a leaf, check if its value equals the remaining sum.
3. **Recursive Check:** Recursively check left and right subtrees with updated remaining sum.
4. **Return Result:** Return `True` if either subtree has a valid path.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [5,4,8,11,null,13,4,7,2,null,null,null,1]$, $targetSum = 22$.

We start at the root node with value 5.

**2.2 Start Checking**

We call `hasPathSum(root, 22)`.

**2.3 Trace Walkthrough**

| Node | targetSum (before) | Is Leaf? | targetSum (after) | Left Result | Right Result | Final Result |
|------|-------------------|----------|-------------------|-------------|--------------|--------------|
| 5 | 22 | No | 17 | Check(4, 17) | Check(8, 17) | OR result |
| 4 | 17 | No | 13 | Check(11, 13) | None | OR result |
| 11 | 13 | No | 2 | Check(7, 2) | Check(2, 2) | OR result |
| 7 | 2 | Yes | -5 | - | - | False |
| 2 | 2 | Yes | 0 | - | - | **True** |

Since node 2 is a leaf and `2 == 2`, we return `True` for the path $5 \to 4 \to 11 \to 2$.

**2.4 Recursive Processing**

For each node:
1. If `not root`, return `False`
2. If leaf (`not root.left and not root.right`), return `root.val == targetSum`
3. Otherwise, recursively check: `hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)`

**2.5 Return Result**

The function returns `True` because there exists a path $5 \to 4 \to 11 \to 2$ with sum $5 + 4 + 11 + 2 = 22$.

