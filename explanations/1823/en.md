## Explanation

### Strategy

**Constraints & Edge Cases**

* **Game Parameters:** n (friends) and k (counting) are both 1-500. This is the classic Josephus problem.
* **Time Complexity:** We use the Josephus recurrence formula which processes each friend once. **Time Complexity: O(n)**, **Space Complexity: O(1)**.
* **Edge Case:** If n=1, there's only one friend, so they win (return 1).

**High-level approach**

The problem asks us to find the winner in a circular elimination game. This is the classic Josephus problem. We use the mathematical recurrence: `J(n,k) = (J(n-1,k) + k) % n`, with base case `J(1,k) = 0` (0-indexed), then convert to 1-indexed.

**Brute force vs. optimized strategy**

* **Brute Force:** Simulate the game step by step, removing friends in order. This would be O(n*k) time.
* **Optimized:** Use the Josephus recurrence formula to calculate the winner directly in O(n) time.

**Decomposition**

1. **Base Case:** For 1 friend, the winner is friend 0 (0-indexed) or friend 1 (1-indexed).
2. **Recurrence:** For n friends, the winner is `(winner(n-1) + k) % n`.
3. **Convert to 1-indexed:** Add 1 to the 0-indexed result.

### Steps

1. **Initialization & Example Setup**
   Let's use `n = 5`, `k = 2` as our example.
   - We'll work in 0-indexed (0,1,2,3,4) and convert to 1-indexed at the end.

2. **Josephus Recurrence**
   - `J(1,2) = 0` (base case: 1 friend, winner is 0).
   - `J(2,2) = (J(1,2) + 2) % 2 = (0 + 2) % 2 = 0`.
   - `J(3,2) = (J(2,2) + 2) % 3 = (0 + 2) % 3 = 2`.
   - `J(4,2) = (J(3,2) + 2) % 4 = (2 + 2) % 4 = 0`.
   - `J(5,2) = (J(4,2) + 2) % 5 = (0 + 2) % 5 = 2`.

3. **Trace Walkthrough**

| n | J(n,2) Calculation | Result (0-indexed) |
|---|-------------------|-------------------|
| 1 | 0 (base case)     | 0                 |
| 2 | (0 + 2) % 2       | 0                 |
| 3 | (0 + 2) % 3       | 2                 |
| 4 | (2 + 2) % 4       | 0                 |
| 5 | (0 + 2) % 5       | 2                 |

4. **Convert to 1-indexed**
   - `J(5,2) = 2` (0-indexed) → `2 + 1 = 3` (1-indexed).

5. **Return Result**
   Return 3, which is the winner in 1-indexed.
