## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `2 <= nodes <= 10^4`, `0 <= Node.val <= 10^5`.
- **Time Complexity:** O(n) - we traverse the tree once to collect values.
- **Space Complexity:** O(n) - we store all node values.
- **Edge Case:** Tree with only two nodes.

**1.2 High-level approach:**
The goal is to find the minimum absolute difference between any two nodes in a BST. We use in-order traversal to get sorted values, then find minimum difference between consecutive values.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Compare all pairs - O(n²) time.
- **Optimized Strategy:** In-order traversal gives sorted order, check adjacent pairs - O(n) time.

**1.4 Decomposition:**
1. Perform in-order traversal to get sorted values.
2. Iterate through sorted values.
3. Calculate difference between consecutive values.
4. Track minimum difference.
5. Return minimum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `root = [4,2,6,1,3]`. In-order traversal gives [1,2,3,4,6].

**2.2 Start Checking:**
We compare consecutive values in sorted order.

**2.3 Trace Walkthrough:**

| i | values[i] | values[i+1] | Difference | Min |
|---|-----------|-------------|------------|-----|
| 0 | 1 | 2 | 1 | 1 |
| 1 | 2 | 3 | 1 | 1 |
| 2 | 3 | 4 | 1 | 1 |
| 3 | 4 | 6 | 2 | 1 |

**2.4 Increment and Loop:**
After checking each pair, we move to the next.

**2.5 Return Result:**
Return `res = 1`, the minimum absolute difference.

