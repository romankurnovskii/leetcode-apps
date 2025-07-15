## Description

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false.

Example:
```
Input: nums = [1,2,3,4,5]
Output: true
```

Constraints:
```
- 1 <= nums.length <= 5 * 10^5
- -2^31 <= nums[i] <= 2^31 - 1
```

## Hint

> Track the smallest and second smallest values as you iterate.

## Explanation

Let's imagine you're looking for three numbers in order, each bigger than the last. We keep track of the smallest number we've seen so far, and then the next smallest after that. If we find a number bigger than both, we know we have a triplet!

We do this because it's much faster than checking every possible combination. By updating our two smallest values as we go, we make sure we're always ready to spot a valid triplet as soon as it appears.

This approach is efficient and uses only constant extra space, making it perfect for large arrays.
