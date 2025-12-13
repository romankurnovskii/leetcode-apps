## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The number of nodes is in the range `[1, 5000]`, and node values are between 1 and 1000.
  * **Time Complexity:** O(n * log(max_val)) - We iterate through n-1 pairs of adjacent nodes, and calculating GCD takes O(log(max_val)) time where max_val is the maximum node value.
  * **Space Complexity:** O(1) - We only use a constant amount of extra space (excluding the output list which is required).
  * **Edge Case:** A list with only one node requires no insertions.

**High-level approach**
We traverse the linked list and insert a new node between each pair of adjacent nodes. The value of the inserted node is the greatest common divisor (GCD) of the two adjacent node values.

**Brute force vs. optimized strategy**

  * **Brute Force:** Calculate GCD for each pair using Euclidean algorithm - this is already optimal.
  * **Optimized Strategy:** Use the Euclidean algorithm to compute GCD efficiently. The algorithm repeatedly applies the modulo operation until one number becomes zero.

**Decomposition**

1.  **Define GCD Function:** Implement Euclidean algorithm to find GCD of two numbers.
2.  **Traverse List:** Move through the linked list, processing each pair of adjacent nodes.
3.  **Calculate GCD:** For each pair, compute the GCD of their values.
4.  **Insert Node:** Create a new node with the GCD value and insert it between the pair.
5.  **Continue:** Move to the next pair and repeat.

### Steps

1.  **Initialization & Example Setup:**
    Let's say we have a linked list: `[18, 6, 10, 3]`
    We start with `current = head` pointing to the node with value 18.

2.  **Start Processing:**
    We check if `current` and `current.next` exist. For the first pair, we have nodes with values 18 and 6.

3.  **Trace Walkthrough:**
    
    | Current Pair | GCD Calculation | GCD Value | Action |
    |-------------|----------------|-----------|--------|
    | 18, 6 | gcd(18, 6) = 6 | 6 | Insert node(6) between 18 and 6 |
    | 6, 10 | gcd(6, 10) = 2 | 2 | Insert node(2) between 6 and 10 |
    | 10, 3 | gcd(10, 3) = 1 | 1 | Insert node(1) between 10 and 3 |

4.  **Result:**
    After all insertions, the list becomes: `[18, 6, 6, 2, 10, 1, 3]`

5.  **Return Result:**
    Return the modified head of the linked list.
