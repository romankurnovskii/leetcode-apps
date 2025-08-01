# 66. Plus One

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/plus-one/

## Problem Description

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return *the resulting array of digits*.

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

**Example 3:**
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

**Constraints:**
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`'s.

## Explanation

### Strategy

This is a **array manipulation problem** that simulates adding 1 to a large integer represented as an array of digits. The key insight is to work from right to left and handle the carry properly.

**Key observations:**
- We need to work from right to left (least significant digit first)
- If a digit becomes 10, we need to carry 1 to the next position
- If all digits are 9, we need to add a new digit at the beginning
- We can modify the array in-place for most cases

**High-level approach:**
1. **Start from the end**: Iterate from the last digit
2. **Add one**: Add 1 to the current digit
3. **Handle carry**: If digit becomes 10, set to 0 and carry 1
4. **Check completion**: If no carry, return the array
5. **Handle overflow**: If carry remains, add new digit at beginning

### Steps

Let's break down the solution step by step:

**Step 1: Start from the end**
- Iterate from the last digit to the first

**Step 2: Add one to current digit**
- Add 1 to the current digit

**Step 3: Check for carry**
- If digit is 10, set to 0 and carry 1
- If digit is less than 10, no carry needed

**Step 4: Handle overflow**
- If we reach the beginning with carry, add new digit

**Example walkthrough:**
Let's trace through the third example:

```
digits = [9]

Step 1: Start from end
i = 0, digit = 9

Step 2: Add one
digits[0] = 9 + 1 = 10

Step 3: Handle carry
digits[0] = 0, carry = 1

Step 4: Check completion
carry = 1, so we need to add new digit

Step 5: Handle overflow
result = [1, 0]

Result: [1, 0]
```

> **Note:** The key insight is to work from right to left, just like how we add numbers manually. This approach handles all cases including the edge case where all digits are 9 and we need to add a new digit.

### Solution

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # Add one to current digit
            digits[i] += 1
            
            # If digit is less than 10, no carry needed
            if digits[i] < 10:
                return digits
            
            # Handle carry: set current digit to 0
            digits[i] = 0
        
        # If we reach here, all digits were 9
        # Add new digit at the beginning
        return [1] + digits
```

**Time Complexity:** O(n) - we visit each digit at most once  
**Space Complexity:** O(1) - we modify the array in-place (except for the edge case) 