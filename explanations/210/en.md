## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** `numCourses` ranges from 1 to 2000, and there are up to `numCourses * (numCourses - 1)` prerequisite pairs.
- **Time Complexity:** O(V + E) where V is the number of courses and E is the number of prerequisites. We visit each course once and process each edge once.
- **Space Complexity:** O(V + E) for the graph adjacency list, in-degree array, and result list.
- **Edge Case:** If there are no prerequisites, return any valid ordering (e.g., [0, 1, 2, ..., numCourses-1]).

**1.2 High-level approach:**
The goal is to find a valid course ordering that satisfies all prerequisites. This is a topological sorting problem. If a cycle exists, return an empty array.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible orderings and check if they satisfy prerequisites. This is exponential time.
- **Optimized Strategy:** Use Kahn's algorithm (topological sort with BFS). Process courses with no prerequisites first, then their dependents, building the ordering as we go.
- **Why optimized is better:** Linear time complexity and naturally produces a valid topological ordering.

**1.4 Decomposition:**
1. Build an adjacency list representing the course dependency graph.
2. Calculate in-degree (number of prerequisites) for each course.
3. Start with courses that have no prerequisites (in-degree = 0).
4. For each completed course, add it to the result and reduce the in-degree of its dependent courses.
5. If a dependent course's in-degree becomes 0, add it to the queue.
6. If we process all courses, return the result; otherwise, return an empty array (cycle detected).

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`

Build graph: `graph[0] = [1,2]`, `graph[1] = [3]`, `graph[2] = [3]`
In-degrees: `in_degree[0] = 0`, `in_degree[1] = 1`, `in_degree[2] = 1`, `in_degree[3] = 2`

**2.2 Start Checking:**
Initialize queue with courses having in-degree 0: `queue = [0]`, `res = []`

**2.3 Trace Walkthrough:**

| Step | Queue | Course | res | Update in-degrees | New Queue |
|------|-------|--------|-----|-------------------|-----------|
| 0 | [0] | - | [] | - | - |
| 1 | [0] | 0 | [0] | `in_degree[1]=0, in_degree[2]=0` | [1,2] |
| 2 | [1,2] | 1 | [0,1] | `in_degree[3]=1` | [2] |
| 3 | [2] | 2 | [0,1,2] | `in_degree[3]=0` | [3] |
| 4 | [3] | 3 | [0,1,2,3] | - | [] |

**2.4 Increment and Loop:**
For each course in the queue:
- Remove it and append to result
- For each dependent course, decrement its in-degree
- If in-degree becomes 0, add to queue

**2.5 Return Result:**
`res = [0,1,2,3]` and `len(res) = 4` equals `numCourses = 4`, so return `[0,1,2,3]` (or any valid ordering like `[0,2,1,3]`).

