# Problem 206: Reverse Linked List

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/reverse-linked-list/

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to reverse a singly linked list, changing the direction of all the links so that the last node becomes the first node and vice versa.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most 5000 nodes, and each node value is between -5000 and 5000.
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We visit each node exactly once.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space for pointers.
- **Edge Case:** If the list is empty (head is None), we return None.

**1.2 High-level approach:**

The goal is to reverse the direction of all links in the list. We use two pointers: one to track the previous node and one to track the current node. As we traverse, we reverse each link by pointing the current node to the previous node.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Store all node values in an array, reverse the array, then create a new linked list. This is $O(n)$ time but $O(n)$ space.
- **Optimized Strategy:** Reverse the links in place using two pointers, modifying the existing list structure. This is $O(n)$ time and $O(1)$ space.
- **Optimization:** By reversing in place without creating new nodes or using extra arrays, we reduce space complexity from $O(n)$ to $O(1)$.

**1.4 Decomposition:**

1. Initialize two pointers: `prev = None` and `current = head`.
2. While `current` is not None:
   - Store the next node before breaking the link.
   - Reverse the link by pointing `current.next` to `prev`.
   - Move `prev` to `current` and `current` to the stored next node.
3. Return `prev` as the new head of the reversed list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `head = [1, 2, 3, 4, 5]`.

- Initialize `prev = None` and `current = head` (pointing to node 1)
- The list structure: `1 -> 2 -> 3 -> 4 -> 5 -> None`

**2.2 Start Checking:**

We begin with the first node and start reversing links.

**2.3 Trace Walkthrough:**

| Step | current.val | next_node | Action | current.next | prev | Updated State |
|------|-------------|-----------|--------|--------------|-----|---------------|
| 1    | 1           | 2         | Store next, reverse link | None | 1 | `None <- 1` (disconnected from 2) |
| 2    | 2           | 3         | Store next, reverse link | 1 | 2 | `None <- 1 <- 2` (disconnected from 3) |
| 3    | 3           | 4         | Store next, reverse link | 2 | 3 | `None <- 1 <- 2 <- 3` (disconnected from 4) |
| 4    | 4           | 5         | Store next, reverse link | 3 | 4 | `None <- 1 <- 2 <- 3 <- 4` (disconnected from 5) |
| 5    | 5           | None      | Store next, reverse link | 4 | 5 | `None <- 1 <- 2 <- 3 <- 4 <- 5` |
| 6    | None        | -         | Exit loop | - | 5 | Reversed list complete |

**2.4 Increment and Loop:**

After reversing each link, we move `prev` to `current` and `current` to `next_node`. This continues until we've processed all nodes.

**2.5 Return Result:**

After the loop, `prev` points to the last node (now the first node) of the reversed list `[5, 4, 3, 2, 1]`, so we return `res = prev`.

