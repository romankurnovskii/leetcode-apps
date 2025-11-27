## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Array Size:** The array can have 2 to 100 elements.
  * **Value Range:** Each element is between 1 and 100.
  * **Time Complexity:** Finding min/max takes $O(n)$, creating a set takes $O(n)$, and checking the range takes $O(n)$ in the worst case. Overall $O(n)$.
  * **Space Complexity:** $O(n)$ for the set.
  * **Edge Cases:**
    * If the array only has 2 elements (min and max), we check all numbers between them.
    * If all numbers in the range are present, return an empty list.

**High-level approach**
The problem asks us to find all missing integers in the range from the minimum to the maximum value in the array.

  * The smallest and largest integers are guaranteed to be present in the array.
  * We need to check all integers in the range $[min, max]$ and identify which ones are missing.
  * Since the array contains unique integers, we can use a set for efficient lookup.

**Brute force vs. optimized strategy**

  * **Brute Force:** For each number in the range, check if it exists in the array by iterating through the array. This would be $O(n \times (max - min))$.
  * **Optimized (Set Lookup):** Convert the array to a set for $O(1)$ lookup. Then iterate through the range and check membership in the set. This is $O(n + (max - min))$, which is more efficient.

**Decomposition**

1.  **Find Range:** Identify the minimum and maximum values in the array.
2.  **Create Set:** Convert the array to a set for fast membership testing.
3.  **Check Range:** Iterate through all integers from $min + 1$ to $max - 1$ (excluding the endpoints since they're guaranteed to be present).
4.  **Collect Missing:** Add any number not found in the set to the result list.
5.  **Return Result:** Return the list of missing elements (already sorted since we iterate in order).

### Steps

1.  **Find Minimum and Maximum**
    Iterate through the array to find the smallest and largest values. For example, in $[1,4,2,5]$, $min = 1$ and $max = 5$.

2.  **Create Set for Lookup**
    Convert the array to a set. This allows $O(1)$ membership testing. For $[1,4,2,5]$, the set is $\{1, 2, 4, 5\}$.

3.  **Iterate Through Range**
    Check all integers from $min + 1$ to $max - 1$ (we skip $min$ and $max$ since they're guaranteed to be present). For the example, we check $2, 3, 4$.

4.  **Check Membership**
    For each number in the range, check if it exists in the set:
      * If not present, add it to the missing list.
      * In the example: $2$ is present, $3$ is missing, $4$ is present.

5.  **Return Result**
    Return the list of missing elements. Since we iterate in increasing order, the result is automatically sorted: $[3]$.

