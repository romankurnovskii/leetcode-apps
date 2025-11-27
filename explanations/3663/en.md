## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Integer Range:** The input $n$ can be as large as $2^{31} - 1$, which means up to 10 digits in decimal representation.
  * **Time Complexity:** We need to iterate through all digits once to count frequencies, then find the minimum. This is $O(\log n)$ where the number of digits is $\log_{10} n$.
  * **Space Complexity:** We store frequency counts for at most 10 distinct digits (0-9), so space is $O(1)$.
  * **Edge Case:** If all digits have the same frequency (e.g., $n=111$), we return the smallest digit among them.

**High-level approach**
The problem asks us to find the digit that appears **least frequently** in the decimal representation of $n$. If multiple digits share the minimum frequency, we choose the **smallest** one.

  * We need to count how many times each digit (0-9) appears in the number.
  * After counting, we find the minimum frequency value.
  * Among all digits that have this minimum frequency, we select the smallest digit.

**Brute force vs. optimized strategy**

  * **Brute Force:** Convert to string, iterate through each digit, manually track counts in separate variables for each digit 0-9.
  * **Optimized (Hash Map):** Convert to string once, use a dictionary to count frequencies in a single pass. This is cleaner and more maintainable.

**Decomposition**

1.  **String Conversion:** Convert the integer $n$ into its decimal string representation to access individual digits.
2.  **Frequency Counting:** Iterate through each digit character and count occurrences using a hash map (dictionary).
3.  **Find Minimum Frequency:** Determine the smallest frequency value among all digit counts.
4.  **Select Smallest Digit:** Among digits with the minimum frequency, return the smallest digit value.

### Steps

1.  **Convert to String**
    Turn the integer $n$ into a string of digits. For example, if $n=1553322$, we get the string `"1553322"`.

2.  **Count Frequencies**
    Iterate through each character in the string and maintain a frequency map. For `"1553322"`:
      * `'1'` appears 1 time
      * `'5'` appears 2 times
      * `'3'` appears 2 times
      * `'2'` appears 2 times

3.  **Find Minimum Frequency**
    Scan through all frequency values to find the minimum. In the example above, the minimum frequency is 1.

4.  **Select Smallest Digit with Minimum Frequency**
    Among all digits that have the minimum frequency, choose the smallest one. If multiple digits share the minimum frequency, return the smallest digit value (e.g., if both 2 and 5 appear once, return 2).

