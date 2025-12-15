## Explanation

### Strategy

**Restate the problem**  
Given preorder traversal of a BST, reconstruct the tree.

**1.1 Constraints & Complexity**  
- **Input Size:** up to 100 nodes.  
- **Time Complexity:** O(n) using a stack to place nodes.  
- **Space Complexity:** O(n) for the stack/tree nodes.  
- **Edge Case:** Single-node preorder list.

**1.2 High-level approach**  
Iterate preorder; use a stack of ancestors. Each value smaller than stack top goes left; otherwise pop until finding parent, then attach right.  
![BST reconstruction from preorder](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Insert each value via BST insert — still O(n²) worst case (sorted input).  
- **Optimized:** Monotonic stack to place nodes in O(n).

**1.4 Decomposition**  
1. Create root from first value; push to stack.  
2. For each next value:  
   - If value < stack top, set as left child of top.  
   - Else pop until stack empty or top > value; last popped is parent; attach as right child.  
3. Push new node to stack.  
4. Return root.

### Steps

**2.1 Initialization & Example Setup**  
Example: `[8,5,1,7,10,12]`; root = 8, stack = [8].

**2.2 Start Checking**  
Process each value, updating stack and children.

**2.3 Trace Walkthrough**  
| val | Stack before | Action                          | Child  |
|-----|--------------|---------------------------------|--------|
| 5   | [8]          | 5 < 8 → left of 8               | left   |
| 1   | [8,5]        | 1 < 5 → left of 5               | left   |
| 7   | [8,5,1]      | pop 1,5 (last popped=5) → right | right  |
| 10  | [8,7]        | pop 7,8 (last popped=8) → right | right  |
| 12  | [10]         | pop none → right of 10          | right  |

**2.4 Increment and Loop**  
Continue until all preorder values are attached.

**2.5 Return Result**  
Root of the constructed BST.

