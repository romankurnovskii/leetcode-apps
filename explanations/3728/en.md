## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $3 \leq n \leq 10^5$ elements. Values are in the range $[-10^9, 10^9]$.
- **Time Complexity:** $O(n)$ where $n$ is the array length. We make a single pass through the array.
- **Space Complexity:** $O(n)$ for the prefix sum array and hash map.
- **Edge Case:** If no stable subarray exists, return 0.

**1.2 High-level approach:**

The goal is to count subarrays where the first and last elements are equal, and each equals the sum of elements strictly between them. Using prefix sums, the condition becomes: `capacity[l] == capacity[r]` and `capacity[l] == prefix[r] - prefix[l+1]`, which rearranges to `prefix[l+1] == prefix[r] - capacity[r]`.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all subarrays of length $\geq 3$ and verify the condition. This is $O(n^3)$ time.
- **Optimized Strategy:** Use prefix sums and a hash map. For each right endpoint $r$, count how many previous indices $l$ satisfy both conditions. This is $O(n)$ time.
- **Why optimized is better:** The hash map allows us to quickly look up valid left endpoints, avoiding nested loops.

**1.4 Decomposition:**

1. Compute prefix sums: `prefix[i] = sum(capacity[0:i])`.
2. Use a hash map: key is `(value, prefix_sum)`, value is count.
3. For each right endpoint $r$:
   - Count matches: look for `(capacity[r], prefix[r] - capacity[r])` in the map.
   - Update map: add `(capacity[r], prefix[r])` for future matches.
4. Return total count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `capacity = [9,3,3,3,9]`

We compute prefix sums: `prefix = [0,9,12,15,18,27]`

**2.2 Start Checking:**

We process each position as a right endpoint and count valid left endpoints.

**2.3 Trace Walkthrough:**

| r | capacity[r] | prefix[r] | target_prefix | Check map | Count | Update map |
|---|--------------|-----------|---------------|-----------|-------|------------|
| 0 | 9 | 9 | 9-9=0 | {} | 0 | {(9,9): 1} |
| 1 | 3 | 12 | 12-3=9 | {(9,9): 1} | 0 | {(9,9): 1, (3,12): 1} |
| 2 | 3 | 15 | 15-3=12 | {(9,9): 1, (3,12): 1} | 1 | {(9,9): 1, (3,12): 1, (3,15): 1} |
| 3 | 3 | 18 | 18-3=15 | {(9,9): 1, (3,12): 1, (3,15): 1} | 1 | {(9,9): 1, (3,12): 1, (3,15): 1, (3,18): 1} |
| 4 | 9 | 27 | 27-9=18 | {(9,9): 1, (3,12): 1, (3,15): 1, (3,18): 1} | 0 | {(9,9): 1, (3,12): 1, (3,15): 1, (3,18): 1, (9,27): 1} |

Total count: 2 (subarrays [3,3,3] and [9,3,3,3,9])

**2.4 Increment and Loop:**

For each index $r$:
- Calculate `target_prefix = prefix[r] - capacity[r]`
- Look up `(capacity[r], target_prefix)` in the map and add to count
- Update map: `map[(capacity[r], prefix[r])] += 1`

**2.5 Return Result:**

After processing all positions, we return the total count of stable subarrays. For the example, we get 2 stable subarrays.

