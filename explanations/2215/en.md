## 2215. Find the Difference of Two Arrays [Easy]

https://leetcode.com/problems/find-the-difference-of-two-arrays

## Description
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

**Examples**
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]

**Constraints**
- 1 <= nums1.length, nums2.length <= 1000
- -1000 <= nums1[i], nums2[i] <= 1000

## Hint
Use sets to efficiently find unique elements in each array.

## Explanation
Let's imagine you have two boxes of colored marbles (numbers). You want to find out which colors are only in the first box and which are only in the second. We use sets to quickly check for unique marbles in each box.

We do this because sets make it easy and fast to find differences—checking if something is in a set is much quicker than searching through a list. By converting the lists to sets, we can use set operations to get the answer efficiently.
