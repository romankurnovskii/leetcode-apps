## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The tree can have up to 5000 nodes.
* **Time Complexity:** O(h) where h is the height of the tree. In the worst case (skewed tree), h = n, giving O(n). In a balanced tree, h = log n.
* **Space Complexity:** O(h) for the recursion stack. In worst case O(n), in balanced tree O(log n).
* **Edge Case:** If the tree is empty or the value doesn't exist, return None.

**1.2 High-level approach:**

The goal is to find a node in a BST with a given value. We use the BST property: left subtree contains smaller values, right subtree contains larger values.

![BST search showing how we navigate left or right based on comparison]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Traverse the entire tree (inorder/preorder/postorder) to find the value. This takes O(n) time.
* **Optimized (BST Property):** Use the BST property to eliminate half of the remaining nodes at each step. This takes O(h) time where h is height.
* **Why it's better:** The BST property allows us to skip entire subtrees, making search much faster than linear traversal.

**1.4 Decomposition:**

1. If the current node is None, return None (value not found).
2. If current node's value equals target, return the current node.
3. If current node's value is greater than target, search in the left subtree.
4. If current node's value is less than target, search in the right subtree.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = [4,2,7,1,3], val = 2

We start at the root node with value 4.

**2.2 Start Checking/Processing:**

We call `searchBST(root, 2)`.

**2.3 Trace Walkthrough:**

| Step | Current Node | Current Val | Comparison | Action |
|------|--------------|-------------|------------|--------|
| 1 | 4 | 4 | 4 > 2 | Go left to node 2 |
| 2 | 2 | 2 | 2 == 2 | Found! Return node 2 |

**2.4 Increment and Loop:**

After each comparison, we recursively search the appropriate subtree.

**2.5 Return Result:**

We return the node with value 2, which is the root of the subtree [2,1,3].

