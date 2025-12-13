## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The bank has dimensions m x n where `1 <= m, n <= 500`.
  * **Time Complexity:** O(m * n) - We iterate through all rows to count devices, then through device counts to calculate beams.
  * **Space Complexity:** O(m) - We store device counts for each row (at most m rows).
  * **Edge Case:** If there's only one row with devices, there are no beams (need at least two rows).

**High-level approach**
We count security devices in each row, skip empty rows, and calculate beams between adjacent non-empty rows. The number of beams between two rows equals the product of device counts in those rows.

**Brute force vs. optimized strategy**

  * **Brute Force:** For each device pair, check if there's a clear path - this is O(m² * n²).
  * **Optimized Strategy:** Count devices per row, then multiply counts of adjacent rows. This is O(m * n).

**Decomposition**

1.  **Count Devices Per Row:** Count '1' characters in each row.
2.  **Filter Non-Empty Rows:** Only keep rows with at least one device.
3.  **Calculate Beams:** For each pair of adjacent rows, multiply their device counts.
4.  **Sum Total:** Add up all beam counts.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `bank = ["011001", "000000", "010100", "001000"]`.
    We create `device_counts = []`.

2.  **Start Counting:**
    We iterate through each row and count '1' characters.

3.  **Trace Walkthrough:**
    
    | Row | Devices | Count | Action |
    |-----|---------|-------|--------|
    | "011001" | 3 | 3 | Add to device_counts |
    | "000000" | 0 | 0 | Skip (empty row) |
    | "010100" | 2 | 2 | Add to device_counts |
    | "001000" | 1 | 1 | Add to device_counts |

    After counting: `device_counts = [3, 2, 1]`

4.  **Calculate Beams:**
    - Between rows 0 and 1: 3 * 2 = 6 beams
    - Between rows 1 and 2: 2 * 1 = 2 beams
    - Total: 6 + 2 = 8 beams

5.  **Return Result:**
    Return `res = 8`.

