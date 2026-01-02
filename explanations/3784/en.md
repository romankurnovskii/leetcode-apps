## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a string and a cost array, we need to find the minimum cost to delete characters so that all remaining characters are the same.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to 10^5.
- **Time Complexity:** O(n) - we iterate through the string once to find consecutive segments, where n is the string length.
- **Space Complexity:** O(1) - we only need variables to track the current segment.
- **Edge Case:** If all characters are already the same, return 0. If each character is unique, we need to keep only one (the cheapest).

**1.2 High-level approach:**

The goal is to group consecutive identical characters, and for each group, keep the character with the highest cost (delete the rest to minimize total deletion cost).

![Character deletion visualization](https://assets.leetcode.com/static_assets/others/char-deletion.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to delete characters. This is exponential.
- **Optimized Strategy:** For each group of consecutive identical characters, keep the one with maximum cost and delete the rest. This is O(n) time.
- **Optimization:** By processing consecutive segments and keeping only the maximum cost character in each segment, we minimize deletion cost efficiently.

**1.4 Decomposition:**

1. Iterate through the string to find consecutive segments of identical characters.
2. For each segment:
   - Collect all costs for characters in that segment.
   - Sort the costs.
   - Keep the maximum cost character, delete the rest (sum of all except maximum).
3. Sum the deletion costs from all segments.
4. Return the total.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "abaac"`, `cost = [1,2,3,4,5]`

- Segments: `['a'], ['b'], ['a','a'], ['c']`
- Result variable: `res = 0`

**2.2 Start Checking:**

We process each consecutive segment.

**2.3 Trace Walkthrough:**

| Step | Segment | Costs | Keep max | Delete cost | res |
| ---- | ------- | ----- | -------- | ----------- | --- |
| 1    | 'a' | [1] | 1 | 0 | 0 |
| 2    | 'b' | [2] | 2 | 0 | 0 |
| 3    | 'aa' | [3,4] | 4 | 3 | 3 |
| 4    | 'c' | [5] | 5 | 0 | 3 |

**2.4 Increment and Loop:**

After processing each segment, we add deletion costs to the total.

**2.5 Return Result:**

The result is `3`, which is the minimum cost to delete characters so all remaining are the same (keeping one 'a' with cost 4, deleting the other with cost 3).
