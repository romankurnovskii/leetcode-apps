## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The linked list has $n$ nodes where $1 \leq n \leq 500$, and $1 \leq left \leq right \leq n$.
* **Time Complexity:** $O(n)$ - We traverse the list once to find the reversal segment, then reverse it in-place.
* **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
* **Edge Case:** If $left == right$, no reversal is needed, return the list as is.

**1.2 High-level approach**

The goal is to reverse a specific segment of a linked list from position $left$ to position $right$, while keeping the rest of the list unchanged. We use a dummy node to handle the case when reversal starts at the head.

![Linked list partial reversal showing how nodes are reversed in a segment]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Convert the linked list to an array, reverse the segment, then rebuild the list. This uses $O(n)$ extra space.
* **Optimized (In-Place Reversal):** Use pointer manipulation to reverse the segment in-place. We find the segment boundaries, then reverse nodes one by one. This uses $O(1)$ extra space.

**1.4 Decomposition**

1. Create a dummy node to handle edge cases.
2. Move to the node before the reversal segment.
3. Reverse the segment by adjusting pointers iteratively.
4. Connect the reversed segment back to the list.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $head = [1,2,3,4,5]$, $left = 2$, $right = 4$.

We initialize:
* `dummy = ListNode(0)` with `dummy.next = head`
* `prev = dummy` (will point to node before reversal segment)

**2.2 Start Processing**

We move `prev` to position $left - 1$ (node with value 1).

**2.3 Trace Walkthrough**

| Step | prev | curr | next_node | List State |
|------|------|------|-----------|------------|
| Initial | node(0) | node(1) | - | [0,1,2,3,4,5] |
| Move prev | node(1) | node(2) | - | [0,1,2,3,4,5] |
| Reverse 1 | node(1) | node(2) | node(3) | [0,1,3,2,4,5] |
| Reverse 2 | node(1) | node(2) | node(4) | [0,1,4,3,2,5] |

After reversal: `[1,4,3,2,5]` (segment [2,3,4] reversed to [4,3,2]).

**2.4 Increment and Loop**

For each iteration in the reversal loop:
1. Save `next_node = curr.next`
2. Set `curr.next = next_node.next` (skip next_node)
3. Set `next_node.next = prev.next` (insert next_node at start)
4. Set `prev.next = next_node` (update prev's next)

**2.5 Return Result**

After reversal, `dummy.next` points to the modified list: `[1,4,3,2,5]`.

