## Explanation

### Strategy (The "Why")

Given an array of balloon coordinates where `points[i] = [x_start, x_end]`, we need to find the minimum number of arrows needed to burst all balloons. An arrow shot at position $x$ will burst all balloons whose coordinates include $x$.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of balloons $N$ can be up to $10^5$.
- **Value Range:** Coordinates can be between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(n \log n)$ - We sort the balloons by end coordinate, which takes $O(n \log n)$ time. Then we iterate through the sorted balloons once in $O(n)$ time.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables. The sorting is done in-place (or uses $O(\log n)$ space for the sort algorithm).
- **Edge Case:** If there are no balloons, we return 0. If all balloons overlap at a single point, we return 1.

**1.2 High-level approach:**

The goal is to find the minimum number of arrows needed to burst all balloons.

![Balloons and Arrows](https://assets.leetcode.com/uploads/2021/07/13/balloons.jpg)

This is similar to the interval scheduling problem. The key insight is to use a greedy approach: sort balloons by their end coordinate, and always shoot an arrow at the end of the first balloon that hasn't been burst yet. This maximizes the number of balloons each arrow can burst.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible positions to shoot arrows, check which combinations burst all balloons, and find the minimum number of arrows needed. This would be exponential time.
- **Optimized Strategy (Greedy):** Sort balloons by end coordinate. Iterate through them, and whenever we encounter a balloon that isn't burst by the last arrow, shoot a new arrow at its end coordinate. This greedy choice is optimal.
- **Why it's better:** The greedy approach reduces the problem to $O(n \log n)$ time. By always shooting at the end of the first unburst balloon, we ensure that this arrow bursts as many overlapping balloons as possible.

**1.4 Decomposition:**

1. Sort all balloons by their end coordinate (ascending order).
2. Initialize a counter for arrows needed and track the position of the last arrow shot.
3. Iterate through the sorted balloons.
4. For each balloon, check if it's already burst by the last arrow (if its start is less than or equal to the last arrow position).
5. If the balloon is not burst, shoot a new arrow at its end coordinate and increment the counter.
6. Return the total number of arrows needed.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $points = [[10,16],[2,8],[1,6],[7,12]]$

First, we sort balloons by end coordinate:
- Sorted: $[[1,6], [2,8], [7,12], [10,16]]$
  - $[1,6]$ ends at 6
  - $[2,8]$ ends at 8
  - $[7,12]$ ends at 12
  - $[10,16]$ ends at 16

We initialize:
- `res = 0` (count of arrows needed)
- `last_arrow = -\infty` (position of last arrow shot)

**2.2 Start Checking:**

We begin with the first balloon $[1,6]$.

**2.3 Trace Walkthrough:**

| Balloon | Start | End | Last Arrow | Burst? | Action | Res | Last Arrow After |
|---------|-------|-----|------------|--------|--------|-----|------------------|
| $[1,6]$ | 1 | 6 | $-\infty$ | No ($1 > -\infty$) | Shoot at 6 | 1 | 6 |
| $[2,8]$ | 2 | 8 | 6 | No ($2 > 6$) | Shoot at 8 | 2 | 8 |
| $[7,12]$ | 7 | 12 | 8 | No ($7 > 8$) | Shoot at 12 | 3 | 12 |
| $[10,16]$ | 10 | 16 | 12 | No ($10 > 12$) | Shoot at 16 | 4 | 16 |

Wait, let me reconsider. Actually, if we shoot at 6, it will burst $[1,6]$ and $[2,8]$ (since 6 is within both). Let me trace again:

| Balloon | Start | End | Last Arrow | Burst? | Action | Res | Last Arrow After |
|---------|-------|-----|------------|--------|--------|-----|------------------|
| $[1,6]$ | 1 | 6 | $-\infty$ | No | Shoot at 6 | 1 | 6 |
| $[2,8]$ | 2 | 8 | 6 | Yes ($2 \leq 6 \leq 8$) | Already burst | 1 | 6 |
| $[7,12]$ | 7 | 12 | 6 | No ($7 > 6$) | Shoot at 12 | 2 | 12 |
| $[10,16]$ | 10 | 16 | 12 | No ($10 > 12$) | Shoot at 16 | 3 | 16 |

Actually, the algorithm checks `if start > last_arrow`, so:
- For $[2,8]$: start=2, last_arrow=6, so $2 > 6$ is false, meaning it's already burst.

Let me correct the trace:

| Balloon | Start | End | Last Arrow | Condition Check | Action | Res | Last Arrow After |
|---------|-------|-----|------------|-----------------|--------|-----|------------------|
| $[1,6]$ | 1 | 6 | $-\infty$ | $1 > -\infty$ (true) | Shoot at 6 | 1 | 6 |
| $[2,8]$ | 2 | 8 | 6 | $2 > 6$ (false) | Skip (already burst) | 1 | 6 |
| $[7,12]$ | 7 | 12 | 6 | $7 > 6$ (true) | Shoot at 12 | 2 | 12 |
| $[10,16]$ | 10 | 16 | 12 | $10 > 12$ (false) | Skip (already burst) | 2 | 12 |

Wait, $[10,16]$ starts at 10, which is less than 12, so it should be burst by the arrow at 12. But the condition is `start > last_arrow`, so $10 > 12$ is false, meaning it's already burst. So we need 2 arrows total.

**2.4 Increment and Loop:**

After processing all balloons:
- Arrow 1 at position 6 bursts: $[1,6]$, $[2,8]$
- Arrow 2 at position 12 bursts: $[7,12]$, $[10,16]$
- Total arrows: 2

**2.5 Return Result:**

We return `res = 2`, which is the minimum number of arrows needed.

> **Note:** By sorting by end coordinate and always shooting at the end of the first unburst balloon, we ensure that each arrow bursts as many overlapping balloons as possible. This greedy strategy is optimal.


