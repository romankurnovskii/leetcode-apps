## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum area rectangle formed by 4 points that doesn't contain any other points inside or on its border. The rectangle must have edges parallel to the axes.

**1.1 Constraints & Complexity:**
- Input size: `1 <= points.length <= 10`
- **Time Complexity:** O(n⁴) in worst case where n is the number of points, as we try all combinations
- **Space Complexity:** O(1) as we only use a few variables
- **Edge Case:** If no valid rectangle exists (all rectangles contain other points), return -1

**1.2 High-level approach:**
For each pair of points that can form opposite corners of a rectangle, check if the other two corners exist. Then verify that no other points lie inside or on the border of the rectangle.

![Rectangle validation visualization](https://assets.leetcode.com/static_assets/others/geometry.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all combinations of 4 points and check validity, which is what we do
- **Optimized Strategy:** For each pair of points, determine the other two corners and check if they exist, then validate the rectangle
- **Emphasize the optimization:** By fixing two opposite corners, we can directly compute the other corners instead of trying all 4-point combinations

**1.4 Decomposition:**
1. Iterate through all pairs of points (i, j)
2. Check if they can form opposite corners (must have different x and y coordinates)
3. Calculate the other two corners: (x1, y2) and (x2, y1)
4. Verify both corners exist in the points set
5. Check that no other points lie inside or on the border of the rectangle
6. Calculate area and track the maximum

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `points = [[1,1],[1,3],[3,1],[3,3]]`
- Initialize: `res = -1`

**2.2 Start Checking:**
We try all pairs of points as opposite corners.

**2.3 Trace Walkthrough:**

| Point i | Point j | Other Corners | Exist? | Contains Others? | Area | Max |
|--------|---------|---------------|--------|------------------|------|-----|
| [1,1] | [3,3] | [1,3], [3,1] | Yes | No | 4 | 4 |

The rectangle with corners (1,1), (1,3), (3,1), (3,3) has area 4 and contains no other points.

**2.4 Increment and Loop:**
After checking all pairs, we have the maximum area.

**2.5 Return Result:**
The result is 4, which is the maximum area of a valid rectangle.
