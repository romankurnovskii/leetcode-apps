## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The length of boxes string `n` is between 1 and 2000.
  * **Time Complexity:** O(n²) - For each of n positions, we iterate through all n boxes to calculate operations.
  * **Space Complexity:** O(n) - We create a result array of size n.
  * **Edge Case:** If all boxes are empty (all '0'), all positions require 0 operations.

**High-level approach**
For each target position, we calculate the total number of operations needed to move all balls from their current positions to that target. Each ball requires `abs(target_position - current_position)` operations to move.

![Visualization showing balls moving from their positions to a target box]

**Brute force vs. optimized strategy**

  * **Brute Force:** For each position, iterate through all boxes and sum the distances. This is O(n²) which is acceptable for n ≤ 2000.
  * **Optimized Strategy:** We could use prefix sums to optimize, but for the given constraints, the brute force approach is straightforward and efficient enough.

**Decomposition**

1.  **Initialize Result Array:** Create an array of zeros with length n.
2.  **For Each Target Position:** Calculate operations needed to move all balls to this position.
3.  **Sum Distances:** For each ball (box with '1'), add the absolute distance to the target.
4.  **Store Result:** Save the total operations for each position.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `boxes = "110"` (boxes at positions 0 and 1 have balls).
    We create `res = [0, 0, 0]` to store operations for each position.

2.  **Start Checking:**
    For each position `i` from 0 to n-1, we'll calculate the total operations.

3.  **Trace Walkthrough:**
    
    | Target Position | Ball at 0 | Ball at 1 | Total Operations |
    |----------------|-----------|-----------|------------------|
    | 0 | abs(0-0) = 0 | abs(0-1) = 1 | 0 + 1 = 1 |
    | 1 | abs(1-0) = 1 | abs(1-1) = 0 | 1 + 0 = 1 |
    | 2 | abs(2-0) = 2 | abs(2-1) = 1 | 2 + 1 = 3 |

4.  **Result:**
    After processing all positions, `res = [1, 1, 3]`

5.  **Return Result:**
    Return the result array `[1, 1, 3]`.

