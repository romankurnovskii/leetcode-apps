## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** `numCourses` ranges from 1 to 2000, and there are up to 5000 prerequisite pairs.
- **Time Complexity:** O(V + E) where V is the number of courses and E is the number of prerequisites. We visit each course once and process each edge once.
- **Space Complexity:** O(V + E) for the graph adjacency list and in-degree array.
- **Edge Case:** If there are no prerequisites, all courses can be finished, so return true.

**1.2 High-level approach:**
The goal is to determine if we can finish all courses given their prerequisites. This is equivalent to detecting cycles in a directed graph. If a cycle exists, we cannot finish all courses.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Use DFS to detect cycles by tracking visited nodes and nodes in the current path. This works but is more complex.
- **Optimized Strategy:** Use Kahn's algorithm (topological sort with BFS). Start with courses that have no prerequisites, remove them, and continue. If we can process all courses, there's no cycle.
- **Why optimized is better:** BFS-based approach is more intuitive and naturally handles the topological ordering.

**1.4 Decomposition:**
1. Build an adjacency list representing the course dependency graph.
2. Calculate in-degree (number of prerequisites) for each course.
3. Start with courses that have no prerequisites (in-degree = 0).
4. For each completed course, reduce the in-degree of its dependent courses.
5. If a dependent course's in-degree becomes 0, add it to the queue.
6. If we can process all courses, return true; otherwise, return false.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `numCourses = 2`, `prerequisites = [[1,0]]`

Build graph: `graph[0] = [1]` (course 0 is prerequisite for course 1)
In-degrees: `in_degree[0] = 0`, `in_degree[1] = 1`

**2.2 Start Checking:**
Initialize queue with courses having in-degree 0: `queue = [0]`

**2.3 Trace Walkthrough:**

| Step | Queue | Course | Count | Update in-degrees | New Queue |
|------|-------|--------|-------|-------------------|-----------|
| 0 | [0] | - | 0 | - | - |
| 1 | [0] | 0 | 1 | `in_degree[1] = 0` | [1] |
| 2 | [1] | 1 | 2 | - | [] |

**2.4 Increment and Loop:**
For each course in the queue:
- Remove it and increment count
- For each dependent course, decrement its in-degree
- If in-degree becomes 0, add to queue

**2.5 Return Result:**
`count = 2` equals `numCourses = 2`, so we can finish all courses. Return `True`.

