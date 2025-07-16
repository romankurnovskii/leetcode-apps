## 238. Product of Array Except Self [Medium]

https://leetcode.com/problems/product-of-array-except-self

## Description
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Examples**
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

**Constraints**
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

## Hint
Use two passes: one to calculate products to the left of each index, and one for the right.

## Explanation
We want to find the product of all numbers except the one at each position. If we used division, we could just multiply everything and divide by nums[i], but the problem says no division!

So, we use two passes. First, we go from left to right, building up the product of all numbers to the left of each index. We do this because it lets us know, for each position, what the product is before that number.

Then, we go from right to left, multiplying each answer by the product of all numbers to the right. This way, each answer[i] ends up being the product of everything except nums[i].

This approach is efficient because it only needs two passes and uses O(1) extra space (not counting the output array), making it perfect for large arrays.
