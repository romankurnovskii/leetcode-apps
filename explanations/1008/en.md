## Explanation

### Strategy

**Constraints & Edge Cases**

* **Preorder Array:** The preorder traversal array has length 1-100, with unique values between 1-1000. The array is guaranteed to form a valid BST.
* **Time Complexity:** We process each element once, and for each element we may need to find the split point. In worst case, this is O(n²), but average case is O(n log n). **Time Complexity: O(n²)** worst case, **O(n log n)** average, **Space Complexity: O(n)** for recursion stack.
* **Edge Case:** If the array has only one element, we return a single node tree.

**High-level approach**

The problem asks us to construct a BST from its preorder traversal. In preorder, the root comes first, followed by all left subtree nodes, then all right subtree nodes.

**Brute force vs. optimized strategy**

* **Brute Force:** For each element, insert it into the BST one by one. This would be O(n²) time.
* **Optimized:** Use the property that in preorder, after the root, all values less than root form the left subtree, and all values greater than root form the right subtree. Recursively build left and right subtrees.

**Decomposition**

1. **Root Selection:** The first element in preorder is always the root.
2. **Split Point:** Find where values transition from less than root to greater than root.
3. **Recursive Construction:** Build left subtree from elements before split, right subtree from elements after split.

### Steps

1. **Initialization & Example Setup**
   Let's use `preorder = [8,5,1,7,10,12]` as our example.
   - If preorder is empty, return None.

2. **Root Creation**
   - Create root node with value `preorder[0] = 8`.

3. **Find Split Point**
   - Start from index 1, find the first index where `preorder[i] >= preorder[0]`.
   - For our example: `preorder[1]=5 < 8`, `preorder[2]=1 < 8`, `preorder[3]=7 < 8`, `preorder[4]=10 >= 8`.
   - Split point `i = 4`.

4. **Trace Walkthrough**

| Step | Left Subtree | Root | Right Subtree | Action |
|------|--------------|------|----------------|--------|
| 1    | [5,1,7]      | 8    | [10,12]        | Create root(8) |
| 2    | [1]          | 5    | [7]            | Build left: root(5) |
| 3    | []           | 1    | []             | Build left of 5: root(1) |
| 4    | []           | 7    | []             | Build right of 5: root(7) |
| 5    | []           | 10   | [12]           | Build right: root(10) |
| 6    | []           | 12   | []             | Build right of 10: root(12) |

5. **Recursive Construction**
   - `root.left = bstFromPreorder([5,1,7])` → builds left subtree
   - `root.right = bstFromPreorder([10,12])` → builds right subtree

6. **Return Result**
   Return the root node of the constructed BST.
