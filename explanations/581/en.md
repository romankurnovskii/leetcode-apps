## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= nums.length <= 10^4`.
- **Value Range:** `-10^5 <= nums[i] <= 10^5`.
- **Time Complexity:** O(n) - we make a few passes through the array.
- **Space Complexity:** O(1) - we only use a constant amount of extra space.
- **Edge Case:** If the array is already sorted, return 0.

**1.2 High-level approach:**

The goal is to find the shortest unsorted subarray that, when sorted, makes the entire array sorted. The approach involves finding the left and right boundaries of the unsorted region, then extending these boundaries based on the minimum and maximum values within the unsorted region.

![Visualization showing the unsorted subarray and how boundaries are extended based on min/max values]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subarrays, sort each one, and check if sorting it makes the entire array sorted. This takes O(n³) time.
- **Optimized Strategy:** Find the boundaries of the unsorted region by scanning from both ends, then extend based on min/max values. This takes O(n) time.
- **Why it's better:** The optimized approach finds the answer in linear time by identifying the problem region and extending it only as necessary.

**1.4 Decomposition:**

1. Find the left boundary: the first index where the order breaks (nums[i] > nums[i+1]).
2. Find the right boundary: the last index where the order breaks (nums[i] < nums[i-1]).
3. If the array is already sorted, return 0.
4. Find the minimum and maximum values in the unsorted subarray.
5. Extend the left boundary backward if there are values greater than the minimum.
6. Extend the right boundary forward if there are values less than the maximum.
7. Return the length of the unsorted subarray.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [2, 6, 4, 8, 10, 9, 15]`.

We need to find the shortest unsorted subarray.

**2.2 Start Checking:**

First, find the left boundary where order breaks.

**2.3 Trace Walkthrough:**

| Step | Action | left | right | Condition | Result |
|------|--------|------|-------|-----------|--------|
| 1 | Find left boundary | 0 | - | Check nums[i] <= nums[i+1] | left = 1 (nums[1]=6 > nums[2]=4) |
| 2 | Find right boundary | 1 | 6 | Check nums[i] >= nums[i-1] | right = 4 (nums[4]=10 > nums[5]=9) |
| 3 | Find min in subarray | 1 | 4 | min(nums[1:5]) | sub_min = 4 |
| 4 | Find max in subarray | 1 | 4 | max(nums[1:5]) | sub_max = 10 |
| 5 | Extend left | 1 | 4 | nums[0]=2 > sub_min=4? No | left = 1 |
| 6 | Extend right | 1 | 4 | nums[5]=9 < sub_max=10? Yes | right = 5 |

Detailed walkthrough:
- Step 1: Scan from left. At index 1, `nums[1] = 6 > nums[2] = 4`, so left boundary is 1.
- Step 2: Scan from right. At index 4, `nums[4] = 10 > nums[5] = 9`, so right boundary is 4.
- Step 3: In subarray `[6, 4, 8, 10]`, min is 4, max is 10.
- Step 4: Check if we need to extend left: `nums[0] = 2` is not greater than `sub_min = 4`, so no extension.
- Step 5: Check if we need to extend right: `nums[5] = 9` is less than `sub_max = 10`, so extend right to 5.

**2.4 Increment and Loop:**

The unsorted subarray is from index 1 to 5: `[6, 4, 8, 10, 9]`.

**2.5 Return Result:**

Return `res = 5` - the length of the unsorted subarray is 5 (indices 1 to 5, inclusive).

