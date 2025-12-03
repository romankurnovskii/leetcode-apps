## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** The list has at most 300 nodes, with values in the range $[-100, 100]$. The list is guaranteed to be sorted in ascending order.
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We traverse the list once.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space (dummy node and pointers).
- **Edge Case:** If the list is empty or contains only duplicates, we return an empty list.

**1.2 High-level approach:**

The goal is to remove all nodes that have duplicate values, keeping only nodes with unique values. We use a two-pointer approach with a dummy node to handle edge cases where the head needs to be removed.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Count occurrences of each value, then rebuild the list with only unique values. This requires $O(n)$ space for counting and $O(n)$ time, but is less efficient in practice.
- **Optimized Strategy:** Use two pointers (`prev` and `curr`) to traverse the list. When duplicates are found, skip all nodes with that value and link `prev` to the node after the duplicates. This is $O(n)$ time and $O(1)$ space.
- **Why optimized is better:** The optimized approach processes the list in a single pass without extra space for counting.

**1.4 Decomposition:**

1. Create a dummy node to handle cases where the head is removed.
2. Use two pointers: `prev` (points to the last unique node) and `curr` (current node being examined).
3. When duplicates are detected, skip all nodes with the duplicate value.
4. Link `prev.next` to the node after the duplicates.
5. Continue until the end of the list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `head = [1,2,3,3,4,4,5]`

We create a dummy node with value 0, and set `dummy.next = head`. This gives us:
- `dummy -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5`
- `prev = dummy`
- `curr = head` (node with value 1)

**2.2 Start Checking:**

We begin traversing the list. `prev` points to the last confirmed unique node, and `curr` points to the current node being examined.

**2.3 Trace Walkthrough:**

| Step | prev.val | curr.val | curr.next.val | Action |
|------|----------|----------|---------------|--------|
| 1 | 0 (dummy) | 1 | 2 | No duplicates, move both pointers |
| 2 | 1 | 2 | 3 | No duplicates, move both pointers |
| 3 | 2 | 3 | 3 | Duplicates found! Skip all 3s |
| 4 | 2 | 4 | 4 | Duplicates found! Skip all 4s |
| 5 | 2 | 5 | None | No duplicates, move both pointers |
| 6 | 5 | None | - | End of list |

**2.4 Increment and Loop:**

When duplicates are found (e.g., `curr.val == curr.next.val`), we:
1. Store the duplicate value.
2. Skip all nodes with that value: `while curr and curr.val == duplicate_val: curr = curr.next`
3. Link `prev.next = curr` to remove the duplicates.

When no duplicates are found, we move both pointers: `prev = curr` and `curr = curr.next`.

**2.5 Return Result:**

After processing, `dummy.next` points to the first unique node. For our example `[1,2,3,3,4,4,5]`, the result is `[1,2,5]`, which is returned.

