# Problem 876: Middle of the Linked List

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/middle-of-the-linked-list/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the middle node of a linked list. If there are two middle nodes (even length), we return the second one.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most 100 nodes, and each node value is between 1 and 100.
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We traverse the list once with the fast pointer.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space for two pointers.
- **Edge Case:** If the list has an even number of nodes, we return the second middle node (e.g., in [1,2,3,4], we return node 3).

**1.2 High-level approach:**

The goal is to find the middle node efficiently without knowing the list length beforehand. We use the "tortoise and hare" approach: one pointer moves slowly (one step at a time) while another moves fast (two steps at a time). When the fast pointer reaches the end, the slow pointer will be at the middle.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** First traverse the list to count nodes, then traverse again to the middle position. This is $O(n)$ time but requires two passes.
- **Optimized Strategy:** Use two pointers moving at different speeds in a single pass. This is $O(n)$ time in a single pass.
- **Optimization:** By using two pointers, we find the middle in one pass instead of two, making the code simpler and slightly more efficient.

**1.4 Decomposition:**

1. Initialize two pointers: `slow` and `fast`, both starting at the head.
2. Move `slow` one step and `fast` two steps in each iteration.
3. Continue until `fast` reaches the end (either `fast` is None or `fast.next` is None).
4. When `fast` reaches the end, `slow` will be at the middle node.
5. Return the node that `slow` points to.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `head = [1, 2, 3, 4, 5]`.

- Initialize `slow = head` (pointing to node 1)
- Initialize `fast = head` (pointing to node 1)
- The list structure: `1 -> 2 -> 3 -> 4 -> 5 -> None`

**2.2 Start Checking:**

We begin moving both pointers, with `slow` moving one step and `fast` moving two steps at a time.

**2.3 Trace Walkthrough:**

| Step | slow.val | fast.val | Condition | Action | Updated slow | Updated fast |
|------|----------|----------|-----------|--------|--------------|--------------|
| 0    | 1        | 1        | fast and fast.next exist | Move pointers | 1 | 1 |
| 1    | 1        | 1        | - | slow = slow.next, fast = fast.next.next | 2 | 3 |
| 2    | 2        | 3        | fast and fast.next exist | Move pointers | 3 | 5 |
| 3    | 3        | 5        | fast.next is None | Exit loop | 3 | 5 |

**2.4 Increment and Loop:**

In each iteration, `slow` moves to `slow.next` and `fast` moves to `fast.next.next`. The loop continues while `fast` and `fast.next` are not None.

**2.5 Return Result:**

After the loop, `slow` points to node 3, which is the middle node. The result is `[3, 4, 5]`, so we return `res = slow`.

