## Explanation

### Strategy (The "Why")

**Restate the problem:** We have n children numbered 0 to n-1 standing in a line. Child 0 initially holds a ball and passes it right. When the ball reaches either end (child 0 or child n-1), the direction reverses. We need to find which child has the ball after k seconds.

**1.1 Constraints & Complexity:**

- **Input Size:** n is between 2 and 50, k is between 1 and 50. These are small values, so simulation is feasible.
- **Time Complexity:** O(k mod period) where period = 2*(n-1). Since k and n are small, this is effectively O(k) in worst case.
- **Space Complexity:** O(1) - we only use a few variables to track position and direction.
- **Edge Case:** When n=2, the period is 2, so the ball alternates between children 0 and 1.

**1.2 High-level approach:**

The goal is to simulate the ball passing pattern. The key insight is that the pattern repeats every 2*(n-1) seconds, so we can use modulo arithmetic to reduce k before simulation.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Simulate all k seconds step by step. This is O(k) time.
- **Optimized Strategy:** Recognize that the pattern repeats every 2*(n-1) seconds. Use k % (2*(n-1)) to reduce the simulation time. This is still O(k) in worst case but more efficient for large k values.
- **Optimization:** By using modulo, we avoid simulating redundant cycles when k is much larger than the period.

**1.4 Decomposition:**

1. Calculate the period of repetition: 2 * (n - 1) seconds.
2. Reduce k using modulo: k_mod = k % period.
3. Initialize position at 0 and direction as 1 (right).
4. Simulate k_mod steps: move position by direction, reverse direction at boundaries.
5. Return the final position.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `n = 3`, `k = 5`.

- Period = 2 * (3 - 1) = 2 * 2 = 4
- k_mod = 5 % 4 = 1
- Initial position = 0, direction = 1 (right)

**2.2 Start Simulation:**

We simulate k_mod = 1 step.

**2.3 Trace Walkthrough:**

| Step | Position | Direction | Action |
|------|----------|-----------|--------|
| 0 | 0 | 1 (right) | Start at child 0 |
| 1 | 1 | 1 (right) | Move right to child 1 |

**2.4 Increment and Loop:**

After k_mod steps, we have the final position.

**2.5 Return Result:**

The final position is 1, so child 1 has the ball after k=5 seconds. This matches the example where after 5 seconds, the ball is at child 1.

