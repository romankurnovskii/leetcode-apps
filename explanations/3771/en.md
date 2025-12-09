## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to calculate the total score across all starting rooms. For each starting room i, we calculate score(i) which is the number of points earned when starting from room i and going through rooms i, i+1, ..., n. We earn a point for room j if remaining HP after damage[j] is at least requirement[j].

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 10^5`, `1 <= hp <= 10^9`
- **Time Complexity:** O(n log n) using prefix sums and binary search - for each room j, we use binary search to count valid starting positions
- **Space Complexity:** O(n) for prefix sums
- **Edge Case:** If damage is very large, HP may become negative quickly

**1.2 High-level approach:**
We reverse the approach: instead of checking each starting position, for each room j we count how many starting positions i <= j would result in earning a point at room j. We use prefix sums and binary search to efficiently count valid starting positions.

![Dungeon simulation visualization](https://assets.leetcode.com/static_assets/others/dungeon-simulation.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each starting position, simulate the entire journey, which is O(n²)
- **Optimized Strategy:** For each room j, use binary search on prefix sums to count valid starting positions i where prefix[i] >= threshold, achieving O(n log n)
- **Emphasize the optimization:** Binary search on non-decreasing prefix array allows O(log n) counting per room instead of O(n) linear scan

**1.4 Decomposition:**
1. Compute prefix sums for damage array
2. For each room j, calculate threshold = requirement[j] - hp + prefix[j+1]
3. Use binary search to find first index i where prefix[i] >= threshold
4. Count all starting positions from that index to j (all satisfy the condition)
5. Sum counts across all rooms to get total score

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `hp = 11`, `damage = [3,6,7]`, `requirement = [4,2,5]`
- Compute prefix sums: `prefix = [0, 3, 9, 16]`
- For each room j, we'll count valid starting positions i <= j

**2.2 Start Processing:**
We iterate through each room j and use binary search to count valid starting positions.

**2.3 Trace Walkthrough:**

| j | requirement[j] | threshold | Binary Search Result | Valid i Count | res |
|---|----------------|-----------|---------------------|---------------|-----|
| 0 | 4 | 4 - 11 + 3 = -4 | prefix[0]=0 >= -4, idx=0 | j+1 - 0 = 1 | 1 |
| 1 | 2 | 2 - 11 + 9 = 0 | prefix[0]=0 >= 0, idx=0 | j+1 - 0 = 2 | 3 |
| 2 | 5 | 5 - 11 + 16 = 10 | prefix[2]=9 < 10, prefix[3]=16 >= 10, idx=3 | j+1 - 3 = 0 | 3 |

**2.4 Increment and Loop:**
For each room j, we calculate threshold, use binary search to find the first valid starting position, and count all valid positions from that index to j.

**2.5 Return Result:**
After processing all rooms, total score = 3, which matches the expected result.
