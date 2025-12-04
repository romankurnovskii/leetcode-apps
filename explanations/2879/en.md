## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** DataFrame with any number of rows.
- **Time Complexity:** O(1) - head(3) is a constant-time operation that just returns a view.
- **Space Complexity:** O(1) - returns a view, not a copy.
- **Edge Case:** DataFrame has fewer than 3 rows, returns all rows.

**1.2 High-level approach:**
The goal is to display the first 3 rows of a DataFrame. In pandas, we use the `head()` method which returns the first n rows.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - head() is already the optimal method.
- **Optimized Strategy:** Use pandas built-in `head(3)` method.

**1.4 Decomposition:**
1. Use the `head(3)` method on the DataFrame.
2. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use a DataFrame with 6 rows. We want to return the first 3 rows.

**2.2 Start Checking:**
We call `employees.head(3)`.

**2.3 Trace Walkthrough:**

| Operation | Input Rows | Output Rows |
|-----------|------------|-------------|
| head(3) | 6 rows | First 3 rows |

**2.4 Increment and Loop:**
Not applicable - this is a single operation.

**2.5 Return Result:**
Return the DataFrame containing the first 3 rows.

