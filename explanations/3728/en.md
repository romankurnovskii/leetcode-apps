## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count subarrays where the first and last elements are equal, and both equal the sum of all elements strictly between them. The subarray must have at least 3 elements.

**1.1 Constraints & Complexity:**

* **Input Size:** The array `capacity` can have up to 10^5 elements, and values can range from -10^9 to 10^9.
* **Time Complexity:** O(n) - We iterate through the array once, building prefix sums and using a hash map for O(1) lookups.
* **Space Complexity:** O(n) - We store prefix sums in an array of size n+1, and a hash map that can store up to n entries.
* **Edge Case:** If no subarray satisfies the condition (e.g., all elements are different), we return 0.

**1.2 High-level approach:**

The goal is to efficiently find all subarrays [l, r] where capacity[l] == capacity[r] and capacity[l] equals the sum of elements between l and r. We use prefix sums to quickly calculate interval sums, and a hash map to count matching left endpoints for each right endpoint.

![Visualization showing a stable subarray with equal boundary elements and interior sum]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Check all possible subarrays by fixing start and end positions, then verify the conditions. This is O(n^2) time.
* **Optimized (Prefix Sum + Hash Map):** For each right endpoint r, we calculate the required prefix sum for a valid left endpoint. We use a hash map to count how many previous left endpoints match both the value and prefix sum requirements. This is O(n) time.
* **Why it's better:** By using prefix sums and hash maps, we avoid recalculating sums and can count valid pairs in O(1) time per right endpoint.

**1.4 Decomposition:**

1. Build a prefix sum array where prefix[i] represents the sum of elements from index 0 to i-1.
2. For each right endpoint r, calculate the required prefix sum for a valid left endpoint.
3. Before counting, add the left endpoint r-2 to our hash map (ensuring subarray length >= 3).
4. Count how many previous left endpoints match both the value and prefix sum requirements.
5. Return the total count of stable subarrays.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `capacity = [9, 3, 3, 3, 9]`

We initialize:
* `prefix = [0, 9, 12, 15, 18, 27]` (prefix sums)
* `res = 0` (result counter)
* `count_map = {}` (hash map to track (value, prefix_sum) pairs)

**2.2 Start Checking:**

We iterate through each position r from 0 to n-1, processing it as a potential right endpoint.

**2.3 Trace Walkthrough:**

| Step | r   | capacity[r] | Add to map? | required_prefix | Check map | res |
| ---- | --- | ----------- | ----------- | --------------- | --------- | --- |
| 0    | 0   | 9           | No (r < 2)  | -               | -         | 0   |
| 1    | 1   | 3           | No (r < 2)  | -               | -         | 0   |
| 2    | 2   | 3           | Yes (l=0)   | 9 - 3 = 6       | (9, 9)?   | 0   |
| 3    | 3   | 3           | Yes (l=1)   | 12 - 3 = 9      | (3, 9)?   | 0   |
| 4    | 4   | 9           | Yes (l=2)   | 15 - 9 = 6      | (9, 6)?   | 1   |

At step 4, we find that capacity[0] = 9 and prefix[1] = 9, which matches (9, 6) after rearranging. The subarray [0, 4] is stable: 9 == 9 and 9 == 3+3+3.

**2.4 Increment and Loop:**

For each r >= 2, we add index r-2 to the map with key (capacity[r-2], prefix[r-1]), then check if any previous left endpoint matches our requirements.

**2.5 Return Result:**

After processing all positions, we return `res = 2`, representing the two stable subarrays: [9, 3, 3, 3, 9] and [3, 3, 3].
