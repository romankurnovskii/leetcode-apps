## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count beautiful subarrays. A subarray is beautiful if we can make all its elements equal to 0 using operations that subtract 2^k from pairs of elements that both have the k-th bit set.

**1.1 Constraints & Complexity:**
- Input size: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^6`
- **Time Complexity:** O(n) where n is the length of nums, as we use a single pass with prefix XOR and hash map lookups
- **Space Complexity:** O(n) in the worst case to store prefix XOR values in the hash map
- **Edge Case:** A subarray with all zeros is beautiful (XOR = 0)

**1.2 High-level approach:**
The key insight is that a subarray is beautiful if and only if its XOR is 0. This is because we can pair up all set bits and subtract them. We use prefix XOR to efficiently compute subarray XORs.

![XOR prefix sum visualization](https://assets.leetcode.com/static_assets/others/xor-prefix.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all O(n²) subarrays and compute XOR for each, which is O(n³) overall.
- **Optimized Strategy:** Use prefix XOR. If `prefix_xor[i] == prefix_xor[j]`, then the subarray from i to j-1 has XOR 0. This is O(n) with hash map lookups.

**1.4 Decomposition:**
1. Initialize prefix XOR to 0 and a hash map to count prefix XOR occurrences
2. For each element, update prefix XOR by XORing with the current element
3. Count how many times we've seen this prefix XOR value before (these form beautiful subarrays)
4. Update the count in the hash map

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [4, 3, 1, 2, 4]`
- Initialize `prefix_xor = 0`
- Initialize `count = {0: 1}` (empty prefix has XOR 0)
- Initialize `res = 0`

**2.2 Start Checking:**
We begin processing each element and updating the prefix XOR.

**2.3 Trace Walkthrough:**
Using the example `nums = [4, 3, 1, 2, 4]`:

| Index | Element | prefix_xor (before) | prefix_xor (after) | Count Before | Beautiful Subarrays | res | count After |
|-------|---------|---------------------|-------------------|--------------|---------------------|-----|-------------|
| 0 | 4 | 0 | 4 | {0:1} | 0 | 0 | {0:1, 4:1} |
| 1 | 3 | 4 | 7 | {0:1, 4:1} | 0 | 0 | {0:1, 4:1, 7:1} |
| 2 | 1 | 7 | 6 | {0:1, 4:1, 7:1} | 0 | 0 | {0:1, 4:1, 6:1, 7:1} |
| 3 | 2 | 6 | 4 | {0:1, 4:1, 6:1, 7:1} | 1 (subarray [1,2,3]) | 1 | {0:1, 4:2, 6:1, 7:1} |
| 4 | 4 | 4 | 0 | {0:1, 4:2, 6:1, 7:1} | 1 (subarray [0,1,2,3,4]) | 2 | {0:2, 4:2, 6:1, 7:1} |

**2.4 Increment and Loop:**
For each element, we XOR it with the current prefix XOR, check how many times we've seen this value before, and update our counts.

**2.5 Return Result:**
After processing all elements, `res = 2`, which is the number of beautiful subarrays: `[3, 1, 2]` (XOR = 0) and `[4, 3, 1, 2, 4]` (XOR = 0).

