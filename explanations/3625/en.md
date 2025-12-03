## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The array $points$ has length $4 \leq n \leq 500$, with coordinates in $[-1000, 1000]$.
* **Time Complexity:** $O(n^2)$ - We process all pairs of points to build slope and midpoint mappings, then count pairs within each group.
* **Space Complexity:** $O(n^2)$ - In the worst case, we store all $O(n^2)$ line segments in the hash tables.
* **Edge Case:** If there are fewer than 4 points, no trapezoid can be formed (but constraints guarantee at least 4).

**1.2 High-level approach**

The goal is to count trapezoids formed by four distinct points. A trapezoid has at least one pair of parallel sides (same slope). We count all quadrilaterals with parallel sides, then subtract parallelograms (which have two pairs of parallel sides and would be double-counted).

![Trapezoid counting visualization showing parallel line segments forming trapezoids]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Check all combinations of 4 points ($O(n^4)$) and verify if they form a trapezoid. This is too slow for $n=500$.
* **Optimized (Hash Table Grouping):** Group line segments by slope to find parallel pairs. For each slope, count pairs of segments (trapezoid bases). Then subtract parallelograms (segments with same midpoint but different slopes). This achieves $O(n^2)$ time.

**1.4 Decomposition**

1. **Process All Pairs:** For each pair of points, calculate slope, intercept, and midpoint.
2. **Group by Slope:** Store intercepts for each slope to identify parallel segments.
3. **Count Trapezoids:** For each slope, count pairs of segments (these form trapezoid bases).
4. **Subtract Parallelograms:** For each midpoint, count pairs of segments with different slopes (these form parallelograms that were double-counted).

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]$.

We initialize:
* `slope_to_intercept = {}` (maps slope to list of intercepts)
* `mid_to_slope = {}` (maps midpoint to list of slopes)
* `res = 0`

**2.2 Start Processing**

We iterate through all pairs of points $(i, j)$ where $i < j$.

**2.3 Trace Walkthrough**

For each pair, we calculate:
- **Slope $k$:** $(y_2 - y_1) / (x_2 - x_1)$, or infinite for vertical lines
- **Intercept $b$:** $y_1 - k \cdot x_1$, or $x_1$ for vertical lines
- **Midpoint:** Encoded as $(x_1 + x_2) \times 10000 + (y_1 + y_2)$

Example for pair $[[-3,2], [2,3]]$:
- $k = (3-2)/(2-(-3)) = 1/5 = 0.2$
- $b = 2 - 0.2 \times (-3) = 2.6$
- $mid = (-3+2) \times 10000 + (2+3) = -10000 + 5 = -9995$

After processing all pairs, we have groups of segments with the same slope.

**2.4 Count Trapezoids**

For each slope group:
- Count pairs of segments with different intercepts
- Each pair forms the parallel bases of a trapezoid
- Add to result: `res += total_sum * count` for each intercept frequency

**2.5 Subtract Parallelograms**

For each midpoint group:
- Count pairs of segments with different slopes
- These form parallelograms (double-counted as trapezoids)
- Subtract from result: `res -= total_sum * count` for each slope frequency

**2.6 Return Result**

After counting trapezoids and subtracting parallelograms, `res` contains the number of unique trapezoids.

> **Note:** Parallelograms are subtracted because they have two pairs of parallel sides, so they were counted twice in the trapezoid count (once for each pair of parallel sides).

