# Problem 21: Merge Two Sorted Lists

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/merge-two-sorted-lists/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to merge two sorted linked lists into one sorted linked list by combining their nodes. The merged list should maintain the sorted order.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most 50 nodes in each list, and each node value is between -100 and 100.
- **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of the two lists. We visit each node exactly once.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space (dummy node and pointer).
- **Edge Case:** If one or both lists are empty, we return the non-empty list or an empty list.

**1.2 High-level approach:**

The goal is to compare nodes from both lists one by one, always selecting the smaller value, and link them together in sorted order. We use a dummy node to simplify handling the head of the merged list.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert both lists to arrays, merge the arrays, then create a new linked list. This is $O(n + m)$ time but $O(n + m)$ space.
- **Optimized Strategy:** Use two pointers to traverse both lists simultaneously, comparing values and linking nodes in place. This is $O(n + m)$ time and $O(1)$ space.
- **Optimization:** By merging in place without creating new nodes, we reduce space complexity from $O(n + m)$ to $O(1)$.

**1.4 Decomposition:**

1. Create a dummy node to serve as the starting point of the merged list.
2. Use a pointer to track the current position in the merged list.
3. While both lists have nodes, compare their values.
4. Link the smaller node to the merged list and move the corresponding pointer forward.
5. After one list is exhausted, attach the remaining nodes from the other list.
6. Return the merged list (starting from dummy.next).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`.

- Create `dummy = ListNode(0)` and `current = dummy`
- `list1` points to node with value 1
- `list2` points to node with value 1

**2.2 Start Checking:**

We begin comparing the first nodes from both lists.

**2.3 Trace Walkthrough:**

| Step | list1.val | list2.val | Comparison | Action | current.next | Updated Pointers |
|------|-----------|-----------|------------|--------|--------------|------------------|
| 1    | 1         | 1         | 1 <= 1     | Link list1 node | list1 (val=1) | list1 → 2, current → 1 |
| 2    | 2         | 1         | 2 > 1      | Link list2 node | list2 (val=1) | list2 → 3, current → 1 |
| 3    | 2         | 3         | 2 <= 3     | Link list1 node | list1 (val=2) | list1 → 4, current → 2 |
| 4    | 4         | 3         | 4 > 3      | Link list2 node | list2 (val=3) | list2 → 4, current → 3 |
| 5    | 4         | 4         | 4 <= 4     | Link list1 node | list1 (val=4) | list1 → None, current → 4 |
| 6    | None      | 4         | -          | Attach remaining | list2 (val=4) | list2 → None, current → 4 |

**2.4 Increment and Loop:**

After linking a node, we move the pointer of the list we took from forward, and move `current` to the newly linked node. This continues until one list is exhausted.

**2.5 Return Result:**

After processing, `dummy.next` points to the head of the merged list `[1, 1, 2, 3, 4, 4]`, so we return `res = dummy.next`.

