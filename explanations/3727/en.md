## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^5$ elements. Values are in the range $[-4 \times 10^4, 4 \times 10^4]$.
- **Time Complexity:** $O(n \log n)$ for sorting the array.
- **Space Complexity:** $O(n)$ for the sorted array.
- **Edge Case:** If the array has one element, return its square.

**1.2 High-level approach:**

The goal is to maximize the alternating sum of squares: $arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...$. Since squares are always positive regardless of the original sign, we want large squares at even indices (positive contribution) and small squares at odd indices (negative contribution).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible rearrangements and calculate the score. This is $O(n!)$ time.
- **Optimized Strategy:** Sort numbers by absolute value in descending order. Assign largest numbers to even indices and smallest to odd indices. This is $O(n \log n)$ time.
- **Why optimized is better:** The greedy assignment maximizes positive contributions and minimizes negative contributions, giving the optimal result.

**1.4 Decomposition:**

1. Convert all numbers to absolute values (since squares are same for positive/negative).
2. Sort in descending order.
3. Assign numbers to positions: even indices get largest numbers, odd indices get smallest numbers.
4. Calculate alternating sum of squares.
5. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1,2,3]`

We convert to absolute values and sort: `[3,2,1]`

**2.2 Start Checking:**

We assign numbers to positions and calculate the score.

**2.3 Trace Walkthrough:**

| Index | Assigned Value | Square | Contribution |
|-------|----------------|--------|--------------|
| 0 (even) | 3 | 9 | +9 |
| 1 (odd) | 2 | 4 | -4 |
| 2 (even) | 1 | 1 | +1 |
| Total | | | 9 - 4 + 1 = 6 |

Wait, let me recalculate. The problem says we can rearrange, so for [1,2,3]:
- Best arrangement: [2,1,3] gives $2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12$

Actually, we want: even positions get largest, odd get smallest.
- [3,1,2]: $3^2 - 1^2 + 2^2 = 9 - 1 + 4 = 12$ ✓

**2.4 Increment and Loop:**

- Sort by absolute value descending: `nums_sorted = sorted([abs(x) for x in nums], reverse=True)`
- Calculate: `for i in range(n): if i % 2 == 0: res += nums_sorted[i]^2 else: res -= nums_sorted[i]^2`

**2.5 Return Result:**

For `nums = [1,2,3]`, sorted by absolute value: `[3,2,1]`. Arrangement `[3,1,2]` gives score $3^2 - 1^2 + 2^2 = 9 - 1 + 4 = 12$. We return `12`.

