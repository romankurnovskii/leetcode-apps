# 136. Single Number [Easy]

[https://leetcode.com/problems/single-number](https://leetcode.com/problems/single-number)

## Description

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**
```text
Input: nums = [2,2,1]
Output: 1
```

**Example 2:**
```text
Input: nums = [4,1,2,1,2]
Output: 4
```

**Example 3:**
```text
Input: nums = [1]
Output: 1
```

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.

## Explanation

### Strategy

This is a **bit manipulation problem** that requires finding the single element in an array where all other elements appear twice. The key insight is to use the XOR (exclusive or) operation, which has special properties that make it perfect for this problem.

**Key observations:**
- XOR of a number with itself is 0: `a ^ a = 0`
- XOR of a number with 0 is the number itself: `a ^ 0 = a`
- XOR is associative and commutative: `a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b`
- All elements appear twice except one, so XORing all elements will cancel out the pairs

**High-level approach:**
1. **Initialize result**: Start with `result = 0`
2. **XOR all elements**: Iterate through the array and XOR each element with the result
3. **Return result**: The final result will be the single number

### Steps

Let's break down the solution step by step:

**Step 1: Initialize result**
- Start with `result = 0`

**Step 2: XOR all elements**
For each number in the array:
- XOR the current number with the result: `result = result ^ num`
- This will cancel out pairs and leave the single number

**Step 3: Return the result**
- The final result is the single number

**Example walkthrough:**
Let's trace through the second example:

```text
nums = [4,1,2,1,2]

Initial state:
result = 0

Step 1: result = 0 ^ 4 = 4

Step 2: result = 4 ^ 1 = 5

Step 3: result = 5 ^ 2 = 7

Step 4: result = 7 ^ 1 = 6

Step 5: result = 6 ^ 2 = 4

Result: Return 4
```

**Why this works:**
- `4 ^ 1 ^ 2 ^ 1 ^ 2`
- `= 4 ^ (1 ^ 1) ^ (2 ^ 2)`
- `= 4 ^ 0 ^ 0`
- `= 4 ^ 0`
- `= 4`

> **Note:** The XOR operation is perfect for this problem because it has the property that `a ^ a = 0` and `a ^ 0 = a`. This means that when you XOR all numbers, pairs of identical numbers will cancel out to 0, leaving only the single number.

**Time Complexity:** O(n) - you visit each element exactly once  
**Space Complexity:** O(1) - you only use a constant amount of extra space 