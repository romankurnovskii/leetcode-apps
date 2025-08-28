## 2119. Minimum Number of Operations to Make Array Continuous [Hard]

https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous

## Description
You are given an integer array `nums`. In one operation, you can replace **any** element in `nums` with **any** integer.

`nums` is considered **continuous** if both of the following conditions are fulfilled:

- All elements in `nums` are **unique**.
- The difference between the **maximum** element and the **minimum** element in `nums` equals `nums.length - 1`.

For example, `nums = [4, 2, 5, 3]` is **continuous**, but `nums = [1, 2, 3, 5, 6]` is **not continuous**.

Return *the **minimum** number of operations to make* `nums` **continuous**.

**Examples**

```tex
Example 1:
Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.

Example 2:
Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

Example 3:
Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.
```

**Constraints**
```tex
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given an array, and you need to find the minimum number of operations to make it continuous. A continuous array has unique elements where the difference between max and min equals the length minus 1.

This is a **sliding window problem** that requires understanding what makes an array continuous and finding the optimal window of elements to keep.

**What is given?** An array of integers that can be very large (up to 100,000 elements).

**What is being asked?** Find the minimum operations to make the array continuous.

**Constraints:** The array can be up to 100,000 elements long, with values up to 10⁹.

**Edge cases:** 
- Single element array
- Already continuous array
- Array with all identical values
- Very large gaps between elements

**High-level approach:**
The solution involves sorting the array and using a sliding window approach to find the optimal subset of elements that can form a continuous array with minimal operations.

**Decomposition:**
1. **Sort the array**: This helps us identify potential continuous subsequences
2. **Use sliding window**: Find the longest window that can be made continuous
3. **Calculate operations**: Determine how many elements need to be changed
4. **Find minimum**: Try different window sizes to find the optimal solution

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible subsets. This is extremely inefficient.
- **Optimized**: Use sliding window with binary search. This takes O(n log n) time.

### Steps
Let's walk through the solution step by step using the second example: `nums = [1,2,3,5,6]`

**Step 1: Sort the array**
- Original: [1,2,3,5,6]
- Sorted: [1,2,3,5,6] (already sorted)

**Step 2: Understand what makes an array continuous**
- For length 5, we need: max - min = 5 - 1 = 4
- So we need elements that span exactly 4 values
- Example: [1,2,3,4,5] has max=5, min=1, difference=4 ✓

**Step 3: Use sliding window approach**
- Start with window size = array length
- Try to find a window that can be made continuous
- For each window, calculate how many operations are needed

**Step 4: Calculate operations for different windows**
- **Window [1,2,3,5,6]**: 
  - Current span: 6 - 1 = 5
  - Need span: 5 - 1 = 4
  - Gap: 5 - 4 = 1
  - Operations needed: 1 (change 6 to 4)

- **Window [1,2,3,5]**:
  - Current span: 5 - 1 = 4
  - Need span: 4 - 1 = 3
  - Gap: 4 - 3 = 1
  - Operations needed: 1 (change 5 to 3)

- **Window [2,3,5,6]**:
  - Current span: 6 - 2 = 4
  - Need span: 4 - 1 = 3
  - Gap: 4 - 3 = 1
  - Operations needed: 1 (change 6 to 4)

**Step 5: Find optimal solution**
- Minimum operations: 1
- Optimal window: [1,2,3,5] → change 5 to 4 → [1,2,3,4]

**Why this works:**
The sliding window approach works because:
1. **Optimal substructure**: The best solution for a larger array must include the best solution for a smaller subarray
2. **Monotonicity**: If a window of size k can be made continuous, then a window of size k-1 can also be made continuous
3. **Efficiency**: We only need to check O(n) different window sizes instead of all possible subsets

> **Note:** The key insight is that we can use a sliding window to find the longest subsequence that can be made continuous, and then calculate the minimum operations needed. This avoids the need to try all possible combinations.

**Time Complexity:** O(n log n) - sorting takes O(n log n), sliding window takes O(n)  
**Space Complexity:** O(1) - we only need a few variables for the sliding window
