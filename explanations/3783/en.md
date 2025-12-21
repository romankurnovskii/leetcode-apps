## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given an integer n. We need to calculate its mirror distance, which is the absolute difference between the number and its reverse (the number formed by reversing its digits).

**1.1 Constraints & Complexity:**

- **Input Size:** The integer n can be up to 10^9, which means up to 10 digits.
- **Time Complexity:** O(log n) - we convert the number to a string (which takes O(log n) time for the number of digits), reverse it, and convert back.
- **Space Complexity:** O(log n) - we store the string representation which has length proportional to log n.
- **Edge Case:** If n is a single digit or a palindrome (like 7 or 121), the mirror distance is 0.

**1.2 High-level approach:**

The goal is to reverse the digits of the number and calculate the absolute difference between the original and reversed numbers.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Extract digits one by one using modulo and division, build the reverse number digit by digit, then calculate the difference. This is O(log n) time and O(1) space.
- **Optimized Strategy:** Convert to string, reverse the string, convert back to integer, then calculate absolute difference. This is also O(log n) time but more readable.
- **Optimization:** Using string reversal is simpler and more intuitive, making the code easier to understand and maintain.

**1.4 Decomposition:**

1. Convert the integer to a string representation.
2. Reverse the string.
3. Convert the reversed string back to an integer.
4. Calculate and return the absolute difference between the original and reversed numbers.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 25`

- Original number: `25`
- String representation: `"25"`
- Reversed string: `"52"`
- Reversed number: `52`

**2.2 Start Processing:**

We convert the number to a string and reverse it.

**2.3 Trace Walkthrough:**

| Step | Operation | Value | Description |
| ---- | --------- | ----- | ----------- |
| 1    | Convert to string | `"25"` | Convert integer 25 to string |
| 2    | Reverse string | `"52"` | Reverse the string characters |
| 3    | Convert to int | `52` | Convert reversed string back to integer |
| 4    | Calculate difference | `abs(25 - 52) = 27` | Calculate absolute difference |

**2.4 Increment and Loop:**

This is a single-pass operation with no loop needed.

**2.5 Return Result:**

The result is 27, which is the absolute difference between 25 and its reverse 52.

