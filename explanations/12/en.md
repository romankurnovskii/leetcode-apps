## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Range:** The integer $num$ is in the range $[1, 3999]$.
* **Time Complexity:** $O(1)$ because the number of Roman numeral symbols is constant (13 symbols), and we process each at most a constant number of times.
* **Space Complexity:** $O(1)$ for the output string, which has a maximum length proportional to the input value.
* **Edge Case:** The number 1 maps to "I", and 3999 maps to "MMMCMXCIX".

**1.2 High-level approach**

The goal is to convert a decimal number to its Roman numeral representation. We use a greedy approach: always subtract the largest possible Roman numeral value from the remaining number.

![Roman numeral conversion showing the greedy selection of largest possible symbols]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible combinations of Roman symbols and find the one that sums to the target. This is exponential in complexity.
* **Optimized (Greedy):** Use a predefined list of values and symbols in descending order. For each value, determine how many times it fits and append the corresponding symbol. This is $O(1)$ time.

**1.4 Decomposition**

1. Define arrays of values and corresponding symbols in descending order (including subtractive forms like IV, IX).
2. For each value-symbol pair, calculate how many times the value fits into the remaining number.
3. Append the symbol that many times to the result.
4. Update the remaining number by taking the remainder after division.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $num = 58$.

We initialize:
* `values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]`
* `symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]`
* `res = ""` (empty string to build result)
* `num = 58` (working copy)

**2.2 Start Checking/Processing**

We iterate through the values array, processing each value-symbol pair.

**2.3 Trace Walkthrough**

| Value | Symbol | num (before) | count | res (before) | res (after) | num (after) |
|-------|--------|--------------|-------|-------------|------------|-------------|
| 1000 | "M" | 58 | 0 | "" | "" | 58 |
| 900 | "CM" | 58 | 0 | "" | "" | 58 |
| 500 | "D" | 58 | 0 | "" | "" | 58 |
| 400 | "CD" | 58 | 0 | "" | "" | 58 |
| 100 | "C" | 58 | 0 | "" | "" | 58 |
| 90 | "XC" | 58 | 0 | "" | "" | 58 |
| 50 | "L" | 58 | 1 | "" | "L" | 8 |
| 40 | "XL" | 8 | 0 | "L" | "L" | 8 |
| 10 | "X" | 8 | 0 | "L" | "L" | 8 |
| 9 | "IX" | 8 | 0 | "L" | "L" | 8 |
| 5 | "V" | 8 | 1 | "L" | "LV" | 3 |
| 4 | "IV" | 3 | 0 | "LV" | "LV" | 3 |
| 1 | "I" | 3 | 3 | "LV" | "LVIII" | 0 |

**2.4 Increment and Loop**

For each value-symbol pair:
1. Calculate `count = num // value`
2. Append the symbol `count` times to `res`
3. Update `num = num % value`

**2.5 Return Result**

After processing all values, `res = "LVIII"`, which is the Roman numeral representation of 58.

