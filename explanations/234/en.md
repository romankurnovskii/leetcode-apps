# Problem 234: Palindrome Linked List
**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/palindrome-linked-list/

## Explanation

### Strategy (The "Why")

The problem asks us to determine if a singly linked list is a palindrome (reads the same forwards and backwards).

**1.1 Constraints & Complexity:**

- **Input Constraints:** The list has $1 \leq n \leq 10^5$ nodes, with values in $[0, 9]$.
- **Time Complexity:** $O(n)$ - We traverse the list once to collect values, then compare them.
- **Space Complexity:** $O(n)$ - We store all node values in an array for comparison.
- **Edge Case:** A single-node list is always a palindrome.

**1.2 High-level approach:**

The goal is to check if the linked list values form a palindrome. We convert the list to an array, then use two pointers to compare values from both ends.

![Palindrome Linked List](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Reverse the entire list, then compare with original. This requires $O(n)$ time and $O(n)$ space for the reversed list.
- **Optimized (Array Conversion):** Convert list to array, then use two pointers. This takes $O(n)$ time and $O(n)$ space.
- **Emphasize the optimization:** While both approaches have similar complexity, the array approach is simpler and more intuitive. For $O(1)$ space, we could reverse half the list, but that's more complex.

**1.4 Decomposition:**

1. **Convert to Array:** Traverse the list and store all values in an array.
2. **Two-Pointer Comparison:** Use left and right pointers to compare values from both ends.
3. **Check Match:** If any pair doesn't match, return `False`. If all pairs match, return `True`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `head = [1,2,2,1]`.

After conversion: `values = [1, 2, 2, 1]`

**2.2 Start Checking:**

Initialize `left = 0` and `right = len(values) - 1 = 3`.

**2.3 Trace Walkthrough:**

| Step | left | right | values[left] | values[right] | Match? | Action |
|------|------|-------|--------------|----------------|--------|--------|
| 1 | 0 | 3 | 1 | 1 | Yes | Continue |
| 2 | 1 | 2 | 2 | 2 | Yes | Continue |
| 3 | 2 | 1 | - | - | - | Stop (left >= right) |

**2.4 Complete Comparison:**

All pairs matched: (1,1) and (2,2).

**2.5 Return Result:**

Since all comparisons passed, the function returns `True`.

> **Note:** The two-pointer technique efficiently checks palindromes by comparing symmetric positions without needing to reverse the list.

