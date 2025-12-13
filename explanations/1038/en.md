## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The number of nodes is in the range `[1, 100]`, and node values are between 0 and 100.
  * **Time Complexity:** O(n) - We traverse each node exactly once in reverse inorder.
  * **Space Complexity:** O(h) - The recursion stack uses space proportional to the height of the tree, where h is at most n.
  * **Edge Case:** A tree with a single node returns itself with the same value.

**High-level approach**
We perform a reverse inorder traversal (right, root, left) of the BST. This visits nodes in descending order. As we traverse, we accumulate the sum of all values we've seen and update each node's value to be the sum of itself and all greater values.

![BST with reverse inorder traversal showing cumulative sum updates]

**Brute force vs. optimized strategy**

  * **Brute Force:** Collect all values, sort them, and update nodes - but this requires extra space.
  * **Optimized Strategy:** Use reverse inorder traversal to visit nodes in descending order naturally, updating values in-place.

**Decomposition**

1.  **Initialize Accumulator:** Create a variable to track the running sum of all values seen.
2.  **Reverse Inorder Traversal:** Traverse right subtree first, then process current node, then left subtree.
3.  **Update Node Value:** Add current node's value to the accumulator and update the node.
4.  **Continue Traversal:** Process all nodes in descending order.

### Steps

1.  **Initialization & Example Setup:**
    Let's say we have a BST: `[4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]`
    We initialize `total = 0`.

2.  **Start Traversal:**
    We begin reverse inorder traversal (right, root, left).

3.  **Trace Walkthrough:**
    
    | Node Value | Total Before | Total After | Node Updated To |
    |------------|--------------|-------------|-----------------|
    | 8 | 0 | 8 | 8 |
    | 7 | 8 | 15 | 15 |
    | 6 | 15 | 21 | 21 |
    | 5 | 21 | 26 | 26 |
    | 4 | 26 | 30 | 30 |
    | 3 | 30 | 33 | 33 |
    | 2 | 33 | 35 | 35 |
    | 1 | 35 | 36 | 36 |
    | 0 | 36 | 36 | 36 |

4.  **Result:**
    The tree is updated in-place with new values.

5.  **Return Result:**
    Return the modified root of the tree.

