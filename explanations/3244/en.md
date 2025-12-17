## Explanation

### Strategy (The "Why")

**Restate the problem:** We have n cities in a line, with initial roads from city i to i+1. We process queries that add new roads, and after each query, we need to find the shortest path length from city 0 to city n-1.

**1.1 Constraints & Complexity:**

- **Input Size:** n can be up to 10^5, and there can be up to 10^5 queries. We need an efficient O(n + q) solution.
- **Time Complexity:** O(n + q) - we initialize the linked list in O(n) and process each query in O(1) amortized time.
- **Space Complexity:** O(n) - we maintain a dictionary representing the linked list structure.
- **Edge Case:** When n=2, there's only one edge, so the path length is always 1.

**1.2 High-level approach:**

The goal is to model the graph as a linked list. Initially, each city i points to i+1. When we add a road from i to j, we remove all intermediate nodes and create a direct link. The shortest path length equals the number of edges in the linked list.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** After each query, run BFS to find shortest path. This is O(q * n) time.
- **Optimized Strategy:** Model as a linked list and maintain it efficiently. When adding edge (i,j), remove nodes between i and j. The path length is the size of the dictionary. This is O(n + q) time.
- **Optimization:** The linked list approach avoids repeated graph traversals and allows us to update the path structure efficiently.

**1.4 Decomposition:**

1. Initialize a dictionary d where d[i] = i+1 for all i from 0 to n-2 (linked list structure).
2. For each query (i, j), if d[i] < j, remove all nodes between i and j, then set d[i] = j.
3. The shortest path length is the number of edges, which equals len(d).
4. Return the path length after each query.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `n = 5`, `queries = [[2,4],[0,2],[0,4]]`

- Initial dictionary: `{0: 1, 1: 2, 2: 3, 3: 4}`
- Initial path length: 4 (edges: 0→1, 1→2, 2→3, 3→4)

**2.2 Start Processing:**

We process each query and update the linked list.

**2.3 Trace Walkthrough:**

| Query | Dictionary Before | Action | Dictionary After | Path Length |
|-------|-------------------|--------|------------------|-------------|
| [2,4] | {0:1, 1:2, 2:3, 3:4} | Remove node 3, set d[2]=4 | {0:1, 1:2, 2:4} | 3 |
| [0,2] | {0:1, 1:2, 2:4} | Remove node 1, set d[0]=2 | {0:2, 2:4} | 2 |
| [0,4] | {0:2, 2:4} | Remove node 2, set d[0]=4 | {0:4} | 1 |

**2.4 Increment and Loop:**

After processing all queries, we have the final path lengths.

**2.5 Return Result:**

The result is [3, 2, 1], which matches the example output. The path lengths decrease as we add shortcuts that bypass intermediate cities.

