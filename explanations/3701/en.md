## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Array Size:** The array can have 1 to 100 elements.
  * **Value Range:** Each element is between 1 and 100.
  * **Time Complexity:** We iterate through the array once, so $O(n)$.
  * **Space Complexity:** $O(1)$ - we only need a few variables.
  * **Edge Case:** If the array has only one element, it's at index 0 (even), so we just return that element.

**High-level approach**
The problem asks us to compute the alternating sum of an array, where we add elements at even indices and subtract elements at odd indices.

  * The pattern is: $nums[0] - nums[1] + nums[2] - nums[3] + ...$
  * Even indices (0, 2, 4, ...) are added.
  * Odd indices (1, 3, 5, ...) are subtracted.
  * We iterate through the array and apply the appropriate operation based on the index parity.

**Brute force vs. optimized strategy**

  * **Brute Force:** This is already the optimal approach. We simply iterate through the array once, checking each index's parity and applying the appropriate operation.
  * **Optimized:** Same as brute force - there's no more efficient way to compute this. We need to examine each element once.

**Decomposition**

1.  **Initialize Result:** Start with a result variable set to 0.
2.  **Iterate Through Array:** Loop through each element with its index.
3.  **Check Index Parity:** Determine if the index is even or odd.
4.  **Apply Operation:** Add if even index, subtract if odd index.
5.  **Return Result:** Return the final alternating sum.

### Steps

1.  **Initialize Result**
    Set a variable `result` to 0. This will accumulate the alternating sum.

2.  **Iterate Through Array**
    Use `enumerate` to get both the index and value for each element. For example, in $[1,3,5,7]$:
      * Index 0, value 1
      * Index 1, value 3
      * Index 2, value 5
      * Index 3, value 7

3.  **Check Index Parity**
    For each element, check if the index is even or odd using `i % 2`:
      * If `i % 2 == 0`: even index → add the value
      * If `i % 2 == 1`: odd index → subtract the value

4.  **Apply Operation**
    Update the result accordingly:
      * Index 0 (even): $result = 0 + 1 = 1$
      * Index 1 (odd): $result = 1 - 3 = -2$
      * Index 2 (even): $result = -2 + 5 = 3$
      * Index 3 (odd): $result = 3 - 7 = -4$

5.  **Return Result**
    Return the final alternating sum: $-4$.

