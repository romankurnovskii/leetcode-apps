## Explanation

### Strategy (The "Why")

**Restate the problem:** We have n tasks, each can be completed using technique1 or technique2, earning different points. We must complete at least k tasks using technique1. We want to maximize total points.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 10^5`
- **Time Complexity:** O(n log n) for sorting
- **Space Complexity:** O(n) for storing deltas
- **Edge Case:** When k = 0, we can use technique2 for all tasks

**1.2 High-level approach:**
Start with all tasks using technique1. Calculate the delta (gain/loss) from switching each task to technique2. Sort deltas descending and apply the largest (n-k) positive deltas.

![Greedy optimization visualization](https://assets.leetcode.com/static_assets/others/greedy-optimization.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all ways to select k tasks for technique1, which is exponential
- **Optimized Strategy:** Start with all technique1, then greedily switch to technique2 where beneficial, achieving O(n log n) time
- **Emphasize the optimization:** By sorting deltas, we can greedily select the most beneficial switches

**1.4 Decomposition:**
1. Start with all tasks using technique1, calculate initial total
2. Calculate delta for each task: technique2[i] - technique1[i]
3. Sort deltas in descending order
4. Apply the largest (n-k) deltas to maximize points
5. Return the maximum total encountered

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `technique1 = [5,2,10]`, `technique2 = [10,3,8]`, `k = 2`
- Initial total: 5 + 2 + 10 = 17
- Deltas: [10-5, 3-2, 8-10] = [5, 1, -2]

**2.2 Start Processing:**
We sort deltas and apply the best switches.

**2.3 Trace Walkthrough:**

| Step | Total | Delta Applied | New Total | Max |
|------|-------|---------------|-----------|-----|
| Initial | 17 | - | - | 17 |
| Apply delta 5 | 17 | +5 | 22 | 22 |
| Apply delta 1 | 22 | +1 | 23 | 23 |

Since k=2, we can switch at most 1 task (n-k=1). We apply the largest delta (5).

**2.4 Increment and Loop:**
After applying the best (n-k) deltas, we have the maximum.

**2.5 Return Result:**
The maximum total is 22 (switching task 0 from technique1 to technique2: 2 + 10 + 10 = 22).
