## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given a circular array `balance` where `balance[i]` is the net balance of person i. In one move, a person can transfer exactly 1 unit to either their left or right neighbor. We need to find the minimum number of moves required so that every person has a non-negative balance. If impossible, return -1.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 10^5 elements in the array.
- **Time Complexity:** O(n) where n is the length - we find the negative index once, then expand outward at most n/2 steps.
- **Space Complexity:** O(1) - we only use a few variables.
- **Edge Case:** If all balances are already non-negative, return 0. If the total sum is negative, return -1.

**1.2 High-level approach:**

The goal is to find the index with negative balance, then greedily transfer from neighbors at increasing distances until the negative balance is covered. We expand outward from the negative index, using the closest positive balances first.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible sequences of transfers, which would be exponential and too slow.
- **Optimized Strategy:** Find the negative index, then expand outward distance by distance, transferring from neighbors at each distance. This is O(n) time.
- **Optimization:** By expanding outward from the negative index, we minimize the transfer distance. The cost is transfer_amount × distance, so using closer neighbors first minimizes the total cost.

**1.4 Decomposition:**

1. Find the index with negative balance (there's at most one).
2. If all balances are non-negative, return 0.
3. If total sum is negative, return -1 (impossible).
4. Expand outward from the negative index:
   - At distance d, get storage from neighbors at positions (j+d) and (j-d) modulo n.
   - Transfer the minimum of the debt and available storage.
   - Add transfer × distance to the result.
   - Update the balance at the negative index.
5. Continue until the negative balance is covered.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `balance = [5, 1, -4]`

- Negative index: `j = 2` (balance[2] = -4)
- Total sum: 5 + 1 + (-4) = 2 (positive, so possible)
- Distance `d = 0` initially

**2.2 Start Processing:**

We begin expanding outward from the negative index.

**2.3 Trace Walkthrough:**

| Step | d | Neighbors | Storage | Debt | Transfer | Cost | Balance at j |
| ---- | - | --------- | ------- | ---- | -------- | ---- | ------------- |
| 1    | 1 | (2+1)%3=0, (2-1)%3=1 | 5 + 1 = 6 | 4 | min(4, 6) = 4 | 4 × 1 = 4 | -4 + 4 = 0 |

At distance 1:
- Neighbor at (2+1) % 3 = 0: balance[0] = 5
- Neighbor at (2-1) % 3 = 1: balance[1] = 1
- Total storage: 5 + 1 = 6
- Debt: 4
- Transfer: min(4, 6) = 4
- Cost: 4 × 1 = 4
- New balance at j: -4 + 4 = 0

**2.4 Increment and Loop:**

We increment the distance and continue until the negative balance is covered.

**2.5 Return Result:**

The result is 4, which is the minimum number of moves required. We transfer 4 units from the neighbors at distance 1, with a cost of 4 moves.
