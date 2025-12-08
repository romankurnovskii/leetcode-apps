## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count the number of square triples (a, b, c) where a² + b² = c² and all three numbers are between 1 and n.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 250`
- **Time Complexity:** O(n²) where n is the input value, as we iterate over all pairs (a, b)
- **Space Complexity:** O(1) as we only use a counter variable
- **Edge Case:** When n = 1, there are no valid triples since we need at least 3 numbers

**1.2 High-level approach:**
We iterate through all possible pairs (a, b), calculate c² = a² + b², and check if the square root of c² is an integer and within the range [1, n].

![Pythagorean triple visualization](https://assets.leetcode.com/static_assets/others/pythagorean-triple.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all combinations of (a, b, c) and check if a² + b² = c², which would be O(n³)
- **Optimized Strategy:** For each pair (a, b), calculate c and verify it's a perfect square, achieving O(n²) time
- **Emphasize the optimization:** By calculating c from a and b, we eliminate the need to iterate over c, reducing complexity from O(n³) to O(n²)

**1.4 Decomposition:**
1. Initialize a counter to zero
2. Iterate through all possible values of a from 1 to n
3. For each a, iterate through all possible values of b from 1 to n
4. Calculate c² = a² + b² and find c as the integer square root
5. Verify that c is a perfect square (c * c == c²) and within range [1, n]
6. Increment the counter for each valid triple

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `n = 5`
- Initialize counter: `res = 0`

**2.2 Start Checking:**
We iterate through all pairs (a, b).

**2.3 Trace Walkthrough:**

| a | b | a² | b² | c² | c | c*c == c²? | 1 <= c <= 5? | Count |
|---|---|----|----|----|---|------------|---------------|-------|
| 3 | 4 | 9 | 16 | 25 | 5 | Yes | Yes | 1 |
| 4 | 3 | 16 | 9 | 25 | 5 | Yes | Yes | 2 |

**2.4 Increment and Loop:**
After checking all pairs, we continue to the result.

**2.5 Return Result:**
The result is 2, representing the two valid triples: (3, 4, 5) and (4, 3, 5).
