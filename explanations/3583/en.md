## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count special triplets (i, j, k) where i < j < k, nums[i] == nums[j] * 2, and nums[k] == nums[j] * 2. In other words, for each middle element j, we need to count how many i < j have nums[i] == target and how many k > j have nums[k] == target, where target = nums[j] * 2.

**1.1 Constraints & Complexity:**
- Input size: `3 <= n <= 10^5`, `0 <= nums[i] <= 10^5`
- **Time Complexity:** O(n) - single pass through array with hash map operations
- **Space Complexity:** O(n) for hash maps storing frequencies
- **Edge Case:** If no triplets exist, return 0

**1.2 High-level approach:**
We process each position j as the middle element. We maintain two frequency maps: one for elements before j (freq_before) and one for elements after j (freq_after). For each j, we count how many i < j have nums[i] == target and how many k > j have nums[k] == target, then multiply these counts.

![Frequency counting for triplets visualization](https://assets.leetcode.com/static_assets/others/frequency-counting-triplets.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all triplets (i, j, k) where i < j < k, which is O(n³)
- **Optimized Strategy:** For each j, use hash maps to count valid i and k positions in O(1), achieving O(n) time
- **Emphasize the optimization:** Hash maps allow us to count frequencies before and after each position efficiently without nested loops

**1.4 Decomposition:**
1. Initialize freq_before (empty) and freq_after (contains all elements initially)
2. Process each position j from left to right
3. Remove nums[j] from freq_after (since j is no longer "after")
4. Calculate target = nums[j] * 2
5. Count valid i positions (freq_before[target]) and valid k positions (freq_after[target])
6. Multiply counts and add to result (modulo 10^9 + 7)
7. Add nums[j] to freq_before for future j positions

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [6, 3, 6]`
- Initialize: `freq_before = {}`, `freq_after = {6: 2, 3: 1}`, `res = 0`, `MOD = 10^9 + 7`

**2.2 Start Processing:**
We iterate through each position j from 0 to n-1.

**2.3 Trace Walkthrough:**

| j | nums[j] | Remove from freq_after | target | freq_before[target] | freq_after[target] | Count | res |
|---|---------|------------------------|--------|---------------------|-------------------|-------|-----|
| 0 | 6 | freq_after = {6: 1, 3: 1} | 12 | 0 | 0 | 0 * 0 = 0 | 0 |
| 0 | - | Add to freq_before | - | freq_before = {6: 1} | - | - | 0 |
| 1 | 3 | freq_after = {6: 1} | 6 | 1 (from freq_before) | 1 (from freq_after) | 1 * 1 = 1 | 1 |
| 1 | - | Add to freq_before | - | freq_before = {6: 1, 3: 1} | - | - | 1 |
| 2 | 6 | freq_after = {} | 12 | 0 | 0 | 0 * 0 = 0 | 1 |

**2.4 Increment and Loop:**
For each j, we update frequency maps and count triplets where j is the middle element.

**2.5 Return Result:**
After processing all positions, `res = 1`, which is the number of special triplets. The triplet is (0, 1, 2) where nums[0] = 6 = 3 * 2 and nums[2] = 6 = 3 * 2.

