## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The string $s$ has length between 1 and 15 characters.
* **Time Complexity:** $O(n)$ where $n$ is the length of the string. We process each character exactly once.
* **Space Complexity:** $O(1)$ for the hash map (constant size) and variables.
* **Edge Case:** Single character strings like "I" return 1. Strings with subtractive forms like "IV" require special handling.

**1.2 High-level approach**

The goal is to convert a Roman numeral string to its integer value. The key insight is that when a smaller value appears before a larger value, it should be subtracted rather than added.

![Roman numeral parsing showing how to handle subtractive forms like IV and IX]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Check for all subtractive forms (IV, IX, XL, XC, CD, CM) first, then process remaining characters. This requires multiple passes.
* **Optimized (Right-to-Left):** Process the string from right to left. If the current value is less than the previous value, subtract it; otherwise, add it. This handles subtractive forms naturally in a single pass.

**1.4 Decomposition**

1. Create a mapping from Roman symbols to their integer values.
2. Process the string from right to left.
3. For each character, compare its value with the previous character's value.
4. If current value is less than previous, subtract; otherwise, add.
5. Accumulate the total.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $s = "MCMXCIV"$ (which represents 1994).

We initialize:
* `roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}`
* `res = 0` (accumulator for the result)
* `prev_value = 0` (value of the previous character)

**2.2 Start Checking/Processing**

We iterate through the string from right to left (from index `len(s) - 1` down to 0).

**2.3 Trace Walkthrough**

| Index | Character | current_value | prev_value | Comparison | Operation | res (before) | res (after) |
|-------|-----------|----------------|------------|------------|-----------|-------------|-------------|
| 6 | 'V' | 5 | 0 | 5 >= 0 | Add | 0 | 5 |
| 5 | 'I' | 1 | 5 | 1 < 5 | Subtract | 5 | 4 |
| 4 | 'C' | 100 | 1 | 100 >= 1 | Add | 4 | 104 |
| 3 | 'X' | 10 | 100 | 10 < 100 | Subtract | 104 | 94 |
| 2 | 'M' | 1000 | 10 | 1000 >= 10 | Add | 94 | 1094 |
| 1 | 'C' | 100 | 1000 | 100 < 1000 | Subtract | 1094 | 994 |
| 0 | 'M' | 1000 | 100 | 1000 >= 100 | Add | 994 | 1994 |

**2.4 Increment and Loop**

For each character from right to left:
1. Get `current_value = roman_map[s[i]]`
2. If `current_value < prev_value`, subtract: `res -= current_value`
3. Otherwise, add: `res += current_value`
4. Update `prev_value = current_value`

**2.5 Return Result**

After processing all characters, `res = 1994`, which is the integer value of the Roman numeral "MCMXCIV".

