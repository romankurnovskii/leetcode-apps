## Explanation

### Strategy (The "Why")

**Restate the problem:** We have a circular array where each person has a balance. In one move, a person can transfer exactly 1 unit to either neighbor. We need to find the minimum moves to make all balances non-negative. If impossible, return -1.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length n can be up to 10^5, and each balance can be between -10^9 and 10^9.
- **Time Complexity:** O(n log n) - we need to sort positive balances by distance, which dominates the complexity.
- **Space Complexity:** O(n) for storing positive balances with their distances.
- **Edge Case:** If the total sum is negative, it's impossible to make all balances non-negative, so return -1.

**1.2 High-level approach:**

The goal is to transfer balance from positive positions to the negative position, using the nearest positive balances first to minimize the total transfer distance (and thus moves).

![Circular array balance transfer visualization](https://assets.leetcode.com/static_assets/others/circular-array.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible sequences of transfers, which would be exponential and too slow.
- **Optimized Strategy:** Use a greedy approach: find the negative balance, collect all positive balances with their distances from the negative position, sort by distance, and greedily transfer from nearest to farthest. This is O(n log n) time.
- **Optimization:** By always using the nearest available positive balance first, we minimize the total distance traveled, which directly minimizes the number of moves needed.

**1.4 Decomposition:**

1. Check if total sum is negative - if so, return -1.
2. Find the index with negative balance.
3. If no negative balance exists, return 0.
4. Collect all positive balances with their circular distances from the negative position.
5. Sort positive balances by distance.
6. Greedily transfer from nearest positives until the negative balance is covered.
7. Return the total moves (sum of transfer_amount * distance).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `balance = [5, 1, -4]`, `n = 3`.

- Total sum: 5 + 1 + (-4) = 2 (non-negative, so possible)
- Negative balance at index 2, amount: 4
- Positive balances: index 0 (amount 5, distance 1), index 1 (amount 1, distance 1)

**2.2 Start Processing:**

We calculate distances and sort positive balances.

**2.3 Trace Walkthrough:**

| Positive Index | Amount | Distance from Index 2 | Sorted Order |
|----------------|--------|----------------------|--------------|
| 0 | 5 | min(\|0-2\|, 3-\|0-2\|) = min(2, 1) = 1 | 1st (tie) |
| 1 | 1 | min(\|1-2\|, 3-\|1-2\|) = min(1, 2) = 1 | 1st (tie) |

We need 4 units total. We can take from index 0 (distance 1): transfer 4 units, cost = 4 * 1 = 4 moves.

**2.4 Increment and Loop:**

After transferring from all necessary positive positions, we calculate the total moves.

**2.5 Return Result:**

The result is 4, which is the minimum number of moves needed. We transfer 4 units from index 0 (distance 1) to index 2, requiring 4 moves.
