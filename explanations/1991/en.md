## 1991. Find the Middle Index in Array [Easy]

https://leetcode.com/problems/find-the-middle-index-in-array

## Description
Given a 0-indexed integer array nums, find the leftmost middleIndex such that the sum of the numbers to the left of middleIndex is equal to the sum of the numbers to the right of middleIndex. Return -1 if no such index exists.

**Examples**
```tex
Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers to the left of index 3 is 4 (2+3-1), and to the right is also 4 (4).

Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers to the left of index 2 is 0 (1-1), and to the right is also 0.

Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.
```

**Constraints**
```tex
- 1 <= nums.length <= 100
- -1000 <= nums[i] <= 1000
```

## Hint
Use prefix sums to keep track of the left and right sums efficiently.

## Explanation
We want to find an index where the sum of all numbers to the left equals the sum to the right. We use a running total (prefix sum) as we move through the array, so we always know the sum to the left. The right sum can be found by subtracting the left sum and the current number from the total sum.

We do this because it lets us check each index in constant time, making our solution efficient. By using prefix sums, we avoid recalculating sums for every index, which would be much slower. 