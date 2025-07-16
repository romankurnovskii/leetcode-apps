## 2352. Equal Row and Column Pairs [Medium]

https://leetcode.com/problems/equal-row-and-column-pairs

## Description
Given a 0-indexed n x n integer matrix grid, return the number of pairs (r_i, c_j) such that row r_i and column c_j are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

**Examples**
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

**Constraints**
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5

## Hint
We can use nested loops to compare every row against every column. Another loop is necessary to compare the row and column element by element. It is also possible to hash the arrays and compare the hashed values instead.

## Explanation
To count equal row and column pairs, we can compare each row with each column. For each row, we check if it matches any column by comparing their elements one by one. To make this efficient, we can use tuples or hashable representations of rows and columns and count their occurrences. If a row matches a column, we increment our answer.

This approach is efficient for n up to 200, and using hash maps or tuples makes the comparison fast and easy to implement. 