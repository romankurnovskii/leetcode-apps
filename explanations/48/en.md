# 48. Rotate Image [Medium]

[https://leetcode.com/problems/rotate-image/](https://leetcode.com/problems/rotate-image/)

## Problem Description

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**
![Rotate Image Example 1](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2:**
![Rotate Image Example 2](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Constraints:**
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Explanation

### Strategy

This is a **matrix transformation problem** that requires rotating a 2D matrix by 90 degrees clockwise **in-place**. The key challenge is understanding the pattern of how elements move during rotation and finding a way to perform this transformation without using extra space.

**Key observations:**
- A 90-degree clockwise rotation transforms the matrix in a specific pattern
- The first row becomes the last column (in reverse order)
- The second row becomes the second-to-last column (in reverse order)
- And so on...
- We need to perform this transformation without allocating a new matrix

**High-level approach:**
1. **Understand the rotation pattern**: For a 90-degree clockwise rotation, each element moves to a new position
2. **Find the mathematical relationship**: For an n×n matrix, element at (i,j) moves to (j, n-1-i)
3. **Use a two-step process**: 
   - First, transpose the matrix (swap rows and columns)
   - Then, reverse each row
4. **Perform in-place**: Modify the matrix directly without extra space

### Steps

Let's break down the solution step by step:

**Step 1: Understand the rotation pattern**
For a 3×3 matrix:
```
Original:     After 90° rotation:
[1,2,3]      [7,4,1]
[4,5,6]  →   [8,5,2]
[7,8,9]      [9,6,3]
```

Notice that:
- The first row `[1,2,3]` becomes the last column `[1,2,3]` (but reversed)
- The second row `[4,5,6]` becomes the middle column `[4,5,6]` (but reversed)
- The third row `[7,8,9]` becomes the first column `[7,8,9]` (but reversed)

**Step 2: Use transpose + reverse approach**
Instead of directly implementing the rotation, we can use a clever two-step process:

1. **Transpose the matrix**: Swap elements across the main diagonal
   ```
   [1,2,3]    [1,4,7]
   [4,5,6] →  [2,5,8]
   [7,8,9]    [3,6,9]
   ```

2. **Reverse each row**: This gives us the final rotated matrix
   ```
   [1,4,7]    [7,4,1]
   [2,5,8] →  [8,5,2]
   [3,6,9]    [9,6,3]
   ```

**Step 3: Implement transpose in-place**
To transpose a matrix in-place:
- For each element at position (i,j) where i < j, swap it with element at (j,i)
- We only need to swap elements above the diagonal to avoid double-swapping

**Step 4: Reverse each row**
After transpose, simply reverse each row to get the final rotated matrix.

**Example walkthrough:**
Let's trace through the first example:

```
Original matrix:
[1,2,3]
[4,5,6]
[7,8,9]

Step 1: Transpose (swap across diagonal)
[1,4,7]
[2,5,8]
[3,6,9]

Step 2: Reverse each row
[7,4,1]
[8,5,2]
[9,6,3]
```

> **Note:** This approach works for any n×n matrix. The transpose operation swaps elements across the main diagonal, and reversing each row completes the 90-degree clockwise rotation.

**Time Complexity:** O(n²) - we need to visit each element once for transpose and once for reverse  
**Space Complexity:** O(1) - we modify the matrix in-place without extra space 