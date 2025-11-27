## Explanation

### Strategy (The "Why")

Given the head of a linked list and an integer $n$, we need to remove the $n$-th node from the end of the list and return the head.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be between $1$ and $30$.
- **Value Range:** Node values are between $1$ and $100$.
- **Time Complexity:** $O(L)$ where $L$ is the length of the list. We make one pass through the list.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If we need to remove the head node ($n$ equals the list length), we need special handling. Using a dummy node simplifies this.

**1.2 High-level approach:**

The goal is to remove the $n$-th node from the end of a linked list.

![Remove Nth Node](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

We use two pointers: a fast pointer and a slow pointer. We move the fast pointer $n+1$ steps ahead, then move both pointers together. When fast reaches the end, slow will be at the node before the one to remove.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** First pass to count the length, second pass to find and remove the $(L-n+1)$-th node from the beginning. This takes two passes.
- **Optimized Strategy (Two Pointers):** Use two pointers with a gap of $n+1$ nodes. Move both together until the fast pointer reaches the end. This takes one pass.
- **Why it's better:** The two-pointer approach is more elegant and requires only one pass through the list, though both approaches have the same time complexity.

**1.4 Decomposition:**

1. Create a dummy node pointing to the head (to handle edge cases).
2. Initialize two pointers (fast and slow) at the dummy node.
3. Move the fast pointer $n+1$ steps ahead.
4. Move both pointers together until fast reaches the end.
5. Remove the node after slow (which is the $n$-th node from the end).
6. Return the head (via dummy.next).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: head = $[1,2,3,4,5]$, $n = 2$

We initialize:
- `dummy = ListNode(0)`, `dummy.next = head`
- `fast = dummy`, `slow = dummy`

**2.2 Start Processing:**

We move the fast pointer $n+1 = 3$ steps ahead.

**2.3 Trace Walkthrough:**

| Step | Fast Position | Slow Position | Action |
|------|---------------|---------------|--------|
| Initial | dummy | dummy | - |
| After moving fast 3 steps | node 4 | dummy | Fast is 3 steps ahead |
| Move both together | node 5 | node 1 | Continue... |
| Move both together | null | node 3 | Fast reached end |

When fast is null, slow is at node 3 (the node before node 4, which is the 2nd from end).

**2.4 Remove Node:**

- `slow.next = slow.next.next` removes node 4
- Result: $[1,2,3,5]$

**2.5 Return Result:**

We return `dummy.next` which points to the new head $[1,2,3,5]$.

> **Note:** The dummy node is crucial because it handles the edge case where we need to remove the head node. Without it, we'd need special handling for that case.

