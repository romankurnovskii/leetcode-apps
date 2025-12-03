## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The string $s$ can have up to $1000$ characters, and `numRows` can be up to $1000$.
* **Time Complexity:** $O(n)$ where $n$ is the length of the string. We visit each character exactly once.
* **Space Complexity:** $O(n)$ to store the result string.
* **Edge Case:** When `numRows = 1`, the string remains unchanged.

**1.2 High-level approach**

The goal is to arrange characters in a zigzag pattern across multiple rows, then read them line by line. Characters move down to the bottom row, then up to the top, creating a zigzag motion.

![Zigzag pattern visualization showing characters distributed across rows in a V-shaped pattern]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Create a 2D grid and fill it character by character, then read row by row. This requires $O(n \times numRows)$ space.
* **Optimized (Row Tracking):** Instead of storing a 2D grid, we maintain an array of strings (one per row) and track which row we're currently on. We change direction when we reach the top or bottom row. This uses $O(n)$ space.

**1.4 Decomposition**

1. Create an array to store characters for each row.
2. Track the current row and direction (down or up).
3. Distribute each character to the appropriate row.
4. Change direction when reaching the top or bottom row.
5. Concatenate all rows to form the result.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $s = "PAYPALISHIRING"$, $numRows = 3$.

We initialize:
* `rows = ["", "", ""]` (three empty strings for three rows)
* `current_row = 0` (start at top row)
* `going_down = False` (will be set to True immediately)

**2.2 Start Checking/Processing**

We iterate through each character in the string, placing it in the appropriate row.

**2.3 Trace Walkthrough**

| Character | current_row | going_down | rows[0] | rows[1] | rows[2] |
|-----------|-------------|------------|---------|---------|---------|
| 'P' | 0 | True | "P" | "" | "" |
| 'A' | 1 | True | "P" | "A" | "" |
| 'Y' | 2 | True | "P" | "A" | "Y" |
| 'P' | 1 | False | "P" | "AP" | "Y" |
| 'A' | 0 | False | "PA" | "AP" | "Y" |
| 'L' | 1 | True | "PA" | "APL" | "Y" |
| 'I' | 2 | True | "PA" | "APL" | "YI" |
| 'S' | 1 | False | "PA" | "APLS" | "YI" |
| 'H' | 0 | False | "PAH" | "APLS" | "YI" |
| 'I' | 1 | True | "PAH" | "APLSI" | "YI" |
| 'R' | 2 | True | "PAH" | "APLSI" | "YIR" |
| 'I' | 1 | False | "PAH" | "APLSII" | "YIR" |
| 'N' | 0 | False | "PAHN" | "APLSII" | "YIR" |
| 'G' | 1 | True | "PAHN" | "APLSIIG" | "YIR" |

**2.4 Increment and Loop**

For each character:
1. Add the character to `rows[current_row]`.
2. If at row 0 or row `numRows - 1`, flip `going_down`.
3. Move to the next row: increment if going down, decrement if going up.

**2.5 Return Result**

After processing all characters:
* `rows[0] = "PAHN"`
* `rows[1] = "APLSIIG"`
* `rows[2] = "YIR"`

Concatenating: `res = "PAHNAPLSIIGYIR"`.

