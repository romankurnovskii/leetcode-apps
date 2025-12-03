## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The array $nums$ has length between 1 and $10^4$, and each element is between 0 and 1000.
* **Time Complexity:** $O(n)$ where $n$ is the length of the array. We visit each position exactly once.
* **Space Complexity:** $O(1)$ as we only use a constant amount of extra space.
* **Edge Case:** If the array has only one element, return 0 (already at the end). It's guaranteed that we can reach the last index.

**1.2 High-level approach**

The goal is to find the minimum number of jumps to reach the last index. We use a greedy approach: at each position, we determine the farthest we can reach, and when we've exhausted the current jump range, we make a jump.

![Greedy jump visualization showing how we track the farthest reachable position and make jumps when needed]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible jump sequences using dynamic programming or BFS, which can be $O(n^2)$ or exponential.
* **Optimized (Greedy):** Track the farthest position reachable with the current number of jumps. When we reach the end of the current range, increment the jump count. This achieves $O(n)$ time.

**1.4 Decomposition**

1. Track the farthest position reachable with the current number of jumps.
2. Track the end of the current jump range.
3. For each position, update the farthest reachable position.
4. When we reach the end of the current range, increment the jump count and update the range.
5. Stop early if we can already reach the last index.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $nums = [2, 3, 1, 1, 4]$.

We initialize:
* `jumps = 0` (number of jumps made)
* `current_end = 0` (end of current jump range)
* `farthest = 0` (farthest position reachable)

**2.2 Start Checking/Processing**

We iterate through the array from index 0 to $n - 2$ (we don't need to process the last element).

**2.3 Trace Walkthrough**

| i | nums[i] | farthest (before) | farthest (after) | current_end | jumps | Action |
|---|---------|-------------------|-------------------|-------------|-------|--------|
| 0 | 2 | 0 | 2 | 0 | 0 | Update farthest |
| 0 | 2 | 2 | 2 | 0 | 1 | i == current_end, jump |
| 1 | 3 | 2 | 4 | 2 | 1 | Update farthest |
| 2 | 1 | 4 | 4 | 2 | 1 | Update farthest |
| 2 | 1 | 4 | 4 | 4 | 2 | i == current_end, jump |
| 3 | 1 | 4 | 4 | 4 | 2 | Update farthest |

At index 2, `current_end = 4 >= 4` (last index), so we can stop early.

**2.4 Increment and Loop**

For each index $i$ from 0 to $n - 2$:
1. Update `farthest = max(farthest, i + nums[i])`
2. If $i == current_end$:
   - Increment `jumps`
   - Update `current_end = farthest`
   - If `current_end >= n - 1`, break early

**2.5 Return Result**

After processing, `jumps = 2`. The minimum number of jumps to reach index 4 is 2:
* Jump 1: from index 0 to index 1 (using 1 step from nums[0] = 2)
* Jump 2: from index 1 to index 4 (using 3 steps from nums[1] = 3)

