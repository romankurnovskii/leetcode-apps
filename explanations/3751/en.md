## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Range Size:** The input numbers go up to 100,000.
  * **Performance:** If we calculate the waviness for every number in the range `[num1, num2]` every time the function is called, we will likely hit a Time Limit Exceeded (TLE) error. The constraints imply we need a faster way to query.
  * **Edge Case:** Numbers less than 100 (0-99) have fewer than 3 digits. You cannot have a "middle" digit with neighbors on both sides, so their waviness is always 0.

**High-level approach**
We will use the **Prefix Sum** technique (also called Cumulative Sum). Instead of calculating the waviness on the fly, we will **precompute** the waviness for every possible number up to the maximum limit (100,000) once. We then store the cumulative totals in an array.

**Brute force vs. optimized strategy**

  * **Brute Force:** Loop from `num1` to `num2`. For each number, convert to string, check digits, count peaks/valleys, and add to total. This repeats the same heavy work for every query.
  * **Optimized:** Create a lookup table `P`.
    `P[i]` stores the total waviness of *all* numbers from `0` to `i`.
    To find the waviness between `num1` and `num2`, we simply do `P[num2] - P[num1 - 1]`. This answers any query in $O(1)$ time.

**Decomposition**

1.  **Helper Logic:** Define how to calculate waviness for a single number (check neighbors).
2.  **Precomputation:** Build an array where we store the cumulative waviness.
3.  **Range Query:** Use the array to answer the user's request instantly.

### Steps

1.  **Define Waviness**
    A digit is part of a "wave" if it is strictly greater than its neighbors (Peak) or strictly smaller than its neighbors (Valley).

      * *Visual Peak:* `1 -> 5 -> 2` (5 is a peak)
      * *Visual Valley:* `9 -> 0 -> 4` (0 is a valley)
      * We ignore the first and last digits because they don't have neighbors on both sides.

2.  **Initialize the Prefix Array**
    We create an array `prefix` of size 100,001 (covering 0 to 100,000).
    We define `running_total` to keep track of the sum as we build the array.

3.  **Populate the Array**
    We loop through every number `i` from 0 to 100,000.

      * Convert `i` to a string (or use math) to access digits.
      * Count the peaks and valleys for `i`.
      * Add this count to `running_total`.
      * Store `running_total` in `prefix[i]`.

4.  **Answer the Query**
    When the user asks for the range `[num1, num2]`:

      * Take the total waviness up to `num2` (`prefix[num2]`).
      * Subtract the total waviness before the range starts (`prefix[num1 - 1]`).
      * Return the result.
