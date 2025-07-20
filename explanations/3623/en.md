## 3623. Count Number of Trapezoids I [Medium]

https://leetcode.com/problems/count-number-of-trapezoids-i

## Description
You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `i`-th point on the Cartesian plane.

A **horizontal trapezoid** is a convex quadrilateral with **at least one pair** of horizontal sides (i.e., parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique **horizontal trapezoids** that can be formed by choosing any four distinct points from `points`.

Since the answer may be very large, return it **modulo** 10^9 + 7.

**Examples**

**Example 1:**

Input:
points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:
There are three distinct ways to pick four points that form a horizontal trapezoid:
- Using points [1,0], [2,0], [3,2], and [2,2].
- Using points [2,0], [3,0], [3,2], and [2,2].
- Using points [1,0], [3,0], [3,2], and [2,2].

![Trapezoid 1](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-6.png)
![Trapezoid 2](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-7.png)
![Trapezoid 3](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-8.png)

**Example 2:**

Input:
points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:
There is only one horizontal trapezoid that can be formed.

![Trapezoid Example 2](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png)

**Constraints**

```text
4 <= points.length <= 10^5
-10^8 <= x_i, y_i <= 10^8
All points are pairwise distinct.
```

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

**High-Level Plan:**
- For a line to be horizontal, all its points must share the same y-coordinate.
- Group the points by their y-coordinate.
- To form a horizontal trapezoid, pick two different y-levels (horizontal lines), and from each, pick two points (to form the two horizontal sides).
- The number of trapezoids is the sum over all pairs of y-levels of (ways to pick 2 points from the first level) * (ways to pick 2 points from the second level).

### Steps

1. **Group points by y-coordinate:**
   - Use a hash map to group all points with the same y.
2. **For each group, count the number of ways to pick 2 points:**
   - For a group of size c, the number of ways to pick 2 points is C(c, 2) = c * (c-1) // 2.
3. **For all pairs of y-levels, multiply their C(c,2) values:**
   - For each pair of y-levels (y1, y2), the number of trapezoids is C(c1,2) * C(c2,2).
   - Sum this over all unordered pairs of y-levels.
4. **Return the total modulo 10^9 + 7.**

> **Note:**
> - We only consider pairs of y-levels with at least 2 points each.
> - The order of y-levels does not matter (unordered pairs).

#### Example Walkthrough
Suppose points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
- y=0: [1,0], [2,0], [3,0] (3 points)
- y=2: [2,2], [3,2] (2 points)
- C(3,2) = 3, C(2,2) = 1
- Number of trapezoids: 3 * 1 = 3

### Complexity Analysis
- **Time Complexity:** O(N + K^2), where N is the number of points and K is the number of y-levels with at least 2 points. In practice, K is much smaller than N.
- **Space Complexity:** O(N) for storing the groups.

| Step | Operation         | Count |
| ---- | ----------------- | ----- |
| 1    | Group points by y | N     |
| 2    | Compute C(c,2)    | K     |
| 3    | Pairwise multiply | K^2   |

For each step, the dominant cost is the pairwise multiplication for y-levels with at least 2 points. 