## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find all missing number ranges in a sorted array between a lower and upper bound. A range can be a single number or a range like "a->b". We must return the smallest sorted list of ranges that covers every missing number.

**1.1 Constraints & Complexity:**
- Input size: `0 <= nums.length <= 100`, `-10^9 <= lower <= upper <= 10^9`
- **Time Complexity:** O(n) where n is the length of nums - we iterate through the array once
- **Space Complexity:** O(1) excluding output - we only use a few variables
- **Edge Case:** If nums is empty, return the range [lower, upper]. If there are no gaps, return an empty list.

**1.2 High-level approach:**
We iterate through the array and check gaps between consecutive numbers. We also check the gap before the first number (from lower) and after the last number (to upper). For each gap, we format it as either a single number or a range.

![Finding missing ranges in sorted array](https://assets.leetcode.com/static_assets/others/missing-ranges.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check every number from lower to upper to see if it's in nums, which is O(upper - lower) and inefficient for large ranges.
- **Optimized Strategy:** Iterate through nums once, checking gaps between consecutive elements. This is O(n) regardless of the range size.
- **Why it's better:** We only process the actual numbers in the array, not every number in the range, making it much more efficient.

**1.4 Decomposition:**
1. Initialize a previous value to lower - 1 to track the last number we've seen
2. Append upper + 1 to nums temporarily to handle the gap after the last element
3. Iterate through each number in the modified array
4. Calculate the gap between previous and current number
5. If gap is 2, add a single number. If gap > 2, add a range

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [0,1,3,50,75]`, `lower = 0`, `upper = 99`
- Initialize `res = []`
- Initialize `prev = lower - 1 = -1`
- Append `upper + 1 = 100` to nums: `[0,1,3,50,75,100]`

**2.2 Start Checking:**
We begin iterating through the modified nums array.

**2.3 Trace Walkthrough:**

| num | prev | gap (num - prev) | Condition | Result | prev after |
|-----|------|-------------------|-----------|--------|------------|
| 0 | -1 | 1 | gap == 1 | Skip (no gap) | 0 |
| 1 | 0 | 1 | gap == 1 | Skip (no gap) | 1 |
| 3 | 1 | 2 | gap == 2 | Add "2" | 3 |
| 50 | 3 | 47 | gap > 2 | Add "4->49" | 50 |
| 75 | 50 | 25 | gap > 2 | Add "51->74" | 75 |
| 100 | 75 | 25 | gap > 2 | Add "76->99" | 100 |

**2.4 Increment and Loop:**
After processing each number, we update prev to the current number and continue to the next iteration.

**2.5 Return Result:**
Return `res = ["2", "4->49", "51->74", "76->99"]`, which represents all missing ranges between 0 and 99.

