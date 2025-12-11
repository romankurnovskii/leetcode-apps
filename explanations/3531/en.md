## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count buildings that are "covered", meaning they have at least one building in all four directions: above (same x, smaller y), below (same x, larger y), left (same y, smaller x), and right (same y, larger x).

**1.1 Constraints & Complexity:**

* **Input Size:** n can be up to 10^5, and we can have up to 10^5 buildings.
* **Time Complexity:** O(n log n) - We group and sort buildings by x and y coordinates, then check each building once.
* **Space Complexity:** O(n) - We store buildings grouped by x and y coordinates.
* **Edge Case:** If a building is at the edge (e.g., x=1 or y=1), it cannot have buildings in all directions.

**1.2 High-level approach:**

The goal is to efficiently check for each building whether it has neighbors in all four directions. We group buildings by their x and y coordinates, then sort each group to quickly check for the existence of buildings in each direction.


**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** For each building, check all other buildings to see if any exist in each of the four directions. This is O(n^2) time.
* **Optimized (Grouping + Sorting):** Group buildings by x and y coordinates, then sort each group. For each building, check if its group has any element smaller/larger than it. This is O(n log n) time.
* **Why it's better:** By grouping and sorting, we avoid checking all pairs and can determine existence in each direction by checking the first/last element of sorted groups.

**1.4 Decomposition:**

1. Group buildings by x-coordinate and y-coordinate into separate dictionaries.
2. Sort each group (by y for x-groups, by x for y-groups).
3. For each building, check if its x-group has buildings above (smaller y) and below (larger y).
4. Check if its y-group has buildings left (smaller x) and right (larger x).
5. Count buildings that have neighbors in all four directions.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 3`, `buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]`

We initialize:
* `by_x = {1: [2], 2: [2,1,3], 3: [2]}` (grouped by x, sorted by y)
* `by_y = {1: [2], 2: [1,2,3], 3: [2]}` (grouped by y, sorted by x)
* `res = 0`

**2.2 Start Checking:**

We check each building to see if it's covered.

**2.3 Trace Walkthrough:**

| Step | Building | x-group | y-group | Above?        | Below?        | Left?         | Right?        | Covered? |
| ---- | -------- | ------- | ------- | ------------- | ------------- | ------------- | ------------- | -------- |
| 1    | [1,2]    | [2]     | [1,2,3] | No (min=2)    | No (max=2)    | No (min=1)    | Yes (max=3)   | No       |
| 2    | [2,2]    | [1,2,3] | [1,2,3] | Yes (min=1<2) | Yes (max=3>2) | Yes (min=1<2) | Yes (max=3>2) | Yes      |
| 3    | [3,2]    | [2]     | [1,2,3] | No (min=2)    | No (max=2)    | Yes (min=1<3) | No (max=3)    | No       |
| 4    | [2,1]    | [1,2,3] | [2]     | No (min=1)    | Yes (max=3>1) | No (min=2)    | No (max=2)    | No       |
| 5    | [2,3]    | [1,2,3] | [2]     | Yes (min=1<3) | No (max=3)    | No (min=2)    | No (max=2)    | No       |

At step 2, building [2,2] is covered because it has buildings in all four directions.

**2.4 Increment and Loop:**

For each building, we check its groups to determine if it has neighbors in all directions.

**2.5 Return Result:**

After checking all buildings, we return `res = 1`, representing the number of covered buildings.
