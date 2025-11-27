## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Array Size:** The array can have up to 100 elements, so brute force is acceptable, but we can use a more efficient approach.
  * **Value Range:** Each element is between 1 and $n$ (the array length).
  * **Time Complexity:** We iterate through the array once to group indices, then for each value with at least 3 occurrences, we check consecutive triplets. This is $O(n)$ overall.
  * **Space Complexity:** $O(n)$ to store indices for each value.
  * **Edge Case:** If no value appears at least 3 times, return -1.

**High-level approach**
The problem asks us to find three distinct indices $(i, j, k)$ where $nums[i] == nums[j] == nums[k]$, and minimize the distance $abs(i - j) + abs(j - k) + abs(k - i)$.

  * The distance formula simplifies: if we have indices $p < q < r$, then $abs(p - q) + abs(q - r) + abs(r - p) = (q - p) + (r - q) + (r - p) = 2 \times (r - p)$.
  * To minimize the distance, we need to minimize $(r - p)$ for three indices of the same value.
  * We group indices by value, then for each value that appears at least 3 times, we find the three indices that minimize the span $(r - p)$.

**Brute force vs. optimized strategy**

  * **Brute Force:** Try all possible triplets $(i, j, k)$ where $nums[i] == nums[j] == nums[k]$. This would be $O(n^3)$, which is acceptable for $n \leq 100$ but not optimal.
  * **Optimized (Grouping + Consecutive Triplets):** Group indices by value using a hash map. For each value with at least 3 occurrences, check consecutive triplets in the sorted list of indices. Since we want to minimize $(r - p)$, checking consecutive triplets is optimal because any non-consecutive triplet would have a larger span. This is $O(n)$.

**Decomposition**

1.  **Group Indices:** Create a hash map that groups all indices where each value appears.
2.  **Filter Values:** Only consider values that appear at least 3 times (necessary for a good tuple).
3.  **Check Consecutive Triplets:** For each value's sorted list of indices, check every three consecutive indices $(p, q, r)$.
4.  **Calculate Distance:** For each triplet, compute $2 \times (r - p)$ and track the minimum.
5.  **Return Result:** Return the minimum distance found, or -1 if no good tuple exists.

### Steps

1.  **Group Indices by Value**
    Iterate through the array and store all indices where each value appears. For example, if $nums = [1,2,1,1,3]$, value 1 appears at indices $[0, 2, 3]$.

2.  **Filter Valid Values**
    Only process values that appear at least 3 times. Values with fewer than 3 occurrences cannot form a good tuple.

3.  **Check Consecutive Triplets**
    For each value's list of indices (which are naturally sorted by array position):
      * Iterate through the list, checking every three consecutive indices.
      * For indices $p < q < r$ at positions $i$, $i+1$, $i+2$ in the sorted list:
        * Calculate distance = $2 \times (r - p)$
        * Update the global minimum distance.

4.  **Why Consecutive Triplets?**
    To minimize $(r - p)$, we want the smallest possible span. If we skip an index between $p$ and $r$, the span would be larger. Therefore, checking consecutive triplets in the sorted list is optimal.

5.  **Return Result**
    If we found at least one good tuple, return the minimum distance. Otherwise, return -1.

