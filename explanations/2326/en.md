## Explanation

### Strategy

**Constraints & Edge Cases**

* **Matrix Size:** m and n can be up to 10^5, but m*n ≤ 10^5. The linked list has 1 to m*n nodes.
* **Time Complexity:** We traverse the linked list once and fill the matrix in spiral order. **Time Complexity: O(m * n)**, **Space Complexity: O(m * n)** for the result matrix.
* **Edge Case:** If the linked list has fewer nodes than m*n, remaining cells are filled with -1.

**High-level approach**

The problem asks us to fill an m x n matrix in spiral (clockwise) order starting from top-left, using values from a linked list. We use direction vectors to navigate the spiral pattern.

**Brute force vs. optimized strategy**

* **Brute Force:** This is essentially what we do - traverse in spiral order. There's no more efficient way.
* **Optimized:** Use direction vectors [(0,1), (1,0), (0,-1), (-1,0)] to represent right, down, left, up. When we hit a boundary or visited cell, rotate direction.

**Decomposition**

1. **Initialize Matrix:** Create m x n matrix filled with -1.
2. **Spiral Traversal:** Use direction vectors to move in spiral pattern.
3. **Direction Change:** When hitting boundary or visited cell, rotate to next direction.
4. **Fill Values:** Place linked list values as we traverse.

### Steps

1. **Initialization & Example Setup**
   Let's use `m = 3`, `n = 5`, `head = [3,0,2,6,8,1,7,9,4,2,5,5,0]` as our example.
   - Initialize `res = [[-1]*5 for _ in range(3)]`.
   - Directions: `[(0,1), (1,0), (0,-1), (-1,0)]` (right, down, left, up).
   - Start at `(0,0)` with `dir_idx = 0` (right).

2. **Spiral Traversal**
   - Place head.val = 3 at (0,0), move right.
   - Continue placing values and moving in current direction.
   - When hitting boundary or -1 (visited), change direction.

3. **Trace Walkthrough**

| Step | Position | Value | Direction | Next Position | Action |
|------|----------|-------|-----------|---------------|--------|
| 1    | (0,0)    | 3     | Right     | (0,1)         | Place 3, move right |
| 2    | (0,1)    | 0     | Right     | (0,2)         | Place 0, move right |
| 3    | (0,2)    | 2     | Right     | (0,3)         | Place 2, move right |
| 4    | (0,3)    | 6     | Right     | (0,4)         | Place 6, move right |
| 5    | (0,4)    | 8     | Right     | (0,5) - out   | Place 8, change to down |
| 6    | (1,4)    | 1     | Down      | (2,4)         | Place 1, move down |
| 7    | (2,4)    | 7     | Down      | (3,4) - out   | Place 7, change to left |
| 8    | (2,3)    | 9     | Left      | (2,2)         | Place 9, move left |
| ...  | ...      | ...   | ...       | ...           | Continue spiral |

4. **Direction Change Logic**
   - Check if next position is out of bounds or already filled (value != -1).
   - If yes, rotate direction: `dir_idx = (dir_idx + 1) % 4`.

5. **Return Result**
   Return the filled matrix with remaining cells as -1.
