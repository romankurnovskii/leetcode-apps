## Explanation

### Strategy (The "Why")

**Restate the problem:** We can flip any 3 consecutive elements in a binary array. We need to find the minimum number of operations to make all elements equal to 1, or return -1 if impossible.

**1.1 Constraints & Complexity:**
- Input size: `3 <= nums.length <= 10^5`
- **Time Complexity:** O(n) where n is the length of nums, as we process each element once
- **Space Complexity:** O(1) as we modify the array in place
- **Edge Case:** If the array length is not a multiple of 3 and has zeros at the end, it might be impossible

**1.2 High-level approach:**
Use a greedy approach: process from left to right. When we encounter a 0, we must flip it (along with the next 2 elements). If we can't flip (not enough elements remaining), return -1.

![Greedy algorithm visualization](https://assets.leetcode.com/static_assets/others/greedy-algorithm.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible sequences of flips, which is exponential
- **Optimized Strategy:** Greedily flip from left to right whenever we see a 0, achieving O(n) time
- **Emphasize the optimization:** The greedy approach ensures we fix problems as early as possible, avoiding the need to backtrack

**1.4 Decomposition:**
1. Iterate through the array from left to right
2. When we encounter a 0, flip it along with the next 2 elements
3. If we can't flip (not enough elements), return -1
4. After processing all elements, verify all are 1
5. Return the operation count or -1

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [0,1,1,1,0,0]`
- Initialize: `res = 0`, `i = 0`

**2.2 Start Processing:**
We iterate through the array, flipping when needed.

**2.3 Trace Walkthrough:**

| i | nums[i] | Action | nums After | res |
|---|---------|--------|------------|-----|
| 0 | 0 | Flip [0,1,2] | [1,0,0,1,0,0] | 1 |
| 1 | 0 | Flip [1,2,3] | [1,1,1,0,0,0] | 2 |
| 2 | 1 | Skip | [1,1,1,0,0,0] | 2 |
| 3 | 0 | Flip [3,4,5] | [1,1,1,1,1,1] | 3 |

**2.4 Increment and Loop:**
After processing all elements, we verify all are 1.

**2.5 Return Result:**
The result is 3, which is the minimum number of operations to make all elements equal to 1.
