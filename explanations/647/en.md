## 647. Longest Subarray of 1's After Deleting One Element [Medium]

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

## Description
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

**Examples**
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

**Constraints**
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

## Hint
Use a sliding window to keep at most one zero in the window.

## Explanation
We want the longest run of 1's after deleting one element. That means we can have at most one zero in our current window, since deleting it would leave only 1's.

We use a sliding window to keep track of the current sequence. Every time we have more than one zero, we move the left end of the window forward until we're back to at most one zero.

We do this because it lets us efficiently find the longest possible sequence without checking every possible subarray. By only moving the window when needed, we keep our solution fast and memory-efficient, especially for large arrays. 