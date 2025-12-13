## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** Array length is between 1 and 16, and values are between 1 and 10⁵.
  * **Time Complexity:** O(2^n * n) - We generate 2^n subsets, and for each subset we compute the OR in O(n) time.
  * **Space Complexity:** O(1) - We only use a constant amount of extra space (excluding the output).
  * **Edge Case:** When all elements are the same, all non-empty subsets have the same OR value.

**High-level approach**
The maximum possible bitwise OR is achieved by taking the OR of all elements. We generate all non-empty subsets and count how many have this maximum OR value.

![Visualization showing subsets and their bitwise OR values]

**Brute force vs. optimized strategy**

  * **Brute Force:** Generate all subsets using bitmasks and check their OR values - this is what we do, and it's efficient for n ≤ 16.
  * **Optimized Strategy:** Same approach - use bitmasking to enumerate all 2^n subsets efficiently.

**Decomposition**

1.  **Calculate Maximum OR:** Compute the OR of all elements to find the maximum possible OR.
2.  **Generate Subsets:** Use bitmasks from 1 to 2^n - 1 to represent all non-empty subsets.
3.  **Compute Subset OR:** For each subset, calculate its bitwise OR.
4.  **Count Matches:** Count how many subsets have OR equal to the maximum.

### Steps

1.  **Initialization & Example Setup:**
    Let's say `nums = [3, 1]`.
    We calculate `max_or = 3 | 1 = 3`.

2.  **Start Processing:**
    We iterate through all bitmasks from 1 to (1 << n) - 1 = 3.

3.  **Trace Walkthrough:**
    
    | Mask (binary) | Subset | OR Value | Match? |
    |---------------|--------|----------|--------|
    | 01 | [3] | 3 | Yes |
    | 10 | [1] | 1 | No |
    | 11 | [3, 1] | 3 | Yes |

4.  **Result:**
    We count 2 subsets with OR = 3.

5.  **Return Result:**
    Return `res = 2`.

