## Description

Given a non-negative integer `x`, return *the square root of* `x` *rounded down to the nearest integer*. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

**Example 1:**
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

**Example 2:**
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

**Constraints:**
- `0 <= x <= 2^31 - 1`

## Explanation

### Strategy

This is a **binary search problem** that requires finding the integer square root of a number. The key insight is to use binary search to find the largest integer whose square is less than or equal to the given number.

**Key observations:**
- The square root of x is the largest integer k where k² ≤ x
- We can use binary search to find this value efficiently
- The search range is from 0 to x (or x/2 for optimization)
- We need to handle edge cases (x = 0, x = 1)

**High-level approach:**
1. **Set search boundaries**: left = 0, right = x
2. **Binary search**: Find the largest k where k² ≤ x
3. **Check mid value**: If mid² ≤ x, search right half
4. **Update boundaries**: Narrow down the search range
5. **Return result**: Return the largest valid value

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If x is 0 or 1, return x

**Step 2: Initialize binary search**
- `left = 0, right = x`

**Step 3: Binary search**
- While `left <= right`:
  - Calculate `mid = (left + right) // 2`
  - If `mid * mid <= x`: search right half
  - Else: search left half

**Step 4: Return result**
- Return `right` (the largest value where k² ≤ x)

**Example walkthrough:**
Let's trace through the second example:

```
x = 8

Step 1: Initialize
left = 0, right = 8

Step 2: First iteration
mid = (0 + 8) // 2 = 4
4 * 4 = 16 > 8, so search left half
right = 3

Step 3: Second iteration
mid = (0 + 3) // 2 = 1
1 * 1 = 1 <= 8, so search right half
left = 2

Step 4: Third iteration
mid = (2 + 3) // 2 = 2
2 * 2 = 4 <= 8, so search right half
left = 3

Step 5: Fourth iteration
mid = (3 + 3) // 2 = 3
3 * 3 = 9 > 8, so search left half
right = 2

Step 6: Exit loop
left = 3, right = 2, so left > right

Result: Return 2
```

> **Note:** The key insight is that we can use binary search to efficiently find the largest integer whose square is less than or equal to x. This approach has logarithmic time complexity and avoids the need for built-in exponent functions.

### Solution

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle edge cases
        if x == 0 or x == 1:
            return x
        
        # Binary search
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid * mid <= x
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        # Return the largest value where k² ≤ x
        return right
```

**Time Complexity:** O(log x) - binary search  
**Space Complexity:** O(1) - we only use a constant amount of extra space 