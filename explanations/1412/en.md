## Explanation

### Strategy (The "Why")

**Restate the problem:** Given exam results with student IDs and scores, we need to find students who never had the highest or lowest score in any exam they took (i.e., "quiet" students who are always in the middle).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of students and exams can be up to 10^4 each.
- **Time Complexity:** O(n log n) where n is the number of exam records - we need to rank scores for each exam and filter students.
- **Space Complexity:** O(n) - we need to store exam statistics and student information.
- **Edge Case:** If a student took only one exam, they cannot be quiet (they are both highest and lowest). If all students have the same score in an exam, no one is highest or lowest.

**1.2 High-level approach:**

The goal is to use SQL window functions to rank students by score in each exam, then identify students who never achieved rank 1 (highest) or the lowest rank (lowest) in any exam.

![SQL window functions visualization](https://assets.leetcode.com/static_assets/others/sql-window.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each student, check all their exams to see if they ever had highest or lowest score. This requires multiple queries.
- **Optimized Strategy:** Use SQL window functions (RANK) to calculate rankings for all students in all exams in one pass, then filter. This is efficient and leverages database optimization.
- **Optimization:** By using window functions, we can calculate all rankings in a single query pass, making the solution efficient.

**1.4 Decomposition:**

1. Use window functions to rank students by score in each exam (both ascending and descending).
2. Identify students who had rank 1 (highest) or lowest rank (lowest) in any exam.
3. Find students who are NOT in the above list (quiet students).
4. Join with Student table to get student names.
5. Order by student ID.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Example data:
- Exam: `[(1, 1, 70), (1, 2, 80), (2, 1, 90), (2, 2, 60)]`
- Student: `[(1, "Alice"), (2, "Bob")]`

**2.2 Start Checking:**

We execute the SQL query with window functions.

**2.3 Trace Walkthrough:**

| Step | Operation | Result |
| ---- | --------- | ------ |
| 1    | RANK() OVER | Calculate ranks per exam |
| 2    | Filter | Students with rank 1 or lowest |
| 3    | NOT IN | Quiet students (not in filtered list) |
| 4    | JOIN | Get student names |
| 5    | ORDER BY | Sort by student_id |

**2.4 Increment and Loop:**

SQL handles the iteration internally through window functions and joins.

**2.5 Return Result:**

The result contains students who never had the highest or lowest score in any exam they took.

