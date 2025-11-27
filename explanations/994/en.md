## Explanation

### Strategy (The "Why")

Given a grid representing a box of oranges where `0` = empty cell, `1` = fresh orange, and `2` = rotten orange, we need to find the minimum number of minutes until no fresh oranges remain. Each minute, rotten oranges rot their 4-directionally adjacent fresh oranges.

**1.1 Constraints & Complexity:**

- **Input Size:** The grid dimensions $m \times n$ can be up to $10 \times 10$.
- **Value Range:** Grid values are 0, 1, or 2.
- **Time Complexity:** $O(m \times n)$ - We visit each cell at most once during BFS.
- **Space Complexity:** $O(m \times n)$ - In the worst case, the queue can contain all cells if all are rotten initially.
- **Edge Case:** If there are no fresh oranges initially, return 0. If there are fresh oranges that cannot be reached by any rotten orange, return -1.

**1.2 High-level approach:**

The goal is to find the minimum time for all fresh oranges to rot.

![Rotting Oranges](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

We use BFS (breadth-first search) starting from all rotten oranges simultaneously. Each level of BFS represents one minute. We track the maximum time needed.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Simulate the rotting process minute by minute, checking all cells each minute. This is inefficient and harder to implement.
- **Optimized Strategy (BFS):** Use BFS to process all oranges that rot at the same time (same level) together. This naturally gives us the time in minutes.
- **Why it's better:** BFS processes all oranges that rot in the same minute together, making it easy to track time. It's also more efficient and cleaner to implement.

**1.4 Decomposition:**

1. Count fresh oranges and add all rotten oranges to a queue with time 0.
2. If there are no fresh oranges, return 0.
3. Use BFS: for each rotten orange, check its 4 neighbors.
4. If a neighbor is fresh, rot it, decrement fresh count, and add it to the queue with time + 1.
5. Track the maximum time seen.
6. After BFS, if there are still fresh oranges, return -1; otherwise, return the maximum time.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $grid = [[2,1,1],[1,1,0],[0,1,1]]$

The grid:
```
2 1 1
1 1 0
0 1 1
```

We initialize:
- `fresh_count = 5` (five fresh oranges)
- `queue = [(0,0,0), ...]` (rotten orange at (0,0) with time 0)
- `max_time = 0`

**2.2 Start BFS:**

We begin BFS from all rotten oranges.

**2.3 Trace Walkthrough:**

| Minute | Queue State | Fresh Count | Action |
|--------|-------------|-------------|--------|
| 0 | $[(0,0,0)]$ | 5 | Process (0,0) |
| 1 | $[(0,1,1), (1,0,1)]$ | 3 | Rot (0,1) and (1,0) |
| 2 | $[(0,2,2), (1,1,2)]$ | 1 | Rot (0,2) and (1,1) |
| 3 | $[(2,1,3)]$ | 0 | Rot (2,1) |

Detailed steps:
- **Minute 0:** Rotten orange at (0,0) rots neighbors (0,1) and (1,0)
- **Minute 1:** Rotten oranges at (0,1) and (1,0) rot neighbors (0,2) and (1,1)
- **Minute 2:** Rotten oranges at (0,2) and (1,1) rot neighbor (2,1)
- **Minute 3:** All fresh oranges are now rotten

**2.4 Final State:**

After 3 minutes:
```
2 2 2
2 2 0
0 2 2
```

All fresh oranges are rotten.

**2.5 Return Result:**

We return `max_time = 3`, which is the minimum number of minutes needed.

> **Note:** BFS is perfect for this problem because it naturally processes all oranges that rot at the same time together. The time for each orange is the BFS level, which we track as we add oranges to the queue.

