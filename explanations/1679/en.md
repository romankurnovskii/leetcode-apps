## Max Number of K-Sum Pairs [Medium]

https://leetcode.com/problems/max-number-of-k-sum-pairs

## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example:
```
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
```

Constraints:
```
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
```

> **Hint:**  Use a hash map to count occurrences and find pairs efficiently.

### Explanation

Imagine you have a bag of numbers and you want to make as many pairs as possible that add up to k. For each number, check if you have seen its complement (k - number) before. If so, you can make a pair! Use a hash map to keep track of the numbers you have seen and how many are left.

This approach is efficient because it lets you find pairs in a single pass through the array. 