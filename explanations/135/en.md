## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 2 \times 10^4$ children. Ratings are in the range $[0, 2 \times 10^4]$.
- **Time Complexity:** $O(n)$ where $n$ is the number of children. We make two passes through the array.
- **Space Complexity:** $O(n)$ for the result array storing candy counts.
- **Edge Case:** If all children have the same rating, each gets 1 candy, total is $n$.

**1.2 High-level approach:**

The goal is to minimize the total number of candies while satisfying: (1) each child gets at least 1 candy, (2) children with higher ratings get more candies than neighbors. We use a two-pass greedy approach: first ensure left-to-right constraints, then right-to-left constraints.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible candy distributions and find the minimum. This is exponential time.
- **Optimized Strategy:** Two-pass greedy: first pass ensures left neighbors are satisfied, second pass ensures right neighbors are satisfied. This is $O(n)$ time.
- **Why optimized is better:** The two-pass approach guarantees optimal solution by independently handling left and right constraints.

**1.4 Decomposition:**

1. Initialize all children with 1 candy.
2. Left to right pass: if `ratings[i] > ratings[i-1]`, give `res[i] = res[i-1] + 1`.
3. Right to left pass: if `ratings[i] > ratings[i+1]`, give `res[i] = max(res[i], res[i+1] + 1)`.
4. Sum all candies in the result array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `ratings = [1,0,2]`

We initialize `res = [1, 1, 1]` (each child starts with 1 candy).

**2.2 Start Checking:**

We perform two passes: first left-to-right, then right-to-left.

**2.3 Trace Walkthrough:**

**Left-to-right pass:**

| Index | ratings[i] | ratings[i-1] | Comparison | res before | res after |
|-------|------------|---------------|------------|-------------|-----------|
| 0 | 1 | - | - | [1,1,1] | [1,1,1] |
| 1 | 0 | 1 | 0 < 1 | [1,1,1] | [1,1,1] |
| 2 | 2 | 0 | 2 > 0 | [1,1,1] | [1,1,2] |

**Right-to-left pass:**

| Index | ratings[i] | ratings[i+1] | Comparison | res before | res after |
|-------|------------|---------------|------------|-------------|-----------|
| 2 | 2 | - | - | [1,1,2] | [1,1,2] |
| 1 | 0 | 2 | 0 < 2 | [1,1,2] | [1,1,2] |
| 0 | 1 | 0 | 1 > 0 | [1,1,2] | [2,1,2] |

**2.4 Increment and Loop:**

- Left-to-right: `for i in range(1, n)`: if `ratings[i] > ratings[i-1]`, set `res[i] = res[i-1] + 1`.
- Right-to-left: `for i in range(n-2, -1, -1)`: if `ratings[i] > ratings[i+1]`, set `res[i] = max(res[i], res[i+1] + 1)`.

**2.5 Return Result:**

After both passes, `res = [2, 1, 2]`. The sum is $2 + 1 + 2 = 5$, which is returned.

