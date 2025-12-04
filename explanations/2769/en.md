## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= num, t <= 50`.
- **Time Complexity:** O(1) - We calculate the answer directly using a mathematical formula.
- **Space Complexity:** O(1) - Only constant space is used.
- **Edge Case:** When `t = 0`, the maximum achievable number equals `num`.

**1.2 High-level approach:**
The goal is to find the maximum value of `x` such that after at most `t` operations (where each operation decreases `x` by 1 and increases `num` by 1), `x` becomes equal to `num`. To maximize `x`, we should always decrease `x` and increase `num` in each operation.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible values of `x` and simulate the operations - O(t) time.
- **Optimized Strategy:** Use mathematical reasoning: after `t` operations, `x - t = num + t`, so `x = num + 2*t` - O(1) time.

**1.4 Decomposition:**
1. Understand that to maximize `x`, we should decrease `x` and increase `num` in each operation.
2. After `t` operations: `x` becomes `x - t` and `num` becomes `num + t`.
3. For them to be equal: `x - t = num + t`.
4. Solve for `x`: `x = num + 2*t`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `num = 4, t = 1`. We want to find the maximum `x` such that after 1 operation, `x` equals `num`.

**2.2 Start Checking:**
We apply the formula: `x = num + 2*t = 4 + 2*1 = 6`.

**2.3 Trace Walkthrough:**

| Operation | x | num | Condition |
|-----------|---|-----|-----------|
| Initial | 6 | 4 | - |
| After 1 op | 6-1=5 | 4+1=5 | 5 == 5 ✓ |

**2.4 Increment and Loop:**
Not applicable - this is a direct calculation.

**2.5 Return Result:**
Return `res = 6`, which is the maximum achievable value of `x`.

