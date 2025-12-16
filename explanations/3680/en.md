## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to generate a schedule where each team plays every other team exactly twice (home and away), with exactly one match per day, and no team plays on consecutive days.

**1.1 Constraints & Complexity:**

- **Input Size:** `2 <= n <= 50`
- **Time Complexity:** O(n²) - Generate n*(n-1) matches
- **Space Complexity:** O(n²) - Store all matches
- **Edge Case:** `n < 5` returns empty array (no valid schedule exists)

**1.2 High-level approach:**

We use a geometric approach: arrange teams in a polygon. Start with adjacent pairs (shortest edges), then progressively add longer edges. For each distance, we add matches in one direction, then reverse direction. This ensures no team plays consecutively.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all permutations of matches, check if schedule is valid. This is factorial complexity.
- **Optimized (Geometric Pattern):** Use a systematic pattern based on distances in a circular arrangement. Start with distance 1 (adjacent), then distance 2, etc. This is O(n²) time.
- **Why it's better:** The geometric pattern naturally ensures that matches are spaced out, preventing consecutive days for any team.

**1.4 Decomposition:**

1. Handle base case: `n < 5` returns empty
2. For odd `n`: Add adjacent pairs going around twice, then reverse
3. For even `n`: Add adjacent pairs in two groups, then reverse
4. For each distance `diff` from 2 to `n//2`:
   - Add matches with distance `diff` in one direction
   - Add matches with distance `diff` in reverse direction
5. For even `n`, handle special case: distance `n/2` (diametrically opposite)

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 5`

- Total matches needed: `5 * 4 = 20`
- Initialize `res = []`

**2.2 Handle Adjacent Pairs (Odd n):**

```python
if n % 2:
    for i in range(0, 2 * n, 2):
        res.append([i % n, (i + 1) % n])
    for i in range(0, 2 * n, 2):
        res.append([(i + 1) % n, i % n])
```

For `n = 5`:
- First pass: `[0,1], [2,3], [4,0], [1,2], [3,4]`
- Second pass (reverse): `[1,0], [3,2], [0,4], [2,1], [4,3]`

**2.3 Handle Longer Distances:**

```python
for diff in range(2, (n + 1) // 2):
    start = res[-1][0] + 1
    for i in range(start, start + n):
        res.append([i % n, (i + diff) % n])
    start = res[-1][-1] - 1
    for i in range(start, start + n):
        res.append([(i + diff) % n, i % n])
```

For `diff = 2`:
- Forward: `[1,3], [2,4], [3,0], [4,1], [0,2]`
- Reverse: `[2,0], [4,2], [0,4], [1,0], [3,1]`

**2.4 Handle Special Case (Even n, distance n/2):**

For even `n`, when `diff = n/2`, all matches are diametrically opposite. We add them in one pass.

**2.5 Return Result:**

Return the complete schedule with all matches.

**Time Complexity:** O(n²) - Generate n*(n-1) matches  
**Space Complexity:** O(n²) - Store all matches

