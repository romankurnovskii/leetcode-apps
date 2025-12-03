## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^5$ gas stations. Gas and cost values are in the range $[0, 10^4]$.
- **Time Complexity:** $O(n)$ where $n$ is the number of gas stations. We traverse the array once.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space.
- **Edge Case:** If total gas is less than total cost, it's impossible to complete the circuit, return $-1$.

**1.2 High-level approach:**

The goal is to find the starting gas station index that allows us to complete a full circuit. We use a greedy approach: if we can't reach station $i$ from the current start, we know we can't reach $i$ from any station before the current start either.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try starting from each station and check if we can complete the circuit. This is $O(n^2)$ time.
- **Optimized Strategy:** Use a single pass. Track total gas/cost and current tank. If current tank becomes negative, reset and try starting from the next station. This is $O(n)$ time.
- **Why optimized is better:** The optimized approach leverages the insight that if we can't reach station $i$ from start $s$, we can't reach $i$ from any station between $s$ and $i$.

**1.4 Decomposition:**

1. Track total gas and total cost to check if a solution exists.
2. Track current tank level as we traverse.
3. If current tank becomes negative, we can't start from any station in the current range, so try starting from the next station.
4. Return the start index if total gas >= total cost, otherwise return $-1$.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`

We initialize:
- `total_gas = 0`
- `total_cost = 0`
- `current_tank = 0`
- `start = 0`

**2.2 Start Checking:**

We iterate through each station, calculating the net gas (gas[i] - cost[i]) and updating our totals.

**2.3 Trace Walkthrough:**

| Station | gas[i] | cost[i] | net | current_tank | total_gas | total_cost | start |
|---------|--------|---------|-----|---------------|-----------|------------|-------|
| 0 | 1 | 3 | -2 | -2 | 1 | 3 | 1 |
| 1 | 2 | 4 | -2 | -2 | 3 | 7 | 2 |
| 2 | 3 | 5 | -2 | -2 | 6 | 12 | 3 |
| 3 | 4 | 1 | +3 | +3 | 10 | 13 | 3 |
| 4 | 5 | 2 | +3 | +6 | 15 | 15 | 3 |

**2.4 Increment and Loop:**

At each station:
- Add `gas[i] - cost[i]` to `current_tank`.
- If `current_tank < 0`, we reset `current_tank = 0` and set `start = i + 1`.
- Update `total_gas` and `total_cost`.

**2.5 Return Result:**

After processing all stations:
- `total_gas = 15`, `total_cost = 15`, so a solution exists.
- `start = 3`, which is the valid starting station.

We return `3`. Starting from station 3, we can complete the circuit.

