## Explanation

### Strategy

**Constraints & Edge Cases**

* **Tree Structure:** n employees (1-160), budget is 1-160. The hierarchy forms a tree where employee 1 is the root. If a parent buys stock, children get 50% discount.
* **Time Complexity:** We use tree DP with knapsack for children. For each node, we merge children's results. **Time Complexity: O(n * budget²)** in worst case, **Space Complexity: O(n * budget)** for memoization.
* **Edge Case:** If budget is 0, return 0. If all stocks have negative profit, return 0.

**High-level approach**

The problem asks us to maximize profit by buying stocks for employees, with a discount rule: if a parent buys, children get half price. We use tree dynamic programming with knapsack to allocate budget optimally among children.

**Brute force vs. optimized strategy**

* **Brute Force:** Try all possible combinations of buying/not buying for each employee. This would be exponential.
* **Optimized:** Use tree DP where for each node, we maintain a dictionary mapping (budget → max_profit). We merge children's results using knapsack approach, considering both buying and skipping the current node.

**Decomposition**

1. **Tree Structure:** Build adjacency list from hierarchy.
2. **DFS with State:** For each employee, track whether parent bought (discount available).
3. **Two Options:** Buy current stock or skip it.
4. **Merge Children:** Use knapsack to optimally allocate budget among children.
5. **Return Maximum:** Return the maximum profit from all budget allocations.

### Steps

1. **Initialization & Example Setup**
   Let's use `n=2, present=[1,2], future=[4,3], hierarchy=[[1,2]], budget=3` as our example.
   - Build tree: employee 1 has child employee 2.
   - Start DFS from employee 0 (1-indexed → 0-indexed).

2. **DFS for Employee 0 (no discount)**
   - Cost: `present[0] = 1`, Profit: `future[0] - 1 = 3`
   - Option 1 (buy): `buy_current = {1: 3}`
   - Option 2 (skip): `skip_current = {0: 0}`
   - Process child (employee 1):
     - If we buy employee 0: child gets discount → `dfs(1, True)` returns `{1: 1}` (cost=1, profit=3-1=2, but wait...)
     - Merge: `buy_current` with child discount results

3. **Trace Walkthrough**

For employee 0 (root, no parent discount):
- Buy option: cost=1, profit=3, remaining budget=2
  - Child with discount: cost=2//2=1, profit=3-1=2
  - Total: budget=1+1=2, profit=3+2=5 ✓
- Skip option: budget=3
  - Child no discount: cost=2, profit=3-2=1
  - Total: budget=2, profit=0+1=1

Result: `{2: 5, 3: 1}` → max = 5

4. **Knapsack Merging**
   - For each child, merge results by trying all budget allocations
   - `new_buy[spent1 + spent2] = max(new_buy[spent1 + spent2], prof1 + prof2)`
   - This ensures optimal budget allocation

5. **Return Result**
   Return `max(result.values()) = 5`.

