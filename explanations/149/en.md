## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 300$ points. Each point has coordinates in the range $[-10^4, 10^4]$. All points are unique.
- **Time Complexity:** $O(n^2)$ where $n$ is the number of points. For each point, we check all other points to calculate slopes.
- **Space Complexity:** $O(n)$ for the slope count dictionary.
- **Edge Case:** If there are 1 or 2 points, return the number of points (all points are on the same line).

**1.2 High-level approach:**

The goal is to find the maximum number of points that lie on the same straight line. For each point, we calculate the slope to all other points and count how many points share the same slope. We use the greatest common divisor (GCD) to normalize slopes and avoid floating-point precision issues.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each pair of points, calculate the line equation and count how many points lie on that line. This is $O(n^3)$ time.
- **Optimized Strategy:** For each point, calculate slopes to all other points and count occurrences of each slope. This is $O(n^2)$ time.
- **Why optimized is better:** The optimized approach reduces time complexity from $O(n^3)$ to $O(n^2)$ by grouping points by slope.

**1.4 Decomposition:**

1. For each point $i$, calculate the slope to every other point $j > i$.
2. Normalize slopes using GCD to handle equivalent slopes (e.g., 1/2 = 2/4).
3. Count how many points share the same slope with point $i$.
4. Track the maximum count across all starting points.
5. Return the maximum count plus 1 (the starting point itself).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `points = [[1,1],[2,2],[3,3]]`

We initialize `res = 0` to track the maximum points on a line.

**2.2 Start Checking:**

For each point, we calculate slopes to all other points and count occurrences.

**2.3 Trace Walkthrough:**

**Starting from point [1,1]:**

| Point j | Slope Calculation | Normalized Slope | Count |
|---------|-------------------|------------------|-------|
| [2,2] | (2-1, 2-1) = (1,1) | (1,1) | 1 |
| [3,3] | (3-1, 3-1) = (2,2) → GCD=2 → (1,1) | (1,1) | 2 |

Total points on line with slope (1,1): 2 + 1 (starting point) = 3

**Starting from point [2,2]:**

| Point j | Slope Calculation | Normalized Slope | Count |
|---------|-------------------|------------------|-------|
| [3,3] | (3-2, 3-2) = (1,1) | (1,1) | 1 |

Total points on line: 1 + 1 = 2

**2.4 Increment and Loop:**

For each point $i$:
- Initialize `slope_count = {}` and `same_point = 1`.
- For each point $j > i$:
  - If points are identical, increment `same_point`.
  - Otherwise, calculate slope `(dx, dy)` and normalize using GCD.
  - Increment count for that slope.
- Update `res = max(res, same_point + max(slope_count.values()))`.

**2.5 Return Result:**

The maximum is 3 (all three points lie on the same line with slope 1). We return `3`.

