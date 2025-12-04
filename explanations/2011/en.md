## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= operations.length <= 100`.
- **Time Complexity:** O(n) where n is the number of operations - we process each operation once.
- **Space Complexity:** O(1) - we only use a constant amount of space for the result variable.
- **Edge Case:** All operations could be increments or all could be decrements.

**1.2 High-level approach:**
The goal is to track the value of variable `X` starting from 0, applying increment or decrement operations. We check each operation string to determine if it's an increment (`++X` or `X++`) or decrement (`--X` or `X--`).

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we need to check each operation once.
- **Optimized Strategy:** Single pass through operations, checking the middle character or the operation type.

**1.4 Decomposition:**
1. Initialize result variable to 0.
2. Iterate through each operation.
3. Check if the operation is an increment (contains `++`) or decrement (contains `--`).
4. Update the result accordingly.
5. Return the final value.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `operations = ["--X","X++","X++"]`. We initialize `res = 0`.

**2.2 Start Checking:**
We process each operation in sequence.

**2.3 Trace Walkthrough:**

| Operation | Type | res Before | res After |
|-----------|------|------------|------------|
| "--X" | Decrement | 0 | -1 |
| "X++" | Increment | -1 | 0 |
| "X++" | Increment | 0 | 1 |

**2.4 Increment and Loop:**
After processing each operation, we move to the next one until all operations are processed.

**2.5 Return Result:**
Return `res = 1`, which is the final value after all operations.

