## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count pairs (i, j) where i < j and the pair satisfies: min(|a-b|, |a+b|) <= min(|a|, |b|) and max(|a-b|, |a+b|) >= max(|a|, |b|), where a=nums[i] and b=nums[j].

**1.1 Constraints & Complexity:**

- **Input Size:** Array length can be up to 10^5.
- **Time Complexity:** O(n log n) - we sort the array and use two pointers.
- **Space Complexity:** O(n) - for the sorted array.
- **Edge Case:** If all numbers have very different magnitudes, there may be no perfect pairs.

**1.2 High-level approach:**

The goal is to work with absolute values and find pairs where the larger value is at most twice the smaller value.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all pairs, which would be O(n^2).
- **Optimized Strategy:** Sort by absolute value, then for each element, use two pointers to find all valid pairs. This is O(n log n).
- **Optimization:** After sorting, the condition simplifies to: for a pair (x, y) where x <= y, we need y <= 2*x.

**1.4 Decomposition:**

1. Create array of absolute values and sort.
2. For each index i, use a pointer j to find the rightmost element such that arr[j] <= 2*arr[i].
3. Count all pairs (i, k) where i < k <= j.
4. Sum all counts.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [0,1,2,3]`

- Absolute values: [0,1,2,3] (already sorted).

**2.2 Start Processing:**

We iterate i from 0 to 3, and for each i, find valid j values.

**2.3 Trace Walkthrough:**

| i | arr[i] | j start | j after loop | Valid pairs (i+1 to j-1) | Count |
|---|--------|---------|--------------|---------------------------|-------|
| 0 | 0 | 1 | 1 (arr[1]=1 > 2*0=0) | None (j-1=0, i+1=1) | 0 |
| 1 | 1 | 2 | 3 (arr[2]=2 <= 2, arr[3]=3 > 2) | (1,2) | 1 |
| 2 | 2 | 3 | 4 (arr[3]=3 <= 4, then j=4 out of bounds) | (2,3) | 1 |

Total: 2 perfect pairs

