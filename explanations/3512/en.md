## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= n <= 500`, `1 <= k <= n`.
- **Time Complexity:** O(n*k*log(k)) - for each subarray, we sort and check consecutiveness.
- **Space Complexity:** O(k) - we store a copy of each subarray for sorting.
- **Edge Case:** All subarrays might be invalid, returning all -1s.

**1.2 High-level approach:**
The goal is to find the power of each k-size subarray. A subarray has power equal to its maximum if it's consecutive and sorted, otherwise -1. We use a sliding window approach.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we must check each subarray.
- **Optimized Strategy:** For each subarray, sort it, check if sorted and consecutive, then return max or -1.

**1.4 Decomposition:**
1. Iterate through all possible starting positions for k-size subarrays.
2. For each subarray, create a sorted copy.
3. Check if the sorted array is consecutive (each element differs by 1 from the next).
4. Check if the original subarray equals the sorted array.
5. If both conditions are met, return the maximum; otherwise return -1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `nums = [1,2,3,4,3,2,5]`, `k = 3`. We initialize `res = []`.

**2.2 Start Checking:**
We check subarrays starting at indices 0, 1, 2, 3, 4.

**2.3 Trace Walkthrough:**

| Start | Subarray | Sorted | Consecutive? | Sorted? | Power |
|-------|----------|--------|--------------|---------|-------|
| 0 | [1,2,3] | [1,2,3] | Yes | Yes | 3 |
| 1 | [2,3,4] | [2,3,4] | Yes | Yes | 4 |
| 2 | [3,4,3] | [3,3,4] | No | No | -1 |
| 3 | [4,3,2] | [2,3,4] | Yes | No | -1 |
| 4 | [3,2,5] | [2,3,5] | No | No | -1 |

**2.4 Increment and Loop:**
After processing each subarray, we move the window forward by one position.

**2.5 Return Result:**
Return `res = [3,4,-1,-1,-1]`.

