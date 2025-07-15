## 283. Move Zeroes [Easy]

https://leetcode.com/problems/move-zeroes

## Description

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

**Examples**

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]

**Constraints**

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

## Hint

> Use two pointers: one to keep track of the current position to place a non-zero, and one to iterate through the array.

## Explanation

We use two pointers: one iterates through the array, and the other keeps track of where to place the next non-zero element. As we iterate, whenever we find a non-zero, we place it at the position of the first pointer and increment it. After all non-zeros are placed, we fill the rest of the array with zeros.

This approach ensures all non-zero elements retain their original order, and all zeros are moved to the end efficiently in a single pass.
