## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** This is the "easy" version of the problem, meaning $n$ is likely a standard integer. The number of digits ($D$) is small enough that we can process them directly without complex prefix arrays.
  * **Zeros:** The core constraint is ignoring zeros.
  * **Edge Case:** If $n = 0$, filtering out zeros leaves an empty set. We must handle this to avoid conversion errors or returning an incorrect result (the answer should be 0).

**High-level approach**
The most readable way to handle digits is to treat the number as a string. We convert the number to text, filter out the characters equal to `'0'`, and then perform two parallel operations on the remaining digits: concatenate them to form a new number $x$, and sum them to form $s$.

**Brute force vs. optimized strategy**

  * **Mathematical Approach:** We could use a loop with `% 10` and `/ 10` to extract digits. While memory-efficient, this logic is verbose because we extract digits in reverse order (right-to-left), requiring us to reverse them back for concatenation.
  * **String Approach:** Converting to a string allows strictly left-to-right processing using Python's powerful list comprehensions. This is $O(\log n)$ (proportional to the number of digits) and extremely clean.

**Decomposition**

1.  **String Conversion:** Turn integer $n$ into string `s`.
2.  **Filter:** Create a list of digits excluding `'0'`.
3.  **Reconstruct:** Join the list to form the integer $x$.
4.  **Sum:** Calculate the sum of the digits.
5.  **Compute:** Return $x \times \text{sum}$.

### Steps

1.  **Convert and Filter**
    Convert the input integer `n` to a string. Iterate through this string and collect only the characters that are not `'0'`.

2.  **Handle Zeros**
    Check if our list of filtered digits is empty. This happens if the input was `0`. In this case, return `0` immediately.

3.  **Form the Number (Concatenation)**
    Use the string `join` method to combine the filtered characters back into a single string, then convert that string into an integer. Let's call this `x`.

4.  **Calculate Digit Sum**
    Iterate through the filtered list again (or use a generator), convert each character to an integer, and sum them up.

5.  **Return Result**
    Multiply `x` by the sum and return the result.
