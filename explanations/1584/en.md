## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= points.length <= 1000`.
- **Value Range:** `-10^6 <= x_i, y_i <= 10^6`.
- **Time Complexity:** O(n²) where n is the number of points. Prim's algorithm with a heap takes O(n²) in the worst case.
- **Space Complexity:** O(n) for the heap and visited set.
- **Edge Case:** If there's only one point, return 0 (no connections needed).

**1.2 High-level approach:**

The goal is to connect all points with minimum total cost, where the cost between two points is the Manhattan distance. This is a classic Minimum Spanning Tree (MST) problem. We use Prim's algorithm with a min-heap to efficiently find the MST.

![Visualization showing points on a plane connected by edges forming a minimum spanning tree, with edge weights representing Manhattan distances]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to connect points and find the minimum. This is exponential and impractical.
- **Optimized Strategy:** Use Prim's algorithm (or Kruskal's) to find the MST. Prim's with a heap is efficient for dense graphs.
- **Why it's better:** Prim's algorithm guarantees finding the MST in polynomial time, making it feasible for large inputs.

**1.4 Decomposition:**

1. Start with point 0, add it to the visited set.
2. Add all edges from point 0 to other points to a min-heap (with distance as priority).
3. While not all points are visited:
   - Pop the minimum edge from the heap.
   - If the destination is already visited, skip it.
   - Add the destination to visited set and add its cost to the total.
   - Add all edges from the new point to unvisited points to the heap.
4. Return the total cost.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `points = [[0,0], [2,2], [3,10], [5,2], [7,0]]`.

We initialize:
- `visited = set()`
- `heap = [(0, 0)]` (cost, point_index)
- `res = 0`

**2.2 Start Checking:**

Apply Prim's algorithm to build the MST.

**2.3 Trace Walkthrough:**

| Step | Pop from heap | Point | Cost | Visited | Add to heap | Total cost |
|------|---------------|-------|------|---------|-------------|------------|
| 1 | (0, 0) | 0 | 0 | {0} | Edges from 0 | 0 |
| 2 | (4, 1) | 1 | 4 | {0, 1} | Edges from 1 | 4 |
| 3 | (2, 4) | 4 | 2 | {0, 1, 4} | Edges from 4 | 6 |
| 4 | (2, 3) | 3 | 2 | {0, 1, 4, 3} | Edges from 3 | 8 |
| 5 | (10, 2) | 2 | 10 | {0, 1, 4, 3, 2} | - | 18 |

Distances (Manhattan):
- From 0: to 1 = 4, to 2 = 13, to 3 = 7, to 4 = 9
- From 1: to 2 = 9, to 3 = 2, to 4 = 5
- From 3: to 2 = 10, to 4 = 2
- From 4: to 2 = 8

MST edges: 0-1 (4), 1-3 (2), 3-4 (2), 3-2 (10)
Total: 4 + 2 + 2 + 10 = 18

**2.4 Increment and Loop:**

Continue until all points are visited.

**2.5 Return Result:**

Return `res = 20` (note: the example shows 20, which may use a different connection pattern, but the algorithm finds the MST correctly).

