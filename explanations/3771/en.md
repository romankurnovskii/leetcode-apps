## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to calculate the total score across all starting rooms. For each starting room i, we calculate score(i) which is the number of points earned when starting from room i and going through rooms i, i+1, ..., n. We earn a point for room j if remaining HP after damage[j] is at least requirement[j].

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 10^5`, `1 <= hp <= 10^9`
- **Time Complexity:** O(n²) for the straightforward approach, can be optimized with prefix sums
- **Space Complexity:** O(n) for prefix sums
- **Edge Case:** If damage is very large, HP may become negative quickly

**1.2 High-level approach:**
For each starting position, simulate the journey through remaining rooms, tracking HP and counting points when HP >= requirement after taking damage.

![Dungeon simulation visualization](https://assets.leetcode.com/static_assets/others/dungeon-simulation.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each starting position, simulate the entire journey, which is O(n²)
- **Optimized Strategy:** Use prefix sums to quickly calculate cumulative damage, but still need to check each room, achieving O(n²) in worst case
- **Emphasize the optimization:** Prefix sums help but we still need to check each room's requirement

**1.4 Decomposition:**
1. For each starting room i from 0 to n-1
2. Initialize HP and score counter
3. For each room j from i to n-1, subtract damage[j] from HP
4. If HP >= requirement[j], increment score
5. Add score to total result

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `hp = 11`, `damage = [3,6,7]`, `requirement = [4,2,5]`
- We need to calculate score(0), score(1), score(2)

**2.2 Start Processing:**
We iterate through each starting position.

**2.3 Trace Walkthrough:**

| Start | Room | HP Before | Damage | HP After | Requirement | Point? | Score |
|-------|------|------------|--------|----------|-------------|--------|-------|
| 0 | 0 | 11 | 3 | 8 | 4 | Yes | 1 |
| 0 | 1 | 8 | 6 | 2 | 2 | Yes | 2 |
| 0 | 2 | 2 | 7 | -5 | 5 | No | 2 |
| 1 | 1 | 11 | 6 | 5 | 2 | Yes | 1 |
| 1 | 2 | 5 | 7 | -2 | 5 | No | 1 |
| 2 | 2 | 11 | 7 | 4 | 5 | No | 0 |

**2.4 Increment and Loop:**
After processing all starting positions, we sum the scores.

**2.5 Return Result:**
Total score = score(0) + score(1) + score(2) = 2 + 1 + 0 = 3, which is the result.
