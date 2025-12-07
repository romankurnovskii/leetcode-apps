## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= nums.length <= 2 * 10^4`.
- **Value Range:** `-1000 <= nums[i] <= 1000`, `-10^7 <= k <= 10^7`.
- **Time Complexity:** O(n) - we make a single pass through the array.
- **Space Complexity:** O(n) - we use a hash map to store prefix sum frequencies.
- **Edge Case:** If `k = 0` and all numbers are non-zero, return 0. If the array is empty, return 0.

**1.2 High-level approach:**

The goal is to count the number of contiguous subarrays whose sum equals `k`. The key insight is to use prefix sums: if the sum from index 0 to j is `prefix_sum[j]`, and the sum from index 0 to i is `prefix_sum[i]`, then the sum from index i+1 to j is `prefix_sum[j] - prefix_sum[i] = k`. This means `prefix_sum[i] = prefix_sum[j] - k`. We can use a hash map to count how many times each prefix sum has appeared.

![Visualization showing prefix sums and how subarray sums are calculated using the difference between prefix sums]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each starting index, iterate through all ending indices and calculate the sum. This takes O(n²) time.
- **Optimized Strategy:** Use prefix sums with a hash map to count subarrays in a single pass. This takes O(n) time.
- **Why it's better:** The optimized approach reduces time complexity from O(n²) to O(n) by using the mathematical relationship between prefix sums and subarray sums.

**1.4 Decomposition:**

1. Initialize a hash map with `{0: 1}` to represent that prefix sum 0 appears once (empty subarray).
2. Maintain a running prefix sum as we iterate through the array.
3. For each element, check if `current_sum - k` exists in the hash map. If it does, add its count to the result.
4. Update the hash map with the current prefix sum.
5. Return the total count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 1, 1]`, `k = 2`.

We initialize:
- `prefix_sum = {0: 1}` (prefix sum 0 appears once)
- `current_sum = 0`
- `res = 0`

**2.2 Start Checking:**

We iterate through each number in the array, updating the prefix sum and checking for subarrays.

**2.3 Trace Walkthrough:**

| Step | num | current_sum | current_sum - k | Is (current_sum - k) in prefix_sum? | Count added | prefix_sum after update |
|------|-----|-------------|------------------|-------------------------------------|-------------|------------------------|
| 1 | 1 | 1 | -1 | No | 0 | {0: 1, 1: 1} |
| 2 | 1 | 2 | 0 | Yes (count=1) | 1 | {0: 1, 1: 1, 2: 1} |
| 3 | 1 | 3 | 1 | Yes (count=1) | 1 | {0: 1, 1: 1, 2: 1, 3: 1} |

Explanation:
- Step 1: `current_sum = 1`, `current_sum - k = -1`. Not in map, so no subarray found. Add `{1: 1}` to map.
- Step 2: `current_sum = 2`, `current_sum - k = 0`. Found in map with count 1, so we found 1 subarray: `[1, 1]` (indices 0-1). Add `{2: 1}` to map.
- Step 3: `current_sum = 3`, `current_sum - k = 1`. Found in map with count 1, so we found 1 subarray: `[1, 1]` (indices 1-2). Add `{3: 1}` to map.

**2.4 Increment and Loop:**

Continue until all elements are processed.

**2.5 Return Result:**

Return `res = 2` - there are 2 subarrays with sum equal to 2: `[1, 1]` (indices 0-1) and `[1, 1]` (indices 1-2).

