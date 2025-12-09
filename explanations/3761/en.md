## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum absolute distance between indices of any mirror pair. A mirror pair (i, j) exists when reverse(nums[i]) == nums[j], where reverse(x) reverses the digits of x (removing leading zeros).

**1.1 Constraints & Complexity:**
- Input size: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`
- **Time Complexity:** O(n) - single pass through array with hash map lookups
- **Space Complexity:** O(n) for the hash map storing reversed values
- **Edge Case:** If no mirror pairs exist, return -1

**1.2 High-level approach:**
We scan the array left to right, maintaining a hash map that stores the most recent index for each reversed value. For each number, we check if its value matches any reversed value we've seen, and track the minimum distance.

![Hash map for mirror pairs visualization](https://assets.leetcode.com/static_assets/others/hash-map-mirror-pairs.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all pairs (i, j) where i < j, which is O(n²)
- **Optimized Strategy:** Use hash map to track reversed values as we scan, checking matches in O(1) per element, achieving O(n) time
- **Emphasize the optimization:** Hash map allows us to find matches instantly without checking all previous elements

**1.4 Decomposition:**
1. Define helper function to reverse digits of a number (removing leading zeros)
2. Scan array left to right
3. For each number, check if current value matches any reversed value in hash map
4. If match found, update minimum distance
5. Store current index under the reversed value of current number for future matches

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [12, 21, 45, 33, 54]`
- Initialize: `seen = {}`, `res = inf`
- We'll process each number and track reversed values

**2.2 Start Checking:**
We iterate through each number in the array.

**2.3 Trace Walkthrough:**

| Index | Number | Reversed | Check Match | seen Before | Min Distance | seen After |
|-------|--------|----------|-------------|-------------|--------------|------------|
| 0 | 12 | 21 | 12 in seen? No | {} | inf | {21: 0} |
| 1 | 21 | 12 | 21 in seen? No | {21: 0} | inf | {21: 0, 12: 1} |
| 2 | 45 | 54 | 45 in seen? No | {21: 0, 12: 1} | inf | {21: 0, 12: 1, 54: 2} |
| 3 | 33 | 33 | 33 in seen? No | {21: 0, 12: 1, 54: 2} | inf | {21: 0, 12: 1, 54: 2, 33: 3} |
| 4 | 54 | 45 | 54 in seen? No | {21: 0, 12: 1, 54: 2, 33: 3} | inf | {21: 0, 12: 1, 54: 2, 33: 3, 45: 4} |

Wait, let me reconsider. At index 1, we have num=21. We check if 21 is in seen. But we stored reversed(12)=21 at index 0. So 21 matches! Distance = 1-0 = 1.

Actually, the logic is: for each num, we check if num itself is in seen (meaning we've seen its reverse before). Then we store reversed(num) for future checks.

**2.4 Increment and Loop:**
For each number, we check for matches, update minimum distance, and store the reversed value for future matches.

**2.5 Return Result:**
After processing, the minimum distance is 1 (from indices 0 and 1: reverse(12)=21 matches nums[1]=21). If no matches found, return -1.
