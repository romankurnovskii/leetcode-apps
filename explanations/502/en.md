## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= k <= 10^5`, `1 <= n <= 10^5`.
- **Time Complexity:** O(n log n + k log n) - sort projects, then k heap operations.
- **Space Complexity:** O(n) - heap and sorted projects.
- **Edge Case:** All projects require more capital than available.

**1.2 High-level approach:**
The goal is to maximize capital by selecting at most k projects. We sort projects by capital, use a max-heap for profits of affordable projects, and greedily select the most profitable one each time.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all combinations - exponential time.
- **Optimized Strategy:** Greedy with heap - O(n log n + k log n) time.

**1.4 Decomposition:**
1. Sort projects by capital requirement.
2. For each of k iterations:
   - Add all affordable projects to max-heap.
   - Select project with maximum profit.
   - Add profit to capital.
3. Return final capital.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `k = 2`, `w = 0`, `profits = [1,2,3]`, `capital = [0,1,1]`.
Sort: [(0,1), (1,2), (1,3)].

**2.2 Start Checking:**
We iterate k times, selecting most profitable affordable project.

**2.3 Trace Walkthrough:**

| Iteration | Capital | Affordable | Heap | Select | New Capital |
|-----------|---------|------------|------|--------|-------------|
| 1 | 0 | [(0,1)] | [1] | 1 | 1 |
| 2 | 1 | [(1,2),(1,3)] | [3,2] | 3 | 4 |

**2.4 Increment and Loop:**
After each selection, we update capital and continue.

**2.5 Return Result:**
Return `res = 4`, the maximized capital.

