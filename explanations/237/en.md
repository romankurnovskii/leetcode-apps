## Explanation

### Strategy

**Constraints & Edge Cases**

* **Linked List:** The list has 2-1000 nodes with unique values. The node to delete is guaranteed to not be the tail node.
* **Time Complexity:** We only need to copy the next node's value and update the pointer, which is O(1). **Time Complexity: O(1)**, **Space Complexity: O(1)**.
* **Edge Case:** Since the node is guaranteed not to be the tail, we can always access `node.next`.

**High-level approach**

The problem asks us to delete a node from a linked list, but we're only given access to that node (not the head). We can't delete the node itself, but we can make it "disappear" by copying the next node's data and skipping the next node.

**Brute force vs. optimized strategy**

* **Brute Force:** There's no brute force needed here - we simply copy the next node's value and update the pointer.
* **Optimized:** Copy `node.next.val` to `node.val`, then set `node.next = node.next.next`. This effectively removes the current node from the list.

**Decomposition**

1. **Copy Value:** Copy the next node's value to the current node.
2. **Skip Next Node:** Update the current node's next pointer to skip the next node.

### Steps

1. **Initialization & Example Setup**
   Let's use `head = [4,5,1,9]`, `node = 5` (the node with value 5) as our example.
   - The node to delete is the second node (value 5).
   - We have: `4 -> 5 -> 1 -> 9`.

2. **Copy Next Node's Value**
   - `node.val = node.next.val` → `node.val = 1`.
   - Now the list looks like: `4 -> 1 -> 1 -> 9` (temporarily has duplicate 1).

3. **Skip Next Node**
   - `node.next = node.next.next` → Skip the node with value 1.
   - Now: `4 -> 1 -> 9`.

4. **Trace Walkthrough**

| Step | Action | List State |
|------|--------|------------|
| Initial | - | 4 -> 5 -> 1 -> 9 |
| 1 | Copy next.val to node.val | 4 -> 1 -> 1 -> 9 |
| 2 | Skip next node | 4 -> 1 -> 9 |

5. **Result**
   The node with value 5 is effectively removed. The list now contains [4,1,9].
