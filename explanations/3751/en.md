## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Range Size:** The range $[num1, num2]$ can contain up to $10^5$ numbers, so we need an efficient approach.
  * **Number Size:** Each number can be up to $10^5$, which means at most 6 digits.
  * **Time Complexity:** For each number, we check its digits once. With up to $10^5$ numbers and at most 6 digits each, this is $O(n \times d)$ where $n$ is the range size and $d$ is the average number of digits. This is acceptable for the constraints.
  * **Edge Cases:**
    * Numbers with fewer than 3 digits have waviness 0 (no middle digits to check).
    * The first and last digits cannot be peaks or valleys (they only have one neighbor).

**High-level approach**
The problem asks us to find the total waviness across all numbers in a range. Waviness is defined as the count of peaks and valleys in a number's digit sequence.

  * A **peak** is a digit that is strictly greater than both its immediate neighbors.
  * A **valley** is a digit that is strictly less than both its immediate neighbors.
  * Only middle digits (not first or last) can be peaks or valleys.
  * For each number in the range, we count its peaks and valleys, then sum all waviness values.

**Brute force vs. optimized strategy**

  * **Brute Force:** Iterate through each number in the range $[num1, num2]$, convert to string, check each middle digit for peaks/valleys, and sum the results. This is straightforward and efficient enough for the given constraints.
  * **Optimized (Digit DP):** Could use digit dynamic programming to count waviness patterns more efficiently, but for the given constraints ($num2 \leq 10^5$), brute force is sufficient and simpler.

**Decomposition**

1.  **Waviness Calculation:** For a single number, convert it to a string and examine each middle digit (positions 1 to len-2).
2.  **Peak/Valley Detection:** For each middle digit, compare it with its left and right neighbors to determine if it's a peak or valley.
3.  **Range Iteration:** Iterate through all numbers from $num1$ to $num2$ (inclusive).
4.  **Summation:** Sum the waviness of all numbers in the range.

### Steps

1.  **Define Waviness Function**
    Create a helper function `get_waviness(num)` that calculates the waviness of a single number:
      * Convert the number to a string to access individual digits.
      * If the number has fewer than 3 digits, return 0 (no middle digits to check).

2.  **Check Middle Digits**
    For each middle digit at position $i$ (where $1 \leq i < len(s) - 1$):
      * Get the digit value and its left and right neighbors.
      * Check if the digit is a **peak**: `digit > left and digit > right`
      * Check if the digit is a **valley**: `digit < left and digit < right`
      * Increment the waviness counter for each peak or valley found.

3.  **Iterate Through Range**
    For each number $n$ from $num1$ to $num2$ (inclusive):
      * Calculate its waviness using the helper function.
      * Add it to the running total.

4.  **Return Total**
    Return the sum of all waviness values across the range.
