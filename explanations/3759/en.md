## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to convert string `source` to `target` with minimum cost. We can change characters using given conversion rules, and we can use intermediate characters to reduce cost.

**1.1 Constraints & Complexity:**
- Input size: `1 <= source.length == target.length <= 10^5`, `1 <= cost.length <= 2000`
- **Time Complexity:** O(26³ + n) = O(n) where n is string length, as Floyd-Warshall on 26 nodes is constant
- **Space Complexity:** O(26²) = O(1) for the distance matrix
- **Edge Case:** If source[i] == target[i], no conversion needed for that position

**1.2 High-level approach:**
We model character conversions as a graph where edges represent direct conversions with costs. We use Floyd-Warshall to find shortest paths between all character pairs, then sum up the minimum costs for each position.

![Graph shortest path visualization](https://assets.leetcode.com/static_assets/others/graph-shortest-path.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible conversion sequences, which is exponential.
- **Optimized Strategy:** Use Floyd-Warshall to precompute shortest paths between all character pairs in O(26³) time, then use these in O(n) time to compute total cost.

**1.4 Decomposition:**
1. Build a graph with 26 nodes (characters) and edges from conversion rules
2. Use Floyd-Warshall algorithm to find shortest paths between all pairs
3. For each position, if characters differ, use the shortest path cost
4. Return total cost, or -1 if any conversion is impossible

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `source = "abcd"`, `target = "acbe"`, `original = ["a","b","c","c","e","d"]`, `changed = ["b","c","b","e","b","e"]`, `cost = [2,5,5,1,2,20]`
- Initialize distance matrix with INF, diagonal with 0
- Add edges: a→b(2), b→c(5), c→b(5), c→e(1), e→b(2), d→e(20)

**2.2 Start Checking:**
We run Floyd-Warshall to compute shortest paths, then process each character position.

**2.3 Trace Walkthrough:**
After Floyd-Warshall, key shortest paths:
- a→c: a→b(2) + b→c(5) = 7, or a→b(2) + b→c(5) = 7
- b→e: b→c(5) + c→e(1) = 6
- d→e: d→e(20) = 20

Processing `source = "abcd"` to `target = "acbe"`:

| Index | source[i] | target[i] | Same? | Conversion | Cost | Total |
|-------|-----------|-----------|-------|------------|------|-------|
| 0 | 'a' | 'a' | Yes | None | 0 | 0 |
| 1 | 'b' | 'c' | No | b→c | 5 | 5 |
| 2 | 'c' | 'b' | No | c→b | 5 | 10 |
| 3 | 'd' | 'e' | No | d→e | 20 | 30 |

Wait, let's recalculate: b→c costs 5, c→b costs 5, but we can also do c→e(1) then e→b(2) = 3, which is better. So c→b = 3.

**2.4 Increment and Loop:**
For each position, we look up the shortest path cost in our precomputed matrix and add it to the total.

**2.5 Return Result:**
The total cost is 0 + 5 + 3 + 20 = 28, which is the minimum cost to convert "abcd" to "acbe".
