## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The number of nodes is in the range `[3, 2 * 10⁵]`, and node values are between 0 and 1000.
  * **Time Complexity:** O(n) - We traverse the linked list once, visiting each node exactly once.
  * **Space Complexity:** O(1) - We only use a constant amount of extra space (excluding the output list).
  * **Edge Case:** The list always starts and ends with zero nodes, and there are no two consecutive zeros.

**High-level approach**
We traverse the linked list, summing values between consecutive zero nodes. Each sum becomes a new node in the result list, and we skip the zero nodes.

**Brute force vs. optimized strategy**

  * **Brute Force:** Create a new list by collecting values between zeros - this is what we do, and it's optimal.
  * **Optimized Strategy:** Same approach - single pass through the list, summing values between zeros.

**Decomposition**

1.  **Skip First Zero:** Start from the node after the first zero.
2.  **Sum Values:** Accumulate values until we encounter the next zero.
3.  **Create Node:** Create a new node with the sum and add it to the result.
4.  **Repeat:** Continue until we've processed all nodes.

### Steps

1.  **Initialization & Example Setup:**
    Let's say we have a linked list: `[0, 3, 1, 0, 4, 5, 2, 0]`
    We skip the first zero and start with `current` pointing to node with value 3.

2.  **Start Processing:**
    We create a dummy node to build the result list: `dummy = ListNode(0)`, `tail = dummy`.

3.  **Trace Walkthrough:**
    
    | Current Node | Value | Sum | Action |
    |-------------|------|-----|--------|
    | 3 | 3 | 3 | Add to sum |
    | 1 | 1 | 4 | Add to sum |
    | 0 | 0 | - | Create node(4), reset sum |
    | 4 | 4 | 4 | Add to sum |
    | 5 | 5 | 9 | Add to sum |
    | 2 | 2 | 11 | Add to sum |
    | 0 | 0 | - | Create node(11), done |

4.  **Result:**
    After processing, we have a list: `[4, 11]`

5.  **Return Result:**
    Return `dummy.next` which points to the first merged node.

