## Explanation

### Strategy

**Restate the problem**  
Delete a given node (not tail) from a singly linked list when only that node reference is provided.

**1.1 Constraints & Complexity**  
- **Input Size:** 2 to 1000 nodes.  
- **Time Complexity:** O(1) for the delete operation.  
- **Space Complexity:** O(1).  
- **Edge Case:** The given node’s next exists (guaranteed).

**1.2 High-level approach**  
Copy the next node’s value into the current node, then bypass the next node.  
![In-place delete by copying next](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Traverse from head to find previous node — impossible without head.  
- **Optimized:** Overwrite current node with next node data; O(1).

**1.4 Decomposition**  
1. Set `node.val = node.next.val`.  
2. Link `node.next = node.next.next`.  
3. Done.

### Steps

**2.1 Initialization & Example Setup**  
List: `4 -> 5 -> 1 -> 9`, node to delete = value 5.

**2.2 Start Checking**  
Copy next (1) into current.

**2.3 Trace Walkthrough**  
| Step | node.val before | node.next.val | Action                      | List becomes        |
|------|-----------------|---------------|-----------------------------|---------------------|
| 1    | 5               | 1             | node.val = 1                | 4 -> 1 -> 1 -> 9    |
| 2    | 1               | 1             | node.next = node.next.next  | 4 -> 1 -> 9         |

**2.4 Increment and Loop**  
No loop; constant steps.

**2.5 Return Result**  
Node effectively removed; list is `4 -> 1 -> 9`.
## Explanation

### Strategy

**Restate the problem**

We need to delete a node from a linked list, but we are only given access to the node to be deleted (not the head). We cannot access the previous node directly.

**1.1 Constraints & Complexity**

- **Input Size:** The linked list has 2 to 1000 nodes.
- **Time Complexity:** O(1) - We only perform a constant number of operations.
- **Space Complexity:** O(1) - No additional space is used.
- **Edge Case:** The node to delete is guaranteed not to be the tail node, so we can safely access node.next.next.

**1.2 High-level approach**

Since we cannot access the previous node, we cannot directly unlink the current node. Instead, we copy the value from the next node into the current node, then skip the next node by linking the current node to the node after the next one.

![Linked list node deletion by copying value](https://assets.leetcode.com/uploads/2020/09/01/node1.jpg)

**1.3 Brute force vs. optimized strategy**

- **Brute Force:** If we had access to the head, we could traverse to find the previous node and update its next pointer. This would be O(n) time.
- **Optimized Strategy:** Copy the next node's value to the current node and skip the next node. This is O(1) time.
- **Why optimized is better:** We achieve constant time deletion by cleverly copying data instead of restructuring the list.

**1.4 Decomposition**

1. **Copy Value:** Copy the value from node.next to node.
2. **Skip Next Node:** Update node.next to point to node.next.next, effectively removing the next node from the list.

### Steps

**2.1 Initialization & Example Setup**

Let's use the example: `head = [4,5,1,9]`, `node = 5` (the node with value 5)

- The linked list: 4 → 5 → 1 → 9
- We are given the node containing value 5 (second node)

**2.2 Start Processing**

We need to delete the node with value 5. Since we only have access to this node, we cannot modify the previous node (4).

**2.3 Trace Walkthrough**

| Step | Current Node Value | Next Node Value | Action | Result |
|------|-------------------|-----------------|--------|--------|
| Initial | 5 | 1 | - | 4 → 5 → 1 → 9 |
| Copy | 5 → 1 | 1 | Copy next value | 4 → 1 → 1 → 9 |
| Skip | 1 | 9 | Link to next.next | 4 → 1 → 9 |

**2.4 Update Pointers**

After copying the value, we update `node.next = node.next.next`, which removes the duplicate node from the list.

**2.5 Return Result**

The list becomes `[4,1,9]`, effectively deleting the original node with value 5. Note that we actually deleted the next node, but from the user's perspective, the node with value 5 is gone.
