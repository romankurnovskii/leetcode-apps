## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a list of paths where each path connects two cities (source to destination), we need to find the destination city - the city that has no outgoing path to another city.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of paths can be up to 100, and each city name can be up to 10 characters long.
- **Time Complexity:** O(n) - we iterate through all paths once to build sets, then perform a set difference operation which is O(n) where n is the number of cities.
- **Space Complexity:** O(n) - we store all source cities and destination cities in sets.
- **Edge Case:** If there's only one path, the destination is simply the second city in that path.

**1.2 High-level approach:**

The goal is to identify which city appears only as a destination (right side) but never as a source (left side). This city has no outgoing paths and is therefore the final destination.

![City path visualization](https://assets.leetcode.com/static_assets/others/city-paths.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each destination city, check if it appears as a source in any path. This requires nested loops and is O(n²) where n is the number of paths.
- **Optimized Strategy:** Use set operations to find the difference between destination cities and source cities. This is O(n) time.
- **Optimization:** By using sets, we can efficiently find the city that exists only in destinations but not in sources using a single set difference operation.

**1.4 Decomposition:**

1. Extract all source cities (left side of each path) into a set.
2. Extract all destination cities (right side of each path) into a set.
3. Find the difference between destination cities and source cities.
4. The result is the city that appears only as a destination.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`

- Source cities: `A = {"London", "New York", "Lima"}`
- Destination cities: `B = {"New York", "Lima", "Sao Paulo"}`
- Result variable: `res = ""`

**2.2 Start Checking:**

We compute the set difference: `B - A = {"Sao Paulo"}`

**2.3 Trace Walkthrough:**

| Step | Source Set (A) | Destination Set (B) | B - A | Action |
| ---- | -------------- | ------------------ | ----- | ------ |
| 1    | {"London", "New York", "Lima"} | {"New York", "Lima", "Sao Paulo"} | {"Sao Paulo"} | Extract the only city from the difference |

**2.4 Increment and Loop:**

No loop needed - the set difference operation directly gives us the answer.

**2.5 Return Result:**

The result is `"Sao Paulo"`, which is the city that has no outgoing path.

