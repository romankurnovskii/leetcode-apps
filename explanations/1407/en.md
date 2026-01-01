## Explanation

### Strategy (The "Why")

**Restate the problem:** Given two database tables (Users and Rides), we need to find the total distance traveled by each user and return them ordered by distance (descending) and name (ascending).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of users and rides can be up to 10^4 each.
- **Time Complexity:** O(n log n) - we need to group and sort the results, where n is the number of rides.
- **Space Complexity:** O(n) - we need to store the grouped results.
- **Edge Case:** If a user has no rides, their total distance should be 0. Users with the same distance should be ordered alphabetically.

**1.2 High-level approach:**

The goal is to join the Users and Rides tables, group by user, sum the distances, and order the results appropriately.

![SQL aggregation visualization](https://assets.leetcode.com/static_assets/others/sql-aggregation.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Process each user separately and calculate their total distance. This is inefficient.
- **Optimized Strategy:** Use SQL's GROUP BY and aggregation functions to efficiently calculate totals for all users at once. This leverages database optimization.
- **Optimization:** By using SQL aggregation, we let the database engine optimize the grouping and sorting operations.

**1.4 Decomposition:**

1. Join the Users table with the Rides table on user ID.
2. Group the results by user ID and name.
3. Sum the distances for each user (using COALESCE to handle users with no rides).
4. Order the results by total distance (descending) and name (ascending).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use a simple example:
- Users: `[(1, "Alice"), (2, "Bob")]`
- Rides: `[(1, 10), (1, 20), (2, 5)]`

**2.2 Start Checking:**

We execute the SQL query to join and aggregate.

**2.3 Trace Walkthrough:**

| Step | Operation | Result |
| ---- | --------- | ------ |
| 1    | LEFT JOIN | All users with their rides |
| 2    | GROUP BY | Group by user |
| 3    | SUM | Alice: 30, Bob: 5 |
| 4    | ORDER BY | Alice (30), Bob (5) |

**2.4 Increment and Loop:**

SQL handles the iteration internally through the GROUP BY and aggregation.

**2.5 Return Result:**

The result is a table with users ordered by total distance: `[("Alice", 30), ("Bob", 5)]`.

