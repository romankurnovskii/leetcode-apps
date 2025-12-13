## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** Array length is between 1 and 10⁵, and values are between 0 and 10⁶.
  * **Time Complexity:** O(n) - We make a single pass through the array.
  * **Space Complexity:** O(n) - We create a result array of size n.
  * **Edge Case:** When the array has only one element, `res[0] = pref[0]`.

**High-level approach**
Given that `pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`, we can recover `arr[i]` using the property that `pref[i] = pref[i-1] ^ arr[i]`, which means `arr[i] = pref[i] ^ pref[i-1]`.

![XOR prefix array showing how to recover original values]

**Brute force vs. optimized strategy**

  * **Brute Force:** Try all possible values for each position - this is exponential and inefficient.
  * **Optimized Strategy:** Use the XOR property: if `a ^ b = c`, then `a = c ^ b`. This allows us to recover each value in O(1) time.

**Decomposition**

1.  **Set First Element:** `res[0] = pref[0]` since the first prefix is just the first element.
2.  **Recover Remaining Elements:** For each position i > 0, compute `res[i] = pref[i] ^ pref[i-1]`.
3.  **Return Result:** Return the recovered array.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `pref = [5, 2, 0, 3, 1]`.
    We create `res = [0, 0, 0, 0, 0]` and set `res[0] = 5`.

2.  **Start Processing:**
    We iterate from index 1 to n-1.

3.  **Trace Walkthrough:**
    
    | i | pref[i] | pref[i-1] | res[i] = pref[i] ^ pref[i-1] | Verification |
    |---|---------|-----------|-------------------------------|--------------|
    | 0 | 5 | - | 5 | pref[0] = 5 ✓ |
    | 1 | 2 | 5 | 2 ^ 5 = 7 | pref[1] = 5 ^ 7 = 2 ✓ |
    | 2 | 0 | 2 | 0 ^ 2 = 2 | pref[2] = 5 ^ 7 ^ 2 = 0 ✓ |
    | 3 | 3 | 0 | 3 ^ 0 = 3 | pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3 ✓ |
    | 4 | 1 | 3 | 1 ^ 3 = 2 | pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1 ✓ |

4.  **Result:**
    After processing, `res = [5, 7, 2, 3, 2]`

5.  **Return Result:**
    Return the array `[5, 7, 2, 3, 2]`.

