## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find, for each index i, the maximum value reachable by following any sequence of valid jumps starting at i. Valid jumps: forward to j>i if nums[j] < nums[i], backward to j<i if nums[j] > nums[i].

**1.1 Constraints & Complexity:**

- **Input Size:** Array length can be up to 10^5.
- **Time Complexity:** O(n) - we compute prefix max and suffix min in O(n), find cuts in O(n), and assign component max values in O(n).
- **Space Complexity:** O(n) - we store prefix max, suffix min, and result arrays.
- **Edge Case:** If the array is already sorted, all indices can reach the maximum value.

**1.2 High-level approach:**

The goal is to identify "connected components" in the jump graph. Indices in the same component can reach each other, and the maximum value in a component is the answer for all indices in that component. A "cut" occurs where we cannot jump across (all left values <= all right values).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each index, use BFS/DFS to explore all reachable indices and find the maximum. This would be O(n^2) in worst case.
- **Optimized Strategy:** Use prefix max and suffix min to identify cuts, then assign the maximum value in each component to all indices in that component. This is O(n) time.
- **Optimization:** By identifying components upfront, we avoid redundant exploration and can compute answers for all indices simultaneously.

**1.4 Decomposition:**

1. Compute prefix maximum array (max value from start to each position).
2. Compute suffix minimum array (min value from each position to end).
3. Identify cuts: positions where prefix_max[i] <= suffix_min[i+1] (cannot jump across).
4. For each component (between cuts), find the maximum value.
5. Assign the component maximum to all indices in that component.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [2,1,3]`

- prefix_max: [2, 2, 3]
- suffix_min: [1, 1, 3]

**2.2 Start Processing:**

We identify cuts and then assign component maximums.

**2.3 Trace Walkthrough:**

Finding cuts:
- Position 0: prefix_max[0]=2, suffix_min[1]=1, 2 > 1, no cut
- Position 1: prefix_max[1]=2, suffix_min[2]=3, 2 <= 3, CUT at position 1

Components:
- Component 1: indices [0, 1], max = max(2, 1) = 2
- Component 2: indices [2], max = 3

Result:
- res[0] = 2 (can reach max in component 1)
- res[1] = 2 (can reach max in component 1)
- res[2] = 3 (can reach max in component 2)

For `nums = [2,3,1]`:
- prefix_max: [2, 3, 3]
- suffix_min: [1, 1, 1]
- No cuts (all prefix_max > suffix_min)
- Single component: [0, 1, 2], max = 3
- Result: [3, 3, 3]

**2.4 Increment and Loop:**

The algorithm processes the array once to find cuts, then once more to assign component maximums.

**2.5 Return Result:**

For `nums = [2,1,3]`, the result is [2, 2, 3]. From index 0 or 1, we can reach value 2. From index 2, we can reach value 3.

