## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the longest valid subsequence where the sum of each pair of consecutive elements has the same parity (all even or all odd). A valid subsequence means (sub[0]+sub[1])%2 == (sub[1]+sub[2])%2 == ...

**1.1 Constraints & Complexity:**
- Input size: `2 <= nums.length <= 2 * 10^5`
- **Time Complexity:** O(n) where n is the length of nums, as we check 4 patterns in one pass
- **Space Complexity:** O(1) as we only track counters
- **Edge Case:** If all numbers have the same parity, the entire array is valid

**1.2 High-level approach:**
There are only 4 possible patterns: all even, all odd, even-odd alternating, or odd-even alternating. We try all four patterns and find the longest subsequence matching each pattern.

![Parity pattern visualization](https://assets.leetcode.com/static_assets/others/pattern-matching.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible subsequences, which is exponential
- **Optimized Strategy:** Recognize there are only 4 parity patterns, try each in one pass, achieving O(n) time
- **Emphasize the optimization:** By limiting to 4 patterns, we can check each in linear time instead of exponential search

**1.4 Decomposition:**
1. Try pattern 1: Count all even numbers
2. Try pattern 2: Count all odd numbers
3. Try pattern 3: Count even-odd alternating sequence
4. Try pattern 4: Count odd-even alternating sequence
5. Return the maximum count across all patterns

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [1,2,3,4]`
- Initialize: `res = 0`

**2.2 Start Processing:**
We try each of the 4 patterns.

**2.3 Trace Walkthrough:**

| Pattern | Description | Count | Result |
|---------|------------|-------|--------|
| All even | [2, 4] | 2 | 2 |
| All odd | [1, 3] | 2 | 2 |
| Even-odd | [2, 3] or [4] | 2 | 2 |
| Odd-even | [1, 2, 3, 4] | 4 | 4 |

For odd-even: Start with 1 (odd), then 2 (even), then 3 (odd), then 4 (even) = 4 elements

**2.4 Increment and Loop:**
After checking all patterns, we have the maximum.

**2.5 Return Result:**
The result is 4, which is the length of the longest valid subsequence [1, 2, 3, 4].
