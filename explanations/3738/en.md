## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Array Size:** The array can have up to $10^5$ elements, so we need an efficient algorithm.
  * **Value Range:** Each element can be between $-10^9$ and $10^9$.
  * **Time Complexity:** We iterate through the array twice to build prefix and suffix arrays, then once more to check replacements. This is $O(n)$.
  * **Space Complexity:** $O(n)$ to store prefix and suffix arrays.
  * **Edge Cases:**
    * Single element array: result is 1.
    * Already non-decreasing array: result is the array length.
    * Replacing first or last element: can only extend one side.

**High-level approach**
The problem asks us to find the longest non-decreasing subarray after replacing at most one element.

  * We can solve this by considering two scenarios:
    * **Without replacement:** Find the longest non-decreasing subarray in the original array.
    * **With replacement:** For each position, try replacing that element to extend or bridge existing non-decreasing segments.
  * We use prefix and suffix arrays to efficiently track non-decreasing segments:
    * `pref[i]` = length of longest non-decreasing subarray ending at index $i$
    * `suff[i]` = length of longest non-decreasing subarray starting at index $i$

**Brute force vs. optimized strategy**

  * **Brute Force:** For each possible replacement position and each possible replacement value, check the longest non-decreasing subarray. This would be $O(n^3)$.
  * **Optimized (Prefix/Suffix Arrays):** Precompute prefix and suffix arrays in $O(n)$. Then for each replacement position, we can calculate the optimal result in $O(1)$ by combining or extending these segments. Total time is $O(n)$.

**Decomposition**

1.  **Build Prefix Array:** Calculate `pref[i]` for each index, representing the longest non-decreasing subarray ending at $i$.
2.  **Build Suffix Array:** Calculate `suff[i]` for each index, representing the longest non-decreasing subarray starting at $i$.
3.  **Initial Maximum:** Set result to the maximum of all prefix and suffix values (best without replacement).
4.  **Try Replacements:** For each index $i$, consider replacing `nums[i]`:
    * If we can bridge prefix and suffix (when `nums[i-1] <= nums[i+1]`), combine them.
    * Otherwise, extend either the prefix or suffix.

### Steps

1.  **Build Prefix Array**
    For each index $i$ from left to right:
      * If `nums[i] >= nums[i-1]`, extend the prefix: `pref[i] = pref[i-1] + 1`
      * Otherwise, start a new segment: `pref[i] = 1`

2.  **Build Suffix Array**
    For each index $i$ from right to left:
      * If `nums[i] <= nums[i+1]`, extend the suffix: `suff[i] = suff[i+1] + 1`
      * Otherwise, start a new segment: `suff[i] = 1`

3.  **Calculate Initial Maximum**
    Find the maximum value in both prefix and suffix arrays. This represents the longest non-decreasing subarray without any replacement.

4.  **Try Replacing Each Element**
    For each index $i$:
      * **Middle elements** ($0 < i < n-1$):
        * If `nums[i-1] <= nums[i+1]`, we can bridge: replace `nums[i]` with a value between `nums[i-1]` and `nums[i+1]` to combine prefix and suffix. Length = `pref[i-1] + 1 + suff[i+1]`.
        * We can also extend the prefix: set `nums[i] >= nums[i-1]`, length = `pref[i-1] + 1`.
        * We can also extend the suffix: set `nums[i] <= nums[i+1]`, length = `1 + suff[i+1]`.
      * **First element** ($i = 0$): Extend suffix by setting `nums[0] <= nums[1]`, length = `1 + suff[1]`.
      * **Last element** ($i = n-1$): Extend prefix by setting `nums[n-1] >= nums[n-2]`, length = `pref[n-2] + 1`.

5.  **Return Maximum**
    Return the maximum value found across all scenarios.

