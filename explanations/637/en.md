## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nodes <= 10^4`.
- **Time Complexity:** O(n) - we visit each node once using BFS.
- **Space Complexity:** O(w) where w is maximum width - queue storage.
- **Edge Case:** Single node tree returns [node.val].

**1.2 High-level approach:**
The goal is to calculate the average value of nodes at each level. We use BFS (level-order traversal) to process nodes level by level, calculating the sum and count for each level.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - BFS is the natural approach.
- **Optimized Strategy:** BFS processes one level at a time, calculate average per level.

**1.4 Decomposition:**
1. Use BFS with a queue.
2. For each level, process all nodes at that level.
3. Calculate sum and count of nodes in the level.
4. Compute average (sum / count).
5. Add to result list.
6. Continue to next level.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `root = [3,9,20,null,null,15,7]`. Initialize queue with [root], res = [].

**2.2 Start Checking:**
We process nodes level by level.

**2.3 Trace Walkthrough:**

| Level | Nodes | Sum | Count | Average | res |
|-------|-------|-----|-------|---------|-----|
| 0 | [3] | 3 | 1 | 3.0 | [3.0] |
| 1 | [9,20] | 29 | 2 | 14.5 | [3.0,14.5] |
| 2 | [15,7] | 22 | 2 | 11.0 | [3.0,14.5,11.0] |

**2.4 Increment and Loop:**
After processing each level, we move to the next.

**2.5 Return Result:**
Return `res = [3.0,14.5,11.0]`, averages for each level.

