## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** Array length n is between 1 and 50, and values are between 1 and n.
  * **Time Complexity:** O(n²) - For each prefix, we check common elements, which takes O(n) time in worst case.
  * **Space Complexity:** O(n) - We maintain two sets, each storing at most n elements.
  * **Edge Case:** At index 0, no elements are common yet, so C[0] = 0.

**High-level approach**
For each prefix position i, we maintain sets of elements seen so far in both arrays. The number of common elements at position i is the size of the intersection of these two sets.

**Brute force vs. optimized strategy**

  * **Brute Force:** For each prefix, check all elements in both arrays up to that position - this is what we do, and it's efficient.
  * **Optimized Strategy:** Use sets to track seen elements and compute intersection - this is optimal for the given constraints.

**Decomposition**

1.  **Initialize Sets:** Create two sets to track elements seen in A and B.
2.  **Process Each Position:** For each index i, add A[i] and B[i] to their respective sets.
3.  **Count Common Elements:** The number of common elements is the size of the set intersection.
4.  **Store Result:** Add the count to the result array.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `A = [1, 3, 2, 4]` and `B = [3, 1, 2, 4]`.
    We create `seen_a = set()`, `seen_b = set()`, and `res = []`.

2.  **Start Processing:**
    We iterate through each index from 0 to n-1.

3.  **Trace Walkthrough:**
    
    | i | A[i] | B[i] | seen_a | seen_b | Common | res |
    |---|------|------|--------|--------|--------|-----|
    | 0 | 1 | 3 | {1} | {3} | 0 | [0] |
    | 1 | 3 | 1 | {1,3} | {3,1} | 2 | [0,2] |
    | 2 | 2 | 2 | {1,3,2} | {3,1,2} | 3 | [0,2,3] |
    | 3 | 4 | 4 | {1,3,2,4} | {3,1,2,4} | 4 | [0,2,3,4] |

4.  **Result:**
    After processing, `res = [0, 2, 3, 4]`

5.  **Return Result:**
    Return the array `[0, 2, 3, 4]`.

