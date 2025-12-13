## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** Points array has up to 500 points, and queries array has up to 500 queries.
  * **Time Complexity:** O(q * p) - For each query, we check all points, where q is the number of queries and p is the number of points.
  * **Space Complexity:** O(q) - We create a result array of size q.
  * **Edge Case:** If a circle has radius 0, only points exactly at the center are inside.

**High-level approach**
For each query circle, we check all points to see if they're inside the circle. A point is inside if the distance from the point to the circle center is less than or equal to the radius.

**Brute force vs. optimized strategy**

  * **Brute Force:** For each query, check all points - this is O(q * p) which is acceptable for the given constraints.
  * **Optimized Strategy:** We could use spatial data structures, but for the given constraints, the brute force approach is simple and efficient.

**Decomposition**

1.  **Process Each Query:** For each circle query, extract center coordinates and radius.
2.  **Check Each Point:** For each point, calculate distance to circle center.
3.  **Check Inclusion:** If distance squared <= radius squared, the point is inside.
4.  **Count Points:** Count how many points are inside each circle.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `points = [[1,3], [3,3], [5,3], [2,2]]` and `queries = [[2,3,1], [4,3,1], [1,1,2]]`.
    We create `res = []`.

2.  **Start Processing:**
    We iterate through each query.

3.  **Trace Walkthrough:**
    
    | Query | Center | Radius | Point | Distance² | Inside? | Count |
    |-------|--------|--------|-------|-----------|---------|-------|
    | [2,3,1] | (2,3) | 1 | [1,3] | (1-2)²+(3-3)²=1 | Yes | 1 |
    | | | | [3,3] | (3-2)²+(3-3)²=1 | Yes | 2 |
    | | | | [5,3] | (5-2)²+(3-3)²=9 | No | 2 |
    | | | | [2,2] | (2-2)²+(2-3)²=1 | Yes | 3 |
    | [4,3,1] | (4,3) | 1 | ... | ... | ... | 2 |
    | [1,1,2] | (1,1) | 2 | ... | ... | ... | 2 |

4.  **Result:**
    After processing all queries, `res = [3, 2, 2]`

5.  **Return Result:**
    Return the array `[3, 2, 2]`.

