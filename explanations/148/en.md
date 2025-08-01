# 148. Sort List

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/sort-list/

## Problem Description

Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

**Example 1:**
```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

**Example 2:**
```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Example 3:**
```
Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?

## Explanation

### Strategy

This is a **divide-and-conquer problem** that requires sorting a linked list in O(n log n) time and O(1) space. The key insight is to use merge sort, which naturally works well with linked lists and can be implemented in-place.

**Key observations:**
- We need O(n log n) time complexity for optimal sorting
- We need O(1) space complexity (no extra data structures)
- Merge sort is perfect for linked lists because we can split and merge in-place
- We can use the fast/slow pointer technique to find the middle

**High-level approach:**
1. **Find the middle**: Use fast/slow pointers to split the list
2. **Recursively sort**: Sort the left and right halves
3. **Merge sorted lists**: Merge the two sorted halves
4. **Return result**: Return the merged sorted list

### Steps

Let's break down the solution step by step:

**Step 1: Handle base cases**
- If head is null or head.next is null, return head (already sorted)

**Step 2: Find the middle of the list**
- Use fast/slow pointer technique
- Slow pointer moves 1 step, fast pointer moves 2 steps
- When fast reaches end, slow is at middle

**Step 3: Split the list**
- Set `mid = slow.next`
- Set `slow.next = None` to split the list

**Step 4: Recursively sort halves**
- Sort the left half: `left = sortList(head)`
- Sort the right half: `right = sortList(mid)`

**Step 5: Merge the sorted halves**
- Use a dummy node to simplify merging
- Compare nodes from both lists and link them in order

**Example walkthrough:**
Let's trace through the first example:

```
head = [4,2,1,3]

Step 1: Find middle
slow = 4, fast = 4
slow = 2, fast = 1
slow = 1, fast = 3
slow = 3, fast = null
middle = 3

Step 2: Split list
left = [4,2,1], right = [3]

Step 3: Recursively sort left
left = [4,2,1] → [1,2,4]

Step 4: Recursively sort right
right = [3] → [3]

Step 5: Merge [1,2,4] and [3]
result = [1,2,3,4]
```

> **Note:** Merge sort is ideal for linked lists because we can split and merge in-place without extra space. The fast/slow pointer technique efficiently finds the middle, and the merge step can be done by simply relinking nodes.

### Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle base cases
        if not head or not head.next:
            return head
        
        # Find the middle of the list
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list
        mid = slow.next
        slow.next = None
        
        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify merging
        dummy = ListNode(0)
        current = dummy
        
        # Merge the two sorted lists
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        # Attach remaining nodes
        if left:
            current.next = left
        if right:
            current.next = right
        
        # Return the merged list (skip dummy node)
        return dummy.next
```

**Time Complexity:** O(n log n) - merge sort time complexity  
**Space Complexity:** O(log n) - recursion stack space (not O(1) due to recursion) 