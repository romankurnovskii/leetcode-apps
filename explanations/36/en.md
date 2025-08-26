Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

**Example 1:**

![Sudoku Example](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```raw
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:**

```raw
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Constraints:**
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

## Explanation

### Strategy

This is a **matrix validation problem** that requires checking three different types of constraints on a 9x9 Sudoku board. The key insight is that we need to validate three separate aspects:

1. **Row validation**: Each row must contain unique digits 1-9
2. **Column validation**: Each column must contain unique digits 1-9  
3. **3x3 box validation**: Each 3x3 sub-box must contain unique digits 1-9

The problem gives us a 9x9 grid where some cells contain digits (1-9) and others contain dots ('.') representing empty cells. We only need to validate the filled cells according to the three rules above.

**Key observations:**
- We can ignore empty cells ('.') - they don't affect validity
- We need to track which numbers we've seen in each row, column, and 3x3 box
- If we see the same number twice in any row, column, or box, the board is invalid
- We can use hash sets or arrays to track seen numbers efficiently

**High-level approach:**
1. Create data structures to track seen numbers in each row, column, and 3x3 box
2. Iterate through each cell in the board
3. For each filled cell (not '.'), check if its number is already seen in its row, column, or 3x3 box
4. If any duplicate is found, return false
5. If we complete the entire board without finding duplicates, return true

### Steps

Let's break down the solution step by step:

**Step 1: Set up tracking data structures**
We need three ways to track seen numbers:
- `rows[i]`: Set of numbers seen in row i
- `cols[j]`: Set of numbers seen in column j  
- `boxes[k]`: Set of numbers seen in 3x3 box k

The box index can be calculated as: `box_index = (row // 3) * 3 + (col // 3)`

**Step 2: Iterate through the board**
For each cell at position (i, j):
- If the cell is empty ('.'), skip it
- If the cell has a number, check if it's already in the corresponding row, column, or box sets

**Step 3: Check for duplicates**
For each filled cell with number `num`:
- Check if `num` is in `rows[i]` - if yes, return false
- Check if `num` is in `cols[j]` - if yes, return false  
- Check if `num` is in `boxes[box_index]` - if yes, return false
- If no duplicates found, add `num` to all three sets

**Step 4: Return result**
If we complete the entire board without finding any duplicates, return true.

**Example walkthrough:**
Let's trace through the first example:


Row 0: ["5","3",".",".","7",".",".",".","."]
- Add 5 to row[0], col[0], box[0]
- Add 3 to row[0], col[1], box[0] 
- Skip "." (empty)
- Skip "." (empty)
- Add 7 to row[0], col[4], box[1]
- Continue...

The key insight is that we can process the entire board in a single pass, checking all three constraints (row, column, box) for each filled cell.

> **Note:** The box calculation `(row // 3) * 3 + (col // 3)` maps each cell to one of 9 boxes (0-8). For example, cell (4, 5) is in box `(4 // 3) * 3 + (5 // 3) = 1 * 3 + 1 = 4`.


**Time Complexity:** O(9²) = O(81) = O(1) since the board is always 9x9  
**Space Complexity:** O(9²) = O(81) = O(1) for storing the sets 