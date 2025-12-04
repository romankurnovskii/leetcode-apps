## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nodes <= 5000`, `1 <= Node.val <= 1000`.
- **Time Complexity:** O(n) where n is the number of nodes - we visit each node once.
- **Space Complexity:** O(1) - we only create new nodes, no additional data structures.
- **Edge Case:** Single node list, no insertion needed.

**1.2 High-level approach:**
The goal is to insert a new node between every pair of adjacent nodes, where the new node's value is the GCD of the two adjacent nodes' values. We traverse the list and insert nodes as we go.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we must visit each node once.
- **Optimized Strategy:** Traverse the list once, calculating GCD and inserting nodes in-place.

**1.4 Decomposition:**
1. Implement GCD calculation using Euclidean algorithm.
2. Traverse the linked list.
3. For each pair of adjacent nodes, calculate their GCD.
4. Create a new node with the GCD value.
5. Insert it between the two nodes.
6. Continue to the next pair.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `head = [18,6,10,3]`. We start at the first node.

**2.2 Start Checking:**
We process each adjacent pair of nodes.

**2.3 Trace Walkthrough:**

| Current | Next | GCD(18,6) | GCD(6,10) | GCD(10,3) | Result |
|---------|------|-----------|-----------|-----------|--------|
| 18 | 6 | 6 | - | - | [18,6,6,...] |
| 6 | 10 | - | 2 | - | [18,6,6,2,10,...] |
| 10 | 3 | - | - | 1 | [18,6,6,2,10,1,3] |

**2.4 Increment and Loop:**
After inserting a node, we move to the node after the inserted one and continue.

**2.5 Return Result:**
Return the modified list `[18,6,6,2,10,1,3]` with GCD nodes inserted.

