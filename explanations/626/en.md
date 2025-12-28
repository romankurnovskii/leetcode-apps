## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to swap the seat IDs of every two consecutive students. If the number of students is odd, the last student's ID remains unchanged. The result should be ordered by id in ascending order.

**1.1 Constraints & Complexity:**

- **Input Size:** The Seat table can have any number of rows, with IDs starting from 1 and incrementing continuously.
- **Time Complexity:** O(n) where n is the number of rows - we scan the table once and perform constant-time operations for each row.
- **Space Complexity:** O(n) - we create a result set with n rows.
- **Edge Case:** When there's an odd number of students, the last student (with the highest ID) keeps their original ID.

**1.2 High-level approach:**

The goal is to swap consecutive seat IDs: even IDs swap with id-1, odd IDs swap with id+1. For the last row (if total count is odd), we handle it specially to keep it unchanged.

![Seat swapping visualization](https://assets.leetcode.com/static_assets/others/seat-swap.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use multiple CASE statements or UNION queries to handle each case separately, which would be verbose and harder to maintain.
- **Optimized Strategy:** Use nested IF statements to handle the swapping logic in a single query. Check if the current id is less than the total count to determine if it should swap, then apply the swap logic based on whether the id is even or odd. This is O(n) time.
- **Optimization:** By using a single query with conditional logic, we avoid multiple table scans and make the solution more concise and efficient.

**1.4 Decomposition:**

1. Count the total number of seats to determine if the last seat should be swapped.
2. For each row, check if its id is less than the total count:
   - If yes: swap even ids with id-1, odd ids with id+1.
   - If no (last row with odd total): keep even ids as id-1, odd ids unchanged.
3. Order the result by id in ascending order.
4. Return the result with swapped ids and original student names.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example with 5 students:
- Original: id=1 (Abbot), id=2 (Doris), id=3 (Emerson), id=4 (Green), id=5 (Jeames)
- Total count: 5 (odd, so last student keeps their id)

**2.2 Start Checking:**

We process each row and apply the swapping logic.

**2.3 Trace Walkthrough:**

| Original id | Student  | id % 2 | id < 5? | New id | Action                    |
| ----------- | -------- | ------ | ------- | ------ | ------------------------- |
| 1           | Abbot    | 1      | Yes     | 2      | Odd: swap with id+1 = 2   |
| 2           | Doris    | 0      | Yes     | 1      | Even: swap with id-1 = 1   |
| 3           | Emerson  | 1      | Yes     | 4      | Odd: swap with id+1 = 4    |
| 4           | Green    | 0      | Yes     | 3      | Even: swap with id-1 = 3   |
| 5           | Jeames   | 1      | No      | 5      | Last odd: keep id = 5      |

**Result after ordering by id:**
| id | student |
|----|---------|
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |

**2.4 Increment and Loop:**

For each row in the seat table:
- We check if the id is less than the total count.
- If yes, we swap: even ids go to id-1, odd ids go to id+1.
- If no (last row with odd total), we keep even ids as id-1 and odd ids unchanged.
- We maintain the original student name.

**2.5 Return Result:**

The result shows swapped seat IDs: 1↔2, 3↔4, with 5 unchanged (since total is odd). Students are now seated in swapped positions, ordered by id.

