# 54. Spiral Matrix

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/spiral-matrix/

## Problem Description

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints:**
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Explanation

### Strategy

This is a **simulation problem** that requires traversing a matrix in spiral order. The key insight is to use boundary tracking and move inwards layer by layer, following the spiral pattern.

**Key observations:**
- We need to traverse the matrix in a spiral pattern: right → down → left → up
- We can use four boundaries: top, bottom, left, right
- After completing each direction, we move the corresponding boundary inward
- We continue until all elements are visited

**High-level approach:**
1. **Set boundaries**: Initialize top, bottom, left, right boundaries
2. **Traverse in spiral order**: Right → Down → Left → Up
3. **Update boundaries**: Move boundaries inward after each direction
4. **Check completion**: Stop when boundaries cross

### Steps

Let's break down the solution step by step:

**Step 1: Initialize boundaries**
- `top = 0, bottom = len(matrix) - 1`
- `left = 0, right = len(matrix[0]) - 1`

**Step 2: Traverse in spiral order**
While `top <= bottom` and `left <= right`:
- **Right**: Traverse from left to right on top row
- **Down**: Traverse from top to bottom on right column
- **Left**: Traverse from right to left on bottom row
- **Up**: Traverse from bottom to top on left column

**Step 3: Update boundaries**
After each direction:
- After right: `top++`
- After down: `right--`
- After left: `bottom--`
- After up: `left++`

**Example walkthrough:**
Let's trace through the first example:

```
matrix = [[1,2,3],[4,5,6],[7,8,9]]

Initial boundaries:
top = 0, bottom = 2, left = 0, right = 2

Step 1: Right (top row)
result = [1,2,3]
top = 1

Step 2: Down (right column)
result = [1,2,3,6,9]
right = 1

Step 3: Left (bottom row)
result = [1,2,3,6,9,8,7]
bottom = 1

Step 4: Up (left column)
result = [1,2,3,6,9,8,7,4]
left = 1

Step 5: Right (remaining elements)
result = [1,2,3,6,9,8,7,4,5]

Result: [1,2,3,6,9,8,7,4,5]
```

> **Note:** The key insight is to use boundary tracking to systematically traverse the matrix. This approach ensures we visit each element exactly once and handles edge cases like single rows or columns correctly.

### Solution

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle edge case
        if not matrix:
            return []
        
        # Initialize boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        
        # Traverse in spiral order
        while top <= bottom and left <= right:
            # Traverse right (top row)
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Traverse down (right column)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse left (bottom row) - check if still valid
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse up (left column) - check if still valid
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        # Return the spiral order
        return result
```

**Time Complexity:** O(m * n) - we visit each element exactly once  
**Space Complexity:** O(1) - we only use a constant amount of extra space (excluding the result array) 