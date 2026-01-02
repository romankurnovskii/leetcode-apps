## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a list of book return days and a due date, we need to calculate the total late fee (sum of days overdue for each book returned after the due date).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of books can be up to 10^4.
- **Time Complexity:** O(n) - we iterate through the books once, where n is the number of books.
- **Space Complexity:** O(1) - we only need variables to track the total fee.
- **Edge Case:** If all books are returned on or before the due date, return 0. If a book is returned exactly on the due date, it's not late.

**1.2 High-level approach:**

The goal is to sum the difference between return day and due date for all books returned after the due date.

![Late fee calculation visualization](https://assets.leetcode.com/static_assets/others/late-fee.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** This problem is straightforward - we just need to check each book and sum late fees.
- **Optimized Strategy:** Iterate through books and for each book returned after due date, add (return_day - due_date) to total. This is O(n) time.
- **Optimization:** The solution is already optimal - linear time is the best we can do.

**1.4 Decomposition:**

1. Initialize total fee to 0.
2. For each book return day:
   - If return_day > due_date, add (return_day - due_date) to total.
3. Return the total fee.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `books = [5, 3, 7, 2]`, `days = 4`

- Due date: `4`
- Result variable: `res = 0`

**2.2 Start Checking:**

We check each book's return day.

**2.3 Trace Walkthrough:**

| Step | Book | Return day | Late? | Fee | res |
| ---- | ---- | ---------- | ----- | --- | --- |
| 1    | 1 | 5 | Yes (5>4) | 1 | 1 |
| 2    | 2 | 3 | No (3<=4) | 0 | 1 |
| 3    | 3 | 7 | Yes (7>4) | 3 | 4 |
| 4    | 4 | 2 | No (2<=4) | 0 | 4 |

**2.4 Increment and Loop:**

After checking each book, we add the late fee if applicable.

**2.5 Return Result:**

The result is `4`, which is the total late fee (1 day for book 1, 3 days for book 3).

