## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to make every element in the array divisible by 3 by adding or subtracting 1. Each operation changes one element by 1, and we want the minimum number of operations.

**1.1 Constraints & Complexity:**
- Input size: `1 <= nums.length <= 50`, and each `1 <= nums[i] <= 50`
- **Time Complexity:** O(n) where n is the length of nums, as we iterate through each element once
- **Space Complexity:** O(1) as we only use a constant amount of extra space
- **Edge Case:** If an element is already divisible by 3, no operation is needed

**1.2 High-level approach:**
The goal is to count how many elements are not divisible by 3, since each such element requires exactly 1 operation to make it divisible by 3.

![Modulo operation visualization](https://assets.leetcode.com/static_assets/others/modulo-operation.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each element, try both adding and subtracting to find the minimum operations. This would be O(n) with unnecessary checks.
- **Optimized Strategy:** For any number x, if `x % 3 != 0`, we can always make it divisible by 3 with exactly 1 operation (either add `(3 - x % 3)` or subtract `(x % 3)`). This is O(n) with a single pass.

**1.4 Decomposition:**
1. Iterate through each number in the array
2. Check if the number is divisible by 3 using modulo operation
3. If not divisible, increment the operation count by 1
4. Return the total count of operations

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [1, 2, 3, 4]`
- Initialize `res = 0` to count operations

**2.2 Start Checking:**
We begin checking each element to see if it's divisible by 3.

**2.3 Trace Walkthrough:**
Using the example `nums = [1, 2, 3, 4]`:

| Element | Remainder (num % 3) | Is Divisible? | Operations Needed | res |
|---------|---------------------|---------------|-------------------|-----|
| 1 | 1 | No | 1 (subtract 1 → 0) | 1 |
| 2 | 2 | No | 1 (add 1 → 3) | 2 |
| 3 | 0 | Yes | 0 | 2 |
| 4 | 1 | No | 1 (subtract 1 → 3) | 3 |

**2.4 Increment and Loop:**
For each element that is not divisible by 3, we add 1 to our result counter. The loop continues until all elements are processed.

**2.5 Return Result:**
After processing all elements, `res = 3`, which is the minimum number of operations needed to make all elements divisible by 3.

