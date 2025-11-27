## Explanation

### Strategy (The "Why")

Given two sorted linked lists `list1` and `list2`, we need to merge them into one sorted list and return the head of the merged list.

**1.1 Constraints & Complexity:**

- **Input Size:** The total number of nodes can be up to $50$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of the two lists. We visit each node exactly once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for the dummy node and pointers.
- **Edge Case:** If one list is empty, return the other list. If both are empty, return `null`.

**1.2 High-level approach:**

The goal is to merge two sorted linked lists into one sorted list.

We use a dummy node to simplify edge cases and a current pointer to build the merged list. We compare nodes from both lists and attach the smaller one to the result, then move the pointer of the list we took from.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert both lists to arrays, merge the arrays, then convert back to a linked list. This takes $O(n + m)$ time and $O(n + m)$ space.
- **Optimized Strategy (Two Pointers):** Use two pointers to traverse both lists simultaneously, building the merged list in-place. This takes $O(n + m)$ time and $O(1)$ space.
- **Why it's better:** The two-pointer approach uses $O(1)$ extra space instead of $O(n + m)$ for arrays, while maintaining the same time complexity.

**1.4 Decomposition:**

1. Create a dummy node to simplify edge cases.
2. Initialize a current pointer at the dummy node.
3. While both lists have nodes, compare the values and attach the smaller node to the result.
4. Move the pointer of the list we took from.
5. Attach the remaining nodes from the non-empty list.
6. Return the head of the merged list (dummy.next).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $list1 = [1,2,4]$, $list2 = [1,3,4]$

We initialize:
- `dummy = ListNode(0)`
- `current = dummy`

**2.2 Start Merging:**

We begin comparing nodes from both lists.

**2.3 Trace Walkthrough:**

| Step | list1.val | list2.val | Compare | Attach | current.next | list1/list2 After |
|------|-----------|-----------|---------|--------|--------------|-------------------|
| 1 | 1 | 1 | Equal | list1 | 1 | list1 = 2 |
| 2 | 2 | 1 | 2 > 1 | list2 | 1 | list2 = 3 |
| 3 | 2 | 3 | 2 < 3 | list1 | 2 | list1 = 4 |
| 4 | 4 | 3 | 4 > 3 | list2 | 3 | list2 = 4 |
| 5 | 4 | 4 | Equal | list1 | 4 | list1 = null |
| 6 | null | 4 | - | list2 | 4 | list2 = null |

**2.4 Final Result:**

After merging: $[1,1,2,3,4,4]$

**2.5 Return Result:**

We return the head of the merged list: $[1,1,2,3,4,4]$

> **Note:** The dummy node simplifies the code by providing a starting point. Without it, we'd need special handling for the first node. The key is to always attach the smaller node and move the corresponding pointer forward.
