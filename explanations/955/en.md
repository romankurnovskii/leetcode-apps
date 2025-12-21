## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given an array of strings, all of the same length. We can delete any columns (indices) from all strings. After deletion, we want the final array to be in lexicographic order (each string is less than or equal to the next). We need to find the minimum number of columns to delete.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 100 strings, each with up to 100 characters.
- **Time Complexity:** O(M × N) where M is the number of strings and N is the length of each string. We iterate through each column once, and for each column, we check all string pairs.
- **Space Complexity:** O(M) to store the sorted status of each pair of adjacent strings.
- **Edge Case:** If the strings are already in lexicographic order, we don't need to delete any columns, so the answer is 0.

**1.2 High-level approach:**

The goal is to greedily decide which columns to keep. We process columns from left to right. For each column, we check if keeping it would break the lexicographic order. If it breaks the order, we delete it. Otherwise, we keep it and update our knowledge of which string pairs are now sorted.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of columns to delete, check if the resulting strings are sorted, and find the minimum. This would be O(2^N × M × N) which is exponential and too slow.
- **Optimized Strategy:** Use a greedy approach - process columns left to right, track which pairs are already sorted, and only delete a column if it breaks the order. This is O(M × N) time.
- **Optimization:** By tracking which pairs are already sorted, we avoid re-checking pairs that we know are sorted from previous columns. This makes the solution efficient.

**1.4 Decomposition:**

1. Initialize a boolean array to track which pairs of adjacent strings are already sorted.
2. For each column from left to right:
   - Check if this column would break the lexicographic order for any unsorted pair.
   - If it breaks the order, delete the column (increment the result counter).
   - If we keep the column, update the sorted status for pairs where this column makes them sorted.
3. Return the total number of deleted columns.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `strs = ["ca", "bb", "ac"]`

- Number of strings `n = 3`, length of each string `m = 2`
- Result `res = 0`
- Sorted pairs array: `sorted_pairs = [False, False]` (we have 2 pairs: "ca"-"bb" and "bb"-"ac")
- We'll process columns: column 0 (first character), then column 1 (second character)

**2.2 Start Checking:**

We begin processing columns from left to right. For each column, we check if it breaks the lexicographic order.

**2.3 Trace Walkthrough:**

| Step | Column | Check Pair | Comparison | Breaks Order? | Action | res | sorted_pairs |
| ---- | ------ | ---------- | ---------- | ------------- | ------ | --- | ------------ |
| 1    | 0      | "ca"-"bb"  | 'c' > 'b'  | Yes           | Delete column 0 | 1   | [False, False] |
| 2    | 1      | "ca"-"bb"  | 'a' < 'b'  | No            | Keep column 1, update sorted | 1   | [True, False] |
| 2    | 1      | "bb"-"ac"  | 'b' < 'c'  | No            | Keep column 1, update sorted | 1   | [True, True] |

Detailed execution:
- **Column 0:** Check unsorted pair 0 ("ca" vs "bb" at position 0): 'c' > 'b' breaks order → Delete column 0, res = 1
- **Column 1:** 
  - Check unsorted pair 0 ("ca" vs "bb" at position 1): 'a' < 'b' doesn't break → Can keep column 1
  - Check unsorted pair 1 ("bb" vs "ac" at position 1): 'b' < 'c' doesn't break → Can keep column 1
  - Since we keep column 1, update sorted_pairs: pair 0 becomes sorted ('a' < 'b'), pair 1 becomes sorted ('b' < 'c')
  - After deleting column 0, the remaining strings are `["a", "b", "c"]` which are sorted

**2.4 Increment and Loop:**

After processing each column, we move to the next column. We continue until all columns are processed.

**2.5 Return Result:**

The result is 1, which means we need to delete 1 column (the first column) to make the strings lexicographically sorted.

