# 67. Add Binary

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/add-binary/

## Problem Description

Given two binary strings `a` and `b`, return *their sum as a binary string*.

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

**Constraints:**
- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## Explanation

### Strategy

This is a **string manipulation problem** that simulates binary addition. The key insight is to work from right to left (least significant bit first) and handle the carry properly, just like manual binary addition.

**Key observations:**
- We need to work from right to left (least significant bit first)
- We need to handle carry (when sum is 2 or 3)
- We need to handle strings of different lengths
- The result might be longer than the input strings due to carry

**High-level approach:**
1. **Start from the end**: Iterate from the last character of both strings
2. **Add corresponding bits**: Add bits from both strings plus carry
3. **Calculate result bit**: Result bit = sum % 2
4. **Update carry**: Carry = sum // 2
5. **Handle remaining bits**: Process any remaining bits from longer string
6. **Add final carry**: If carry remains, add it to the beginning

### Steps

Let's break down the solution step by step:

**Step 1: Initialize variables**
- `result = ""`: Store the result string
- `carry = 0`: Track the carry
- `i, j`: Pointers for both strings

**Step 2: Add corresponding bits**
- While both strings have bits: add bits + carry
- Calculate result bit: `sum % 2`
- Update carry: `sum // 2`

**Step 3: Handle remaining bits**
- Process remaining bits from longer string
- Continue adding with carry

**Step 4: Add final carry**
- If carry is 1, add it to the beginning

**Example walkthrough:**
Let's trace through the first example:

```
a = "11", b = "1"

Step 1: Initialize
result = "", carry = 0, i = 1, j = 0

Step 2: Add corresponding bits
i = 1, j = 0: a[1] = '1', b[0] = '1'
sum = 1 + 1 + 0 = 2
result_bit = 2 % 2 = 0
carry = 2 // 2 = 1
result = "0"

Step 3: Continue
i = 0, j = -1: a[0] = '1', b[-1] = None
sum = 1 + 0 + 1 = 2
result_bit = 2 % 2 = 0
carry = 2 // 2 = 1
result = "00"

Step 4: Add final carry
carry = 1, so add to beginning
result = "100"

Result: "100"
```

> **Note:** The key insight is to work from right to left, just like manual binary addition. This approach handles all cases including different string lengths and carry overflow.

### Solution

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize variables
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Add corresponding bits
        while i >= 0 or j >= 0:
            # Get current bits (0 if index is out of range)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate sum
            total = bit_a + bit_b + carry
            
            # Calculate result bit and carry
            result_bit = total % 2
            carry = total // 2
            
            # Add result bit to beginning
            result = str(result_bit) + result
            
            # Move pointers
            i -= 1
            j -= 1
        
        # Add final carry if exists
        if carry:
            result = "1" + result
        
        # Return result
        return result
```

**Time Complexity:** O(max(len(a), len(b))) - we visit each character at most once  
**Space Complexity:** O(max(len(a), len(b))) - to store the result string 