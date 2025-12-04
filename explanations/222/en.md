## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The tree has 0 to 5*10^4 nodes and is guaranteed to be complete.
- **Time Complexity:** O(log² n) - We do O(log n) work at each level, and there are O(log n) levels.
- **Space Complexity:** O(log n) for the recursion stack.
- **Edge Case:** If the root is None, return 0.

**1.2 High-level approach:**
The goal is to count nodes in a complete binary tree efficiently. We use the property that in a complete tree, we can check if subtrees are full by comparing left and right heights.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Recursively count all nodes: O(n) time.
- **Optimized Strategy:** Use the complete tree property. If left and right heights are equal, the left subtree is full. Otherwise, the right subtree is full. This allows us to skip counting full subtrees.
- **Why optimized is better:** We avoid counting nodes in full subtrees, reducing time complexity to O(log² n).

**1.4 Decomposition:**
1. Calculate the height of the left subtree by following left children.
2. Calculate the height of the right subtree by following left children from the right child.
3. If heights are equal, the left subtree is full (2^height - 1 nodes), so recursively count the right subtree.
4. If heights differ, the right subtree is full, so recursively count the left subtree.
5. Add 1 for the root and the full subtree size.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Example tree: `[1,2,3,4,5,6]` (complete binary tree with 6 nodes)

Root = 1, left = 2, right = 3

**2.2 Start Checking:**
Calculate left height from root.left (node 2): follow left children → 4 → None, height = 2
Calculate right height from root.right (node 3): follow left children → None, height = 0

**2.3 Trace Walkthrough:**

| Node | Left Height | Right Height | Action |
|------|-------------|---------------|--------|
| 1 | 2 | 0 | Heights differ, right is full. Count = 2^0 + countNodes(left) |
| 2 | 1 | 0 | Heights differ, right is full. Count = 2^0 + countNodes(left) |
| 4 | 0 | 0 | Heights equal, left is full. Count = 2^0 + countNodes(right) |
| 5 | 0 | 0 | Base case, return 1 |

**2.4 Increment and Loop:**
Recursively:
- If left_height == right_height: return (1 << left_height) + countNodes(right)
- Else: return (1 << right_height) + countNodes(left)

**2.5 Return Result:**
Total count = 1 (root) + 1 (node 2) + 1 (node 4) + 1 (node 5) + 1 (node 3) + 1 (node 6) = 6 nodes.

