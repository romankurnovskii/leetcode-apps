## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $0 \leq n \leq 2000$ nodes, with values in $[-100, 100]$.
* **Time Complexity:** $O(n)$ - We visit each node exactly once during the flattening process.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
* **Edge Case:** An empty tree requires no modification. A single-node tree remains unchanged.

**1.2 High-level approach**

The goal is to flatten a binary tree into a linked list in pre-order traversal order. We recursively flatten subtrees, then rearrange pointers to form a linear structure.

![Tree flattening visualization showing how tree nodes are rearranged into a linked list]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Store pre-order traversal in a list, then rebuild the tree as a linked list. This uses $O(n)$ extra space.
* **Optimized (In-Place):** Flatten subtrees recursively, then rearrange pointers in-place. This uses $O(h)$ space for recursion stack.

**1.4 Decomposition**

1. **Flatten Subtrees:** Recursively flatten left and right subtrees.
2. **Save Right:** Store the right subtree before modifying pointers.
3. **Move Left to Right:** Set `root.right = root.left` and `root.left = None`.
4. **Attach Saved Right:** Find the end of the flattened left subtree and attach the saved right subtree.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [1,2,5,3,4,null,6]$.

We start at the root node with value 1.

**2.2 Start Processing**

We call `flatten(root)`.

**2.3 Trace Walkthrough**

The flattening process happens bottom-up:

**Step 1: Flatten leaf nodes**
- Node 3: Already flat (no children)
- Node 4: Already flat (no children)
- Node 6: Already flat (no children)

**Step 2: Flatten node 2**
- Left subtree [3,4] is already flat
- Right subtree is None
- Move left to right: `2.right = 2.left = [3,4]`, `2.left = None`

**Step 3: Flatten node 5**
- Left subtree is None
- Right subtree [6] is already flat
- No change needed

**Step 4: Flatten root 1**
- Left subtree [2,3,4] is flattened
- Right subtree [5,6] is flattened
- Save right: `right = [5,6]`
- Move left to right: `1.right = [2,3,4]`, `1.left = None`
- Find end of [2,3,4] (node 4) and attach: `4.right = [5,6]`

**2.4 Recursive Processing**

For each node:
1. If `not root`, return (base case)
2. Recursively flatten `root.left`
3. Recursively flatten `root.right`
4. Save `right = root.right`
5. Set `root.right = root.left` and `root.left = None`
6. Traverse to end of new right subtree and set `curr.right = right`

**2.5 Return Result**

After flattening, the tree becomes a linked list: `[1,null,2,null,3,null,4,null,5,null,6]`, which matches the pre-order traversal.

