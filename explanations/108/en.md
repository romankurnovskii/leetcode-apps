## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The array $nums$ has length $1 \leq n \leq 10^4$, with values in $[-10^4, 10^4]$.
* **Time Complexity:** $O(n)$ - We visit each element exactly once to build the tree.
* **Space Complexity:** $O(n)$ - The recursion stack depth is $O(\log n)$ for a balanced tree, and the tree itself uses $O(n)$ space.
* **Edge Case:** An empty array returns `None`. A single-element array creates a tree with one node.

**1.2 High-level approach**

The goal is to convert a sorted array into a height-balanced binary search tree. We use the middle element as the root to ensure balance, then recursively build left and right subtrees.

![BST construction from sorted array showing how middle element becomes root]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible tree structures and check if they're balanced. This is exponential in complexity.
* **Optimized (Divide and Conquer):** Always choose the middle element as root, ensuring the tree is balanced. This achieves $O(n)$ time and creates an optimal height-balanced tree.

**1.4 Decomposition**

1. **Choose Root:** Select the middle element of the current range as the root.
2. **Build Left Subtree:** Recursively build BST from elements before the middle.
3. **Build Right Subtree:** Recursively build BST from elements after the middle.
4. **Return Root:** Connect subtrees and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $nums = [-10,-3,0,5,9]$.

We initialize:
* `left = 0`, `right = 4`
* Middle index: $mid = (0 + 4) // 2 = 2$

**2.2 Start Building**

Root is `nums[2] = 0`.

**2.3 Trace Walkthrough**

| Level | left | right | mid | nums[mid] | Left Range | Right Range | Action |
|-------|------|-------|-----|-----------|------------|-------------|--------|
| 0 | 0 | 4 | 2 | 0 | [0,1] | [3,4] | Create root(0) |
| 1 (left) | 0 | 1 | 0 | -10 | [0,-1] | [1,1] | Create left(-10) |
| 1 (right) | 3 | 4 | 3 | 5 | [3,2] | [4,4] | Create right(5) |
| 2 (left) | 1 | 1 | 1 | -3 | [1,0] | [1,1] | Create right(-3) |
| 2 (right) | 4 | 4 | 4 | 9 | [4,3] | [4,4] | Create right(9) |

**2.4 Recursive Building**

For each recursive call:
1. If `left > right`, return `None` (base case)
2. Calculate `mid = (left + right) // 2`
3. Create root with `nums[mid]`
4. Recursively build left subtree: `build(left, mid - 1)`
5. Recursively build right subtree: `build(mid + 1, right)`

**2.5 Return Result**

The function returns the root of the balanced BST: `[0,-10,5,null,-3,null,9]`.

