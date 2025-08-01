# 61. Rotate List

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/rotate-list/

## Problem Description

Given the `head` of a linked list, rotate the list to the right by `k` places.

**Example 1:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

**Example 2:**
```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

**Constraints:**
- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Explanation

### Strategy

This is a **linked list manipulation problem** that requires rotating a linked list to the right by k positions. The key insight is to find the new head position and break/reconnect the list appropriately.

**Key observations:**
- Rotating by k positions moves the last k nodes to the front
- If k is larger than the list length, we can use modulo to reduce it
- We need to find the new head position (length - k % length)
- We need to break the list at the new head position and reconnect

**High-level approach:**
1. **Find list length**: Count the number of nodes
2. **Normalize k**: Use `k % length` to handle large k values
3. **Find new head**: Calculate the position of the new head
4. **Break and reconnect**: Break the list and reconnect to form rotated list

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If head is null or head.next is null, return head
- If k is 0, return head

**Step 2: Find list length**
- Count the number of nodes in the list

**Step 3: Normalize k**
- Calculate `k = k % length` to handle large k values

**Step 4: Find new head position**
- Calculate `new_head_pos = length - k`

**Step 5: Break and reconnect**
- Find the node before the new head
- Break the list at that point
- Connect the end to the original head

**Example walkthrough:**
Let's trace through the first example:

```
head = [1,2,3,4,5], k = 2

Step 1: Find length
length = 5

Step 2: Normalize k
k = 2 % 5 = 2

Step 3: Find new head position
new_head_pos = 5 - 2 = 3

Step 4: Find the node before new head
current = head, count = 0
current = 2, count = 1
current = 3, count = 2 (this is the node before new head)

Step 5: Break and reconnect
new_head = 4
current.next = None (break at 3)
last_node.next = head (connect 5 to 1)

Result: [4,5,1,2,3]
```

> **Note:** The key insight is that rotating by k positions is equivalent to moving the last k nodes to the front. We can achieve this by finding the new head position and breaking/reconnecting the list at the appropriate point.

### Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Find the length of the list
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        
        # Normalize k
        k = k % length
        if k == 0:
            return head
        
        # Find the new head position
        new_head_pos = length - k
        
        # Find the node before the new head
        current = head
        for _ in range(new_head_pos - 1):
            current = current.next
        
        # Break the list and reconnect
        new_head = current.next
        current.next = None
        
        # Connect the end to the original head
        last_node = new_head
        while last_node.next:
            last_node = last_node.next
        last_node.next = head
        
        # Return the new head
        return new_head
```

**Time Complexity:** O(n) - we visit each node at most twice  
**Space Complexity:** O(1) - we only use a constant amount of extra space 