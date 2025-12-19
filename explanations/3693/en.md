## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to climb a staircase with n+1 steps (numbered 0 to n), starting at step 0. From step i, we can jump to step i+1, i+2, or i+3. The cost of jumping from step i to step j is `costs[j] + (j - i)^2`. We want to find the minimum total cost to reach step n.

**1.1 Constraints & Complexity:**

- **Input Size:** n can be up to 10^5, and each cost is between 1 and 10^4.
- **Time Complexity:** O(n) - we iterate through all n steps once, computing the minimum cost for each step.
- **Space Complexity:** O(1) - we use a rolling array of size 3 instead of storing all n values, trading space for constant memory usage.
- **Edge Case:** If n = 1, we can only jump from step 0 to step 1 with cost `costs[0] + 1`.

**1.2 High-level approach:**

The goal is to compute the minimum cost to reach each step by considering the three possible previous steps (i-1, i-2, i-3) and choosing the one with minimum total cost.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Recursively try all paths from step 0 to step n, which would be O(3^n) exponential time.
- **Optimized Strategy:** Use dynamic programming with a rolling array. For each step i, we only need the costs of steps i-1, i-2, and i-3, so we can use a 3-element array and update it in place. This is O(n) time and O(1) space.
- **Optimization:** Since we only need the last 3 values at any time, we use a rolling array instead of storing all n values, reducing space from O(n) to O(1).

**1.4 Decomposition:**

1. Initialize three variables to represent the minimum cost to reach the previous three steps (initially all 0 for step 0).
2. For each step from 1 to n, calculate the minimum cost by considering jumps from the three previous steps.
3. Update the rolling array by shifting values: the oldest value is discarded, and the new value becomes the minimum cost for the current step.
4. Return the cost to reach step n.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 4, costs = [1, 2, 3, 4]`

- We start at step 0 with cost 0.
- Initialize: `v0 = 0, v1 = 0, v2 = 0` (costs to reach steps -2, -1, 0, which are all 0)

**2.2 Start Processing:**

We iterate through each cost in the costs array, computing the minimum cost to reach each step.

**2.3 Trace Walkthrough:**

| Step | Cost | v0 | v1 | v2 | Calculation | New v2 |
|------|------|----|----|----|-------------|--------|
| 0 | - | 0 | 0 | 0 | Initial state | - |
| 1 | 1 | 0 | 0 | 0 | min(0+9, 0+4, 0+1) + 1 = 1 | 1 |
| 2 | 2 | 0 | 0 | 1 | min(0+9, 0+4, 1+1) + 2 = 4 | 4 |
| 3 | 3 | 0 | 1 | 4 | min(0+9, 1+4, 4+1) + 3 = 8 | 8 |
| 4 | 4 | 1 | 4 | 8 | min(1+9, 4+4, 8+1) + 4 = 13 | 13 |

After each iteration, we shift: `v0, v1, v2 = v1, v2, new_value`

**2.4 Increment and Loop:**

For each step i, we compute:
- Jump from i-3: `v0 + 9 + costs[i-1]`
- Jump from i-2: `v1 + 4 + costs[i-1]`
- Jump from i-1: `v2 + 1 + costs[i-1]`

We take the minimum of these three options.

**2.5 Return Result:**

The result is `13`, which is the minimum cost to reach step 4. The optimal path is 0 → 1 → 2 → 4 with costs: (1+1) + (2+1) + (4+4) = 2 + 3 + 8 = 13.

