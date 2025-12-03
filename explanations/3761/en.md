## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^5$ elements. Values are in the range $[1, 10^9]$.
- **Time Complexity:** $O(n \times d)$ where $n$ is the array length and $d$ is the average number of digits. Reversing a number takes $O(d)$ time.
- **Space Complexity:** $O(n)$ for the hash map storing last occurrences.
- **Edge Case:** If no mirror pair exists, return $-1$.

**1.2 High-level approach:**

The goal is to find the minimum absolute distance between indices $(i, j)$ where `reverse(nums[i]) == nums[j]` and $i < j$. We use a hash map to track the last occurrence of each reversed number as we traverse from left to right.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all pairs $(i, j)$ where $i < j$ and see if `reverse(nums[i]) == nums[j]`. This is $O(n^2)$ time.
- **Optimized Strategy:** Traverse from left to right. For each position $j$, check if `nums[j]` appeared as a reversed number before. Store the last occurrence of each reversed number to minimize distance. This is $O(n \times d)$ time.
- **Why optimized is better:** By tracking last occurrences, we ensure we always use the closest previous index, minimizing the distance.

**1.4 Decomposition:**

1. Create a helper function to reverse an integer (removing leading zeros).
2. Initialize a hash map to store last occurrence index of reversed numbers.
3. Store the reverse of the first element.
4. For each subsequent element, check if it exists in the map (meaning its reverse appeared before).
5. Update the minimum distance if a match is found.
6. Update the map with the reverse of the current element.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [12,21,45,33,54]`

We initialize:
- `last_occ = {}` (hash map)
- `res = inf` (minimum distance)

**2.2 Start Checking:**

We process each element from left to right.

**2.3 Trace Walkthrough:**

| Index | Value | Reverse | Check nums[j] in map? | last_occ before | Update | last_occ after |
|-------|-------|---------|----------------------|-----------------|--------|----------------|
| 0 | 12 | 21 | - | {} | - | {21: 0} |
| 1 | 21 | 12 | Yes (21 in map) | {21: 0} | res = min(inf, 1-0) = 1 | {21: 0, 12: 1} |
| 2 | 45 | 54 | No | {21: 0, 12: 1} | - | {21: 0, 12: 1, 54: 2} |
| 3 | 33 | 33 | No | {21: 0, 12: 1, 54: 2} | - | {21: 0, 12: 1, 54: 2, 33: 3} |
| 4 | 54 | 45 | Yes (54 in map) | {21: 0, 12: 1, 54: 2, 33: 3} | res = min(1, 4-2) = 1 | {21: 0, 12: 1, 54: 2, 33: 3, 45: 4} |

**2.4 Increment and Loop:**

For each index $j$ from 1 to $n-1$:
- If `nums[j]` is in `last_occ`, update `res = min(res, j - last_occ[nums[j]])`
- Update `last_occ[reverse(nums[j])] = j`

**2.5 Return Result:**

After processing, `res = 1` (from pair (0,1) where reverse(12)=21). We return `1`.

