## Explanation

### Strategy

**The Bug Analysis**
Your current logic checks two things for feasibility:

1.  Is `target` greater than the maximum possible sum (`total_sum`)? (Handled by `diff < 0`)
2.  Is the parity correct? (Handled by `diff % 2 != 0`)

However, it misses the **Lower Bound** check.
In your failing test case:

  * `n = 1`
  * `target = -3`
  * Max possible sum (all positive) = $1$.
  * Min possible sum (all negative) = $-1$.

The target $-3$ is smaller than the minimum possible sum $-1$. Your code calculates a `negative_budget` of 2 (meaning we need to flip numbers summing to 2), but we only have the number 1 available. The greedy loop runs, subtracts 1, leaves the budget at 1, and returns `[-1]` (which sums to -1, not -3).

**The Fix**
We must verify that the `target` is not smaller than the purely negative sum.
Alternatively, and more robustly, we can check if `negative_budget` is exactly `0` after our greedy loop. If the budget isn't 0, it means we couldn't find enough numbers to flip to satisfy the target.

### Steps

1.  **Calculate Total Sum:** Same as before ($n(n+1)/2$).
2.  **Expanded Feasibility Check:**
      * Check `abs(target) > total_sum`. If the target is outside the range `[-total_sum, total_sum]`, return `[]`.
      * Check parity (`diff % 2 != 0`).
3.  **Greedy Loop:** Same as before.
4.  **Final Verification:** (Optional if bounds check is strict, but good practice) Ensure `negative_budget` reached 0.
