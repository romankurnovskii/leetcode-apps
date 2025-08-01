# 142. Linked List Cycle II

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/linked-list-cycle-ii/

## Problem Description

Given the `head` of a linked list, return *the node where the cycle begins. If there is no cycle, return* `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:**
```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

**Constraints:**
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Explanation

### Strategy

This is a **two-pointer problem** that extends the cycle detection problem to find the starting node of the cycle. The key insight is to use Floyd's Cycle-Finding Algorithm in two phases: first to detect the cycle, then to find its starting point.

**Key observations:**
- If there's a cycle, we can find the meeting point using fast/slow pointers
- The distance from head to cycle start equals the distance from meeting point to cycle start
- We can use this mathematical relationship to find the cycle start
- This approach uses O(1) space, which is optimal

**High-level approach:**
1. **Phase 1 - Detect cycle**: Use fast/slow pointers to find meeting point
2. **Phase 2 - Find cycle start**: Use two pointers from head and meeting point
3. **Return result**: The node where these pointers meet is the cycle start

### Steps

Let's break down the solution step by step:

**Phase 1: Detect the cycle**
- Use fast and slow pointers to find the meeting point
- If no meeting point is found, return null (no cycle)

**Phase 2: Find the cycle start**
- Reset slow pointer to head
- Move both pointers one step at a time
- The node where they meet is the cycle start

**Mathematical proof:**
- Let `F` be the distance from head to cycle start
- Let `C` be the cycle length
- Let `a` be the distance from cycle start to meeting point
- When fast and slow meet: `slow` has traveled `F + a`, `fast` has traveled `F + a + n*C`
- Since fast moves twice as fast: `2(F + a) = F + a + n*C`
- Simplifying: `F + a = n*C`
- Therefore: `F = n*C - a`
- This means the distance from head to cycle start equals the distance from meeting point to cycle start

**Example walkthrough:**
Let's trace through the first example:

```
head = [3,2,0,-4], pos = 1 (cycle from -4 back to 2)

Phase 1 - Detect cycle:
slow = 3, fast = 2
slow = 2, fast = 0
slow = 0, fast = 2
slow = -4, fast = 0
slow = 2, fast = 2 (meeting point found!)

Phase 2 - Find cycle start:
slow = 3 (reset to head), fast = 2 (meeting point)
slow = 2, fast = 0
slow = 0, fast = -4
slow = -4, fast = 2 (they meet at node 2!)

Result: Return node with value 2
```

> **Note:** This algorithm is optimal because it uses O(1) space and O(n) time. The mathematical proof ensures that the two pointers will meet at the cycle start after the second phase.

### Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next:
            return None
        
        # Phase 1: Find the meeting point
        slow = head
        fast = head
        
        # Find meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If pointers meet, cycle detected
            if slow == fast:
                break
        else:
            # No cycle found
            return None
        
        # Phase 2: Find the cycle start
        slow = head
        
        # Move both pointers one step at a time
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Return the cycle start
        return slow
```

**Time Complexity:** O(n) - we visit each node at most twice  
**Space Complexity:** O(1) - we only use two pointers regardless of input size 