# 169. Majority Element [Easy]

https://leetcode.com/problems/majority-element/

## Description

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**
```text
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**
```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**
```text
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
```

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## Explanation

### Strategy

This is a **counting and voting problem** that requires finding the element that appears more than half the time in an array. The key insight is that since the majority element appears more than `⌊n/2⌋` times, it will always "win" in a voting process.

**Key observations:**
- The majority element appears more than half the time
- You can use a voting algorithm (Boyer-Moore Voting Algorithm)
- The majority element will always have a positive count at the end
- You don't need to count all occurrences, just track the current candidate

**High-level approach:**

1. **Use a voting algorithm**: Track a candidate and its count
2. **Initialize**: Set the first element as candidate with count 1
3. **Iterate through array**: For each element, either increment count or change candidate
4. **Return the winner**: The candidate at the end is the majority element

> Boyer-Moore Voting Algorithm

### Steps

Let's break down the solution step by step:

**Step 1: Initialize the voting process**
- Set the first element as the candidate
- Set the count to 1

**Step 2: Iterate through the array**
For each element starting from the second:
- If the current element equals the candidate, increment count
- If the current element is different from the candidate, decrement count
- If count becomes 0, set the current element as the new candidate with count 1

**Step 3: Return the result**
- The candidate at the end is guaranteed to be the majority element

**Example walkthrough:**
Let's trace through the second example:

```sh
nums = [2,2,1,1,1,2,2]

Initial state:
candidate = 2, count = 1

Step 1: nums[1] = 2 == candidate
count = 2

Step 2: nums[2] = 1 != candidate
count = 1

Step 3: nums[3] = 1 != candidate
count = 0, set candidate = 1, count = 1

Step 4: nums[4] = 1 == candidate
count = 2

Step 5: nums[5] = 2 != candidate
count = 1

Step 6: nums[6] = 2 != candidate
count = 0, set candidate = 2, count = 1

Result: Return candidate = 2
```

> **Note:** The Boyer-Moore Voting Algorithm works because the majority element appears more than half the time. Even if all other elements "vote against" it, it will still have a positive count at the end.

**Time Complexity:** O(n) - you visit each element exactly once  
**Space Complexity:** O(1) - you only use a constant amount of extra space
