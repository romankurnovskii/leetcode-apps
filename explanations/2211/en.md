## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The input string `directions` has length up to 10^5, containing only 'L', 'R', or 'S' characters.
- **Time Complexity:** O(n) where n is the length of the string. We process each character once.
- **Space Complexity:** O(n) for the string manipulation, though we could optimize to O(1) with a two-pass approach.
- **Edge Case:** If all cars are moving in the same direction (all L's or all R's) or if leading L's and trailing R's are removed leaving an empty string, there are no collisions.

**1.2 High-level approach:**
The goal is to count all collisions that will occur. The key insight is that cars moving left at the beginning and cars moving right at the end will never collide because they're moving away from the center. Only cars in the middle section (after removing leading L's and trailing R's) will eventually collide.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Simulate each collision step by step, tracking positions and directions. This would be O(n^2) in worst case as each collision might trigger a chain reaction.
- **Optimized Strategy:** Remove leading L's (moving left, escaping) and trailing R's (moving right, escaping). Count all non-stationary cars in the remaining middle section. Each will eventually collide. This is O(n) time.
- **Why optimized is better:** We avoid simulation and directly count collisions by recognizing that only the middle section matters.

**1.4 Decomposition:**
1. Remove all leading 'L' characters (cars moving left that escape without collision).
2. Remove all trailing 'R' characters (cars moving right that escape without collision).
3. In the remaining middle section, count all non-stationary cars ('L' and 'R').
4. Each non-stationary car in the middle will eventually collide, contributing 1 to the collision count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `directions = "RLRSLL"`

After removing leading L's: `"RLRSLL"` (no leading L's to remove)
After removing trailing R's: `"RLRSLL"` (no trailing R's to remove)

**2.2 Start Checking:**
Initialize `res = 0`. The string after trimming is `"RLRSLL"`.

**2.3 Trace Walkthrough:**

| Position | Character | Is Stationary? | Action |
|----------|-----------|----------------|--------|
| 0 | R | No | Will collide, add 1 |
| 1 | L | No | Will collide, add 1 |
| 2 | R | No | Will collide, add 1 |
| 3 | S | Yes | Stationary, skip |
| 4 | L | No | Will collide, add 1 |
| 5 | L | No | Will collide, add 1 |

**2.4 Increment and Loop:**
We iterate through each character in the trimmed string. For each non-stationary car ('R' or 'L'), we increment the result by 1.

**2.5 Return Result:**
After processing all characters, `res = 5`. This matches the expected output: 5 collisions will occur.

