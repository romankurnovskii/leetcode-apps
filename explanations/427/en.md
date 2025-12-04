## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `n == grid.length == grid[i].length`, `n == 2^x` where `0 <= x <= 6`.
- **Time Complexity:** O(n²) - we process each cell, but with divide-and-conquer optimization.
- **Space Complexity:** O(log n) - recursion depth.
- **Edge Case:** All cells have the same value, single leaf node.

**1.2 High-level approach:**
The goal is to construct a Quad-Tree from a binary grid. We use divide-and-conquer: if all values in a region are the same, create a leaf; otherwise, divide into 4 quadrants and recurse.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - divide-and-conquer is the natural approach.
- **Optimized Strategy:** Recursively divide grid into quadrants until uniform or single cell.

**1.4 Decomposition:**
1. Check if all values in current region are the same.
2. If yes, create a leaf node with that value.
3. If no, divide into 4 quadrants (top-left, top-right, bottom-left, bottom-right).
4. Recursively construct each quadrant.
5. Create internal node with 4 children.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `grid = [[0,1],[1,0]]`. We start with the entire 2x2 grid.

**2.2 Start Checking:**
We check if all values are the same.

**2.3 Trace Walkthrough:**

| Region | All Same? | Action | Result |
|--------|-----------|--------|--------|
| [[0,1],[1,0]] | No | Divide | Internal node |
| Top-left [0] | Yes | Leaf | Node(val=0, isLeaf=True) |
| Top-right [1] | Yes | Leaf | Node(val=1, isLeaf=True) |
| Bottom-left [1] | Yes | Leaf | Node(val=1, isLeaf=True) |
| Bottom-right [0] | Yes | Leaf | Node(val=0, isLeaf=True) |

**2.4 Increment and Loop:**
After processing each quadrant, we combine results.

**2.5 Return Result:**
Return root node with 4 leaf children.

