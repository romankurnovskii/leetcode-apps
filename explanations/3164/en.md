## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count subarrays of size (m+1) in nums that match a given pattern. The pattern specifies relationships between consecutive elements: 1 means increasing, 0 means equal, -1 means decreasing.

**1.1 Constraints & Complexity:**
- Input size: `2 <= n <= 100`, `1 <= m < n`
- **Time Complexity:** O(n * m) where n is array length and m is pattern length, as we check each starting position and each pattern element
- **Space Complexity:** O(1) as we only use a counter
- **Edge Case:** When m = 0, all subarrays of size 1 match (trivially)

**1.2 High-level approach:**
For each possible starting position, we check if the subarray matches the pattern by verifying each pattern condition against the corresponding elements in the subarray.

![Pattern matching visualization](https://assets.leetcode.com/static_assets/others/pattern-matching.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all subarrays and verify pattern, which is what we do - this is already optimal for the constraints
- **Optimized Strategy:** For each starting position, verify pattern conditions sequentially, breaking early if a condition fails
- **Emphasize the optimization:** Early termination when a pattern condition fails avoids unnecessary checks

**1.4 Decomposition:**
1. Iterate through all possible starting positions i (from 0 to n-m-1)
2. For each starting position, check if the subarray matches the pattern
3. For each pattern element k, verify the relationship between nums[i+k] and nums[i+k+1]
4. If all pattern conditions are satisfied, increment the counter
5. Return the total count

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [1,2,3,4,5,6]`, `pattern = [1,1]`
- Initialize counter: `res = 0`
- Pattern means: nums[i+1] > nums[i] and nums[i+2] > nums[i+1]

**2.2 Start Checking:**
We check each possible starting position.

**2.3 Trace Walkthrough:**

| Start i | Subarray | Check nums[i+1] > nums[i]? | Check nums[i+2] > nums[i+1]? | Match? | Count |
|---------|----------|----------------------------|------------------------------|--------|-------|
| 0 | [1,2,3] | 2 > 1 ✓ | 3 > 2 ✓ | Yes | 1 |
| 1 | [2,3,4] | 3 > 2 ✓ | 4 > 3 ✓ | Yes | 2 |
| 2 | [3,4,5] | 4 > 3 ✓ | 5 > 4 ✓ | Yes | 3 |
| 3 | [4,5,6] | 5 > 4 ✓ | 6 > 5 ✓ | Yes | 4 |

**2.4 Increment and Loop:**
After checking all starting positions, we have the total count.

**2.5 Return Result:**
The result is 4, representing the 4 subarrays that match the pattern.
