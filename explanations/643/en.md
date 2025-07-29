## 643. Maximum Average Subarray I [Easy]

https://leetcode.com/problems/maximum-average-subarray-i

## Description
Given an array consisting of n integers, find the contiguous subarray of length k that has the maximum average value. Return this value.

**Examples**
```text
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Input: nums = [5], k = 1
Output: 5.0
```

**Constraints**
```text
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4
```

## Hint
Use a sliding window to keep track of the sum of `k` elements.

## Explanation
Let's imagine the array as a long row of numbers. We want to find a group of `k` numbers in a row that, when averaged, gives us the biggest value. Instead of checking every possible group from scratch, we use a sliding window: we add the next number and remove the first number from the previous group.

We do this because it saves us from recalculating the sum for every window, making our solution much faster, especially for large arrays. By updating the sum as we slide the window, we always know the current total for the `k` numbers we're looking at.

This approach is efficient and perfect for problems where you need to look at all subarrays of a fixed size. 