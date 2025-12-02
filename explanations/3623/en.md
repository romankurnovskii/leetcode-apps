## Explanation

### Strategy

Let's restate the problem:
- We are given a set of points on a 2D plane.
- We want to count the number of ways to pick 4 distinct points that form a convex quadrilateral with at least one pair of horizontal sides (i.e., two sides parallel to the x-axis).

**Type:** Geometry, Combinatorics, Hash Map

**What is being asked?**
- Count the number of unique horizontal trapezoids (convex quadrilaterals with at least one pair of horizontal sides) that can be formed from the given points.

**What is given?**
- A list of points, all distinct.

**Constraints/Edge Cases:**
- Large input size (up to 10^5 points).
- All points are distinct.

**Why is the naive approach too slow?**
- The naive approach groups points by y-coordinate, then for every pair of y-levels, multiplies the number of ways to pick 2 points from each. This is O(K^2) where K is the number of y-levels with at least 2 points. For large K, this is too slow and leads to TLE.

**Optimized Plan:**
- Instead of iterating over all pairs, use the mathematical identity:
  - The total number of unordered pairs of y-levels is C(K,2).
  - If we precompute the number of ways to pick 2 points from each y-level (call this list `pairs`), then the sum over all pairs is:
    - sum_{i<j} pairs[i] * pairs[j] = (total_sum^2 - sum_of_squares) // 2
  - Where total_sum = sum(pairs), sum_of_squares = sum(x*x for x in pairs).
- This reduces the time complexity to O(N + K), which is efficient for large inputs.

### Steps

1. **Group points by y-coordinate:**
   - Use a hash map to group all points with the same y.
2. **For each group, count the number of ways to pick 2 points:**
   - For a group of size c, the number of ways to pick 2 points is C(c, 2) = c * (c-1) // 2.
   - Only consider groups with at least 2 points.
3. **Sum up all C(c,2) values:**
   - Let `pairs` be the list of C(c,2) for each y-level with at least 2 points.
4. **Compute the total number of trapezoids:**
   - Use the formula: res = (total_sum^2 - sum_of_squares) // 2
   - Return res modulo 10^9 + 7.

> **Note:**
> - We only consider y-levels with at least 2 points.
> - The order of y-levels does not matter (unordered pairs).
> - This approach avoids the O(K^2) double loop and is much faster.

#### Example Walkthrough
Suppose points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
- y=0: [1,0], [2,0], [3,0] (3 points)
- y=2: [2,2], [3,2] (2 points)
- C(3,2) = 3, C(2,2) = 1
- pairs = [3, 1]
- total_sum = 4, sum_of_squares = 9 + 1 = 10
- res = (4*4 - 10) // 2 = (16 - 10) // 2 = 3

### Complexity Analysis
- **Time Complexity:** O(N + K), where N is the number of points and K is the number of y-levels with at least 2 points.
- **Space Complexity:** O(N) for storing the groups.

```text
| Step | Operation         | Count |
| ---- | ----------------- | ----- |
| 1    | Group points by y | N     |
| 2    | Compute C(c,2)    | K     |
| 3    | Math formula      | K     |
```
