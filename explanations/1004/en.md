## Max Consecutive Ones III [Medium]
https://leetcode.com/problems/max-consecutive-ones-iii

## Description

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive 1's in the array if you can flip at most `k` 0's.

Example:
```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1] -> flip two zeros

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
```

Constraints:
```
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
```

---

> **Hint:**  Use a sliding window to keep track of the number of zeros in the current window.

### Explanation

Let's imagine the array as a row of light switches, where 1 is on and 0 is off. We want to find the longest stretch of lights that can be on, if we're allowed to flip up to k switches from off to on.

We use a sliding window to keep track of the current stretch. Every time we add a new number, we check if we've flipped more than k zeros. If so, we move the left end of the window forward until we're back within our limit.

We do this because it lets us efficiently find the longest possible stretch without checking every possible subarray. By only moving the window when needed, we keep our solution fast and memory-efficient. 