## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The tree can have up to 1000 nodes.
* **Time Complexity:** O(n) - We visit each node once during DFS, where n is the number of nodes.
* **Space Complexity:** O(h) for recursion stack where h is the height, plus O(n) in worst case for the prefix sum map.
* **Edge Case:** If the tree is empty, return 0. If targetSum is 0 and there are nodes with value 0, we need to count paths correctly.

**1.2 High-level approach:**

The goal is to count all paths in a binary tree where the sum of node values equals targetSum. A path can start and end anywhere, but must go downward. We use prefix sums to efficiently count paths ending at each node.

![Tree showing paths with prefix sum tracking]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** For each node, explore all downward paths starting from it. This is O(n^2) in the worst case.
* **Optimized (Prefix Sum with Hash Map):** Use a hash map to store prefix sums along the current path. For each node, check if (current_sum - targetSum) exists in the map. This is O(n) time.
* **Why it's better:** The prefix sum approach avoids redundant calculations and reduces time complexity from O(n^2) to O(n).

**1.4 Decomposition:**

1. Use DFS to traverse the tree.
2. Maintain a prefix sum map that tracks sums along the current path.
3. At each node, add the node's value to current sum.
4. Check if (current_sum - targetSum) exists in the map to count paths ending here.
5. Recursively process left and right children.
6. Backtrack by decrementing the prefix sum count before returning.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8

We initialize:
* `res = 0` (count of paths)
* `prefix_sums = {}` (map of prefix sum -> count)
* `current_sum = 0`

**2.2 Start Checking/Processing:**

We call `dfs(root, 0)` to start traversal.

**2.3 Trace Walkthrough:**

| Node | current_sum | prefix_sums | current_sum - 8 | Paths Found |
|------|-------------|-------------|-----------------|-------------|
| 10 | 10 | {10:1} | 2 | 0 |
| 5 | 15 | {10:1, 15:1} | 7 | 0 |
| 3 | 18 | {10:1, 15:1, 18:1} | 10 | 1 (18-8=10 exists) |
| -2 | 16 | {10:1, 15:1, 18:1, 16:1} | 8 | 1 (16-8=8, but 8 not in map, but current_sum=16, check if 16==8: no) |
| 2 | 17 | {10:1, 15:1, 18:1, 16:1, 17:1} | 9 | 0 |
| 1 | 18 | {10:1, 15:1, 18:2, 16:1, 17:1} | 10 | 1 (18-8=10 exists) |

**2.4 Increment and Loop:**

After processing each node and its children, we backtrack by decrementing the prefix sum count.

**2.5 Return Result:**

After processing all nodes, `res = 3` is returned (paths: 5->3, 5->2->1, -3->11).

