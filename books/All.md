# All



## 1. Two Sum [Easy]
https://leetcode.com/problems/two-sum/

### Explanation

To solve the Two Sum problem, we want to find two numbers in the array that add up to a given target. The most efficient way is to use a hash map (dictionary) to store the numbers we have seen so far and their indices. As we iterate through the array, for each number, we check if the complement (target - current number) exists in the hash map. If it does, we have found the solution. Otherwise, we add the current number and its index to the hash map. This approach has O(n) time complexity.

## Hint

Try using a hash map to keep track of the numbers you have seen so far and their indices.

## Points

- Time complexity: O(n) using a hash map.
- Brute-force solution is O(n^2) and not efficient for large arrays.
- There is always exactly one solution, and you may not use the same element twice.
- Be careful with duplicate numbers in the array.

### Solution

```python
def two_sum(nums, target):
    """Find two numbers that add up to target using a hash map for O(n) time complexity."""
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
```

## 2. Add Two Numbers [Medium]
https://leetcode.com/problems/add-two-numbers/

### Explanation

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```text
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

Constraints:
```text
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```

## Explanation

The Add Two Numbers problem involves adding two numbers represented by linked lists, where each node contains a single digit and the digits are stored in reverse order. To solve this, we iterate through both linked lists, adding corresponding digits along with any carry from the previous addition. We create a new linked list to store the result. If one list is shorter, treat missing digits as 0. If there is a carry left after processing both lists, add a new node with the carry value.

## Hint

Use a dummy head node to simplify the code for building the result list. Remember to handle the carry at the end.

## Points

- Time complexity: O(max(m, n)), where m and n are the lengths of the two lists.
- Handle different lengths of input lists.
- Don’t forget to add a node if there is a carry left after the main loop.
- Each node contains a single digit (0-9).

### Solution

```python
def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## 19. Remove Nth Node From End of List [Medium]
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

### Explanation

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

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Two pointers: fast and slow
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next
```

## 21. Merge Two Sorted Lists [Easy]
https://leetcode.com/problems/merge-two-sorted-lists/

### Explanation

## Explanation

### Strategy (The "Why")

Given two sorted linked lists `list1` and `list2`, we need to merge them into one sorted list and return the head of the merged list.

**1.1 Constraints & Complexity:**

- **Input Size:** The total number of nodes can be up to $50$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of the two lists. We visit each node exactly once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for the dummy node and pointers.
- **Edge Case:** If one list is empty, return the other list. If both are empty, return `null`.

**1.2 High-level approach:**

The goal is to merge two sorted linked lists into one sorted list.

We use a dummy node to simplify edge cases and a current pointer to build the merged list. We compare nodes from both lists and attach the smaller one to the result, then move the pointer of the list we took from.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert both lists to arrays, merge the arrays, then convert back to a linked list. This takes $O(n + m)$ time and $O(n + m)$ space.
- **Optimized Strategy (Two Pointers):** Use two pointers to traverse both lists simultaneously, building the merged list in-place. This takes $O(n + m)$ time and $O(1)$ space.
- **Why it's better:** The two-pointer approach uses $O(1)$ extra space instead of $O(n + m)$ for arrays, while maintaining the same time complexity.

**1.4 Decomposition:**

1. Create a dummy node to simplify edge cases.
2. Initialize a current pointer at the dummy node.
3. While both lists have nodes, compare the values and attach the smaller node to the result.
4. Move the pointer of the list we took from.
5. Attach the remaining nodes from the non-empty list.
6. Return the head of the merged list (dummy.next).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $list1 = [1,2,4]$, $list2 = [1,3,4]$

We initialize:
- `dummy = ListNode(0)`
- `current = dummy`

**2.2 Start Merging:**

We begin comparing nodes from both lists.

**2.3 Trace Walkthrough:**

| Step | list1.val | list2.val | Compare | Attach | current.next | list1/list2 After |
|------|-----------|-----------|---------|--------|--------------|-------------------|
| 1 | 1 | 1 | Equal | list1 | 1 | list1 = 2 |
| 2 | 2 | 1 | 2 > 1 | list2 | 1 | list2 = 3 |
| 3 | 2 | 3 | 2 < 3 | list1 | 2 | list1 = 4 |
| 4 | 4 | 3 | 4 > 3 | list2 | 3 | list2 = 4 |
| 5 | 4 | 4 | Equal | list1 | 4 | list1 = null |
| 6 | null | 4 | - | list2 | 4 | list2 = null |

**2.4 Final Result:**

After merging: $[1,1,2,3,4,4]$

**2.5 Return Result:**

We return the head of the merged list: $[1,1,2,3,4,4]$

> **Note:** The dummy node simplifies the code by providing a starting point. Without it, we'd need special handling for the first node. The key is to always attach the smaller node and move the corresponding pointer forward.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes
        current.next = list1 if list1 else list2
        
        return dummy.next
```

## 23. Merge k Sorted Lists [Hard]
https://leetcode.com/problems/merge-k-sorted-lists/

### Explanation

## Explanation

### Strategy (The "Why")

Given an array of $k$ sorted linked lists, we need to merge all of them into one sorted linked list and return it.

**1.1 Constraints & Complexity:**

- **Input Size:** $k$ can be between $0$ and $10^4$, and the total number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-10^4$ and $10^4$.
- **Time Complexity:** $O(n \log k)$ where $n$ is the total number of nodes. We use a heap of size $k$, and each insertion/extraction takes $O(\log k)$ time. We do this for $n$ nodes.
- **Space Complexity:** $O(k)$ - We maintain a heap of size $k$.
- **Edge Case:** If the array is empty, return null. If all lists are empty, return null.

**1.2 High-level approach:**

The goal is to merge $k$ sorted linked lists into one sorted list.

We use a min heap to always get the smallest node among all lists. We add the first node from each list to the heap, then repeatedly extract the minimum, add it to the result, and add the next node from that list to the heap.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Merge lists one by one. This takes $O(kn)$ time where $n$ is the average list length.
- **Optimized Strategy (Min Heap):** Use a min heap to efficiently get the minimum node at each step. This takes $O(n \log k)$ time.
- **Why it's better:** The heap approach reduces time complexity by maintaining only $k$ nodes in the heap instead of comparing all $k$ lists at each step.

**1.4 Decomposition:**

1. Create a min heap and add the first node from each non-empty list.
2. Create a dummy node to simplify edge cases.
3. While the heap is not empty:
   - Extract the minimum node from the heap.
   - Add it to the result list.
   - If that node has a next node, add the next node to the heap.
4. Return the head of the merged list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $lists = [[1,4,5],[1,3,4],[2,6]]$

We initialize:
- `heap = [(1,0,node1), (1,1,node1), (2,2,node2)]`
- `dummy = ListNode(0)`
- `current = dummy`

**2.2 Start Merging:**

We begin extracting from the heap.

**2.3 Trace Walkthrough:**

| Step | Extract | current.next | Add to heap | heap After |
|------|---------|--------------|-------------|------------|
| 1 | (1,0) | 1 | (4,0) | [(1,1), (2,2), (4,0)] |
| 2 | (1,1) | 1 | (3,1) | [(2,2), (3,1), (4,0)] |
| 3 | (2,2) | 2 | (6,2) | [(3,1), (4,0), (6,2)] |
| 4 | (3,1) | 3 | (4,1) | [(4,0), (4,1), (6,2)] |
| ... | ... | ... | ... | ... |

**2.4 Final Result:**

After merging: $[1,1,2,3,4,4,5,6]$

**2.5 Return Result:**

We return the head of the merged list: $[1,1,2,3,4,4,5,6]$.

> **Note:** The key insight is to use a min heap to efficiently get the minimum node among all lists at each step. By maintaining only the current head of each list in the heap, we avoid storing all nodes and achieve $O(n \log k)$ time complexity.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Create a min heap
        heap = []
        
        # Add first node from each list to heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Create dummy node
        dummy = ListNode(0)
        current = dummy
        
        # Merge lists
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # Add next node from the same list if it exists
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
```

## 25. Reverse Nodes in k-Group [Hard]
https://leetcode.com/problems/reverse-nodes-in-k-group/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The linked list has $n$ nodes where $1 \leq k \leq n \leq 5000$.
* **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We visit each node exactly once.
* **Space Complexity:** $O(n/k)$ for the recursion stack, which is $O(n)$ in the worst case when $k = 1$.
* **Edge Case:** If the number of nodes is not a multiple of $k$, the remaining nodes at the end stay in their original order.

**1.2 High-level approach**

The goal is to reverse nodes in groups of $k$. We reverse each group of $k$ nodes, then recursively process the remaining list. If there are fewer than $k$ nodes remaining, we leave them unchanged.

![Linked list reversal in groups showing how k nodes are reversed at a time]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Convert the linked list to an array, reverse groups in the array, then rebuild the list. This uses $O(n)$ extra space.
* **Optimized (In-Place Reversal):** Reverse groups of $k$ nodes in-place using pointer manipulation. This uses $O(1)$ extra space (excluding recursion stack) and maintains the linked list structure.

**1.4 Decomposition**

1. Check if there are at least $k$ nodes remaining.
2. If yes, reverse the first $k$ nodes.
3. Recursively process the remaining list.
4. Connect the reversed group with the result of the recursive call.
5. If fewer than $k$ nodes remain, return the list as is.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $head = [1,2,3,4,5]$, $k = 2$.

The linked list: `1 -> 2 -> 3 -> 4 -> 5 -> None`

**2.2 Start Checking/Processing**

We first check if there are at least $k$ nodes. For the first call, we have 5 nodes, which is more than 2.

**2.3 Trace Walkthrough**

**First group (nodes 1-2):**
1. Count nodes: We have 5 nodes, so we can reverse a group of 2.
2. Reverse nodes 1-2:
   - Before: `1 -> 2 -> 3 -> 4 -> 5`
   - After: `2 -> 1 -> 3 -> 4 -> 5`
3. Recursively process remaining: `3 -> 4 -> 5`

**Second group (nodes 3-4):**
1. Count nodes: We have 3 nodes, so we can reverse a group of 2.
2. Reverse nodes 3-4:
   - Before: `3 -> 4 -> 5`
   - After: `4 -> 3 -> 5`
3. Recursively process remaining: `5`

**Remaining (node 5):**
1. Count nodes: We have 1 node, which is less than 2.
2. Return as is: `5`

**Final result:** `2 -> 1 -> 4 -> 3 -> 5`

**2.4 Increment and Loop**

The reversal process:
1. Use a helper function to reverse a segment from `start` to `end` (exclusive).
2. The helper reverses the segment by:
   - Setting `prev = None`
   - For each node, save `next`, point `curr.next` to `prev`, move `prev` and `curr` forward
3. After reversing $k$ nodes, recursively call on the remaining list.
4. Connect the reversed head with the result of recursion.

**2.5 Return Result**

After processing all groups, the list becomes `[2,1,4,3,5]`:
* Group 1: `[1,2]` → `[2,1]`
* Group 2: `[3,4]` → `[4,3]`
* Remaining: `[5]` → `[5]`

The final result is `2 -> 1 -> 4 -> 3 -> 5`.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a linked list segment
        def reverse_segment(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Count nodes to check if we have enough for a group
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            # Reverse the first k nodes
            reversed_head = reverse_segment(head, curr)
            # Recursively reverse the rest
            head.next = self.reverseKGroup(curr, k)
            return reversed_head
        
        # Not enough nodes, return as is
        return head
```

## 42. Trapping Rain Water [Hard]
https://leetcode.com/problems/trapping-rain-water/

### Explanation

## 42. Trapping Rain Water [Hard]

https://leetcode.com/problems/trapping-rain-water

## Description
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Examples**

```text
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints**
```text
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
```

## Explanation

### Strategy
Let's restate the problem: You're given an array representing the heights of walls in a landscape. When it rains, water gets trapped between these walls. Your job is to calculate how much water can be trapped.

This is a **two-pointer and dynamic programming problem** that requires understanding how water trapping works in real life.

**What is given?** An array of non-negative integers representing wall heights.

**What is being asked?** Calculate the total amount of water that can be trapped between the walls.

**Constraints:** The array can be quite large (up to 20,000 elements), so we need an efficient solution. All heights are non-negative.

**Edge cases:** 
- If the array has less than 3 elements, no water can be trapped (need at least 3 walls to form a container)
- If all heights are the same, no water can be trapped
- If heights are strictly increasing or decreasing, no water can be trapped

**High-level approach:**
The key insight is that for any position, the amount of water that can be trapped depends on the **minimum** of the highest wall to its left and the highest wall to its right. Water can only be trapped up to the height of the shorter of these two walls.

Think of it like this: at any point, water will rise to the level of the lower "dam" on either side. If you're in a valley between two mountains, the water level is limited by the shorter mountain.

**Decomposition:**
1. **Precompute left and right maximums**: For each position, find the highest wall to its left and right
2. **Calculate trapped water**: For each position, the trapped water is the minimum of left and right max, minus the current height (if positive)
3. **Sum up all trapped water**: Add up the water trapped at each position

**Brute force vs. optimized strategy:**
- **Brute force**: For each position, scan left and right to find maximums. This takes O(n²) time.
- **Optimized**: Precompute left and right maximums in two passes, then calculate water in one pass. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`

**Step 1: Understand the visualization**
Imagine this array as a landscape:
```
    ■
    ■   ■     ■
  ■ ■ ■ ■ ■ ■ ■ ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■
0 1 0 2 1 0 1 3 2 1 2 1
```

**Step 2: Precompute left maximums**
We'll create an array `left_max` where `left_max[i]` is the highest wall to the left of position `i` (including position `i` itself).

```
height:    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left_max:  [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
```

How we calculate this:
- `left_max[0] = height[0] = 0` (no walls to the left)
- `left_max[1] = max(left_max[0], height[1]) = max(0, 1) = 1`
- `left_max[2] = max(left_max[1], height[2]) = max(1, 0) = 1`
- `left_max[3] = max(left_max[2], height[3]) = max(1, 2) = 2`
- And so on...

**Step 3: Precompute right maximums**
Similarly, create `right_max` where `right_max[i]` is the highest wall to the right of position `i` (including position `i` itself).

```
height:     [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
right_max:  [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
```

How we calculate this (from right to left):
- `right_max[11] = height[11] = 1` (no walls to the right)
- `right_max[10] = max(right_max[11], height[10]) = max(1, 2) = 2`
- `right_max[9] = max(right_max[10], height[9]) = max(2, 1) = 2`
- And so on...

**Step 4: Calculate trapped water at each position**
For each position `i`, the water trapped is:
```
water[i] = min(left_max[i], right_max[i]) - height[i]
```

But only if this value is positive (we can't have negative water).

Let's calculate for a few positions:
- Position 0: `min(0, 3) - 0 = 0` (no water trapped)
- Position 1: `min(1, 3) - 1 = 0` (no water trapped)
- Position 2: `min(1, 3) - 0 = 1` (1 unit of water trapped)
- Position 3: `min(2, 3) - 2 = 0` (no water trapped)
- Position 4: `min(2, 3) - 1 = 1` (1 unit of water trapped)
- Position 5: `min(2, 3) - 0 = 2` (2 units of water trapped)

**Step 5: Sum up all trapped water**
```
water = [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]
total = 0 + 0 + 1 + 0 + 1 + 2 + 1 + 0 + 0 + 1 + 0 + 0 = 6
```

> **Note:** The key insight is that water can only be trapped up to the height of the lower "dam" on either side. This is why we take the minimum of the left and right maximums.

**Time Complexity:** O(n) - we make three passes through the array  
**Space Complexity:** O(n) - we store two additional arrays of size n

### Solution

```python
def trap(height):
    """
    Calculate the amount of water that can be trapped between walls.
    
    Args:
        height: List[int] - Array representing wall heights
        
    Returns:
        int - Total amount of water trapped
    """
    # Handle edge cases
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    
    # Step 1: Precompute left maximums
    # left_max[i] = highest wall to the left of position i (including i)
    left_max = [0] * n
    left_max[0] = height[0]
    
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Step 2: Precompute right maximums
    # right_max[i] = highest wall to the right of position i (including i)
    right_max = [0] * n
    right_max[n-1] = height[n-1]
    
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Step 3: Calculate trapped water at each position
    res = 0
    for i in range(n):
        # Water trapped = min(left_max, right_max) - current_height
        # But only if positive (can't have negative water)
        water = min(left_max[i], right_max[i]) - height[i]
        if water > 0:
            res += water
    
    return res
```

## 61. Rotate List [Medium]
https://leetcode.com/problems/rotate-list/

### Explanation

Given the `head` of a linked list, rotate the list to the right by `k` places.

**Example 1:**
```text
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

![1](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

**Example 2:**
```text
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

![2](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

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

```text
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

**Time Complexity:** O(n) - we visit each node at most twice  
**Space Complexity:** O(1) - we only use a constant amount of extra space

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
```

## 82. Remove Duplicates from Sorted List II [Medium]
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

### Explanation

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

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr and curr.next:
            # If we find duplicates
            if curr.val == curr.next.val:
                # Skip all nodes with the same value
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                # Link prev to the node after duplicates
                prev.next = curr
            else:
                # No duplicates, move both pointers
                prev = curr
                curr = curr.next
        
        return dummy.next
```

## 86. Partition List [Medium]
https://leetcode.com/problems/partition-list/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** The list has at most 200 nodes, with values in the range $[-100, 100]$. The partition value $x$ is in the range $[-200, 200]$.
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We traverse the list once.
- **Space Complexity:** $O(1)$ as we only use constant extra space (two dummy nodes and pointers).
- **Edge Case:** If the list is empty, return `None`. If all nodes are less than $x$ or all are greater than or equal to $x$, we still maintain relative order.

**1.2 High-level approach:**

The goal is to partition the list such that all nodes with values less than $x$ come before nodes with values greater than or equal to $x$, while preserving the original relative order within each partition.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Create two separate lists, collect nodes less than $x$ in one list and nodes greater than or equal to $x$ in another, then concatenate them. This requires $O(n)$ space.
- **Optimized Strategy:** Use two dummy nodes to build two partitions in-place as we traverse. This is $O(n)$ time and $O(1)$ space.
- **Why optimized is better:** The optimized approach maintains $O(1)$ space complexity while still being straightforward to implement.

**1.4 Decomposition:**

1. Create two dummy nodes: one for nodes less than $x$, one for nodes greater than or equal to $x$.
2. Traverse the original list, appending each node to the appropriate partition.
3. Connect the two partitions: link the end of the "less than" partition to the start of the "greater than or equal to" partition.
4. Set the tail of the "greater than or equal to" partition to `None` to terminate the list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `head = [1,4,3,2,5,2]`, `x = 3`

We create two dummy nodes:
- `less_head` for nodes with value < 3
- `greater_head` for nodes with value >= 3

We also create pointers `less` and `greater` that point to the current tail of each partition.

**2.2 Start Checking:**

We begin traversing the list from `head`. For each node, we check if its value is less than $x$ or greater than or equal to $x$.

**2.3 Trace Walkthrough:**

| Node Value | Comparison | Action | less partition | greater partition |
|------------|------------|--------|----------------|-------------------|
| 1 | 1 < 3 | Append to less | [1] | [] |
| 4 | 4 >= 3 | Append to greater | [1] | [4] |
| 3 | 3 >= 3 | Append to greater | [1] | [4,3] |
| 2 | 2 < 3 | Append to less | [1,2] | [4,3] |
| 5 | 5 >= 3 | Append to greater | [1,2] | [4,3,5] |
| 2 | 2 < 3 | Append to less | [1,2,2] | [4,3,5] |

**2.4 Increment and Loop:**

After processing all nodes:
- `less` partition: `1 -> 2 -> 2`
- `greater` partition: `4 -> 3 -> 5`

We connect them: `less.next = greater_head.next`, which gives: `1 -> 2 -> 2 -> 4 -> 3 -> 5`

**2.5 Return Result:**

We set `greater.next = None` to terminate the list, then return `less_head.next`, which points to `1`. The final result is `[1,2,2,4,3,5]`.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes for less than x and greater than or equal to x
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less = less_head
        greater = greater_head
        
        curr = head
        
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        
        # Connect the two partitions
        less.next = greater_head.next
        greater.next = None  # Important: break the chain
        
        return less_head.next
```

## 89. Gray Code [Medium]
https://leetcode.com/problems/gray-code/

### Explanation

## 89. Gray Code [Medium]

https://leetcode.com/problems/gray-code

## Description
An **n-bit gray code sequence** is a sequence of `2ⁿ` integers where:

- Every integer is in the **inclusive** range `[0, 2ⁿ - 1]`,
- The first integer is `0`,
- An integer appears **no more than once** in the sequence,
- The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and
- The binary representation of the **first** and **last** integers differs by **exactly one bit**.

Given an integer `n`, return *any valid **n-bit gray code sequence***.

**Examples**

```tex
Example 1:
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit

Example 2:
Input: n = 1
Output: [0,1]
```

**Constraints**
```tex
- 1 <= n <= 16
```

## Explanation

### Strategy
Let's restate the problem: You need to generate a sequence of `2ⁿ` numbers from 0 to `2ⁿ - 1` where each adjacent pair differs by exactly one bit, and the first and last numbers also differ by exactly one bit.

This is a **bit manipulation problem** that involves understanding binary representations and finding patterns in how numbers can be arranged to satisfy the Gray code properties.

**What is given?** An integer `n` representing the number of bits.

**What is being asked?** Generate any valid n-bit Gray code sequence.

**Constraints:** `n` is between 1 and 16, so the sequences can be quite long.

**Edge cases:** 
- `n = 1`: Simple case with only two numbers
- `n = 2`: Small enough to visualize easily
- Large `n`: Requires efficient algorithm

**High-level approach:**
The solution involves understanding the mathematical properties of Gray codes and using a recursive or iterative approach to generate them.

**Decomposition:**
1. **Understand Gray code properties**: Each adjacent pair differs by exactly one bit
2. **Use reflection method**: Build larger Gray codes from smaller ones
3. **Generate sequence**: Create the complete sequence efficiently
4. **Return result**: Return the valid Gray code sequence

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible permutations and check Gray code properties. This is extremely inefficient.
- **Optimized**: Use the reflection method or mathematical properties to generate Gray codes directly.

### Steps
Let's walk through the solution step by step using the example `n = 2`:

**Step 1: Start with base case**
- For `n = 1`, the Gray code is `[0, 1]`
- Binary: `[0, 1]` or `[00, 01]`

**Step 2: Use reflection method**
- Take the existing sequence: `[0, 1]`
- Reflect it: `[1, 0]`
- Add prefix `0` to first half: `[00, 01]`
- Add prefix `1` to reflected half: `[11, 10]`
- Combine: `[00, 01, 11, 10]`

**Step 3: Convert to decimal**
- `00` = 0
- `01` = 1
- `11` = 3
- `10` = 2
- Result: `[0, 1, 3, 2]`

**Step 4: Verify properties**
- Adjacent pairs differ by exactly one bit:
  - `00` and `01`: differ in last bit
  - `01` and `11`: differ in first bit
  - `11` and `10`: differ in last bit
  - `10` and `00`: differ in first bit
- First and last differ by exactly one bit: `00` and `10` differ in first bit

**Why this works:**
The reflection method works because:
1. **Prefix property**: Adding `0` or `1` as a prefix preserves the one-bit difference property
2. **Reflection symmetry**: Reflecting the sequence and adding `1` as prefix creates the necessary transitions
3. **Mathematical induction**: If it works for `n-1`, it works for `n`

> **Note:** The key insight is that Gray codes can be built recursively by reflecting smaller Gray codes and adding appropriate prefixes. This is much more efficient than trying to find valid sequences through brute force.

**Time Complexity:** O(2ⁿ) - we generate exactly 2ⁿ numbers  
**Space Complexity:** O(2ⁿ) - we need to store the entire sequence

### Solution

```python
def grayCode(n):
    """
    Generate an n-bit Gray code sequence.
    
    Args:
        n: int - Number of bits for the Gray code sequence
        
    Returns:
        List[int] - Valid n-bit Gray code sequence
    """
    # Handle edge case
    if n == 0:
        return [0]
    
    # Start with base case: 1-bit Gray code
    result = [0, 1]
    
    # Build larger Gray codes using reflection method
    for i in range(2, n + 1):
        # Get the size of the current sequence
        size = len(result)
        
        # Reflect the current sequence and add prefix '1'
        for j in range(size - 1, -1, -1):
            # Add 2^(i-1) to create the reflected part with prefix '1'
            result.append(result[j] + (1 << (i - 1)))
    
    return result
```

## 92. Reverse Linked List II [Medium]
https://leetcode.com/problems/reverse-linked-list-ii/

### Explanation

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

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create dummy node to handle edge case when left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move to the node before the reversal starts
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the segment
        curr = prev.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
```

## 94. Binary Tree Inorder Traversal [Easy]
https://leetcode.com/problems/binary-tree-inorder-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to return the inorder traversal of its nodes' values.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $100$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Edge Case:** If the tree is empty, return an empty list. If the tree has only one node, return that node's value.

**1.2 High-level approach:**

The goal is to traverse the tree in inorder (left, root, right) order.

We use recursion to implement inorder traversal. We recursively traverse the left subtree, visit the root, then recursively traverse the right subtree.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree.
- **Optimized Strategy (Recursion):** Use recursion to naturally implement inorder traversal. This is the standard and efficient approach.
- **Why it's better:** Recursion naturally follows the tree structure and implements inorder traversal efficiently. An iterative approach using a stack is also possible but more complex.

**1.4 Decomposition:**

1. Define a recursive function that takes a node.
2. Base case: if node is null, return.
3. Recursively traverse left subtree.
4. Visit current node (add value to result).
5. Recursively traverse right subtree.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,null,2,3]$

The tree structure:
```
    1
     \
      2
     /
    3
```

We initialize:
- `res = []`

**2.2 Start Traversal:**

We begin from the root.

**2.3 Trace Walkthrough:**

| Node | Action | res After |
|------|--------|-----------|
| 1 | Go left (null) | [] |
| 1 | Visit 1 | [1] |
| 1 | Go right (2) | [1] |
| 2 | Go left (3) | [1] |
| 3 | Go left (null) | [1] |
| 3 | Visit 3 | [1,3] |
| 3 | Go right (null) | [1,3] |
| 2 | Visit 2 | [1,3,2] |
| 2 | Go right (null) | [1,3,2] |

**2.4 Final Result:**

After traversal: `res = [1,3,2]`

**2.5 Return Result:**

We return `[1,3,2]`, which is the inorder traversal.

> **Note:** The key is to follow the inorder order: left subtree first, then root, then right subtree. Recursion naturally implements this by processing the left subtree before the root, and the root before the right subtree.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def inorderTraversal(self, root) -> List[int]:
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res
```

## 98. Validate Binary Search Tree [Medium]
https://leetcode.com/problems/validate-binary-search-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to determine if it is a valid binary search tree (BST). A BST is valid if for every node, all nodes in its left subtree are less than it, and all nodes in its right subtree are greater than it.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Edge Case:** An empty tree is a valid BST. A tree with only one node is a valid BST.

**1.2 High-level approach:**

The goal is to validate that a binary tree satisfies the BST property.

We use recursion with range validation. For each node, we check if its value is within the valid range (min_val, max_val). The range is updated as we traverse: left children must be less than the parent, right children must be greater than the parent.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each node, check if all nodes in its left subtree are less and all nodes in its right subtree are greater. This would be $O(n^2)$ time.
- **Optimized Strategy (Range Validation):** Use recursion with min and max bounds. Each node must be within its allowed range. This takes $O(n)$ time.
- **Why it's better:** The range validation approach reduces time complexity from $O(n^2)$ to $O(n)$ by passing down constraints instead of checking all descendants for each node.

**1.4 Decomposition:**

1. Define a recursive function that takes a node and its allowed range (min_val, max_val).
2. If the node is null, return true (base case).
3. Check if the node's value is within the range (strictly greater than min_val and strictly less than max_val).
4. Recursively validate left subtree with range (min_val, node.val).
5. Recursively validate right subtree with range (node.val, max_val).
6. Return true only if all checks pass.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[5,1,4,null,null,3,6]$

The tree structure:
```
    5
   / \
  1   4
     / \
    3   6
```

We initialize:
- Call `validate(root, -∞, +∞)`

**2.2 Start Validation:**

We begin validating from the root.

**2.3 Trace Walkthrough:**

| Node | min_val | max_val | node.val | Check | Result |
|------|---------|---------|----------|-------|--------|
| 5 | -∞ | +∞ | 5 | $-∞ < 5 < +∞$ | ✓ |
| 1 | -∞ | 5 | 1 | $-∞ < 1 < 5$ | ✓ |
| 4 | 5 | +∞ | 4 | $5 < 4 < +∞$ | ✗ |

**2.4 Explanation:**

- Root (5): Valid, within range (-∞, +∞)
- Left child (1): Valid, within range (-∞, 5)
- Right child (4): Invalid! It should be greater than 5, but 4 < 5

**2.5 Return Result:**

We return `False` because node 4 violates the BST property (it's in the right subtree of 5 but is less than 5).

> **Note:** The key insight is to pass down the allowed range for each node. A node's value must be strictly within its range, and we update the range for children: left children get (min_val, node.val) and right children get (node.val, max_val).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, min_val, max_val):
            # Empty tree is valid
            if not node:
                return True
            
            # Check if current node value is within valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
```

## 100. Same Tree [Easy]
https://leetcode.com/problems/same-tree/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to determine if two binary trees are structurally identical and have the same node values.

**1.1 Constraints & Complexity:**

- **Input Constraints:** Both trees have at most 100 nodes, and node values are in the range $[-10^4, 10^4]$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once, where $n$ is the minimum number of nodes in the two trees.
- **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In the worst case (skewed tree), $h = n$, giving $O(n)$ space.
- **Edge Case:** Both trees are empty (both roots are `None`), which should return `True`.

**1.2 High-level approach:**

The goal is to check if two trees have the same structure and values by comparing them node by node recursively. We compare the root values, then recursively check left and right subtrees.

![Binary tree comparison](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert both trees to arrays using traversal, then compare arrays. This requires $O(n)$ time and $O(n)$ space for storing both arrays.
- **Optimized (Recursive Comparison):** Compare nodes directly during traversal without storing intermediate results. This uses $O(n)$ time but only $O(h)$ space for the recursion stack.
- **Emphasize the optimization:** By comparing nodes directly during traversal, we can short-circuit early if we find a mismatch, potentially avoiding full tree traversal.

**1.4 Decomposition:**

1. **Base Cases:** If both nodes are `None`, return `True`. If only one is `None`, return `False`.
2. **Value Comparison:** Check if the current nodes have the same value.
3. **Recursive Check:** Recursively check if left subtrees match and right subtrees match.
4. **Combine Results:** Return `True` only if values match and both subtrees match.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `p = [1,2,3]`, `q = [1,2,3]`.

Both trees have the same structure and values.

**2.2 Start Comparison:**

We begin at the root nodes of both trees.

**2.3 Trace Walkthrough:**

| Node Pair | p.val | q.val | Match? | Left Check | Right Check | Result |
|-----------|-------|-------|--------|------------|-------------|--------|
| Root (1, 1) | 1 | 1 | Yes | Check (2, 2) | Check (3, 3) | Continue |
| Left (2, 2) | 2 | 2 | Yes | Check (None, None) | Check (None, None) | True |
| Right (3, 3) | 3 | 3 | Yes | Check (None, None) | Check (None, None) | True |

**2.4 Recursive Unwinding:**

- Both left subtrees (2, 2) match: both have value 2 and no children.
- Both right subtrees (3, 3) match: both have value 3 and no children.
- Root nodes (1, 1) match.

**2.5 Return Result:**

Since all nodes match in structure and value, the function returns `True`.

> **Note:** The algorithm short-circuits: if any node comparison fails, the entire function returns `False` immediately without checking remaining nodes.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are None
        if not p and not q:
            return True
        
        # One is None, the other is not
        if not p or not q:
            return False
        
        # Both exist, check values and recursively check children
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## 101. Symmetric Tree [Easy]
https://leetcode.com/problems/symmetric-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to check whether it is a mirror of itself (symmetric around its center).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $1000$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$.
- **Edge Case:** An empty tree is symmetric. A tree with only one node is symmetric.

**1.2 High-level approach:**

The goal is to determine if a binary tree is symmetric (mirror of itself).

We use recursion to check if the left and right subtrees are mirrors of each other. Two trees are mirrors if their roots have the same value, and the left subtree of one is a mirror of the right subtree of the other, and vice versa.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must check the mirror property.
- **Optimized Strategy (Recursion):** Use recursion to check if left and right subtrees are mirrors. This is the standard and efficient approach.
- **Why it's better:** Recursion naturally checks the mirror property by comparing corresponding nodes in the left and right subtrees.

**1.4 Decomposition:**

1. Define a helper function that checks if two trees are mirrors.
2. Two trees are mirrors if:
   - Both are null (base case: true).
   - One is null and the other is not (false).
   - Both roots have the same value, and:
     - Left subtree of first is mirror of right subtree of second.
     - Right subtree of first is mirror of left subtree of second.
3. Check if root's left and right subtrees are mirrors.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,2,2,3,4,4,3]$

The tree structure:
```
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

We initialize:
- Call `is_mirror(root.left, root.right)`

**2.2 Start Checking:**

We begin checking if left and right subtrees are mirrors.

**2.3 Trace Walkthrough:**

| left | right | left.val | right.val | Check | Result |
|------|-------|----------|-----------|-------|--------|
| 2 | 2 | 2 | 2 | Equal ✓ | Check children |
| 3 | 3 | 3 | 3 | Equal ✓ | Both null ✓ |
| 4 | 4 | 4 | 4 | Equal ✓ | Both null ✓ |
| 4 | 4 | 4 | 4 | Equal ✓ | Both null ✓ |
| 3 | 3 | 3 | 3 | Equal ✓ | Both null ✓ |

**2.4 Explanation:**

- Root's left (2) and right (2) have same value ✓
- Left's left (3) and right's right (3) are mirrors ✓
- Left's right (4) and right's left (4) are mirrors ✓

**2.5 Return Result:**

We return `True` because the tree is symmetric.

> **Note:** The key insight is that a tree is symmetric if its left and right subtrees are mirrors. Two trees are mirrors if their roots match and the left of one mirrors the right of the other (and vice versa).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and 
                    is_mirror(left.left, right.right) and 
                    is_mirror(left.right, right.left))
        
        if not root:
            return True
        
        return is_mirror(root.left, root.right)
```

## 102. Binary Tree Level Order Traversal [Medium]
https://leetcode.com/problems/binary-tree-level-order-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to return the level-order traversal of its nodes' values (i.e., from left to right, level by level).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be up to $2000$.
- **Value Range:** Node values are between $-1000$ and $1000$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level, which is $O(n)$ in the worst case.
- **Edge Case:** If the tree is empty, return an empty list.

**1.2 High-level approach:**

The goal is to traverse the tree level by level, collecting values at each level.

![Level Order Traversal](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

We use BFS (breadth-first search) with a queue. We process nodes level by level, adding all nodes at the current level to a list before moving to the next level.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree.
- **Optimized Strategy (BFS with Queue):** Use a queue to process nodes level by level. For each level, process all nodes in the queue (which represents the current level), then add their children for the next level.
- **Why it's better:** BFS naturally processes nodes level by level. Using a queue ensures we process all nodes at one level before moving to the next.

**1.4 Decomposition:**

1. If the tree is empty, return an empty list.
2. Initialize a queue with the root node.
3. While the queue is not empty:
   - Get the number of nodes at the current level (queue size).
   - Process all nodes at this level, adding their values to a level list.
   - Add all children of these nodes to the queue for the next level.
   - Add the level list to the result.
4. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[3,9,20,null,null,15,7]$

The tree structure:
```
    3
   / \
  9   20
     /  \
    15   7
```

We initialize:
- `queue = deque([3])`
- `res = []`

**2.2 Start BFS:**

We begin processing level by level.

**2.3 Trace Walkthrough:**

| Level | Queue Before | Level Size | Process Nodes | Level List | Queue After |
|-------|--------------|------------|---------------|------------|-------------|
| 0 | [3] | 1 | 3 | [3] | [9, 20] |
| 1 | [9, 20] | 2 | 9, 20 | [9, 20] | [15, 7] |
| 2 | [15, 7] | 2 | 15, 7 | [15, 7] | [] |

**2.4 Final Result:**

After processing all levels:
- `res = [[3], [9, 20], [15, 7]]`

**2.5 Return Result:**

We return `[[3], [9, 20], [15, 7]]`, which represents the level-order traversal.

> **Note:** The key is to process all nodes at the current level before moving to the next. We do this by getting the queue size at the start of each iteration, which represents the number of nodes at the current level.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res
```

## 103. Binary Tree Zigzag Level Order Traversal [Medium]
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to return the zigzag level order traversal of a binary tree: left-to-right for even levels, right-to-left for odd levels.

**1.1 Constraints & Complexity:**

- **Input Constraints:** The tree has $0 \leq n \leq 2000$ nodes with values in $[-100, 100]$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level.
- **Edge Case:** Empty tree returns empty list.

**1.2 High-level approach:**

The goal is to traverse the tree level by level, alternating the direction at each level. We use BFS with a flag to track direction.

![Zigzag Traversal](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Do regular level-order traversal, then reverse every other level. This takes $O(n)$ time and $O(n)$ space.
- **Optimized (BFS with Direction Flag):** Use BFS and reverse the level list when needed based on a flag. This takes $O(n)$ time and $O(n)$ space.
- **Emphasize the optimization:** While complexity is the same, the direction flag approach is cleaner and more efficient than reversing after collection.

**1.4 Decomposition:**

1. **BFS Traversal:** Use a queue to process nodes level by level.
2. **Track Direction:** Use a boolean flag to alternate between left-to-right and right-to-left.
3. **Reverse When Needed:** For odd levels (right-to-left), reverse the level list before adding to result.
4. **Return Result:** Return the list of levels.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [3,9,20,null,null,15,7]`.

Initialize: `queue = [3]`, `left_to_right = True`, `res = []`

**2.2 Start Processing:**

Process level 0 (root).

**2.3 Trace Walkthrough:**

| Level | Queue Before | Level Values | Direction | After Reverse | Result |
|-------|--------------|--------------|-----------|---------------|--------|
| 0 | [3] | [3] | L→R | [3] | [[3]] |
| 1 | [9, 20] | [9, 20] | R→L | [20, 9] | [[3], [20, 9]] |
| 2 | [15, 7] | [15, 7] | L→R | [15, 7] | [[3], [20, 9], [15, 7]] |

**2.4 Complete Traversal:**

All levels processed: Level 0 (L→R), Level 1 (R→L), Level 2 (L→R).

**2.5 Return Result:**

The function returns `[[3], [20, 9], [15, 7]]`.

> **Note:** The direction alternates at each level: even levels (0, 2, ...) are left-to-right, odd levels (1, 3, ...) are right-to-left.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = [root]
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse if needed for zigzag
            if not left_to_right:
                level.reverse()
            
            res.append(level)
            left_to_right = not left_to_right
        
        return res
```

## 104. Maximum Depth of Binary Tree [Easy]
https://leetcode.com/problems/maximum-depth-of-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the tree can be between $0$ and $10^4$.
- **Value Range:** Node values are between $-100$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Edge Case:** If the tree is empty (root is null), return 0.

**1.2 High-level approach:**

The goal is to find the maximum depth of a binary tree.

![Maximum Depth](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

We use recursion: the maximum depth of a tree is 1 plus the maximum of the depths of its left and right subtrees.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree to find the depth.
- **Optimized Strategy (Recursion):** Recursively compute the depth of left and right subtrees, then return 1 plus the maximum. This is the natural and efficient approach.
- **Why it's better:** Recursion naturally follows the tree structure. Each node's depth depends only on its children's depths, creating optimal substructure.

**1.4 Decomposition:**

1. Base case: if the root is null, return 0.
2. Recursively find the maximum depth of the left subtree.
3. Recursively find the maximum depth of the right subtree.
4. Return 1 (for current node) plus the maximum of the two subtree depths.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[3,9,20,null,null,15,7]$

The tree structure:
```
    3
   / \
  9   20
     /  \
    15   7
```

**2.2 Start Recursion:**

We begin from the root node (value 3).

**2.3 Trace Walkthrough:**

| Node | Left Depth | Right Depth | Max Depth | Return Value |
|------|------------|--------------|-----------|--------------|
| 3 | ? | ? | - | Compute... |
| 9 | 0 (null) | 0 (null) | 0 | $0 + 1 = 1$ |
| 20 | ? | ? | - | Compute... |
| 15 | 0 (null) | 0 (null) | 0 | $0 + 1 = 1$ |
| 7 | 0 (null) | 0 (null) | 0 | $0 + 1 = 1$ |
| 20 | 1 | 1 | 1 | $1 + 1 = 2$ |
| 3 | 1 | 2 | 2 | $2 + 1 = 3$ |

**2.4 Recursion Flow:**

- Root (3): left depth = 1, right depth = 2, return $max(1, 2) + 1 = 3$
- Node 9: both children null, return $0 + 1 = 1$
- Node 20: left depth = 1, right depth = 1, return $max(1, 1) + 1 = 2$

**2.5 Return Result:**

We return 3, which is the maximum depth of the tree.

> **Note:** The recursive approach naturally handles the tree structure. The depth of each node is computed from its children's depths, working from the leaves upward to the root.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        # Recursively find max depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return max depth plus 1 for current node
        return max(left_depth, right_depth) + 1
```

## 105. Construct Binary Tree from Preorder and Inorder Traversal [Medium]
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to construct a binary tree from its preorder and inorder traversal arrays.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 3000$, values in $[-3000, 3000]$, all values are unique.
- **Time Complexity:** $O(n)$ - We visit each node once. The hash map lookup is $O(1)$.
- **Space Complexity:** $O(n)$ - Hash map for inorder indices takes $O(n)$, recursion stack takes $O(h)$ where $h$ is tree height.
- **Edge Case:** Empty arrays return `None`.

**1.2 High-level approach:**

The goal is to reconstruct the tree using the property that in preorder, the root comes first, and in inorder, the root separates left and right subtrees.

![Tree Construction](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each root, search for it in inorder array linearly. This takes $O(n^2)$ time.
- **Optimized (Hash Map):** Use a hash map to store inorder indices for $O(1)$ lookup. This takes $O(n)$ time.
- **Emphasize the optimization:** The hash map reduces the time complexity from $O(n^2)$ to $O(n)$ by eliminating linear searches.

**1.4 Decomposition:**

1. **Build Hash Map:** Create a map from values to their inorder indices.
2. **Recursive Build:** Use preorder to get root, use inorder to split left/right subtrees.
3. **Calculate Ranges:** Determine preorder and inorder ranges for left and right subtrees.
4. **Return Root:** Build and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`.

Hash map: `{9:0, 3:1, 15:2, 20:3, 7:4}`

**2.2 Start Building:**

Root is `preorder[0] = 3`. Find its position in inorder: `inorder[1] = 3`.

**2.3 Trace Walkthrough:**

| Root | Preorder Range | Inorder Range | Left Size | Left Subtree | Right Subtree |
|------|----------------|---------------|-----------|--------------|---------------|
| 3 | [0:4] | [0:4] | 1 | pre[1:2], in[0:0] | pre[2:5], in[2:4] |
| 9 | [1:2] | [0:0] | 0 | None | None |
| 20 | [2:5] | [2:4] | 1 | pre[3:4], in[2:2] | pre[4:5], in[3:4] |
| 15 | [3:4] | [2:2] | 0 | None | None |
| 7 | [4:5] | [3:4] | 0 | None | None |

**2.4 Complete Construction:**

Tree structure: `3` (root) with left child `9` and right child `20`. `20` has left child `15` and right child `7`.

**2.5 Return Result:**

The function returns the root node of the constructed tree.

> **Note:** The key insight is that preorder gives us the root, and inorder tells us how many nodes are in the left subtree, allowing us to split the preorder array correctly.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Create a map for O(1) lookup of inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            # Root is the first element in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find root position in inorder
            root_idx = inorder_map[root_val]
            
            # Calculate sizes of left and right subtrees
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

## 106. Construct Binary Tree from Inorder and Postorder Traversal [Medium]
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to construct a binary tree from its inorder and postorder traversal arrays.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 3000$, values in $[-3000, 3000]$, all values are unique.
- **Time Complexity:** $O(n)$ - We visit each node once. The hash map lookup is $O(1)$.
- **Space Complexity:** $O(n)$ - Hash map for inorder indices takes $O(n)$, recursion stack takes $O(h)$.
- **Edge Case:** Empty arrays return `None`.

**1.2 High-level approach:**

The goal is to reconstruct the tree using the property that in postorder, the root comes last, and in inorder, the root separates left and right subtrees.

![Tree Construction](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each root, search for it in inorder array linearly. This takes $O(n^2)$ time.
- **Optimized (Hash Map):** Use a hash map to store inorder indices for $O(1)$ lookup. This takes $O(n)$ time.
- **Emphasize the optimization:** The hash map reduces the time complexity from $O(n^2)$ to $O(n)$ by eliminating linear searches.

**1.4 Decomposition:**

1. **Build Hash Map:** Create a map from values to their inorder indices.
2. **Recursive Build:** Use postorder to get root (last element), use inorder to split left/right subtrees.
3. **Calculate Ranges:** Determine inorder and postorder ranges for left and right subtrees.
4. **Return Root:** Build and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `inorder = [9,3,15,20,7]`, `postorder = [9,15,7,20,3]`.

Hash map: `{9:0, 3:1, 15:2, 20:3, 7:4}`

**2.2 Start Building:**

Root is `postorder[4] = 3`. Find its position in inorder: `inorder[1] = 3`.

**2.3 Trace Walkthrough:**

| Root | Inorder Range | Postorder Range | Left Size | Left Subtree | Right Subtree |
|------|---------------|-----------------|-----------|--------------|---------------|
| 3 | [0:4] | [0:4] | 1 | in[0:0], post[0:0] | in[2:4], post[1:3] |
| 9 | [0:0] | [0:0] | 0 | None | None |
| 20 | [2:4] | [1:3] | 1 | in[2:2], post[1:1] | in[3:4], post[2:2] |
| 15 | [2:2] | [1:1] | 0 | None | None |
| 7 | [3:4] | [2:2] | 0 | None | None |

**2.4 Complete Construction:**

Tree structure: `3` (root) with left child `9` and right child `20`. `20` has left child `15` and right child `7`.

**2.5 Return Result:**

The function returns the root node of the constructed tree.

> **Note:** Similar to problem 105, but here the root is the last element in postorder instead of the first in preorder.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # Create a map for O(1) lookup of inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None
            
            # Root is the last element in postorder
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # Find root position in inorder
            root_idx = inorder_map[root_val]
            
            # Calculate sizes of left and right subtrees
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(in_start, root_idx - 1, post_start, post_start + left_size - 1)
            root.right = build(root_idx + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
```

## 108. Convert Sorted Array to Binary Search Tree [Easy]
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The array $nums$ has length $1 \leq n \leq 10^4$, with values in $[-10^4, 10^4]$.
* **Time Complexity:** $O(n)$ - We visit each element exactly once to build the tree.
* **Space Complexity:** $O(n)$ - The recursion stack depth is $O(\log n)$ for a balanced tree, and the tree itself uses $O(n)$ space.
* **Edge Case:** An empty array returns `None`. A single-element array creates a tree with one node.

**1.2 High-level approach**

The goal is to convert a sorted array into a height-balanced binary search tree. We use the middle element as the root to ensure balance, then recursively build left and right subtrees.

![BST construction from sorted array showing how middle element becomes root]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible tree structures and check if they're balanced. This is exponential in complexity.
* **Optimized (Divide and Conquer):** Always choose the middle element as root, ensuring the tree is balanced. This achieves $O(n)$ time and creates an optimal height-balanced tree.

**1.4 Decomposition**

1. **Choose Root:** Select the middle element of the current range as the root.
2. **Build Left Subtree:** Recursively build BST from elements before the middle.
3. **Build Right Subtree:** Recursively build BST from elements after the middle.
4. **Return Root:** Connect subtrees and return the root node.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $nums = [-10,-3,0,5,9]$.

We initialize:
* `left = 0`, `right = 4`
* Middle index: $mid = (0 + 4) // 2 = 2$

**2.2 Start Building**

Root is `nums[2] = 0`.

**2.3 Trace Walkthrough**

| Level | left | right | mid | nums[mid] | Left Range | Right Range | Action |
|-------|------|-------|-----|-----------|------------|-------------|--------|
| 0 | 0 | 4 | 2 | 0 | [0,1] | [3,4] | Create root(0) |
| 1 (left) | 0 | 1 | 0 | -10 | [0,-1] | [1,1] | Create left(-10) |
| 1 (right) | 3 | 4 | 3 | 5 | [3,2] | [4,4] | Create right(5) |
| 2 (left) | 1 | 1 | 1 | -3 | [1,0] | [1,1] | Create right(-3) |
| 2 (right) | 4 | 4 | 4 | 9 | [4,3] | [4,4] | Create right(9) |

**2.4 Recursive Building**

For each recursive call:
1. If `left > right`, return `None` (base case)
2. Calculate `mid = (left + right) // 2`
3. Create root with `nums[mid]`
4. Recursively build left subtree: `build(left, mid - 1)`
5. Recursively build right subtree: `build(mid + 1, right)`

**2.5 Return Result**

The function returns the root of the balanced BST: `[0,-10,5,null,-3,null,9]`.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None
            
            # Choose middle element as root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)
```

## 112. Path Sum [Easy]
https://leetcode.com/problems/path-sum/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $0 \leq n \leq 5000$ nodes, with values in $[-1000, 1000]$.
* **Time Complexity:** $O(n)$ - We visit each node at most once in the worst case.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
* **Edge Case:** An empty tree returns `False`. A single-node tree returns `True` if the node value equals `targetSum`.

**1.2 High-level approach**

The goal is to check if there exists a root-to-leaf path where the sum of node values equals `targetSum`. We traverse the tree recursively, subtracting each node's value from the remaining sum, and check if we reach a leaf with the correct sum.

![Path sum visualization showing root-to-leaf paths and their sums]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Find all root-to-leaf paths, calculate their sums, then check if any equals `targetSum`. This requires storing all paths, using $O(n \times h)$ space.
* **Optimized (Recursive DFS):** Traverse the tree and check the sum incrementally. If we find a valid path, return immediately. This uses $O(h)$ space for recursion stack.

**1.4 Decomposition**

1. **Base Case:** If node is `None`, return `False`.
2. **Leaf Check:** If node is a leaf, check if its value equals the remaining sum.
3. **Recursive Check:** Recursively check left and right subtrees with updated remaining sum.
4. **Return Result:** Return `True` if either subtree has a valid path.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [5,4,8,11,null,13,4,7,2,null,null,null,1]$, $targetSum = 22$.

We start at the root node with value 5.

**2.2 Start Checking**

We call `hasPathSum(root, 22)`.

**2.3 Trace Walkthrough**

| Node | targetSum (before) | Is Leaf? | targetSum (after) | Left Result | Right Result | Final Result |
|------|-------------------|----------|-------------------|-------------|--------------|--------------|
| 5 | 22 | No | 17 | Check(4, 17) | Check(8, 17) | OR result |
| 4 | 17 | No | 13 | Check(11, 13) | None | OR result |
| 11 | 13 | No | 2 | Check(7, 2) | Check(2, 2) | OR result |
| 7 | 2 | Yes | -5 | - | - | False |
| 2 | 2 | Yes | 0 | - | - | **True** |

Since node 2 is a leaf and `2 == 2`, we return `True` for the path $5 \to 4 \to 11 \to 2$.

**2.4 Recursive Processing**

For each node:
1. If `not root`, return `False`
2. If leaf (`not root.left and not root.right`), return `root.val == targetSum`
3. Otherwise, recursively check: `hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)`

**2.5 Return Result**

The function returns `True` because there exists a path $5 \to 4 \to 11 \to 2$ with sum $5 + 4 + 11 + 2 = 22$.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # If leaf node, check if value equals remaining sum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check left and right subtrees
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
```

## 114. Flatten Binary Tree to Linked List [Medium]
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $0 \leq n \leq 2000$ nodes, with values in $[-100, 100]$.
* **Time Complexity:** $O(n)$ - We visit each node exactly once during the flattening process.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
* **Edge Case:** An empty tree requires no modification. A single-node tree remains unchanged.

**1.2 High-level approach**

The goal is to flatten a binary tree into a linked list in pre-order traversal order. We recursively flatten subtrees, then rearrange pointers to form a linear structure.

![Tree flattening visualization showing how tree nodes are rearranged into a linked list]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Store pre-order traversal in a list, then rebuild the tree as a linked list. This uses $O(n)$ extra space.
* **Optimized (In-Place):** Flatten subtrees recursively, then rearrange pointers in-place. This uses $O(h)$ space for recursion stack.

**1.4 Decomposition**

1. **Flatten Subtrees:** Recursively flatten left and right subtrees.
2. **Save Right:** Store the right subtree before modifying pointers.
3. **Move Left to Right:** Set `root.right = root.left` and `root.left = None`.
4. **Attach Saved Right:** Find the end of the flattened left subtree and attach the saved right subtree.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [1,2,5,3,4,null,6]$.

We start at the root node with value 1.

**2.2 Start Processing**

We call `flatten(root)`.

**2.3 Trace Walkthrough**

The flattening process happens bottom-up:

**Step 1: Flatten leaf nodes**
- Node 3: Already flat (no children)
- Node 4: Already flat (no children)
- Node 6: Already flat (no children)

**Step 2: Flatten node 2**
- Left subtree [3,4] is already flat
- Right subtree is None
- Move left to right: `2.right = 2.left = [3,4]`, `2.left = None`

**Step 3: Flatten node 5**
- Left subtree is None
- Right subtree [6] is already flat
- No change needed

**Step 4: Flatten root 1**
- Left subtree [2,3,4] is flattened
- Right subtree [5,6] is flattened
- Save right: `right = [5,6]`
- Move left to right: `1.right = [2,3,4]`, `1.left = None`
- Find end of [2,3,4] (node 4) and attach: `4.right = [5,6]`

**2.4 Recursive Processing**

For each node:
1. If `not root`, return (base case)
2. Recursively flatten `root.left`
3. Recursively flatten `root.right`
4. Save `right = root.right`
5. Set `root.right = root.left` and `root.left = None`
6. Traverse to end of new right subtree and set `curr.right = right`

**2.5 Return Result**

After flattening, the tree becomes a linked list: `[1,null,2,null,3,null,4,null,5,null,6]`, which matches the pre-order traversal.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Save right subtree
        right = root.right
        
        # Move left subtree to right
        root.right = root.left
        root.left = None
        
        # Find the end of the new right subtree and attach saved right
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right
```

## 116. Populating Next Right Pointers in Each Node [Medium]
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

### Explanation

## Explanation

### Strategy (The "Why")

Given a perfect binary tree, we need to populate each node's `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be up to $2^{12} - 1$ (perfect binary tree).
- **Value Range:** Node values are between $-1000$ and $1000$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space, not counting the recursion stack. The `next` pointers are part of the output.
- **Edge Case:** If the tree is empty, return null. For a perfect binary tree, all levels are completely filled.

**1.2 High-level approach:**

The goal is to connect nodes at the same level using the `next` pointer.

![Next Right Pointers](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

We use level-order traversal, but instead of using a queue, we leverage the `next` pointers we've already set. We process level by level, connecting children as we go.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use BFS with a queue to process each level, then connect nodes at the same level. This takes $O(n)$ time and $O(n)$ space for the queue.
- **Optimized Strategy (Level-by-level):** Process level by level using the `next` pointers. For each node, connect its left child to right child, and right child to next node's left child. This takes $O(n)$ time and $O(1)$ extra space.
- **Why it's better:** The optimized approach uses $O(1)$ extra space instead of $O(n)$ for a queue, by leveraging the tree structure and `next` pointers we're building.

**1.4 Decomposition:**

1. Start from the root level (which has no `next` pointers to set).
2. For each level, iterate through nodes using the `next` pointers.
3. For each node, connect its left child to its right child.
4. If the node has a `next` pointer, connect its right child to the `next` node's left child.
5. Move to the next level by following the leftmost node's left child.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,2,3,4,5,6,7]$

The tree structure:
```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

**2.2 Start Connecting:**

We begin at the root level.

**2.3 Trace Walkthrough:**

**Level 1 (root):**
- Node 1: No connections needed at root level

**Level 2:**
- Node 2: Connect 2.left (4) → 2.right (5)
- Node 2: Connect 2.right (5) → 2.next.left (6) [since 2.next = 3]
- Node 3: Connect 3.left (6) → 3.right (7)

**2.4 Final Connections:**

After processing:
- Level 1: 1 → NULL
- Level 2: 2 → 3 → NULL
- Level 3: 4 → 5 → 6 → 7 → NULL

**2.5 Return Result:**

We return the root with all `next` pointers properly set.

> **Note:** The key insight is that we can use the `next` pointers we've already set to traverse the current level, eliminating the need for a queue. This makes the space complexity $O(1)$.

### Solution

```python
def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Start with the root node
        leftmost = root
        
        # While we have a level to process
        while leftmost.left:
            # Current node in the current level
            current = leftmost
            
            # Iterate through the current level
            while current:
                # Connect left child to right child
                current.left.next = current.right
                
                # Connect right child to next node's left child (if exists)
                if current.next:
                    current.right.next = current.next.left
                
                # Move to next node in the same level
                current = current.next
            
            # Move to the next level
            leftmost = leftmost.left
        
        return root
```

## 117. Populating Next Right Pointers in Each Node II [Medium]
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $0 \leq n \leq 6000$ nodes, with values in $[-100, 100]$.
* **Time Complexity:** $O(n)$ - We visit each node exactly once using BFS.
* **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level.
* **Edge Case:** An empty tree returns `None`. A single-node tree has no next pointers to set.

**1.2 High-level approach**

The goal is to connect each node's `next` pointer to its next right node at the same level. We use level-order traversal (BFS) to process nodes level by level, connecting them as we go.

![Next pointer connection showing how nodes are connected level by level]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Store nodes by level in separate arrays, then connect them. This uses $O(n)$ extra space for level arrays.
* **Optimized (BFS with Queue):** Use a queue to process nodes level by level. Connect nodes within the same level as we process them. This uses $O(n)$ space for the queue, which is necessary for BFS.

**1.4 Decomposition**

1. **Level-Order Traversal:** Use BFS to process nodes level by level.
2. **Track Level Size:** Process exactly `level_size` nodes at each iteration.
3. **Connect Nodes:** For each node in a level, set `prev.next = node` (except the first node).
4. **Update Queue:** Add children to queue for next level.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [1,2,3,4,5,null,7]$.

We initialize:
* `queue = deque([1])` (root node)
* `prev = None` (previous node in current level)

**2.2 Start Processing**

We process level 0 (root).

**2.3 Trace Walkthrough**

| Level | Queue Before | Level Size | Process | prev | Queue After | Next Pointers |
|-------|--------------|------------|---------|------|-------------|---------------|
| 0 | [1] | 1 | 1 | None | [2,3] | 1.next = None |
| 1 | [2,3] | 2 | 2 | None | [3,4,5] | 2.next = None |
| 1 | [3,4,5] | - | 3 | 2 | [4,5,7] | 2.next = 3, 3.next = None |
| 2 | [4,5,7] | 3 | 4 | None | [5,7] | 4.next = None |
| 2 | [5,7] | - | 5 | 4 | [7] | 4.next = 5, 5.next = None |
| 2 | [7] | - | 7 | 5 | [] | 5.next = 7, 7.next = None |

**2.4 Level Processing**

For each level:
1. Get `level_size = len(queue)`
2. Initialize `prev = None`
3. For `level_size` iterations:
   - Pop node from queue
   - If `prev` exists, set `prev.next = node`
   - Update `prev = node`
   - Add children to queue

**2.5 Return Result**

After processing, all nodes have their `next` pointers set correctly:
- Level 0: `1.next = None`
- Level 1: `2.next = 3`, `3.next = None`
- Level 2: `4.next = 5`, `5.next = 7`, `7.next = None`

### Solution

```python
def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            prev = None
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if prev:
                    prev.next = node
                prev = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
```

## 124. Binary Tree Maximum Path Sum [Hard]
https://leetcode.com/problems/binary-tree-maximum-path-sum/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $1 \leq n \leq 3 \times 10^4$ nodes, with values in $[-1000, 1000]$.
* **Time Complexity:** $O(n)$ - We visit each node exactly once during DFS traversal.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
* **Edge Case:** A single-node tree returns the node's value. All negative values require careful handling (we use `max(0, ...)` to avoid negative contributions).

**1.2 High-level approach**

The goal is to find the maximum path sum in a binary tree, where a path can start and end at any nodes (not necessarily root or leaf). We use DFS to calculate the maximum path sum that can be extended upward from each node, while tracking the global maximum.

![Maximum path sum visualization showing paths that can go through any node]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Try all possible paths in the tree. This is exponential in complexity.
* **Optimized (DFS with Global Tracking):** For each node, calculate the maximum path sum that can be extended upward (for parent) and the maximum path sum through the node (for global maximum). This achieves $O(n)$ time.

**1.4 Decomposition**

1. **DFS Traversal:** Recursively visit each node.
2. **Calculate Contributions:** For each node, get maximum contributions from left and right subtrees (non-negative only).
3. **Update Global Maximum:** Calculate path sum through current node and update global maximum.
4. **Return Upward Contribution:** Return the maximum path sum that can be extended to parent.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [-10,9,20,null,null,15,7]$.

We initialize:
* `res = -inf` (global maximum path sum)
* Start DFS from root node (-10)

**2.2 Start Processing**

We call `dfs(root)`.

**2.3 Trace Walkthrough**

| Node | left_sum | right_sum | Path Through Node | Return Value | res (after) |
|------|----------|-----------|-------------------|--------------|-------------|
| -10 | max(0, dfs(9)) | max(0, dfs(20)) | -10 + 0 + 0 = -10 | -10 + max(0,0) = -10 | -10 |
| 9 | 0 | 0 | 9 + 0 + 0 = 9 | 9 + 0 = 9 | 9 |
| 20 | max(0, dfs(15)) | max(0, dfs(7)) | 20 + 15 + 7 = 42 | 20 + max(15,7) = 35 | 42 |
| 15 | 0 | 0 | 15 + 0 + 0 = 15 | 15 + 0 = 15 | 42 |
| 7 | 0 | 0 | 7 + 0 + 0 = 7 | 7 + 0 = 7 | 42 |

**2.4 Recursive Processing**

For each node:
1. If `not node`, return 0 (base case)
2. Recursively get `left_sum = max(0, dfs(node.left))` (non-negative only)
3. Recursively get `right_sum = max(0, dfs(node.right))` (non-negative only)
4. Update global: `res = max(res, node.val + left_sum + right_sum)`
5. Return: `node.val + max(left_sum, right_sum)` (for parent)

**2.5 Return Result**

After processing all nodes, `res = 42`, which is the maximum path sum from the path $15 \to 20 \to 7$.

> **Note:** We use `max(0, ...)` to ensure we only consider positive contributions from subtrees. If a subtree contributes negatively, we ignore it (treat as 0).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            # Get max path sum from left and right subtrees
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            
            # Update global maximum (path through current node)
            res = max(res, node.val + left_sum + right_sum)
            
            # Return max path sum that can be extended upward
            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        return res
```

## 125. Valid Palindrome [Easy]
https://leetcode.com/problems/valid-palindrome/

### Explanation

## 125. Valid Palindrome [Easy]

https://leetcode.com/problems/valid-palindrome

## Description
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or *`false`* otherwise.*

**Examples**

```tex
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints**
```tex
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters
```

## Explanation

### Strategy
Let's restate the problem: You're given a string that may contain letters, numbers, spaces, and punctuation marks. You need to determine if it's a palindrome after cleaning it up (removing non-alphanumeric characters and converting to lowercase).

This is a **two-pointer problem** that involves string preprocessing and then checking for palindrome properties.

**What is given?** A string that may contain various characters including letters, numbers, spaces, and punctuation.

**What is being asked?** Determine if the cleaned string (only alphanumeric characters, all lowercase) is a palindrome.

**Constraints:** The string can be up to 200,000 characters long and contains only printable ASCII characters.

**Edge cases:** 
- Empty string (should return true)
- String with only non-alphanumeric characters (should return true)
- Single character (should return true)
- String with mixed case and punctuation

**High-level approach:**
The solution involves two main steps:
1. **Preprocessing**: Clean the string by removing non-alphanumeric characters and converting to lowercase
2. **Palindrome check**: Use two pointers to check if the cleaned string reads the same forward and backward

**Decomposition:**
1. **Clean the string**: Remove all non-alphanumeric characters and convert to lowercase
2. **Initialize pointers**: Place one pointer at the start and one at the end
3. **Compare characters**: Move pointers inward while comparing characters
4. **Return result**: Return true if all characters match, false otherwise

**Brute force vs. optimized strategy:**
- **Brute force**: Create a new cleaned string and then check if it equals its reverse. This takes O(n) time and O(n) space.
- **Optimized**: Use two pointers to check palindrome property in-place. This takes O(n) time and O(1) space.

### Steps
Let's walk through the solution step by step using the first example: `s = "A man, a plan, a canal: Panama"`

**Step 1: Preprocessing**
- Remove all non-alphanumeric characters: spaces, commas, colons
- Convert all letters to lowercase
- Result: `"amanaplanacanalpanama"`

**Step 2: Initialize pointers**
- `left = 0` (points to the first character: 'a')
- `right = 24` (points to the last character: 'a')

**Step 3: Compare characters**
- `s[left] = 'a'`, `s[right] = 'a'`
- `'a' == 'a'` ✓, so move both pointers inward
- `left = 1`, `right = 23`

**Step 4: Continue comparison**
- `s[left] = 'm'`, `s[right] = 'm'`
- `'m' == 'm'` ✓, so move both pointers inward
- `left = 2`, `right = 22`

**Step 5: Continue until pointers meet**
- Continue this process, comparing characters at both ends
- Move pointers inward after each successful comparison
- Stop when `left >= right`

**Step 6: Check result**
- If we reach the middle without finding a mismatch, it's a palindrome
- In this case, all characters match, so return `true`

**Why this works:**
A palindrome reads the same forward and backward. By using two pointers that start at opposite ends and move inward, we can efficiently check this property. If at any point the characters don't match, we know it's not a palindrome. If we reach the middle with all characters matching, it must be a palindrome.

> **Note:** The key insight is that we don't need to create a new cleaned string. We can process the original string character by character, skipping non-alphanumeric characters and converting case on-the-fly.

**Time Complexity:** O(n) - we process each character at most once  
**Space Complexity:** O(1) - we only use a constant amount of extra space for the pointers

### Solution

```python
def isPalindrome(s):
    """
    Check if a string is a palindrome after removing non-alphanumeric characters
    and converting to lowercase.
    
    Args:
        s: str - Input string that may contain various characters
        
    Returns:
        bool - True if the cleaned string is a palindrome, False otherwise
    """
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    # Use two pointers to check palindrome property
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # If pointers haven't crossed, compare characters
        if left < right:
            # Convert to lowercase and compare
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
    
    # If we reach here, all characters matched
    return True
```

## 128. Longest Consecutive Sequence [Medium]
https://leetcode.com/problems/longest-consecutive-sequence/

### Explanation

## 128. Longest Consecutive Sequence [Medium]

https://leetcode.com/problems/longest-consecutive-sequence

## Description
Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

**Examples**

```tex
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
```

**Constraints**
```tex
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given an unsorted array of integers, and you need to find the length of the longest sequence of consecutive integers. The challenge is to do this in O(n) time, which means we can't sort the array (as sorting takes O(n log n) time).

This is a **hash table problem** that requires finding sequences of consecutive numbers efficiently by using the properties of consecutive sequences.

**What is given?** An unsorted array of integers that can be very large (up to 100,000 elements).

**What is being asked?** Find the length of the longest sequence of consecutive integers.

**Constraints:** The array can be up to 100,000 elements long, with values ranging from -10⁹ to 10⁹.

**Edge cases:** 
- Empty array
- Array with single element
- Array with all identical elements
- Array with no consecutive sequences

**High-level approach:**
The solution involves using a hash set to quickly check if numbers exist, then for each number, expanding in both directions to find the complete consecutive sequence.

**Decomposition:**
1. **Convert array to hash set**: For O(1) lookup time
2. **Find sequence starting points**: Look for numbers that are the start of a consecutive sequence
3. **Expand sequences**: For each starting point, expand in both directions to find the complete sequence
4. **Track maximum length**: Keep track of the longest sequence found

**Brute force vs. optimized strategy:**
- **Brute force**: Sort the array and find consecutive sequences. This takes O(n log n) time.
- **Optimized**: Use hash set and expand sequences from starting points. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `nums = [100,4,200,1,3,2]`

**Step 1: Convert array to hash set**
- `nums = [100,4,200,1,3,2]`
- `num_set = {100, 4, 200, 1, 3, 2}`

**Step 2: Find sequence starting points**
- For each number, check if it's the start of a consecutive sequence
- A number is a starting point if `num - 1` is NOT in the set
- Starting points: `[100, 200, 1]` (because 99, 199, and 0 are not in the set)

**Step 3: Expand sequences from starting points**
- **Starting point 100**: 
  - Check if 101 exists: No
  - Sequence length: 1
- **Starting point 200**: 
  - Check if 201 exists: No
  - Sequence length: 1
- **Starting point 1**: 
  - Check if 2 exists: Yes
  - Check if 3 exists: Yes
  - Check if 4 exists: Yes
  - Check if 5 exists: No
  - Sequence: [1, 2, 3, 4]
  - Sequence length: 4

**Step 4: Track maximum length**
- Maximum sequence length found: 4
- Result: 4

**Why this works:**
By identifying starting points (numbers that don't have a predecessor in the set), we ensure that we only expand each sequence once. This gives us O(n) time complexity because:
1. We visit each number at most twice (once when checking if it's a starting point, once when expanding sequences)
2. Each number is part of at most one sequence
3. The total work is bounded by O(n)

> **Note:** The key insight is identifying starting points of consecutive sequences and expanding from there. This avoids redundant work and ensures O(n) time complexity.

**Time Complexity:** O(n) - we visit each number at most twice  
**Space Complexity:** O(n) - we need to store the hash set

### Solution

```python
def longestConsecutive(nums):
    if not nums:
        return 0
    
    # Convert array to hash set for O(1) lookup
    num_set = set(nums)
    max_length = 0
    
    # For each number, check if it's the start of a consecutive sequence
    for num in num_set:
        # A number is a starting point if num - 1 is NOT in the set
        if num - 1 not in num_set:
            current_length = 1
            current_num = num
            
            # Expand the sequence by checking consecutive numbers
            while current_num + 1 in num_set:
                current_length += 1
                current_num += 1
            
            # Update maximum length if current sequence is longer
            max_length = max(max_length, current_length)
    
    return max_length
```

## 129. Sum Root to Leaf Numbers [Medium]
https://leetcode.com/problems/sum-root-to-leaf-numbers/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The tree has $1 \leq n \leq 1000$ nodes, with values in $[0, 9]$, and depth at most 10.
* **Time Complexity:** $O(n)$ - We visit each node exactly once during DFS traversal.
* **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. Given depth ≤ 10, this is effectively $O(1)$.
* **Edge Case:** A single-node tree returns the node's value. All nodes have digit values (0-9).

**1.2 High-level approach**

The goal is to sum all numbers formed by root-to-leaf paths. Each path represents a number where digits are concatenated. We use DFS to traverse all paths, building numbers as we go, and sum them when we reach leaves.

![Root-to-leaf number visualization showing how paths form numbers]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Collect all root-to-leaf paths, convert each to a number, then sum. This requires storing all paths, using $O(n \times h)$ space.
* **Optimized (DFS with Running Sum):** Build numbers incrementally during traversal. When reaching a leaf, add the number to the total. This uses $O(h)$ space for recursion stack.

**1.4 Decomposition**

1. **DFS Traversal:** Recursively visit each node.
2. **Build Number:** For each node, update the running number: $current = current \times 10 + node.val$.
3. **Leaf Check:** If node is a leaf, add the number to the result.
4. **Recursive Calls:** Process left and right subtrees with updated number.
5. **Return Sum:** Return the total sum of all root-to-leaf numbers.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $root = [1,2,3]$.

We initialize:
* `res = 0` (accumulator for sum)
* `current_sum = 0` (running number being built)

**2.2 Start Processing**

We call `dfs(root, 0)`.

**2.3 Trace Walkthrough**

| Node | current_sum (before) | current_sum (after) | Is Leaf? | Action | res |
|------|----------------------|---------------------|----------|--------|-----|
| 1 | 0 | 1 | No | Continue | 0 |
| 2 (left) | 1 | 12 | Yes | Add 12 | 12 |
| 3 (right) | 1 | 13 | Yes | Add 13 | 25 |

**2.4 Recursive Processing**

For each node:
1. If `not node`, return (base case)
2. Update: `current_sum = current_sum * 10 + node.val`
3. If leaf (`not node.left and not node.right`):
   - Add to result: `res += current_sum`
   - Return
4. Recursively process: `dfs(node.left, current_sum)` and `dfs(node.right, current_sum)`

**2.5 Return Result**

After processing all paths:
- Path $1 \to 2$: number = 12
- Path $1 \to 3$: number = 13
- Sum: $12 + 13 = 25$

The function returns `res = 25`.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node, current_sum):
            nonlocal res
            if not node:
                return
            
            # Update current number
            current_sum = current_sum * 10 + node.val
            
            # If leaf node, add to result
            if not node.left and not node.right:
                res += current_sum
                return
            
            # Recursively process left and right subtrees
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        
        dfs(root, 0)
        return res
```

## 133. Clone Graph [Medium]
https://leetcode.com/problems/clone-graph/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** The graph has at most 100 nodes. Each node has a unique value in the range $[1, 100]$. The graph is connected and undirected.
- **Time Complexity:** $O(V + E)$ where $V$ is the number of vertices and $E$ is the number of edges. We visit each node and edge once.
- **Space Complexity:** $O(V)$ for the hash map storing original-to-clone mappings and the recursion stack.
- **Edge Case:** If the input node is `None`, return `None`. If the graph has only one node, return a clone of that node.

**1.2 High-level approach:**

The goal is to create a deep copy of the graph. We use a hash map to track which nodes have been cloned, and recursively clone each node and its neighbors.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Create all nodes first, then set up connections. This requires two passes and is more complex.
- **Optimized Strategy:** Use DFS with a hash map. When cloning a node, recursively clone its neighbors. The hash map prevents creating duplicate clones of the same node.
- **Why optimized is better:** The optimized approach handles cycles naturally and is more elegant, requiring only one traversal.

**1.4 Decomposition:**

1. Create a hash map to store mappings from original nodes to cloned nodes.
2. Use DFS to clone nodes recursively.
3. For each node, if it's already cloned, return the clone from the map.
4. Otherwise, create a new node, add it to the map, and recursively clone all neighbors.
5. Return the cloned graph starting from the given node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `adjList = [[2,4],[1,3],[2,4],[1,3]]`

This represents a graph with 4 nodes:
- Node 1 is connected to nodes 2 and 4
- Node 2 is connected to nodes 1 and 3
- Node 3 is connected to nodes 2 and 4
- Node 4 is connected to nodes 1 and 3

We initialize an empty hash map `node_map = {}`.

**2.2 Start Checking:**

We call the `clone` function with the given node (node 1).

**2.3 Trace Walkthrough:**

| Step | Node | Action | node_map |
|------|------|--------|----------|
| 1 | 1 | Create clone(1), add to map | {1: clone(1)} |
| 2 | Clone neighbors of 1: [2,4] | Clone node 2 | {1: clone(1), 2: clone(2)} |
| 3 | Clone neighbors of 2: [1,3] | Node 1 already cloned, use it | {1: clone(1), 2: clone(2), 3: clone(3)} |
| 4 | Clone neighbors of 3: [2,4] | Node 2 already cloned, use it | {1: clone(1), 2: clone(2), 3: clone(3), 4: clone(4)} |
| 5 | Clone neighbors of 4: [1,3] | Both already cloned, use them | Complete |

**2.4 Increment and Loop:**

The recursive `clone` function:
1. Checks if the node is already in `node_map`. If yes, returns the clone.
2. Creates a new `Node` with the same value.
3. Adds the mapping to `node_map`.
4. Recursively clones all neighbors and adds them to the clone's neighbors list.

**2.5 Return Result:**

The function returns `clone(node)`, which is the cloned version of the input node. The entire graph structure is cloned, with all connections preserved.

### Solution

```python
def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to map original nodes to cloned nodes
        node_map = {}
        
        def clone(node):
            # If already cloned, return the clone
            if node in node_map:
                return node_map[node]
            
            # Create a new node
            clone_node = Node(node.val)
            node_map[node] = clone_node
            
            # Clone all neighbors
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            
            return clone_node
        
        return clone(node)
```

## 138. Copy List with Random Pointer [Medium]
https://leetcode.com/problems/copy-list-with-random-pointer/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $0 \leq n \leq 1000$ nodes. Node values are in the range $[-10^4, 10^4]$. Random pointers can point to any node or `None`.
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes. We make two passes through the list.
- **Space Complexity:** $O(n)$ for the hash map storing original-to-clone node mappings.
- **Edge Case:** If the list is empty (`head` is `None`), return `None`.

**1.2 High-level approach:**

The goal is to create a deep copy of the linked list where each node has both `next` and `random` pointers. We use a hash map to store mappings from original nodes to cloned nodes, then set up the pointers in a second pass.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Create all nodes first, then try to set random pointers. This is complex because random pointers can point to nodes we haven't created yet.
- **Optimized Strategy:** Two-pass approach: first pass creates all nodes and stores mappings, second pass sets `next` and `random` pointers using the map. This is $O(n)$ time and $O(n)$ space.
- **Why optimized is better:** The two-pass approach cleanly separates node creation from pointer setup, making the logic straightforward.

**1.4 Decomposition:**

1. Create a hash map to store mappings from original nodes to cloned nodes.
2. First pass: traverse the list and create a clone of each node, storing the mapping.
3. Second pass: traverse the list again and set `next` and `random` pointers for each clone using the map.
4. Return the cloned head node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`

This represents:
- Node 0: value 7, random = null
- Node 1: value 13, random = node 0
- Node 2: value 11, random = node 4
- Node 3: value 10, random = node 2
- Node 4: value 1, random = node 0

We initialize `node_map = {}`.

**2.2 Start Checking:**

We perform two passes: first to create nodes, second to set pointers.

**2.3 Trace Walkthrough:**

**First pass (create nodes):**

| Original Node | Value | Clone Created | node_map |
|---------------|-------|---------------|----------|
| Node 0 | 7 | Clone(7) | {Node0: Clone(7)} |
| Node 1 | 13 | Clone(13) | {Node0: Clone(7), Node1: Clone(13)} |
| Node 2 | 11 | Clone(11) | {Node0: Clone(7), Node1: Clone(13), Node2: Clone(11)} |
| Node 3 | 10 | Clone(10) | {Node0: Clone(7), Node1: Clone(13), Node2: Clone(11), Node3: Clone(10)} |
| Node 4 | 1 | Clone(1) | {Node0: Clone(7), ..., Node4: Clone(1)} |

**Second pass (set pointers):**

| Original Node | next points to | random points to | Clone's next | Clone's random |
|---------------|----------------|------------------|--------------|----------------|
| Node 0 | Node 1 | null | Clone(13) | null |
| Node 1 | Node 2 | Node 0 | Clone(11) | Clone(7) |
| Node 2 | Node 3 | Node 4 | Clone(10) | Clone(1) |
| Node 3 | Node 4 | Node 2 | Clone(1) | Clone(11) |
| Node 4 | null | Node 0 | null | Clone(7) |

**2.4 Increment and Loop:**

- First pass: `while curr: node_map[curr] = Node(curr.val); curr = curr.next`
- Second pass: `while curr: node_map[curr].next = node_map.get(curr.next); node_map[curr].random = node_map.get(curr.random); curr = curr.next`

**2.5 Return Result:**

We return `node_map[head]`, which is the cloned head node. The entire list structure is cloned with all `next` and `random` pointers correctly set.

### Solution

```python
def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # First pass: create new nodes and map old to new
        node_map = {}
        curr = head
        
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: set next and random pointers
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]
```

## 141. Linked List Cycle [Easy]
https://leetcode.com/problems/linked-list-cycle/

### Explanation

# 141. Linked List Cycle [Easy]

https://leetcode.com/problems/linked-list-cycle

## Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:**
```text
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:**
```text
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:**
```text
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.


**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Explanation

### Strategy

This is a **two-pointer problem** that requires detecting a cycle in a linked list. The key insight is to use Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm), which uses two pointers moving at different speeds.

**Key observations:**
- If there's a cycle, a fast pointer will eventually catch up to a slow pointer
- If there's no cycle, the fast pointer will reach the end (null)
- The fast pointer moves twice as fast as the slow pointer
- This approach uses O(1) space, which is optimal

**High-level approach:**
1. **Use two pointers**: Slow pointer (tortoise) and fast pointer (hare)
2. **Move pointers**: Slow moves 1 step, fast moves 2 steps
3. **Check for cycle**: If fast catches slow, there's a cycle
4. **Check for end**: If fast reaches null, there's no cycle

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If head is null or head.next is null, return false

**Step 2: Initialize pointers**
- `slow = head` (moves 1 step at a time)
- `fast = head.next` (moves 2 steps at a time)

**Step 3: Move pointers until they meet or reach end**
While `fast` is not null and `fast.next` is not null:
- Move slow pointer: `slow = slow.next`
- Move fast pointer: `fast = fast.next.next`
- If slow and fast meet, return true (cycle detected)

**Step 4: Return result**
- If you exit the loop, return false (no cycle)

**Example walkthrough:**
Let's trace through the first example:

```text
head = [3,2,0,-4], pos = 1 (cycle from -4 back to 2)

Initial state:
slow = 3, fast = 2

Step 1: slow = 2, fast = 0
Step 2: slow = 0, fast = 2
Step 3: slow = -4, fast = 0
Step 4: slow = 2, fast = 2 (they meet!)

Result: Return true (cycle detected)
```

> **Note:** Floyd's Cycle-Finding Algorithm is optimal because it uses O(1) space and O(n) time. The mathematical proof shows that if there's a cycle, the fast pointer will eventually catch the slow pointer within one cycle length.

**Time Complexity:** O(n) - in the worst case, you visit each node at most twice  
**Space Complexity:** O(1) - you only use two pointers regardless of input size

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.next = None
```

## 142. Linked List Cycle II [Medium]
https://leetcode.com/problems/linked-list-cycle-ii/

### Explanation

## Explanation

### Strategy (The "Why")

Given the head of a linked list, we need to return the node where the cycle begins. If there is no cycle, return `null`.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $10^4$.
- **Value Range:** Node values can be any integer.
- **Time Complexity:** $O(n)$ - We traverse the list at most twice with Floyd's algorithm.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If the list has no cycle, return `null`. If the list has only one node pointing to itself, that node is the cycle start.

**1.2 High-level approach:**

The goal is to find the starting node of a cycle in a linked list.

We use Floyd's cycle detection algorithm (tortoise and hare). First, we detect if there's a cycle by having two pointers move at different speeds. If they meet, there's a cycle. Then, we find the cycle start by moving one pointer back to the head and moving both at the same speed until they meet again.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use a hash set to store visited nodes. The first node we encounter that's already in the set is the cycle start. This takes $O(n)$ time and $O(n)$ space.
- **Optimized Strategy (Floyd's Algorithm):** Use two pointers moving at different speeds to detect the cycle, then use mathematical properties to find the start. This takes $O(n)$ time and $O(1)$ space.
- **Why it's better:** Floyd's algorithm uses $O(1)$ extra space instead of $O(n)$ for a hash set, while maintaining the same time complexity.

**1.4 Decomposition:**

1. Use two pointers (slow and fast) starting at the head.
2. Move slow one step and fast two steps at a time.
3. If they meet, there's a cycle. If fast reaches the end, there's no cycle.
4. If a cycle is detected, move slow back to the head.
5. Move both pointers one step at a time until they meet. The meeting point is the cycle start.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: head = $[3,2,0,-4]$ with cycle at node with value 2

We initialize:
- `slow = head`
- `fast = head`

**2.2 Start Detection:**

We begin moving the pointers.

**2.3 Trace Walkthrough:**

**Phase 1: Detect Cycle**

| Step | slow position | fast position | Action |
|------|---------------|---------------|--------|
| 0 | 3 | 3 | Start |
| 1 | 2 | 0 | Move |
| 2 | 0 | 2 | Move |
| 3 | -4 | -4 | **Meet!** Cycle detected |

**Phase 2: Find Cycle Start**

| Step | slow position | fast position | Action |
|------|---------------|---------------|--------|
| 0 | 3 (head) | -4 | Reset slow to head |
| 1 | 2 | 3 | Move both one step |
| 2 | 0 | 2 | Move both one step |
| 3 | -4 | 0 | Move both one step |
| 4 | 3 | -4 | Move both one step |
| 5 | 2 | 2 | **Meet!** Cycle start found |

**2.4 Explanation:**

- When slow and fast meet in phase 1, the distance from head to cycle start equals the distance from meeting point to cycle start.
- Moving both pointers one step at a time from head and meeting point will make them meet at the cycle start.

**2.5 Return Result:**

We return the node with value 2, which is where the cycle begins.

> **Note:** Floyd's algorithm uses the mathematical property that when the slow and fast pointers meet, the distance from the head to the cycle start equals the distance from the meeting point to the cycle start (moving in the cycle direction).

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        # Floyd's cycle detection algorithm
        slow = head
        fast = head
        
        # Find meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected, find the start of cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None
```

## 146. LRU Cache [Medium]
https://leetcode.com/problems/lru-cache/

### Explanation

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Example 1:**

```raw
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Constraints:**
- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Explanation

### Strategy

This is a **design problem** that requires implementing an LRU (Least Recently Used) cache. The key insight is to combine a hash map for O(1) lookups with a doubly linked list for O(1) insertions/deletions to maintain the order of usage.

**Key observations:**

- We need O(1) time for both get and put operations
- We need to track the order of usage (most recently used to least recently used)
- When capacity is exceeded, we need to remove the least recently used item
- A hash map provides O(1) lookups, but doesn't maintain order
- A doubly linked list maintains order and allows O(1) insertions/deletions

**High-level approach:**

1. **Use a hash map**: For O(1) key-value lookups
2. **Use a doubly linked list**: To maintain usage order
3. **Combine both**: Hash map stores key -> node mappings
4. **Update order**: Move accessed items to front (most recently used)
5. **Evict LRU**: Remove from end when capacity exceeded

### Steps

Let's break down the solution step by step:

**Step 1: Design the data structure**

- `capacity`: Maximum number of items in cache
- `cache`: Hash map for key -> node mappings
- `head`: Dummy head node of doubly linked list
- `tail`: Dummy tail node of doubly linked list

**Step 2: Implement get operation**

- Check if key exists in hash map
- If not found, return -1
- If found, move node to front (most recently used)
- Return the value

**Step 3: Implement put operation**

- If key exists, update value and move to front
- If key doesn't exist:
  - Create new node
  - Add to front of list
  - Add to hash map
  - If capacity exceeded, remove LRU item (from end)

**Step 4: Helper methods**

- `_add_to_front(node)`: Add node to front of list
- `_remove_node(node)`: Remove node from list
- `_remove_lru()`: Remove least recently used item

**Example walkthrough:**

Let's trace through the example:

```raw
capacity = 2

put(1, 1): cache = {1=1}, list = [1]
put(2, 2): cache = {1=1, 2=2}, list = [2, 1]
get(1): return 1, list = [1, 2] (move 1 to front)
put(3, 3): cache = {1=1, 3=3}, list = [3, 1] (evict 2)
get(2): return -1 (not found)
put(4, 4): cache = {3=3, 4=4}, list = [4, 3] (evict 1)
get(1): return -1 (not found)
get(3): return 3, list = [3, 4]
get(4): return 4, list = [4, 3]
```

> **Note:** The doubly linked list with dummy head and tail nodes makes it easy to add/remove nodes at the beginning and end. The hash map provides O(1) access to any node, and the list maintains the order of usage.

**Time Complexity:** O(1) for both get and put operations  
**Space Complexity:** O(capacity) - we store at most capacity items

### Solution

```python
def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node mapping

        # Initialize doubly linked list with dummy nodes
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Check if key exists
        if key not in self.cache:
            return -1

        # Move node to front (most recently used)
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # If key exists, update value and move to front
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_front(node)
        else:
            # Create new node
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            # If capacity exceeded, remove LRU item
            if len(self.cache) > self.capacity:
                self._remove_lru()

    def _add_to_front(self, node):
        """Add node to front of list (after dummy head)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove node from list"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_lru(self):
        """Remove least recently used item (before dummy tail)"""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        del self.cache[lru_node.key]


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
```

## 148. Sort List [Medium]
https://leetcode.com/problems/sort-list/

### Explanation

Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

**Example 1:**

```tex
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

**Example 2:**

```tex
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Example 3:**

```tex
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

```tex
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

**Time Complexity:** O(n log n) - merge sort time complexity  
**Space Complexity:** O(log n) - recursion stack space (not O(1) due to recursion)

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(
        self, left: Optional[ListNode], right: Optional[ListNode]
    ) -> Optional[ListNode]:
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

## 155. Min Stack [Medium]
https://leetcode.com/problems/min-stack/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** Values are in the range $[-2^{31}, 2^{31} - 1]$. At most $3 \times 10^4$ operations will be performed. Operations are called on non-empty stacks.
- **Time Complexity:** $O(1)$ for all operations (push, pop, top, getMin). Each operation is constant time.
- **Space Complexity:** $O(n)$ where $n$ is the number of elements pushed. We maintain two stacks.
- **Edge Case:** If we push the same minimum value multiple times, we need to track all occurrences to handle pops correctly.

**1.2 High-level approach:**

The goal is to design a stack that supports retrieving the minimum element in $O(1)$ time. We use two stacks: one for all elements and one to track minimum values. When pushing, if the new value is less than or equal to the current minimum, we also push it to the min stack.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Store all elements and scan for minimum when `getMin()` is called. This is $O(n)$ time for `getMin()`.
- **Optimized Strategy:** Maintain a separate stack for minimum values. When pushing, if the value is $\leq$ current min, push to min stack. When popping, if the popped value equals the current min, pop from min stack. This gives $O(1)$ for all operations.
- **Why optimized is better:** The optimized strategy achieves $O(1)$ time for `getMin()` by trading a small amount of space for constant-time operations.

**1.4 Decomposition:**

1. Maintain two stacks: `stack` for all elements and `min_stack` for minimum values.
2. `push(val)`: Push to `stack`. If `min_stack` is empty or `val <= min_stack[-1]`, push to `min_stack`.
3. `pop()`: Pop from `stack`. If the popped value equals `min_stack[-1]`, pop from `min_stack`.
4. `top()`: Return `stack[-1]`.
5. `getMin()`: Return `min_stack[-1]`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `["MinStack","push","push","push","getMin","pop","top","getMin"]` with values `[[],[-2],[0],[-3],[],[],[],[]]`

We initialize:
- `stack = []`
- `min_stack = []`

**2.2 Start Checking:**

We perform each operation in sequence.

**2.3 Trace Walkthrough:**

| Operation | Value | stack | min_stack | Return |
|-----------|-------|-------|-----------|--------|
| push(-2) | -2 | [-2] | [-2] | - |
| push(0) | 0 | [-2,0] | [-2] | - |
| push(-3) | -3 | [-2,0,-3] | [-2,-3] | - |
| getMin() | - | [-2,0,-3] | [-2,-3] | -3 |
| pop() | - | [-2,0] | [-2] | - |
| top() | - | [-2,0] | [-2] | 0 |
| getMin() | - | [-2,0] | [-2] | -2 |

**2.4 Increment and Loop:**

- **push(val)**: 
  - `stack.append(val)`
  - If `not min_stack or val <= min_stack[-1]`: `min_stack.append(val)`

- **pop()**: 
  - `val = stack.pop()`
  - If `val == min_stack[-1]`: `min_stack.pop()`

**2.5 Return Result:**

After all operations:
- `top()` returns `0` (the top element).
- `getMin()` returns `-2` (the minimum element in the remaining stack).

The stack correctly maintains both the elements and the minimum value in $O(1)$ time for all operations.

### Solution

```python
def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack only if it's empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # Pop from min_stack if the popped value is the current min
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## 156. Binary Tree Upside Down [Medium]
https://leetcode.com/problems/binary-tree-upside-down/

### Explanation

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to flip a binary tree upside down, where the original leftmost node becomes the new root, and the original root becomes the rightmost leaf. The transformation follows a specific pattern where left children become parents and right children become left children.

**1.1 Constraints & Complexity:**
- Input size: The tree can have up to O(n) nodes where n is the number of nodes
- **Time Complexity:** O(n) where n is the number of nodes - we visit each node exactly once
- **Space Complexity:** O(h) where h is the height of the tree - the recursion stack depth equals the tree height
- **Edge Case:** If the tree is empty or has no left child, return the root as-is

**1.2 High-level approach:**
We use recursion to traverse to the leftmost node, which becomes the new root. During the backtracking phase, we reassign pointers to transform the tree structure according to the upside-down pattern.

![Binary tree upside down transformation](https://assets.leetcode.com/static_assets/others/binary-tree-upside-down.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Create a new tree by copying nodes and reassigning pointers iteratively. This requires O(n) extra space.
- **Optimized Strategy:** Use recursion to transform the tree in-place by reassigning pointers during backtracking. This uses O(h) space for recursion.
- **Why it's better:** We modify the tree in-place without creating new nodes, making it more memory efficient.

**1.4 Decomposition:**
1. Recursively traverse to the leftmost node, which will become the new root
2. During backtracking, reassign the current node's left child's left pointer to the current node's right child
3. Reassign the current node's left child's right pointer to the current node itself
4. Set the current node's left and right pointers to None to break old connections
5. Return the new root (leftmost node) from the deepest recursion

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example tree with nodes [1,2,3,4,5]:
- Root: 1, left: 2, right: 3
- Node 2: left: 4, right: 5
- After transformation, node 4 becomes the new root

**2.2 Start Processing:**
We begin recursive traversal starting from the root, always going left first.

**2.3 Trace Walkthrough:**

| Node | Has Left? | Action | New Root | Transformations |
|------|-----------|--------|----------|------------------|
| 1 | Yes | Go left to 2 | - | - |
| 2 | Yes | Go left to 4 | - | - |
| 4 | No | Return 4 | 4 | - |
| 2 | - | Backtrack | 4 | 4.left = 5, 4.right = 2, 2.left = None, 2.right = None |
| 1 | - | Backtrack | 4 | 2.left = 3, 2.right = 1, 1.left = None, 1.right = None |

**2.4 Increment and Loop:**
The recursion naturally handles the traversal. We continue until we reach a node with no left child.

**2.5 Return Result:**
Return the new root (node 4), which is the leftmost node from the original tree. The tree is now upside down with all pointers correctly reassigned.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        
        new_root = self.upsideDownBinaryTree(root.left)
        
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        
        return new_root
```

## 160. Intersection of Two Linked Lists [Easy]
https://leetcode.com/problems/intersection-of-two-linked-lists/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** We have two linked lists with `m` and `n` nodes respectively, where `1 <= m, n <= 3 * 10^4`. Each node value is between `1` and `10^5`.
- **Time Complexity:** O(m + n) - In the worst case, we traverse both lists once before finding the intersection or determining there is none.
- **Space Complexity:** O(1) - We only use two pointer variables, no additional data structures.
- **Edge Case:** When the two lists have no intersection, both pointers will eventually become `None` and the loop will terminate, returning `None`.

**1.2 High-level approach:**
The goal is to find the node where two linked lists intersect, or return `None` if they don't intersect. The key insight is that if we traverse both lists simultaneously, switching to the other list when we reach the end, both pointers will eventually meet at the intersection point (if it exists) after traversing the same total distance.

![Two linked lists intersecting](https://assets.leetcode.com/uploads/2021/03/05/160_statement.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each node in list A, check if it exists in list B by traversing list B. This would take O(m * n) time complexity.
- **Optimized Strategy (Two Pointers):** Use two pointers that traverse both lists, switching lists when reaching the end. This ensures both pointers cover the same total distance and will meet at the intersection. Time complexity is O(m + n) with O(1) space.

**1.4 Decomposition:**
1. Initialize two pointers, one for each list.
2. Traverse both lists simultaneously, moving each pointer forward.
3. When a pointer reaches the end of its list, switch it to the head of the other list.
4. Continue until both pointers point to the same node (intersection found) or both are `None` (no intersection).

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `headA = [4,1,8,4,5]` and `headB = [5,6,1,8,4,5]`, where the lists intersect at node with value 8.

Initialize:
- `p1 = headA` (points to node 4)
- `p2 = headB` (points to node 5)

**2.2 Start Checking:**
We enter a loop that continues while `p1 != p2`.

**2.3 Trace Walkthrough:**

| Step | p1 position | p2 position | p1 value | p2 value | Action |
|------|-------------|--------------|----------|----------|--------|
| 1 | headA[0] | headB[0] | 4 | 5 | Both advance |
| 2 | headA[1] | headB[1] | 1 | 6 | Both advance |
| 3 | headA[2] | headB[2] | 8 | 1 | Both advance |
| 4 | headA[3] | headB[3] | 4 | 8 | Both advance |
| 5 | headA[4] | headB[4] | 5 | 4 | Both advance |
| 6 | None | headB[5] | - | 5 | p1 switches to headB |
| 7 | headB[0] | None | 5 | - | p2 switches to headA |
| 8 | headB[1] | headA[0] | 6 | 4 | Both advance |
| 9 | headB[2] | headA[1] | 1 | 1 | Both advance |
| 10 | headB[3] | headA[2] | 8 | 8 | **Match!** Intersection found |

**2.4 Increment and Loop:**
At each iteration:
- If `p1` is not `None`, move it to `p1.next`; otherwise, set it to `headB`.
- If `p2` is not `None`, move it to `p2.next`; otherwise, set it to `headA`.

**2.5 Return Result:**
When `p1 == p2`, the loop exits. This happens either:
- When both point to the intersection node (return that node)
- When both are `None` (no intersection, return `None`)

In our example, both pointers meet at the node with value 8, which is the intersection point.

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Two pointer approach: traverse both lists
        # When one pointer reaches end, switch to other list
        # This way both pointers will meet at intersection (if exists)
        # or both will be None (if no intersection)
        
        p1, p2 = headA, headB
        
        while p1 != p2:
            # If p1 reaches end, switch to headB
            p1 = p1.next if p1 else headB
            # If p2 reaches end, switch to headA
            p2 = p2.next if p2 else headA
        
        return p1
```

## 170. Two Sum III - Data structure design [Easy]
https://leetcode.com/problems/two-sum-iii-data-structure-design/

### Explanation

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to design a data structure that supports adding numbers and checking if any two numbers in the structure sum to a target value. This is similar to the classic Two Sum problem, but we need to handle dynamic additions and queries.

**1.1 Constraints & Complexity:**
- Input size: Number of add operations and find operations can be large
- **Time Complexity:** O(1) for add, O(n) for find where n is the number of distinct numbers added
- **Space Complexity:** O(n) where n is the number of distinct numbers stored
- **Edge Case:** If we add the same number twice and look for 2*number, we need at least 2 occurrences. If we look for a sum that requires two different numbers, we need both to exist.

**1.2 High-level approach:**
We use a hash map to store the frequency of each number added. For the find operation, we iterate through all numbers and check if their complement (target - number) exists in the map. We handle the special case where the complement equals the number itself.

![Hash map storing number frequencies](https://assets.leetcode.com/static_assets/others/two-sum-hashmap.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Store numbers in a list, and for each find, check all pairs O(n²) time.
- **Optimized Strategy:** Use a hash map for O(1) lookups. For find, iterate through keys and check complements in O(1) time each.
- **Why it's better:** Hash map lookups are O(1) average case, making find operations much faster than checking all pairs.

**1.4 Decomposition:**
1. Initialize a hash map to store number frequencies in the constructor
2. For add operation, increment the count of the number in the hash map
3. For find operation, iterate through all numbers in the hash map
4. For each number, calculate its complement (target - number)
5. Check if complement exists, handling the case where complement equals the number (need count >= 2)

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `add(1)`, `add(3)`, `add(5)`, `find(4)`, `find(7)`
- Initialize `num_counts = {}` (empty hash map)

**2.2 Start Adding:**
We add numbers to the data structure.

**2.3 Trace Walkthrough:**

| Operation | number | num_counts after | - |
|-----------|--------|-------------------|---|
| add(1) | 1 | {1: 1} | - |
| add(3) | 3 | {1: 1, 3: 1} | - |
| add(5) | 5 | {1: 1, 3: 1, 5: 1} | - |
| find(4) | - | {1: 1, 3: 1, 5: 1} | Check: 1→complement=3 (exists), return True |
| find(7) | - | {1: 1, 3: 1, 5: 1} | Check: 1→complement=6 (not exists), 3→complement=4 (not exists), 5→complement=2 (not exists), return False |

**Detailed find(4) check:**
- num=1: complement = 4-1 = 3, exists in map → return True

**Detailed find(7) check:**
- num=1: complement = 7-1 = 6, not in map
- num=3: complement = 7-3 = 4, not in map
- num=5: complement = 7-5 = 2, not in map
- return False

**2.4 Increment and Loop:**
For find operations, we iterate through all keys in the hash map. We stop early if we find a valid pair.

**2.5 Return Result:**
Return True if any pair sums to the target value, False otherwise. For find(4), we return True because 1 + 3 = 4. For find(7), we return False because no pair sums to 7.

### Solution

```python
def __init__(self):
        self.num_counts = defaultdict(int)
    
    def add(self, number: int) -> None:
        self.num_counts[number] += 1
    
    def find(self, value: int) -> bool:
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                if complement != num or self.num_counts[num] > 1:
                    return True
        return False
```

## 173. Binary Search Tree Iterator [Medium]
https://leetcode.com/problems/binary-search-tree-iterator/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^5$ nodes. Node values are in the range $[0, 10^6]$. At most $10^5$ calls to `next()` and `hasNext()`.
- **Time Complexity:** 
  - `__init__`: $O(h)$ where $h$ is the height of the tree (we push left nodes).
  - `next()`: Amortized $O(1)$ per call.
  - `hasNext()`: $O(1)$.
- **Space Complexity:** $O(h)$ for the stack storing nodes along the path to the leftmost node.
- **Edge Case:** If the tree has only one node, the stack contains that node initially.

**1.2 High-level approach:**

The goal is to implement an iterator that returns nodes in in-order traversal (left, root, right) order. We use a stack to simulate the in-order traversal. Initially, we push all left nodes. When `next()` is called, we pop a node, push its right subtree's left nodes, and return the node's value.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Perform full in-order traversal, store all values in a list, then iterate through the list. This requires $O(n)$ space and doesn't meet the $O(h)$ space requirement.
- **Optimized Strategy:** Use a stack to maintain only the nodes needed for the current path. Push left nodes initially, and when popping, push left nodes of the right child. This uses $O(h)$ space.
- **Why optimized is better:** The optimized approach meets the $O(h)$ space requirement and provides amortized $O(1)$ time for `next()`.

**1.4 Decomposition:**

1. In `__init__`, push all left nodes starting from the root.
2. In `next()`, pop a node from the stack, push all left nodes of its right child, and return the node's value.
3. In `hasNext()`, check if the stack is non-empty.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `root = [7, 3, 15, null, null, 9, 20]`

The tree structure:
```
      7
     / \
    3   15
       /  \
      9    20
```

We initialize `stack = []` and call `_push_left(root)`.

**2.2 Start Checking:**

The `_push_left` function pushes all left nodes: 7, then 3. So `stack = [7, 3]` (top is 3).

**2.3 Trace Walkthrough:**

| Operation | Stack before | Action | Stack after | Return |
|-----------|--------------|--------|-------------|--------|
| __init__ | [] | Push left: 7, 3 | [7, 3] | - |
| next() | [7, 3] | Pop 3, push left of 3.right (none) | [7] | 3 |
| next() | [7] | Pop 7, push left of 7.right: 15, 9 | [15, 9] | 7 |
| hasNext() | [15, 9] | Check stack non-empty | [15, 9] | True |
| next() | [15, 9] | Pop 9, push left of 9.right (none) | [15] | 9 |
| next() | [15] | Pop 15, push left of 15.right: 20 | [20] | 15 |
| next() | [20] | Pop 20, push left of 20.right (none) | [] | 20 |
| hasNext() | [] | Check stack empty | [] | False |

**2.4 Increment and Loop:**

- **`_push_left(node)`**: While `node` is not None, push `node` to stack and move to `node.left`.
- **`next()`**: 
  - Pop a node from the stack.
  - Call `_push_left(node.right)` to push all left nodes of the right subtree.
  - Return the popped node's value.

**2.5 Return Result:**

The iterator returns values in in-order order: 3, 7, 9, 15, 20. Each call to `next()` returns the next value, and `hasNext()` correctly indicates when more values are available.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # Push all left nodes to stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the smallest element
        node = self.stack.pop()
        # Push all left nodes of the right child
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

## 199. Binary Tree Right Side View [Medium]
https://leetcode.com/problems/binary-tree-right-side-view/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to return the values of the nodes you can see when standing on the right side of the tree, ordered from top to bottom.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ can be up to $100$.
- **Value Range:** Node values are between $0$ and $100$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(n)$ - The queue can contain at most all nodes at the widest level.
- **Edge Case:** If the tree is empty, return an empty list. If the tree has only one node, return that node's value.

**1.2 High-level approach:**

The goal is to find the rightmost node at each level of the tree.

![Right Side View](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

We use BFS (breadth-first search) level by level. For each level, we add the rightmost node (the last node processed at that level) to our result.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the tree.
- **Optimized Strategy (BFS):** Use BFS to process nodes level by level. For each level, track the last node processed, which is the rightmost node. This is the same as level-order traversal, but we only keep the last element of each level.
- **Why it's better:** BFS naturally processes nodes level by level from left to right, so the last node at each level is the rightmost node.

**1.4 Decomposition:**

1. If the tree is empty, return an empty list.
2. Initialize a queue with the root node.
3. While the queue is not empty:
   - Get the number of nodes at the current level.
   - Process all nodes at this level.
   - For the last node at each level (rightmost), add its value to the result.
   - Add all children to the queue for the next level.
4. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,2,3,null,5,null,4]$

The tree structure:
```
    1
   / \
  2   3
   \   \
    5   4
```

We initialize:
- `queue = deque([1])`
- `res = []`

**2.2 Start BFS:**

We begin processing level by level.

**2.3 Trace Walkthrough:**

| Level | Queue Before | Level Size | Process | Rightmost Node | res |
|-------|--------------|------------|---------|----------------|-----|
| 0 | [1] | 1 | Node 1 (last) | 1 | [1] |
| 1 | [2, 3] | 2 | Node 2, Node 3 (last) | 3 | [1, 3] |
| 2 | [5, 4] | 2 | Node 5, Node 4 (last) | 4 | [1, 3, 4] |

**2.4 Explanation:**

- Level 0: Only node 1 → add 1
- Level 1: Nodes 2 and 3 → add 3 (rightmost)
- Level 2: Nodes 5 and 4 → add 4 (rightmost)

**2.5 Return Result:**

We return `[1, 3, 4]`, which are the values of the rightmost nodes at each level.

> **Note:** The key is to identify the last node processed at each level during BFS. Since BFS processes nodes from left to right, the last node at each level is the rightmost node visible from the right side.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from collections import deque

class Solution:
    def rightSideView(self, root) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Add the rightmost node of each level
                if i == level_size - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
```

## 206. Reverse Linked List [Easy]
https://leetcode.com/problems/reverse-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

Given the head of a singly linked list, we need to reverse the list and return the reversed list's head.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be between $0$ and $5000$.
- **Value Range:** Node values are between $-5000$ and $5000$.
- **Time Complexity:** $O(n)$ - We visit each node exactly once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If the list is empty (head is null), return null. If the list has only one node, return that node.

**1.2 High-level approach:**

The goal is to reverse the links between nodes in a linked list.

We use an iterative approach with three pointers: `prev` (previous node), `current` (current node), and `next_node` (next node). We traverse the list, reversing each link as we go.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert the list to an array, reverse the array, then convert back to a linked list. This takes $O(n)$ time and $O(n)$ space.
- **Optimized Strategy (Iterative):** Use pointers to reverse links in-place. This takes $O(n)$ time and $O(1)$ space.
- **Why it's better:** The iterative approach uses $O(1)$ extra space instead of $O(n)$ for an array, while maintaining the same time complexity.

**1.4 Decomposition:**

1. Initialize `prev = None` and `current = head`.
2. While `current` is not null:
   - Store the next node.
   - Reverse the link: `current.next = prev`.
   - Move pointers forward: `prev = current`, `current = next_node`.
3. Return `prev` (which is the new head).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $head = [1,2,3,4,5]$

We initialize:
- `prev = None`
- `current = 1`

**2.2 Start Reversing:**

We begin reversing links.

**2.3 Trace Walkthrough:**

| Step | current | next_node | current.next | prev After | current After |
|------|---------|-----------|--------------|------------|---------------|
| 1 | 1 | 2 | None | 1 | 2 |
| 2 | 2 | 3 | 1 | 2 | 3 |
| 3 | 3 | 4 | 2 | 3 | 4 |
| 4 | 4 | 5 | 3 | 4 | 5 |
| 5 | 5 | None | 4 | 5 | None |

**2.4 Final State:**

After reversing:
- Original: $1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow null$
- Reversed: $5 \rightarrow 4 \rightarrow 3 \rightarrow 2 \rightarrow 1 \rightarrow null$

**2.5 Return Result:**

We return the node with value 5, which is the new head of the reversed list.

> **Note:** The key insight is to maintain three pointers: previous, current, and next. We reverse the link from current to previous, then move all pointers forward. The previous pointer becomes the new head at the end.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        
        while current:
            # Store next node
            next_node = current.next
            # Reverse the link
            current.next = prev
            # Move pointers forward
            prev = current
            current = next_node
        
        return prev
```

## 208. Implement Trie (Prefix Tree) [Medium]
https://leetcode.com/problems/implement-trie-prefix-tree/

### Explanation

## Explanation

### Strategy (The "Why")

We need to implement a Trie (prefix tree) data structure that supports inserting words, searching for complete words, and checking if any word starts with a given prefix.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of operations $N$ can be up to $3 \times 10^4$.
- **Value Range:** Words and prefixes consist of lowercase English letters only, with length between 1 and 2000.
- **Time Complexity:** 
  - `insert`: $O(m)$ where $m$ is the length of the word
  - `search`: $O(m)$ where $m$ is the length of the word
  - `startsWith`: $O(m)$ where $m$ is the length of the prefix
- **Space Complexity:** $O(ALPHABET\_SIZE \times N \times M)$ where $N$ is the number of words and $M$ is the average length. In practice, this is $O(\text{total characters in all words})$.
- **Edge Case:** Searching for an empty string should return false (unless an empty word was inserted). Checking prefix of empty string should return true if any word exists.

**1.2 High-level approach:**

The goal is to implement a Trie data structure that efficiently stores and retrieves words.

![Trie Structure](https://assets.leetcode.com/uploads/2021/04/28/trie-1.png)

A Trie is a tree-like data structure where each node represents a character. Words that share common prefixes share the same path in the tree. This makes prefix searches very efficient.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Store all words in a list. For search and prefix operations, iterate through all words checking each one. This takes $O(n \times m)$ time where $n$ is the number of words.
- **Optimized Strategy (Trie):** Use a tree structure where each node has children representing possible next characters. This allows us to search in $O(m)$ time regardless of how many words are stored.
- **Why it's better:** The Trie structure eliminates the need to check every word. We only traverse the path relevant to the word or prefix we're looking for, making it much more efficient for large datasets.

**1.4 Decomposition:**

1. Create a `TrieNode` class with a dictionary of children and a flag indicating if it's the end of a word.
2. Initialize the Trie with a root `TrieNode`.
3. For `insert`: Traverse the tree, creating nodes as needed, and mark the final node as an end-of-word.
4. For `search`: Traverse the tree following the word's characters. Return true only if we reach the end and the final node is marked as end-of-word.
5. For `startsWith`: Similar to search, but return true if we can traverse the entire prefix, regardless of whether it's a complete word.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example operations:
- `insert("apple")`
- `search("apple")` → returns true
- `search("app")` → returns false
- `startsWith("app")` → returns true
- `insert("app")`
- `search("app")` → returns true

We initialize:
- A root `TrieNode` with empty children dictionary
- `is_end = False` for all nodes initially

**2.2 Start Inserting:**

We begin by inserting "apple".

**2.3 Trace Walkthrough:**

**Insert "apple":**

| Step | Current Node | Character | Action | New Node Created? |
|------|--------------|-----------|--------|-------------------|
| 1 | root | 'a' | Create node for 'a' | Yes |
| 2 | a-node | 'p' | Create node for 'p' | Yes |
| 3 | p-node | 'p' | Create node for 'p' | Yes |
| 4 | p-node | 'l' | Create node for 'l' | Yes |
| 5 | l-node | 'e' | Create node for 'e', mark as end | Yes |

**Search "apple":**

| Step | Current Node | Character | Found? | Action |
|------|--------------|-----------|--------|--------|
| 1 | root | 'a' | Yes | Move to 'a' node |
| 2 | a-node | 'p' | Yes | Move to 'p' node |
| 3 | p-node | 'p' | Yes | Move to 'p' node |
| 4 | p-node | 'l' | Yes | Move to 'l' node |
| 5 | l-node | 'e' | Yes | Check is_end → true → Return true |

**Search "app":**

| Step | Current Node | Character | Found? | Action |
|------|--------------|-----------|--------|--------|
| 1 | root | 'a' | Yes | Move to 'a' node |
| 2 | a-node | 'p' | Yes | Move to 'p' node |
| 3 | p-node | 'p' | Yes | Check is_end → false → Return false |

**startsWith "app":**

| Step | Current Node | Character | Found? | Action |
|------|--------------|-----------|--------|--------|
| 1 | root | 'a' | Yes | Move to 'a' node |
| 2 | a-node | 'p' | Yes | Move to 'p' node |
| 3 | p-node | 'p' | Yes | All characters found → Return true |

**2.4 Insert "app" and Search Again:**

After inserting "app", the second 'p' node now has `is_end = true`. So searching "app" will now return true.

**2.5 Return Result:**

The Trie correctly handles all operations, allowing efficient word storage and prefix matching.

> **Note:** The key difference between `search` and `startsWith` is that `search` requires the final node to be marked as an end-of-word, while `startsWith` only requires that the path exists.

### Solution

```python
def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

## 211. Design Add and Search Words Data Structure [Medium]
https://leetcode.com/problems/design-add-and-search-words-data-structure/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Word length is 1 to 25, and there are at most 10^4 calls to `addWord` and `search`. Search queries have at most 2 dots.
- **Time Complexity:** 
  - `addWord`: O(m) where m is the word length
  - `search`: O(m * 26^k) in worst case where k is the number of dots, but typically much better
- **Space Complexity:** O(N * M) where N is the number of words and M is the average word length.
- **Edge Case:** Searching for a word with no dots is O(m) time, same as a regular trie search.

**1.2 High-level approach:**
The goal is to design a data structure that supports adding words and searching with wildcard characters (dots). A trie (prefix tree) is perfect for this, with special handling for dots during search.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Store words in a list. For search with dots, check each word character by character. This is O(N * M) per search.
- **Optimized Strategy:** Use a trie to store words. For dots, recursively search all possible children. This is much more efficient for prefix matching.
- **Why optimized is better:** Trie allows early termination when prefixes don't match and efficiently handles wildcard searches.

**1.4 Decomposition:**
1. Build a trie data structure with nodes containing children and an `is_end` flag.
2. For `addWord`, traverse the trie, creating nodes as needed, and mark the end.
3. For `search`, use DFS to handle dots by recursively searching all children when encountering a dot.
4. Return true if we find a complete word matching the pattern.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Initialize: `root = TrieNode()`

Add words: "bad", "dad", "mad"

**2.2 Start Checking:**
Search for: ".ad"

**2.3 Trace Walkthrough:**

| Step | Current Node | Char | Action |
|------|---------------|------|--------|
| 0 | root | '.' | Check all children (b, d, m) |
| 1 | node['b'] | 'a' | Check if 'a' in children |
| 2 | node['b']['a'] | 'd' | Check if 'd' in children and is_end |
| 3 | - | - | Found "bad", return True |

For ".ad", we check all first-level children (b, d, m), then continue with 'a' and 'd'.

**2.4 Increment and Loop:**
For each character in the search word:
- If it's a dot, recursively search all children
- If it's a regular character, follow that child if it exists
- If we reach the end and `is_end` is true, return true

**2.5 Return Result:**
The search ".ad" matches "bad", "dad", or "mad", so return `True`.

### Solution

```python
def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end
            
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)
```

## 212. Word Search II [Hard]
https://leetcode.com/problems/word-search-ii/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Board size is up to 12x12, word length is 1 to 10, and there are up to 3*10^4 words.
- **Time Complexity:** O(M * N * 4^L) where M and N are board dimensions and L is the maximum word length. With trie optimization, we can prune early.
- **Space Complexity:** O(AL) where A is the alphabet size and L is the total length of all words for the trie, plus O(L) for recursion stack.
- **Edge Case:** If no words can be formed, return an empty list.

**1.2 High-level approach:**
The goal is to find all words from a list that can be formed on the board by moving to adjacent cells. We use a trie to store words and backtracking to explore the board.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each word, use DFS to search the board. This is O(W * M * N * 4^L) where W is the number of words.
- **Optimized Strategy:** Build a trie from all words, then use backtracking with the trie to search all words simultaneously. Prune branches when the current path doesn't match any word prefix.
- **Why optimized is better:** The trie allows us to search all words in parallel and prune early when no words match the current path.

**1.4 Decomposition:**
1. Build a trie from all words, storing the complete word at the end node.
2. For each cell on the board, start DFS if the cell's character matches a trie root child.
3. During DFS, mark the cell as visited, check if we found a word, explore neighbors, and restore the cell.
4. Prune the trie by removing nodes with no children after processing.
5. Collect all found words and return them.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Board: `[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`
Words: `["oath","pea","eat","rain"]`

Build trie with all words.

**2.2 Start Checking:**
Start DFS from each cell that matches a trie root child.

**2.3 Trace Walkthrough:**

Starting from (0,0) with 'o':
- 'o' matches trie root child
- Mark (0,0) as '#'
- Explore neighbors: (0,1)='a', (1,0)='e'
- From (0,1): 'a' matches, continue to 't', then 'h'
- Found "oath", add to result
- Continue exploring...

**2.4 Increment and Loop:**
For each cell (i, j):
- If board[i][j] matches a trie child, start DFS
- During DFS: mark visited, check for word, explore neighbors, restore cell
- Prune trie nodes with no children

**2.5 Return Result:**
After processing all cells, `res = ["eat","oath"]`. Return this list.

### Solution

```python
def __init__(self):
        self.children = {}
        self.word = None

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        
        res = []
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, node):
            char = board[row][col]
            curr_node = node.children[char]
            
            # Check if we found a word
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # Avoid duplicates
            
            # Mark as visited
            board[row][col] = '#'
            
            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    board[new_row][new_col] in curr_node.children):
                    dfs(new_row, new_col, curr_node)
            
            # Restore character
            board[row][col] = char
            
            # Prune if node has no children
            if not curr_node.children:
                node.children.pop(char)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i, j, root)
        
        return res
```

## 222. Count Complete Tree Nodes [Easy]
https://leetcode.com/problems/count-complete-tree-nodes/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The tree has 0 to 5*10^4 nodes and is guaranteed to be complete.
- **Time Complexity:** O(log² n) - We do O(log n) work at each level, and there are O(log n) levels.
- **Space Complexity:** O(log n) for the recursion stack.
- **Edge Case:** If the root is None, return 0.

**1.2 High-level approach:**
The goal is to count nodes in a complete binary tree efficiently. We use the property that in a complete tree, we can check if subtrees are full by comparing left and right heights.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Recursively count all nodes: O(n) time.
- **Optimized Strategy:** Use the complete tree property. If left and right heights are equal, the left subtree is full. Otherwise, the right subtree is full. This allows us to skip counting full subtrees.
- **Why optimized is better:** We avoid counting nodes in full subtrees, reducing time complexity to O(log² n).

**1.4 Decomposition:**
1. Calculate the height of the left subtree by following left children.
2. Calculate the height of the right subtree by following left children from the right child.
3. If heights are equal, the left subtree is full (2^height - 1 nodes), so recursively count the right subtree.
4. If heights differ, the right subtree is full, so recursively count the left subtree.
5. Add 1 for the root and the full subtree size.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Example tree: `[1,2,3,4,5,6]` (complete binary tree with 6 nodes)

Root = 1, left = 2, right = 3

**2.2 Start Checking:**
Calculate left height from root.left (node 2): follow left children → 4 → None, height = 2
Calculate right height from root.right (node 3): follow left children → None, height = 0

**2.3 Trace Walkthrough:**

| Node | Left Height | Right Height | Action |
|------|-------------|---------------|--------|
| 1 | 2 | 0 | Heights differ, right is full. Count = 2^0 + countNodes(left) |
| 2 | 1 | 0 | Heights differ, right is full. Count = 2^0 + countNodes(left) |
| 4 | 0 | 0 | Heights equal, left is full. Count = 2^0 + countNodes(right) |
| 5 | 0 | 0 | Base case, return 1 |

**2.4 Increment and Loop:**
Recursively:
- If left_height == right_height: return (1 << left_height) + countNodes(right)
- Else: return (1 << right_height) + countNodes(left)

**2.5 Return Result:**
Total count = 1 (root) + 1 (node 2) + 1 (node 4) + 1 (node 5) + 1 (node 3) + 1 (node 6) = 6 nodes.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Get left and right heights
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        if left_height == right_height:
            # Left subtree is full, right subtree may not be
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is full, left subtree may not be
            return (1 << right_height) + self.countNodes(root.left)
    
    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
```

## 226. Invert Binary Tree [Easy]
https://leetcode.com/problems/invert-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The tree has 0 to 100 nodes, and node values range from -100 to 100.
- **Time Complexity:** O(n) where n is the number of nodes. We visit each node once.
- **Space Complexity:** O(h) where h is the height of the tree for the recursion stack. In worst case (skewed tree), this is O(n).
- **Edge Case:** If the root is None, return None.

**1.2 High-level approach:**
The goal is to invert a binary tree by swapping left and right children at every node. We use recursion to process each node.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same recursive approach - there's no significantly different brute force method for this problem.
- **Optimized Strategy:** Use recursion to swap children at each node, then recursively invert the subtrees.
- **Why optimized is better:** This is the natural and most efficient approach for tree problems.

**1.4 Decomposition:**
1. If the node is None, return None (base case).
2. Swap the left and right children of the current node.
3. Recursively invert the left subtree.
4. Recursively invert the right subtree.
5. Return the root.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Example tree: `[4,2,7,1,3,6,9]`

```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

**2.2 Start Checking:**
Start from the root and recursively process each node.

**2.3 Trace Walkthrough:**

| Node | Before Swap | After Swap | Left Child | Right Child |
|------|------------|------------|------------|--------------|
| 4 | left=2, right=7 | left=7, right=2 | Invert 7 | Invert 2 |
| 7 | left=6, right=9 | left=9, right=6 | Invert 9 | Invert 6 |
| 2 | left=1, right=3 | left=3, right=1 | Invert 3 | Invert 1 |

**2.4 Increment and Loop:**
For each node:
- Swap: `root.left, root.right = root.right, root.left`
- Recursively invert: `self.invertTree(root.left)`, `self.invertTree(root.right)`

**2.5 Return Result:**
After inversion:
```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

Return the root node.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

## 228. Summary Ranges [Easy]
https://leetcode.com/problems/summary-ranges/

### Explanation

## 228. Summary Ranges [Easy]

https://leetcode.com/problems/summary-ranges

## Description
You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Examples**

```tex
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

**Constraints**
```tex
- 0 <= nums.length <= 20
- -2^31 <= nums[i] <= 2^31 - 1
- All the values of nums are unique
- nums is sorted in ascending order
```

## Explanation

### Strategy
Let's restate the problem: You're given a sorted array of unique integers, and you need to create a summary of consecutive ranges. The goal is to represent consecutive sequences as ranges (e.g., "0->2") and single numbers as themselves (e.g., "7").

This is an **array traversal problem** that requires identifying consecutive sequences and formatting them appropriately.

**What is given?** A sorted array of unique integers (up to 20 elements).

**What is being asked?** Create a list of ranges that cover all numbers exactly, representing consecutive sequences as ranges and single numbers as themselves.

**Constraints:** The array is small (up to 20 elements), sorted, and contains unique values.

**Edge cases:** 
- Empty array
- Single element array
- Array with no consecutive sequences
- Array with all consecutive sequences

**High-level approach:**
The solution involves traversing the array and identifying consecutive sequences. When we find a break in the sequence, we format the range appropriately and continue.

**Decomposition:**
1. **Handle edge cases**: Empty array returns empty list
2. **Initialize variables**: Track start of current range and result list
3. **Traverse array**: Look for consecutive sequences
4. **Format ranges**: Convert consecutive sequences to appropriate string format
5. **Handle final range**: Don't forget the last range when loop ends

**Brute force vs. optimized strategy:**
- **Brute force**: Check each possible range combination. This is inefficient.
- **Optimized**: Single pass through the array, identifying consecutive sequences as we go. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `nums = [0,1,2,4,5,7]`

**Step 1: Handle edge case**
- Array is not empty, continue

**Step 2: Initialize variables**
- `start = 0` (start of current range)
- `result = []` (list to store ranges)

**Step 3: Traverse array looking for consecutive sequences**
- `i = 0`: `nums[0] = 0`
  - Start new range: `start = 0`
- `i = 1`: `nums[1] = 1`
  - Check if consecutive: `1 == 0 + 1` ✓
  - Continue current range
- `i = 2`: `nums[2] = 2`
  - Check if consecutive: `2 == 1 + 1` ✓
  - Continue current range
- `i = 3`: `nums[3] = 4`
  - Check if consecutive: `4 == 2 + 1` ✗
  - Break in sequence! Format range [0,2] as "0->2"
  - Add to result: `result = ["0->2"]`
  - Start new range: `start = 3`
- `i = 4`: `nums[4] = 5`
  - Check if consecutive: `5 == 4 + 1` ✓
  - Continue current range
- `i = 5`: `nums[5] = 7`
  - Check if consecutive: `7 == 5 + 1` ✗
  - Break in sequence! Format range [4,5] as "4->5"
  - Add to result: `result = ["0->2", "4->5"]`
  - Start new range: `start = 5`

**Step 4: Handle final range**
- Loop ended, need to handle the last range [7,7]
- Since start == end (7 == 7), format as "7"
- Add to result: `result = ["0->2", "4->5", "7"]`

**Step 5: Return result**
- Final result: `["0->2","4->5","7"]`

**Why this works:**
By traversing the array once and checking for consecutive numbers, we can identify ranges efficiently. The key insights are:
1. A break in the sequence occurs when `nums[i] != nums[i-1] + 1`
2. Single numbers (where start == end) are formatted as "a"
3. Ranges (where start != end) are formatted as "a->b"

> **Note:** The key insight is identifying consecutive sequences by checking if each number is exactly one more than the previous number. This allows us to build ranges efficiently in a single pass.

**Time Complexity:** O(n) - we visit each element once  
**Space Complexity:** O(n) - we need to store the result list

### Solution

```python
def summaryRanges(nums):
    """
    Create a summary of ranges from a sorted array of unique integers.
    
    Args:
        nums: List[int] - Sorted array of unique integers
        
    Returns:
        List[str] - List of range strings
    """
    # Handle edge case
    if not nums:
        return []
    
    result = []
    start = 0
    
    # Traverse array looking for consecutive sequences
    for i in range(1, len(nums)):
        # Check if current number is consecutive to previous
        if nums[i] != nums[i-1] + 1:
            # Break in sequence, format the range
            if start == i - 1:
                # Single number
                result.append(str(nums[start]))
            else:
                # Range of numbers
                result.append(f"{nums[start]}->{nums[i-1]}")
            
            # Start new range
            start = i
    
    # Handle the final range
    if start == len(nums) - 1:
        # Single number
        result.append(str(nums[start]))
    else:
        # Range of numbers
        result.append(f"{nums[start]}->{nums[-1]}")
    
    return result
```

## 230. Kth Smallest Element in a BST [Medium]
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary search tree (BST) and an integer $k$, we need to find the $k$-th smallest element in the BST.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the BST can be up to $10^4$.
- **Value Range:** Node values are between $1$ and $10^4$.
- **Time Complexity:** $O(n)$ - We traverse all nodes in the BST using in-order traversal, which visits each node exactly once.
- **Space Complexity:** $O(n)$ - In the worst case (a skewed tree), the recursion stack can be $O(n)$ deep. Additionally, we store all node values in a list, which requires $O(n)$ space.
- **Edge Case:** If $k$ is 1, we return the smallest element. If $k$ equals the number of nodes, we return the largest element.

**1.2 High-level approach:**

The goal is to find the $k$-th smallest element in a BST.

![BST In-order Traversal](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

A key property of a BST is that an in-order traversal (left → root → right) visits nodes in ascending order. Therefore, the $k$-th element visited during an in-order traversal is the $k$-th smallest element.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Perform an in-order traversal to collect all node values in a list, then return the element at index $k-1$. This approach is straightforward and works correctly.
- **Optimized Strategy:** We can optimize by stopping the traversal once we've found the $k$-th element, using an iterative approach or early termination in recursion. However, for clarity and beginner-friendliness, we'll use the complete traversal approach.
- **Why it's better:** The brute force approach is actually quite efficient for this problem. A more optimized version would use iterative in-order traversal with early termination, but the complete traversal approach is easier to understand.

**1.4 Decomposition:**

1. Perform an in-order traversal of the BST (visit left subtree, then root, then right subtree).
2. Collect all node values in a list during the traversal.
3. Since in-order traversal of a BST produces values in sorted order, the list will be sorted.
4. Return the element at index $k-1$ (since $k$ is 1-indexed).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[3, 1, 4, null, 2]$, $k = 1$

The BST structure:
```
    3
   / \
  1   4
   \
    2
```

We initialize:
- An empty list `res = []` to store node values
- We'll perform in-order traversal starting from the root

**2.2 Start Traversing:**

We begin the in-order traversal from the root node (value 3).

**2.3 Trace Walkthrough:**

The in-order traversal visits nodes in this order:

| Step | Current Node | Action | List State |
|------|--------------|--------|------------|
| 1 | 3 (root) | Go to left child (1) | [] |
| 2 | 1 | Go to left child (null) | [] |
| 3 | null | Return (base case) | [] |
| 4 | 1 | Add 1 to list | [1] |
| 5 | 1 | Go to right child (2) | [1] |
| 6 | 2 | Go to left child (null) | [1] |
| 7 | null | Return (base case) | [1] |
| 8 | 2 | Add 2 to list | [1, 2] |
| 9 | 2 | Go to right child (null) | [1, 2] |
| 10 | null | Return (base case) | [1, 2] |
| 11 | 3 | Add 3 to list | [1, 2, 3] |
| 12 | 3 | Go to right child (4) | [1, 2, 3] |
| 13 | 4 | Go to left child (null) | [1, 2, 3] |
| 14 | null | Return (base case) | [1, 2, 3] |
| 15 | 4 | Add 4 to list | [1, 2, 3, 4] |
| 16 | 4 | Go to right child (null) | [1, 2, 3, 4] |
| 17 | null | Return (base case) | [1, 2, 3, 4] |

After traversal: `res = [1, 2, 3, 4]`

**2.4 Return Result:**

Since $k = 1$ (1-indexed), we return `res[0] = 1`, which is the 1st smallest element.

For $k = 3$, we would return `res[2] = 3`, which is the 3rd smallest element.

> **Note:** In-order traversal of a BST always produces values in ascending order because of the BST property: all values in the left subtree are less than the root, and all values in the right subtree are greater than the root.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        # In-order traversal to get elements in sorted order
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Return the k-th smallest element (1-indexed)
        return res[k - 1]
```

## 234. Palindrome Linked List [Easy]
https://leetcode.com/problems/palindrome-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to determine if a singly linked list is a palindrome (reads the same forwards and backwards).

**1.1 Constraints & Complexity:**

- **Input Constraints:** The list has $1 \leq n \leq 10^5$ nodes, with values in $[0, 9]$.
- **Time Complexity:** $O(n)$ - We traverse the list once to collect values, then compare them.
- **Space Complexity:** $O(n)$ - We store all node values in an array for comparison.
- **Edge Case:** A single-node list is always a palindrome.

**1.2 High-level approach:**

The goal is to check if the linked list values form a palindrome. We convert the list to an array, then use two pointers to compare values from both ends.

![Palindrome Linked List](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Reverse the entire list, then compare with original. This requires $O(n)$ time and $O(n)$ space for the reversed list.
- **Optimized (Array Conversion):** Convert list to array, then use two pointers. This takes $O(n)$ time and $O(n)$ space.
- **Emphasize the optimization:** While both approaches have similar complexity, the array approach is simpler and more intuitive. For $O(1)$ space, we could reverse half the list, but that's more complex.

**1.4 Decomposition:**

1. **Convert to Array:** Traverse the list and store all values in an array.
2. **Two-Pointer Comparison:** Use left and right pointers to compare values from both ends.
3. **Check Match:** If any pair doesn't match, return `False`. If all pairs match, return `True`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `head = [1,2,2,1]`.

After conversion: `values = [1, 2, 2, 1]`

**2.2 Start Checking:**

Initialize `left = 0` and `right = len(values) - 1 = 3`.

**2.3 Trace Walkthrough:**

| Step | left | right | values[left] | values[right] | Match? | Action |
|------|------|-------|--------------|----------------|--------|--------|
| 1 | 0 | 3 | 1 | 1 | Yes | Continue |
| 2 | 1 | 2 | 2 | 2 | Yes | Continue |
| 3 | 2 | 1 | - | - | - | Stop (left >= right) |

**2.4 Complete Comparison:**

All pairs matched: (1,1) and (2,2).

**2.5 Return Result:**

Since all comparisons passed, the function returns `True`.

> **Note:** The two-pointer technique efficiently checks palindromes by comparing symmetric positions without needing to reverse the list.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Convert linked list to array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Check if array is palindrome
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        
        return True
```

## 235. Lowest Common Ancestor of a Binary Search Tree [Medium]
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. The LCA is the lowest node that has both nodes as descendants.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the BST can be between $2$ and $10^5$.
- **Value Range:** All node values are unique and between $-10^9$ and $10^9$.
- **Time Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Space Complexity:** $O(h)$ - The recursion stack can be as deep as the height of the tree. In the worst case, this is $O(n)$, and in the average case, this is $O(\log n)$.
- **Edge Case:** Both nodes are guaranteed to exist in the BST. The LCA could be one of the nodes itself (if one is an ancestor of the other).

**1.2 High-level approach:**

The goal is to find the lowest common ancestor of two nodes in a BST.

![BST LCA](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

We leverage the BST property: if both nodes are less than the current root, the LCA is in the left subtree. If both are greater, the LCA is in the right subtree. Otherwise, the current root is the LCA.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find paths from root to both nodes, then find the last common node in both paths. This requires storing paths and comparing them.
- **Optimized Strategy (BST Property):** Use the BST property to navigate directly. If both nodes are on the same side of the root, recurse on that side. Otherwise, the root is the LCA.
- **Why it's better:** The BST property allows us to eliminate half of the tree at each step, making this much more efficient than a general binary tree LCA algorithm.

**1.4 Decomposition:**

1. Compare the values of both nodes with the current root.
2. If both nodes are less than the root, the LCA is in the left subtree - recurse left.
3. If both nodes are greater than the root, the LCA is in the right subtree - recurse right.
4. Otherwise (one is less and one is greater, or one equals the root), the current root is the LCA.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[6,2,8,0,4,7,9,null,null,3,5]$, $p = 2$, $q = 8$

The BST structure:
```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```

**2.2 Start Checking:**

We begin at the root node (value 6).

**2.3 Trace Walkthrough:**

| Step | Current Root | p | q | Comparison | Action |
|------|--------------|---|---|------------|--------|
| 1 | 6 | 2 | 8 | $2 < 6$ and $8 > 6$ | Root (6) is LCA |

Since $p = 2 < 6$ and $q = 8 > 6$, they are on opposite sides of the root. Therefore, the root (6) is the LCA.

**2.4 Another Example:**

If $p = 2$ and $q = 4$:
- Step 1: Root = 6, both $2 < 6$ and $4 < 6$, so recurse left
- Step 2: Root = 2, $2 == 2$ and $4 > 2$, so root (2) is LCA

**2.5 Return Result:**

We return the root node (6), which is the LCA.

> **Note:** The BST property makes this problem much simpler than finding LCA in a general binary tree. We don't need to search both subtrees - we can always determine which direction to go.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # If both p and q are less than root, LCA is in left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both p and q are greater than root, LCA is in right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Otherwise, root is the LCA
        return root
```

## 236. Lowest Common Ancestor of a Binary Tree [Medium]
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to find the lowest common ancestor (LCA) of two nodes in a binary tree. The LCA is the deepest node that has both nodes as descendants (a node can be a descendant of itself).

**1.1 Constraints & Complexity:**

- **Input Constraints:** The tree has $2 \leq n \leq 10^5$ nodes with unique values in $[-10^9, 10^9]$.
- **Time Complexity:** $O(n)$ - We may need to visit all nodes in the worst case.
- **Space Complexity:** $O(h)$ - The recursion stack depth is at most the height $h$ of the tree. In worst case (skewed tree), $h = n$.
- **Edge Case:** If one node is an ancestor of the other, return that ancestor node.

**1.2 High-level approach:**

The goal is to find the deepest node that is an ancestor of both target nodes. We use recursive DFS: if we find both nodes in a subtree, the current root is the LCA.

![Binary Tree LCA](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Find paths to both nodes, then find the last common node in both paths. This requires storing paths and takes $O(n)$ time and $O(n)$ space.
- **Optimized (Recursive DFS):** Recursively search both subtrees. If both subtrees return non-null, the current root is the LCA. This takes $O(n)$ time and $O(h)$ space.
- **Emphasize the optimization:** The recursive approach finds the LCA in a single pass without storing paths, making it more space-efficient.

**1.4 Decomposition:**

1. **Base Case:** If root is `None` or equals `p` or `q`, return root.
2. **Recursive Search:** Recursively search left and right subtrees for `p` and `q`.
3. **Combine Results:** If both subtrees return non-null, root is the LCA. Otherwise, return whichever subtree found a node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 1`.

**2.2 Start Searching:**

Begin at root node `3`.

**2.3 Trace Walkthrough:**

| Node | Left Result | Right Result | Action |
|------|-------------|--------------|---------|
| 3 | Search left (5) | Search right (1) | Both found → Return 3 |
| 5 | Search left (6) | Search right (2) | Found p → Return 5 |
| 1 | Search left (0) | Search right (8) | Found q → Return 1 |

**2.4 Recursive Unwinding:**

- Node `5` returns itself (found `p`).
- Node `1` returns itself (found `q`).
- Node `3` receives both results, so it's the LCA.

**2.5 Return Result:**

The function returns node `3`, which is the LCA of nodes `5` and `1`.

> **Note:** The key insight is that if both left and right subtrees return non-null, the current root must be the LCA. If only one subtree returns non-null, that subtree contains the LCA.

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or root is p or q, return root
        if not root or root == p or root == q:
            return root
        
        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return non-None, root is the LCA
        if left and right:
            return root
        
        # Otherwise, return whichever side found p or q
        return left if left else right
```

## 242. Valid Anagram [Easy]
https://leetcode.com/problems/valid-anagram/

### Explanation

Given two strings `s` and `t`, return `true` if `t` is an [anagram](https://en.wikipedia.org/wiki/Anagram) of `s`, and `false` otherwise.

**Examples**

```tex
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
```

**Constraints**
```tex
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters
```

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Explanation

### Strategy
Let's restate the problem: You're given two strings, and you need to determine if one is an anagram of the other. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

This is a **character counting problem** that can be solved using hash tables to track the frequency of each character in both strings.

**What is given?** Two strings `s` and `t` of potentially different lengths.

**What is being asked?** Determine if `t` is an anagram of `s`.

**Constraints:** The strings can be up to 50,000 characters long and contain only lowercase English letters.

**Edge cases:** 
- Strings of different lengths
- Empty strings
- Strings with repeated characters
- Strings with all identical characters

**High-level approach:**
The solution involves counting the frequency of each character in both strings and comparing them. If the character counts match exactly, the strings are anagrams.

**Decomposition:**
1. **Check length equality**: If strings have different lengths, they can't be anagrams
2. **Count characters in first string**: Use a hash table to track character frequencies
3. **Decrement counts for second string**: For each character in the second string, decrement its count
4. **Verify all counts are zero**: If any count is not zero, the strings are not anagrams

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible permutations of one string. This takes O(n!) time.
- **Optimized**: Use character counting with hash tables. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `s = "anagram"`, `t = "nagaram"`

**Step 1: Check string lengths**
- `s.length = 7`, `t.length = 7`
- Lengths match ✓

**Step 2: Initialize character count dictionary**
- `char_count = {}`

**Step 3: Count characters in first string (s)**
- `s = "anagram"`
- `char_count['a'] = 3` (appears 3 times)
- `char_count['n'] = 1` (appears 1 time)
- `char_count['g'] = 1` (appears 1 time)
- `char_count['r'] = 1` (appears 1 time)
- `char_count['m'] = 1` (appears 1 time)

**Step 4: Decrement counts for second string (t)**
- `t = "nagaram"`
- `t[0] = 'n'`: `char_count['n'] = 1 - 1 = 0`
- `t[1] = 'a'`: `char_count['a'] = 3 - 1 = 2`
- `t[2] = 'g'`: `char_count['g'] = 1 - 1 = 0`
- `t[3] = 'a'`: `char_count['a'] = 2 - 1 = 1`
- `t[4] = 'r'`: `char_count['r'] = 1 - 1 = 0`
- `t[5] = 'a'`: `char_count['a'] = 1 - 1 = 0`
- `t[6] = 'm'`: `char_count['m'] = 1 - 1 = 0`

**Step 5: Verify all counts are zero**
- All character counts are now 0
- The strings are anagrams: `true`

**Why this works:**
By counting characters in the first string and then decrementing for the second string, we ensure that:
1. Both strings contain the same characters
2. Each character appears the same number of times in both strings
3. The final count of 0 for all characters confirms the anagram property

> **Note:** The key insight is using character frequency counting to verify that both strings contain exactly the same characters with the same frequencies. This is much more efficient than trying to find permutations.

**Time Complexity:** O(n) - we visit each character once in each string  
**Space Complexity:** O(k) - where k is the number of unique characters (bounded by the character set size)

### Solution

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        
        char_count[char] -= 1
        
        # If count becomes negative, strings are not anagrams
        if char_count[char] < 0:
            return False
    
    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return False
    
    return True
```

## 274. H-Index [Medium]
https://leetcode.com/problems/h-index/

### Explanation

## 274. H-Index [Medium]

https://leetcode.com/problems/h-index

## Description
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `iᵗʰ` paper, return *the researcher's h-index*.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

**Examples**

```tex
Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
```

**Constraints**
```tex
- n == citations.length
- 1 <= n <= 5000
- 0 <= citations[i] <= 1000
```

## Explanation

### Strategy
Let's restate the problem: You're given an array representing the number of citations for each paper a researcher has published. You need to find the maximum value `h` such that the researcher has at least `h` papers with at least `h` citations each.

This is a **sorting problem** that requires understanding the definition of h-index and finding the optimal value efficiently.

**What is given?** An array of integers representing citation counts for each paper.

**What is being asked?** Find the maximum h-index value that satisfies the h-index definition.

**Constraints:** The array can be up to 5000 elements long, with citation counts ranging from 0 to 1000.

**Edge cases:** 
- Array with all zeros
- Array with all high citation counts
- Array with single element
- Array with mixed citation counts

**High-level approach:**
The solution involves understanding the h-index definition and using sorting to efficiently find the maximum valid h value.

**Decomposition:**
1. **Sort the array**: Arrange citations in descending order to easily check h-index conditions
2. **Iterate through sorted array**: Check each position as a potential h-index
3. **Verify h-index condition**: Ensure at least h papers have at least h citations
4. **Return maximum valid h**: Find the largest h that satisfies the condition

**Brute force vs. optimized strategy:**
- **Brute force**: Try each possible h value and check if it satisfies the condition. This takes O(n²) time.
- **Optimized**: Sort the array and use a single pass to find the h-index. This takes O(n log n) time.

### Steps
Let's walk through the solution step by step using the first example: `citations = [3,0,6,1,5]`

**Step 1: Sort the array in descending order**
- Original: `[3,0,6,1,5]`
- Sorted: `[6,5,3,1,0]`

**Step 2: Check each position as potential h-index**
- Position 0: `h = 1`, check if `citations[0] >= 1` ✓ (6 >= 1)
- Position 1: `h = 2`, check if `citations[1] >= 2` ✓ (5 >= 2)
- Position 2: `h = 3`, check if `citations[2] >= 3` ✓ (3 >= 3)
- Position 3: `h = 4`, check if `citations[3] >= 4` ✗ (1 < 4)

**Step 3: Find the maximum valid h**
- The largest h where `citations[h-1] >= h` is 3
- At position 2 (0-indexed), we have `h = 3` and `citations[2] = 3 >= 3`

**Step 4: Verify the h-index condition**
- We need at least 3 papers with at least 3 citations
- Papers with ≥3 citations: 6, 5, 3 (3 papers) ✓
- Remaining papers: 1, 0 (≤3 citations) ✓
- H-index is 3

**Why this works:**
After sorting in descending order, the array position `i` (0-indexed) represents `h = i + 1`. For a position to be a valid h-index, we need `citations[i] >= h`. The largest valid h is our answer.

> **Note:** The key insight is that after sorting, we can directly check each position as a potential h-index. The sorting makes it easy to verify the h-index condition in a single pass.

**Time Complexity:** O(n log n) - dominated by sorting the array  
**Space Complexity:** O(1) - we only use a constant amount of extra space (excluding the sorted array if we modify the input)

### Solution

```python
def hIndex(citations):
    """
    Calculate the h-index for a researcher based on their paper citations.
    
    Args:
        citations: List[int] - Array of citation counts for each paper
        
    Returns:
        int - The researcher's h-index
    """
    # Handle edge cases
    if not citations:
        return 0
    
    # Sort citations in descending order
    citations.sort(reverse=True)
    
    # Check each position as a potential h-index
    for i in range(len(citations)):
        # h-index is i + 1 (1-indexed)
        h = i + 1
        
        # Check if citations[i] >= h
        # If not, we've found our answer
        if citations[i] < h:
            return i
        
        # If we reach the end, the h-index is the length of the array
        if i == len(citations) - 1:
            return h
    
    # This line should never be reached
    return 0
```

## 289. Game of Life [Medium]
https://leetcode.com/problems/game-of-life/

### Explanation

## 289. Game of Life [Medium]

https://leetcode.com/problems/game-of-life

## Description
According to [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: **live** (represented by a `1`) or **dead** (represented by a `0`). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the `m x n` grid `board`. In this process, births and deaths occur **simultaneously**.

Given the current state of the `board`, **update** the `board` to reflect its next state.

**Note** that you do not need to return anything.

**Examples**

```tex
Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```

**Constraints**
```tex
- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] is 0 or 1
```

**Follow up:**
- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

## Explanation

### Strategy
Let's restate the problem: You're given a 2D grid representing the current state of Conway's Game of Life, where each cell is either alive (1) or dead (0). You need to update the board to the next generation based on specific rules about cell survival and reproduction.

This is a **simulation problem** that requires careful handling to update all cells simultaneously without interfering with the calculation of other cells.

**What is given?** An m x n grid where each cell is either 0 (dead) or 1 (live).

**What is being asked?** Update the board to the next generation based on the Game of Life rules.

**Constraints:** The grid can be up to 25x25, and all cells contain only 0 or 1.

**Edge cases:** 
- Grid with all dead cells
- Grid with all live cells
- Single row or column
- Grid with live cells on borders

**High-level approach:**
The solution involves using a two-pass approach where we first mark cells with their next state using special values, then convert these markers to the final states.

**Decomposition:**
1. **First pass**: Mark cells with their next state using special values (2 for live→dead, 3 for dead→live)
2. **Second pass**: Convert special values to final states (2→0, 3→1)
3. **Count neighbors**: For each cell, count its eight neighbors to determine its fate

**Brute force vs. optimized strategy:**
- **Brute force**: Create a copy of the board and update it. This takes O(mn) space.
- **Optimized**: Use special values to mark next states in-place. This takes O(1) space.

### Steps
Let's walk through the solution step by step using the first example: `board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]`

**Step 1: First pass - mark cells with next state**
- For each cell, count its eight neighbors
- Apply Game of Life rules and mark with special values:
  - `2` = currently live, will die (live→dead)
  - `3` = currently dead, will live (dead→live)
  - `0` = currently dead, will stay dead
  - `1` = currently live, will stay live

**Step 2: Count neighbors for each cell**
- For cell `board[0][1] = 1` (live):
  - Neighbors: `[0,0,1,0,0,1,1,1]` = 4 live neighbors
  - Rule 3: More than 3 live neighbors → dies
  - Mark as `2` (live→dead)

- For cell `board[1][2] = 1` (live):
  - Neighbors: `[1,0,1,1,1,0,0,0]` = 4 live neighbors
  - Rule 3: More than 3 live neighbors → dies
  - Mark as `2` (live→dead)

**Step 3: Second pass - convert special values**
- Convert `2` → `0` (dead)
- Convert `3` → `1` (live)
- Final board: `[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]`

**Why this works:**
By using special values (2 and 3) to mark the next state, we can update the board in-place without losing information about the current state. The two-pass approach ensures all cells are updated simultaneously as required.

> **Note:** The key insight is using special values to represent both current and next states, allowing us to solve the problem in-place while maintaining the requirement that all cells update simultaneously.

**Time Complexity:** O(mn) - we visit each cell twice  
**Space Complexity:** O(1) - we only use a constant amount of extra space

### Solution

```python
def gameOfLife(board):
    """
    Update the board to the next generation of Conway's Game of Life.
    This is done in-place using O(1) space.
    
    Args:
        board: List[List[int]] - The board to update in-place
        
    Returns:
        None - Modifies the board in-place
    """
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    
    # First pass: mark cells with their next state using special values
    # 2 = currently live, will die (live→dead)
    # 3 = currently dead, will live (dead→live)
    for i in range(m):
        for j in range(n):
            live_neighbors = countLiveNeighbors(board, i, j, m, n)
            
            if board[i][j] == 1:  # Currently live
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 2  # Mark as live→dead
            else:  # Currently dead
                if live_neighbors == 3:
                    board[i][j] = 3  # Mark as dead→live
    
    # Second pass: convert special values to final states
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0  # Convert live→dead to dead
            elif board[i][j] == 3:
                board[i][j] = 1  # Convert dead→live to live
```

## 290. Word Pattern [Easy]
https://leetcode.com/problems/word-pattern/

### Explanation

## 290. Word Pattern [Easy]

https://leetcode.com/problems/word-pattern

## Description
Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`. Specifically:

- Each letter in `pattern` maps to **exactly** one unique word in `s`.
- Each unique word in `s` maps to **exactly** one letter in `pattern`.
- No two letters map to the same word, and no two words map to the same letter.

**Examples**

```tex
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
- 'a' maps to "dog".
- 'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Constraints**
```tex
- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '
- s does not contain any leading or trailing spaces
- All the words in s are separated by a single space
```

## Explanation

### Strategy
Let's restate the problem: You're given a pattern string (like "abba") and a string of words (like "dog cat cat dog"), and you need to determine if the words follow the same pattern. This means there should be a one-to-one mapping between letters in the pattern and words in the string.

This is a **hash table problem** that requires tracking bidirectional mappings between pattern characters and words, similar to the isomorphic strings problem but with words instead of individual characters.

**What is given?** A pattern string and a string of space-separated words.

**What is being asked?** Determine if the words follow the same pattern as the given pattern string.

**Constraints:** The pattern can be up to 300 characters, and the string can be up to 3000 characters with words separated by single spaces.

**Edge cases:** 
- Pattern and words have different lengths
- Empty pattern or empty string
- Pattern with repeated characters
- String with repeated words

**High-level approach:**
The solution involves using two hash maps to track character-to-word and word-to-character mappings, ensuring that the bijection property is maintained.

**Decomposition:**
1. **Split the string into words**: Convert the space-separated string into a list of words
2. **Check length consistency**: If pattern length doesn't match word count, return false
3. **Create mapping dictionaries**: Track character-to-word and word-to-character mappings
4. **Verify bijection**: Ensure each character maps to exactly one word and vice versa

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible mappings. This is extremely inefficient.
- **Optimized**: Use hash tables to track mappings in a single pass. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `pattern = "abba"`, `s = "dog cat cat dog"`

**Step 1: Split the string into words**
- `s = "dog cat cat dog"`
- `words = ["dog", "cat", "cat", "dog"]`

**Step 2: Check length consistency**
- `pattern.length = 4`
- `words.length = 4`
- Lengths match ✓

**Step 3: Initialize mapping dictionaries**
- `char_to_word = {}` (maps pattern characters to words)
- `word_to_char = {}` (maps words to pattern characters)

**Step 4: Check first character-word pair**
- `pattern[0] = 'a'`, `words[0] = "dog"`
- Check if 'a' is already mapped: No
- Check if "dog" is already mapped: No
- Add mappings: `char_to_word['a'] = "dog"`, `word_to_char["dog"] = 'a'`

**Step 5: Check second character-word pair**
- `pattern[1] = 'b'`, `words[1] = "cat"`
- Check if 'b' is already mapped: No
- Check if "cat" is already mapped: No
- Add mappings: `char_to_word['b'] = "cat"`, `word_to_char["cat"] = 'b'`

**Step 6: Check third character-word pair**
- `pattern[2] = 'b'`, `words[2] = "cat"`
- Check if 'b' is already mapped: Yes, to "cat"
- Verify consistency: `char_to_word['b'] == "cat"` ✓
- Check if "cat" is already mapped: Yes, to 'b'
- Verify consistency: `word_to_char["cat"] == 'b'` ✓

**Step 7: Check fourth character-word pair**
- `pattern[3] = 'a'`, `words[3] = "dog"`
- Check if 'a' is already mapped: Yes, to "dog"
- Verify consistency: `char_to_word['a'] == "dog"` ✓
- Check if "dog" is already mapped: Yes, to 'a'
- Verify consistency: `word_to_char["dog"] == 'a'` ✓

**Step 8: Result**
- All character-word pairs are consistent
- Pattern is followed: `true`

**Why this works:**
By maintaining mappings in both directions, we ensure that:
1. Each character in the pattern maps to exactly one word
2. Each word maps to exactly one character
3. The bijection property is maintained throughout the pattern

> **Note:** The key insight is using bidirectional mapping to ensure the bijection property. This is similar to the isomorphic strings problem but operates on words instead of individual characters.

**Time Complexity:** O(n) - we visit each character/word once  
**Space Complexity:** O(k) - where k is the number of unique characters/words

### Solution

```python
def wordPattern(pattern, s):
    """
    Determine if the string s follows the given pattern.
    
    Args:
        pattern: str - The pattern string to match against
        s: str - The string of space-separated words
        
    Returns:
        bool - True if s follows the pattern, False otherwise
    """
    # Split the string into words
    words = s.split()
    
    # Check if pattern length matches word count
    if len(pattern) != len(words):
        return False
    
    # Create mapping dictionaries for both directions
    char_to_word = {}  # maps pattern characters to words
    word_to_char = {}  # maps words to pattern characters
    
    # Check each character-word pair
    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]
        
        # Check if char is already mapped
        if char in char_to_word:
            # Verify the mapping is consistent
            if char_to_word[char] != word:
                return False
        else:
            # Check if word is already mapped to by another character
            if word in word_to_char:
                return False
            
            # Add new mapping
            char_to_word[char] = word
            word_to_char[word] = char
    
    return True
```

## 295. Find Median from Data Stream [Hard]
https://leetcode.com/problems/find-median-from-data-stream/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Numbers range from -10^5 to 10^5, and there are at most 5*10^4 calls to `addNum` and `findMedian`.
- **Time Complexity:** 
  - `addNum`: O(log n) to insert into a heap
  - `findMedian`: O(1) to access heap tops
- **Space Complexity:** O(n) to store all numbers in the heaps.
- **Edge Case:** If only one number has been added, the median is that number.

**1.2 High-level approach:**
The goal is to efficiently find the median of a stream of numbers. We maintain two heaps: a max-heap for the smaller half and a min-heap for the larger half. The median is the top of the larger heap or the average of both tops.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Store all numbers in a list and sort to find median. This is O(n log n) per median query.
- **Optimized Strategy:** Use two heaps to maintain the two halves. Insertion is O(log n) and median query is O(1).
- **Why optimized is better:** Heaps allow efficient insertion and constant-time median access, much better than sorting.

**1.4 Decomposition:**
1. Maintain two heaps: `max_heap` (smaller half, use negative values) and `min_heap` (larger half).
2. For `addNum`, insert into the appropriate heap and balance if needed (difference should be at most 1).
3. For `findMedian`, if heaps are equal size, return average of both tops; otherwise, return the top of the larger heap.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Initialize: `max_heap = []`, `min_heap = []`

Add numbers: 1, 2, 3

**2.2 Start Checking:**
After each addition, balance the heaps to maintain the property that the size difference is at most 1.

**2.3 Trace Walkthrough:**

| Step | Number | max_heap | min_heap | Action |
|------|--------|----------|----------|--------|
| 0 | - | [] | [] | Initialize |
| 1 | 1 | [-1] | [] | Add to max_heap |
| 2 | 2 | [-1] | [2] | Add to min_heap, balanced |
| 3 | 3 | [-1] | [2,3] | Add to min_heap, balance: move 2 to max_heap |
| 4 | - | [-2,-1] | [3] | Balanced, find median |

**2.4 Increment and Loop:**
For each `addNum`:
- Insert into appropriate heap
- Balance if size difference > 1

**2.5 Return Result:**
After adding 1, 2, 3:
- `max_heap = [-2, -1]`, `min_heap = [3]`
- Median = (-(-2) + 3) / 2 = (2 + 3) / 2 = 2.5 (if equal sizes)
- Or median = -(-2) = 2 (if max_heap is larger)

### Solution

```python
def __init__(self):
        # max_heap for smaller half, min_heap for larger half
        self.max_heap = []  # Use negative values for max heap
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])
```

## 297. Serialize and Deserialize Binary Tree [Hard]
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

The problem asks us to design an algorithm to serialize a binary tree to a string and deserialize it back to the original tree structure.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $0 \leq n \leq 10^4$ nodes with values in $[-1000, 1000]$.
- **Time Complexity:** $O(n)$ - We visit each node once during both serialization and deserialization.
- **Space Complexity:** $O(n)$ - The serialized string and queue both require $O(n)$ space.
- **Edge Case:** Empty tree serializes to empty string and deserializes to `None`.

**1.2 High-level approach:**

The goal is to convert a tree to a string representation and reconstruct it. We use level-order (BFS) traversal to serialize, then use the same order to deserialize.

![Serialize Deserialize](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use preorder/inorder or postorder/inorder pairs. This requires two traversals and more complex deserialization.
- **Optimized (Level-Order BFS):** Use BFS to serialize level by level, including null nodes. Deserialize by processing nodes in the same order. This is straightforward and intuitive.
- **Emphasize the optimization:** Level-order serialization is easier to understand and implement, making it a practical choice despite similar complexity.

**1.4 Decomposition:**

1. **Serialize:** Use BFS to traverse tree level by level, adding node values (or "null") to result string.
2. **Deserialize:** Split string, use BFS to reconstruct tree level by level, creating nodes as we process the values.
3. **Handle Nulls:** Include null nodes in serialization to preserve tree structure.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `root = [1,2,3,null,null,4,5]`.

**2.2 Serialization:**

Start with queue containing root.

**2.3 Trace Walkthrough (Serialize):**

| Step | Queue | Process | Result So Far |
|------|-------|---------|---------------|
| 0 | [1] | 1 | "1" |
| 1 | [2, 3] | 2 | "1,2" |
| 2 | [3, null, null] | 3 | "1,2,3" |
| 3 | [null, null, 4, 5] | null | "1,2,3,null" |
| ... | ... | ... | "1,2,3,null,null,4,5" |

**2.4 Deserialization:**

Split string: `["1","2","3","null","null","4","5"]`

| Step | Queue | Value | Action | Tree State |
|------|-------|-------|--------|------------|
| 0 | [1] | "1" | Create root(1) | 1 |
| 1 | [2, 3] | "2" | Create left(2) | 1→2 |
| 2 | [3] | "3" | Create right(3) | 1→2,3 |
| 3 | [4, 5] | "null" | Skip | 1→2,3 |
| 4 | [5] | "null" | Skip | 1→2,3 |
| 5 | [] | "4" | Create left(4) | 1→2,3→4 |
| 6 | [] | "5" | Create right(5) | 1→2,3→4,5 |

**2.5 Return Result:**

Deserialization returns the original tree structure.

> **Note:** Level-order serialization preserves the tree structure naturally, making it easier to reconstruct than preorder/inorder approaches.

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        res = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root
```

## 328. Odd Even Linked List [Medium]
https://leetcode.com/problems/odd-even-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The linked list can have up to 10^4 nodes.
* **Time Complexity:** O(n) - We traverse the list once, where n is the number of nodes.
* **Space Complexity:** O(1) - We only use a constant amount of extra space for pointers.
* **Edge Case:** If the list has 0 or 1 node, return it as-is since there's nothing to reorder.

**1.2 High-level approach:**

The goal is to group all nodes at odd positions together, followed by all nodes at even positions, while maintaining their relative order within each group.

![Linked list showing odd nodes (1,3,5) followed by even nodes (2,4)]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Create two separate lists for odd and even nodes, then concatenate them. This requires O(n) extra space.
* **Optimized (In-place):** Use two pointers to separate odd and even nodes in-place by rewiring the next pointers. This uses O(1) extra space.
* **Why it's better:** The in-place approach meets the O(1) space requirement and is more memory efficient.

**1.4 Decomposition:**

1. Use two pointers: `odd` for odd-positioned nodes and `even` for even-positioned nodes.
2. Keep track of the head of the even list.
3. Rewire connections: odd.next = even.next, even.next = odd.next.next.
4. Move both pointers forward.
5. Connect the end of the odd list to the head of the even list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: head = [1,2,3,4,5]

We initialize:
* `odd = head` (points to node 1)
* `even = head.next` (points to node 2)
* `even_head = even` (save the head of even list)

**2.2 Start Checking/Processing:**

We enter a loop while `even` and `even.next` exist.

**2.3 Trace Walkthrough:**

| Step | odd.val | even.val | odd.next.val | even.next.val | Action |
|------|---------|----------|--------------|---------------|--------|
| Initial | 1 | 2 | 3 | 3 | Setup |
| 1 | 1 | 2 | 3 | 4 | odd.next = 3, even.next = 4 |
| 2 | 3 | 4 | 5 | 5 | odd.next = 5, even.next = None |
| Final | 5 | 4 | 2 | - | Connect odd.next = even_head |

**2.4 Increment and Loop:**

After each iteration, we move `odd = odd.next` and `even = even.next` to process the next pair.

**2.5 Return Result:**

The final list is [1,3,5,2,4], which is returned.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head
```

## 337. House Robber III [Medium]
https://leetcode.com/problems/house-robber-iii/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** The tree has at most 10^4 nodes, and each node value is between 0 and 10^4.
- **Time Complexity:** O(n) - We visit each node exactly once, where n is the number of nodes.
- **Space Complexity:** O(h) - The recursion stack depth is at most the height h of the tree. In the worst case (skewed tree), h = n, giving O(n) space.
- **Edge Case:** If the tree is empty (root is None), return 0.

**1.2 High-level approach:**
The goal is to find the maximum amount of money we can rob from a binary tree without robbing two directly connected nodes. We use dynamic programming with a post-order traversal, where for each node we calculate two values: the maximum if we rob this node, and the maximum if we don't rob this node.

![House Robber III tree](https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible combinations of robbing/not robbing each node, checking constraints. This would be exponential time O(2^n).
- **Optimized Strategy (DP with DFS):** For each node, calculate the maximum profit for two cases: robbing this node (can't rob children) and not robbing this node (can rob children). This takes O(n) time.
- **Emphasize the optimization:** By storing both possibilities at each node, we avoid recalculating subproblems and reduce time complexity from exponential to linear.

**1.4 Decomposition:**
1. Perform a post-order traversal of the tree.
2. For each node, return a tuple: (rob_this, dont_rob_this).
3. If we rob this node, we can't rob its children, so we take children's "don't rob" values.
4. If we don't rob this node, we can choose the maximum from each child's two options.
5. Return the maximum of the root's two options.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `root = [3,2,3,null,3,null,1]`

Initialize:
- Start DFS from root node with value 3.

**2.2 Start Processing:**
We traverse the tree using post-order DFS (process children before parent).

**2.3 Trace Walkthrough:**

| Node | Left Child Result | Right Child Result | Rob This | Don't Rob This | Max |
|------|-------------------|-------------------|----------|----------------|-----|
| 1 (leaf) | (0,0) | (0,0) | 1 + 0 + 0 = 1 | 0 + 0 = 0 | 1 |
| 3 (leaf) | (0,0) | (0,0) | 3 + 0 + 0 = 3 | 0 + 0 = 0 | 3 |
| 2 | (0,0) | (3,0) | 2 + 0 + 0 = 2 | 0 + 3 = 3 | 3 |
| 3 (root) | (2,3) | (1,0) | 3 + 3 + 0 = 6 | 3 + 1 = 4 | 7 |

**2.4 Return Result:**
The final result is max(rob_root, dont_rob_root) = max(6, 4) = 7.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob this node, don't rob this node)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we can't rob children
            rob_this = node.val + left[1] + right[1]
            
            # If we don't rob this node, we can choose to rob or not rob children
            dont_rob_this = max(left) + max(right)
            
            return (rob_this, dont_rob_this)
        
        return max(dfs(root))
```

## 380. Insert Delete GetRandom O(1) [Medium]
https://leetcode.com/problems/insert-delete-getrandom-o1/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** At most `2 * 10^5` calls to insert, remove, getRandom.
- **Time Complexity:** O(1) average for all operations - using array and hash map.
- **Space Complexity:** O(n) where n is the number of elements stored.
- **Edge Case:** Removing the last element, getting random from single element.

**1.2 High-level approach:**
The goal is to implement a data structure with O(1) insert, remove, and getRandom. We use an array for random access and a hash map to track indices for O(1) removal.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Use only array - remove is O(n), getRandom is O(1).
- **Optimized Strategy:** Use array + hash map - all operations O(1) average.

**1.4 Decomposition:**
1. Maintain an array of values and a hash map from value to index.
2. Insert: Add to array, store index in map.
3. Remove: Swap with last element, update map, remove last.
4. GetRandom: Use random.choice on array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Initialize `nums = []`, `val_to_index = {}`.

**2.2 Start Checking:**
We perform operations: insert(1), remove(2), insert(2), getRandom().

**2.3 Trace Walkthrough:**

| Operation | nums | val_to_index | Result |
|-----------|------|--------------|--------|
| insert(1) | [1] | {1:0} | True |
| remove(2) | [1] | {1:0} | False |
| insert(2) | [1,2] | {1:0,2:1} | True |
| getRandom() | [1,2] | {1:0,2:1} | 1 or 2 |

**2.4 Increment and Loop:**
Not applicable - these are individual operations.

**2.5 Return Result:**
Operations return their respective results.

### Solution

```python
def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        # Move last element to the position of element to remove
        index = self.val_to_index[val]
        last_val = self.nums[-1]
        
        self.nums[index] = last_val
        self.val_to_index[last_val] = index
        
        # Remove the last element
        self.nums.pop()
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

## 427. Construct Quad Tree [Medium]
https://leetcode.com/problems/construct-quad-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `n == grid.length == grid[i].length`, `n == 2^x` where `0 <= x <= 6`.
- **Time Complexity:** O(n²) - we process each cell, but with divide-and-conquer optimization.
- **Space Complexity:** O(log n) - recursion depth.
- **Edge Case:** All cells have the same value, single leaf node.

**1.2 High-level approach:**
The goal is to construct a Quad-Tree from a binary grid. We use divide-and-conquer: if all values in a region are the same, create a leaf; otherwise, divide into 4 quadrants and recurse.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - divide-and-conquer is the natural approach.
- **Optimized Strategy:** Recursively divide grid into quadrants until uniform or single cell.

**1.4 Decomposition:**
1. Check if all values in current region are the same.
2. If yes, create a leaf node with that value.
3. If no, divide into 4 quadrants (top-left, top-right, bottom-left, bottom-right).
4. Recursively construct each quadrant.
5. Create internal node with 4 children.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `grid = [[0,1],[1,0]]`. We start with the entire 2x2 grid.

**2.2 Start Checking:**
We check if all values are the same.

**2.3 Trace Walkthrough:**

| Region | All Same? | Action | Result |
|--------|-----------|--------|--------|
| [[0,1],[1,0]] | No | Divide | Internal node |
| Top-left [0] | Yes | Leaf | Node(val=0, isLeaf=True) |
| Top-right [1] | Yes | Leaf | Node(val=1, isLeaf=True) |
| Bottom-left [1] | Yes | Leaf | Node(val=1, isLeaf=True) |
| Bottom-right [0] | Yes | Leaf | Node(val=0, isLeaf=True) |

**2.4 Increment and Loop:**
After processing each quadrant, we combine results.

**2.5 Return Result:**
Return root node with 4 leaf children.

### Solution

```python
def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r1, c1, r2, c2):
            # Check if all values in the grid are the same
            all_same = True
            first_val = grid[r1][c1]
            
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break
            
            if all_same:
                return Node(first_val == 1, True, None, None, None, None)
            
            # Divide into four quadrants
            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2
            
            top_left = build(r1, c1, mid_r, mid_c)
            top_right = build(r1, mid_c + 1, mid_r, c2)
            bottom_left = build(mid_r + 1, c1, r2, mid_c)
            bottom_right = build(mid_r + 1, mid_c + 1, r2, c2)
            
            return Node(False, False, top_left, top_right, bottom_left, bottom_right)
        
        n = len(grid)
        res = build(0, 0, n - 1, n - 1)
        return res
```

## 437. Path Sum III [Medium]
https://leetcode.com/problems/path-sum-iii/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The tree can have up to 1000 nodes.
* **Time Complexity:** O(n) - We visit each node once during DFS, where n is the number of nodes.
* **Space Complexity:** O(h) for recursion stack where h is the height, plus O(n) in worst case for the prefix sum map.
* **Edge Case:** If the tree is empty, return 0. If targetSum is 0 and there are nodes with value 0, we need to count paths correctly.

**1.2 High-level approach:**

The goal is to count all paths in a binary tree where the sum of node values equals targetSum. A path can start and end anywhere, but must go downward. We use prefix sums to efficiently count paths ending at each node.

![Tree showing paths with prefix sum tracking]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** For each node, explore all downward paths starting from it. This is O(n^2) in the worst case.
* **Optimized (Prefix Sum with Hash Map):** Use a hash map to store prefix sums along the current path. For each node, check if (current_sum - targetSum) exists in the map. This is O(n) time.
* **Why it's better:** The prefix sum approach avoids redundant calculations and reduces time complexity from O(n^2) to O(n).

**1.4 Decomposition:**

1. Use DFS to traverse the tree.
2. Maintain a prefix sum map that tracks sums along the current path.
3. At each node, add the node's value to current sum.
4. Check if (current_sum - targetSum) exists in the map to count paths ending here.
5. Recursively process left and right children.
6. Backtrack by decrementing the prefix sum count before returning.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8

We initialize:
* `res = 0` (count of paths)
* `prefix_sums = {}` (map of prefix sum -> count)
* `current_sum = 0`

**2.2 Start Checking/Processing:**

We call `dfs(root, 0)` to start traversal.

**2.3 Trace Walkthrough:**

| Node | current_sum | prefix_sums | current_sum - 8 | Paths Found |
|------|-------------|-------------|-----------------|-------------|
| 10 | 10 | {10:1} | 2 | 0 |
| 5 | 15 | {10:1, 15:1} | 7 | 0 |
| 3 | 18 | {10:1, 15:1, 18:1} | 10 | 1 (18-8=10 exists) |
| -2 | 16 | {10:1, 15:1, 18:1, 16:1} | 8 | 1 (16-8=8, but 8 not in map, but current_sum=16, check if 16==8: no) |
| 2 | 17 | {10:1, 15:1, 18:1, 16:1, 17:1} | 9 | 0 |
| 1 | 18 | {10:1, 15:1, 18:2, 16:1, 17:1} | 10 | 1 (18-8=10 exists) |

**2.4 Increment and Loop:**

After processing each node and its children, we backtrack by decrementing the prefix sum count.

**2.5 Return Result:**

After processing all nodes, `res = 3` is returned (paths: 5->3, 5->2->1, -3->11).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        prefix_sums = {}
        
        def dfs(node, current_sum):
            nonlocal res, prefix_sums
            if not node:
                return
            
            current_sum += node.val
            if current_sum == targetSum:
                res += 1
            
            res += prefix_sums.get(current_sum - targetSum, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            prefix_sums[current_sum] -= 1
        
        dfs(root, 0)
        return res
```

## 443. String Compression [Medium]
https://leetcode.com/problems/string-compression/

### Explanation

## 443. String Compression [Medium]

https://leetcode.com/problems/string-compression

## Description
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

**Examples**
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

**Constraints**
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

## Hint
Use two pointers: one for reading, one for writing.

## Explanation
We want to compress the string by replacing sequences of the same character with that character followed by the count. We use two pointers: one to read through the array, and one to write the compressed result.

We do this because it lets us modify the array in-place, which saves memory and meets the problem's requirements. By counting consecutive characters and writing the count only when needed, we keep the result as short as possible.

This approach is efficient and avoids creating extra arrays, making it suitable for large inputs.

### Solution

```python
def compress(chars):
    write = 0
    read = 0
    n = len(chars)
    while read < n:
        char = chars[read]
        count = 0
        while read < n and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1
        if count > 1:
            for c in str(count):
                chars[write] = c
                write += 1
    return write
```

## 450. Delete Node in a BST [Medium]
https://leetcode.com/problems/delete-node-in-a-bst/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary search tree and a key, we need to delete the node with the given key and return the root of the BST.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-10^5$ and $10^5$.
- **Time Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Space Complexity:** $O(h)$ - The recursion stack can be as deep as the height of the tree.
- **Edge Case:** If the key doesn't exist, return the original tree. If the node to delete has no children, simply remove it.

**1.2 High-level approach:**

The goal is to delete a node from a BST while maintaining the BST property.

We use recursion to find the node. If found, we handle three cases: no children, one child, or two children. For two children, we replace the node's value with the minimum value from its right subtree, then delete that minimum node.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must maintain the BST structure.
- **Optimized Strategy (Recursion):** Use recursion to find and delete the node, handling each case appropriately. This is the standard and efficient approach.
- **Why it's better:** The recursive approach naturally handles the tree structure and maintains BST properties efficiently.

**1.4 Decomposition:**

1. If root is null, return null.
2. If key is less than root.val, recursively delete from left subtree.
3. If key is greater than root.val, recursively delete from right subtree.
4. If key equals root.val:
   - If no left child, return right child.
   - If no right child, return left child.
   - If two children, find minimum in right subtree, replace root's value, and delete the minimum node.
5. Return the root.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[5,3,6,2,4,null,7]$, key = 3

The tree structure:
```
    5
   / \
  3   6
 / \   \
2   4   7
```

**2.2 Start Searching:**

We search for the node with key = 3.

**2.3 Trace Walkthrough:**

| Step | Current Node | Key Comparison | Action |
|------|--------------|----------------|--------|
| 1 | 5 | 3 < 5 | Go left |
| 2 | 3 | 3 == 3 | Found! Delete node 3 |

**Deleting node 3:**
- Node 3 has two children (2 and 4)
- Find minimum in right subtree: min(4) = 4
- Replace node 3's value with 4
- Delete node 4 from right subtree (node 4 has no children, so simply remove it)

**2.4 Final Tree:**

After deletion:
```
    5
   / \
  4   6
 /     \
2       7
```

**2.5 Return Result:**

We return the root of the modified tree.

> **Note:** The key insight is that when deleting a node with two children, we can replace it with the minimum node from its right subtree (or maximum from left subtree). This maintains the BST property because the minimum in the right subtree is greater than all left children and less than all other right children.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Node has two children
                # Find the minimum value in right subtree
                min_node = self.findMin(root.right)
                # Replace root's value with min value
                root.val = min_node.val
                # Delete the min node from right subtree
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
```

## 460. LFU Cache [Hard]
https://leetcode.com/problems/lfu-cache/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Capacity is between 1 and 10^4, keys are between 0 and 10^5, values are between 0 and 10^9. At most 2 * 10^5 calls to get and put.
- **Time Complexity:** O(1) average for both get and put operations - We use hash maps and ordered dictionaries for constant-time access.
- **Space Complexity:** O(capacity) - We store at most capacity key-value pairs.
- **Edge Case:** When capacity is 0, all operations return -1 or do nothing.

**1.2 High-level approach:**
The goal is to implement an LFU (Least Frequently Used) cache that evicts the least frequently used item when at capacity. For ties in frequency, we evict the least recently used item. We maintain frequency buckets using OrderedDict to track both frequency and recency.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Store (value, frequency, timestamp) for each key, and find minimum on eviction by scanning all keys. This takes O(capacity) time for eviction.
- **Optimized Strategy (Frequency Buckets with OrderedDict):** Use frequency buckets where each bucket is an OrderedDict maintaining insertion order. This allows O(1) access and O(1) eviction.
- **Emphasize the optimization:** By organizing keys by frequency and using OrderedDict for recency, we can find the LFU key in O(1) time.

**1.4 Decomposition:**
1. Maintain a dictionary mapping keys to their frequencies.
2. Maintain frequency buckets: each frequency maps to an OrderedDict of keys.
3. Track the minimum frequency currently in use.
4. For get: update frequency, move key to new frequency bucket.
5. For put: if at capacity, evict from min_freq bucket (FIFO), then add/update key.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's trace: `capacity = 2`, operations: `put(1,1)`, `put(2,2)`, `get(1)`, `put(3,3)`, `get(2)`, `get(3)`, `put(4,4)`, `get(1)`, `get(3)`, `get(4)`

Initialize:
- `key_to_freq = {}`
- `freq_to_keys = {1: OrderedDict()}`
- `key_to_val = {}`
- `min_freq = 1`

**2.2 Start Processing:**
Process each operation step by step.

**2.3 Trace Walkthrough:**

| Operation | Key | Value | State After | min_freq |
|-----------|-----|-------|-------------|----------|
| put(1,1) | 1 | 1 | {1:1}, freq1={1} | 1 |
| put(2,2) | 2 | 2 | {1:1,2:2}, freq1={1,2} | 1 |
| get(1) | 1 | 1 | {1:2,2:1}, freq1={2}, freq2={1} | 1 |
| put(3,3) | 3 | 3 | Evict 2, {1:2,3:1}, freq1={3}, freq2={1} | 1 |
| get(2) | 2 | -1 | Not found | 1 |
| get(3) | 3 | 3 | {1:2,3:2}, freq2={1,3} | 2 |
| put(4,4) | 4 | 4 | Evict 1, {3:2,4:1}, freq1={4}, freq2={3} | 1 |
| get(1) | 1 | -1 | Not found | 1 |
| get(3) | 3 | 3 | {3:3,4:1}, freq1={4}, freq3={3} | 1 |
| get(4) | 4 | 4 | {3:3,4:2}, freq2={4}, freq3={3} | 2 |

**2.4 Return Result:**
Final sequence: `[null, null, null, 1, null, -1, 3, null, -1, 3, 4]`

### Solution

```python
def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_freq = {}  # key -> frequency
        self.freq_to_keys = defaultdict(OrderedDict)  # frequency -> OrderedDict of keys
        self.key_to_val = {}  # key -> value

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        # Update frequency
        freq = self.key_to_freq[key]
        self.freq_to_keys[freq].pop(key)
        
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None
        
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_val:
            # Update existing key
            self.key_to_val[key] = value
            self.get(key)  # Update frequency
            return
        
        # Remove LFU key if at capacity
        if len(self.key_to_val) >= self.capacity:
            # Remove least recently used key with min_freq
            lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[lfu_key]
            del self.key_to_freq[lfu_key]
        
        # Add new key
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
```

## 530. Minimum Absolute Difference in BST [Easy]
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `2 <= nodes <= 10^4`, `0 <= Node.val <= 10^5`.
- **Time Complexity:** O(n) - we traverse the tree once to collect values.
- **Space Complexity:** O(n) - we store all node values.
- **Edge Case:** Tree with only two nodes.

**1.2 High-level approach:**
The goal is to find the minimum absolute difference between any two nodes in a BST. We use in-order traversal to get sorted values, then find minimum difference between consecutive values.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Compare all pairs - O(n²) time.
- **Optimized Strategy:** In-order traversal gives sorted order, check adjacent pairs - O(n) time.

**1.4 Decomposition:**
1. Perform in-order traversal to get sorted values.
2. Iterate through sorted values.
3. Calculate difference between consecutive values.
4. Track minimum difference.
5. Return minimum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `root = [4,2,6,1,3]`. In-order traversal gives [1,2,3,4,6].

**2.2 Start Checking:**
We compare consecutive values in sorted order.

**2.3 Trace Walkthrough:**

| i | values[i] | values[i+1] | Difference | Min |
|---|-----------|-------------|------------|-----|
| 0 | 1 | 2 | 1 | 1 |
| 1 | 2 | 3 | 1 | 1 |
| 2 | 3 | 4 | 1 | 1 |
| 3 | 4 | 6 | 2 | 1 |

**2.4 Increment and Loop:**
After checking each pair, we move to the next.

**2.5 Return Result:**
Return `res = 1`, the minimum absolute difference.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        values = inorder(root)
        res = float('inf')
        
        for i in range(len(values) - 1):
            res = min(res, values[i + 1] - values[i])
        
        return res
```

## 543. Diameter of Binary Tree [Easy]
https://leetcode.com/problems/diameter-of-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Tree has between 1 and 10^4 nodes, and node values are between -100 and 100.
- **Time Complexity:** O(n) - We visit each node exactly once during DFS, where n is the number of nodes.
- **Space Complexity:** O(h) - The recursion stack depth is at most the height h of the tree. In the worst case (skewed tree), h = n, giving O(n) space.
- **Edge Case:** If the tree has only one node, the diameter is 0 (no edges).

**1.2 High-level approach:**
The goal is to find the diameter (longest path between any two nodes) of a binary tree. The diameter may or may not pass through the root. We use DFS to calculate the depth of each subtree and track the maximum diameter found so far.

![Diameter of Binary Tree](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each node, find the longest path passing through it by calculating depths of left and right subtrees. This still requires visiting each node once, so it's O(n) but with redundant calculations.
- **Optimized Strategy (DFS with Global Tracking):** Perform a single DFS pass, calculating subtree depths and updating the maximum diameter as we go. This takes O(n) time with a single traversal.
- **Emphasize the optimization:** By tracking the maximum diameter during a single DFS pass, we avoid multiple traversals and redundant calculations.

**1.4 Decomposition:**
1. Perform DFS traversal of the tree.
2. For each node, calculate the depth of its left and right subtrees.
3. The diameter passing through this node is left_depth + right_depth.
4. Update the global maximum diameter if this is larger.
5. Return the depth of the current subtree (1 + max(left_depth, right_depth)).

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `root = [1,2,3,4,5]`

Initialize:
- `res = 0` (global maximum diameter)

**2.2 Start Processing:**
We perform DFS starting from the root.

**2.3 Trace Walkthrough:**

| Node | Left Depth | Right Depth | Diameter Through Node | Max Diameter | Return Depth |
|------|------------|-------------|----------------------|--------------|--------------|
| 4 (leaf) | 0 | 0 | 0 | 0 | 1 |
| 5 (leaf) | 0 | 0 | 0 | 0 | 1 |
| 2 | 1 | 1 | 2 | 2 | 2 |
| 3 (leaf) | 0 | 0 | 0 | 2 | 1 |
| 1 (root) | 2 | 1 | 3 | 3 | 3 |

**2.4 Return Result:**
The maximum diameter found is 3, which is the path [4,2,1,3] or [5,2,1,3].

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # Diameter passing through this node
            res = max(res, left_depth + right_depth)
            
            # Return depth of this subtree
            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return res
```

## 617. Merge Two Binary Trees [Easy]
https://leetcode.com/problems/merge-two-binary-trees/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes in both trees is in the range `[0, 2000]`.
- **Value Range:** `-10^4 <= Node.val <= 10^4`.
- **Time Complexity:** O(min(m, n)) where m and n are the number of nodes in the two trees. We visit each node at most once.
- **Space Complexity:** O(min(m, n)) for the recursion stack in the worst case (skewed tree).
- **Edge Case:** If one tree is null, return the other tree. If both are null, return null.

**1.2 High-level approach:**

The goal is to merge two binary trees by summing overlapping nodes and using non-null nodes when one tree has a node and the other doesn't. We use recursion to traverse both trees simultaneously, creating new nodes for the merged tree.

![Visualization showing how two binary trees are merged node by node, with overlapping nodes summed and non-overlapping nodes preserved]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse both trees to merge them.
- **Optimized Strategy:** Use recursive depth-first search to traverse both trees simultaneously, creating merged nodes as we go.
- **Why it's better:** Recursion naturally handles the tree structure and allows us to process each node exactly once.

**1.4 Decomposition:**

1. If both nodes are null, return null.
2. If one node is null, return the other node (no merging needed).
3. If both nodes exist, create a new node with the sum of their values.
4. Recursively merge the left subtrees.
5. Recursively merge the right subtrees.
6. Return the merged node.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example:
- `root1 = [1, 3, 2, 5]` (tree structure: 1 has left=3, right=2; 3 has left=5)
- `root2 = [2, 1, 3, null, 4, null, 7]` (tree structure: 2 has left=1, right=3; 1 has right=4; 3 has right=7)

**2.2 Start Checking:**

We start from the root nodes of both trees.

**2.3 Trace Walkthrough:**

| Step | root1 node | root2 node | Action | Merged value | Left child | Right child |
|------|------------|------------|--------|--------------|------------|-------------|
| 1 | 1 | 2 | Both exist | 1 + 2 = 3 | Merge(3, 1) | Merge(2, 3) |
| 2 | 3 | 1 | Both exist | 3 + 1 = 4 | Merge(5, null) | Merge(null, 4) |
| 3 | 5 | null | root2 is null | 5 | null | null |
| 4 | null | 4 | root1 is null | 4 | null | null |
| 5 | 2 | 3 | Both exist | 2 + 3 = 5 | Merge(null, null) | Merge(null, 7) |
| 6 | null | null | Both null | null | - | - |
| 7 | null | 7 | root1 is null | 7 | null | null |

The merged tree structure:
- Root: 3 (1 + 2)
  - Left: 4 (3 + 1)
    - Left: 5 (5 + null)
    - Right: 4 (null + 4)
  - Right: 5 (2 + 3)
    - Left: null
    - Right: 7 (null + 7)

**2.4 Increment and Loop:**

Recursion handles the traversal automatically.

**2.5 Return Result:**

Return the merged tree root: `[3, 4, 5, 5, 4, null, 7]`.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        # Merge values
        merged = TreeNode(root1.val + root2.val)
        
        # Recursively merge left and right subtrees
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        
        return merged
```

## 637. Average of Levels in Binary Tree [Easy]
https://leetcode.com/problems/average-of-levels-in-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nodes <= 10^4`.
- **Time Complexity:** O(n) - we visit each node once using BFS.
- **Space Complexity:** O(w) where w is maximum width - queue storage.
- **Edge Case:** Single node tree returns [node.val].

**1.2 High-level approach:**
The goal is to calculate the average value of nodes at each level. We use BFS (level-order traversal) to process nodes level by level, calculating the sum and count for each level.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - BFS is the natural approach.
- **Optimized Strategy:** BFS processes one level at a time, calculate average per level.

**1.4 Decomposition:**
1. Use BFS with a queue.
2. For each level, process all nodes at that level.
3. Calculate sum and count of nodes in the level.
4. Compute average (sum / count).
5. Add to result list.
6. Continue to next level.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `root = [3,9,20,null,null,15,7]`. Initialize queue with [root], res = [].

**2.2 Start Checking:**
We process nodes level by level.

**2.3 Trace Walkthrough:**

| Level | Nodes | Sum | Count | Average | res |
|-------|-------|-----|-------|---------|-----|
| 0 | [3] | 3 | 1 | 3.0 | [3.0] |
| 1 | [9,20] | 29 | 2 | 14.5 | [3.0,14.5] |
| 2 | [15,7] | 22 | 2 | 11.0 | [3.0,14.5,11.0] |

**2.4 Increment and Loop:**
After processing each level, we move to the next.

**2.5 Return Result:**
Return `res = [3.0,14.5,11.0]`, averages for each level.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level_sum / level_size)
        
        return res
```

## 647. Palindromic Substrings [Medium]
https://leetcode.com/problems/palindromic-substrings/

### Explanation

## 647. Longest Subarray of 1's After Deleting One Element [Medium]

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

## Description
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

**Examples**
```text
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```
**Constraints**
```text
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
```

## Hint
Use a sliding window to keep at most one zero in the window.

## Explanation
We want the longest run of 1's after deleting one element. That means we can have at most one zero in our current window, since deleting it would leave only 1's.

We use a sliding window to keep track of the current sequence. Every time we have more than one zero, we move the left end of the window forward until we're back to at most one zero.

We do this because it lets us efficiently find the longest possible sequence without checking every possible subarray. By only moving the window when needed, we keep our solution fast and memory-efficient, especially for large arrays.

### Solution

```python
def longestSubarray(nums):
    left = 0
    zeros = 0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len, right - left)
    return max_len
```

## 700. Search in a Binary Search Tree [Easy]
https://leetcode.com/problems/search-in-a-binary-search-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The tree can have up to 5000 nodes.
* **Time Complexity:** O(h) where h is the height of the tree. In the worst case (skewed tree), h = n, giving O(n). In a balanced tree, h = log n.
* **Space Complexity:** O(h) for the recursion stack. In worst case O(n), in balanced tree O(log n).
* **Edge Case:** If the tree is empty or the value doesn't exist, return None.

**1.2 High-level approach:**

The goal is to find a node in a BST with a given value. We use the BST property: left subtree contains smaller values, right subtree contains larger values.

![BST search showing how we navigate left or right based on comparison]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Traverse the entire tree (inorder/preorder/postorder) to find the value. This takes O(n) time.
* **Optimized (BST Property):** Use the BST property to eliminate half of the remaining nodes at each step. This takes O(h) time where h is height.
* **Why it's better:** The BST property allows us to skip entire subtrees, making search much faster than linear traversal.

**1.4 Decomposition:**

1. If the current node is None, return None (value not found).
2. If current node's value equals target, return the current node.
3. If current node's value is greater than target, search in the left subtree.
4. If current node's value is less than target, search in the right subtree.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = [4,2,7,1,3], val = 2

We start at the root node with value 4.

**2.2 Start Checking/Processing:**

We call `searchBST(root, 2)`.

**2.3 Trace Walkthrough:**

| Step | Current Node | Current Val | Comparison | Action |
|------|--------------|-------------|------------|--------|
| 1 | 4 | 4 | 4 > 2 | Go left to node 2 |
| 2 | 2 | 2 | 2 == 2 | Found! Return node 2 |

**2.4 Increment and Loop:**

After each comparison, we recursively search the appropriate subtree.

**2.5 Return Result:**

We return the node with value 2, which is the root of the subtree [2,1,3].

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
```

## 701. Insert into a Binary Search Tree [Medium]
https://leetcode.com/problems/insert-into-a-binary-search-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root node of a binary search tree (BST) and a value to insert, we need to insert the value into the BST and return the root node of the BST after insertion.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes $N$ in the BST can be up to $10^4$.
- **Value Range:** Values are between $-10^8$ and $10^8$.
- **Time Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$. In the average case (balanced tree), $h = \log n$, so $O(\log n)$.
- **Space Complexity:** $O(h)$ - The recursion stack can be as deep as the height of the tree. In the worst case, this is $O(n)$, and in the average case, this is $O(\log n)$.
- **Edge Case:** If the tree is empty (root is null), we create a new node with the given value and return it.

**1.2 High-level approach:**

The goal is to insert a new value into a BST while maintaining the BST property: all values in the left subtree are less than the root, and all values in the right subtree are greater than the root.

![BST Insertion](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

We use the BST property to navigate to the correct insertion point: if the value is less than the current node, go left; if greater, go right. When we reach a null position, that's where we insert the new node.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach for BST insertion. We must use the BST property to find the correct position.
- **Optimized Strategy (Recursive):** Recursively traverse the tree using the BST property. When we find a null position, create and return a new node. This naturally maintains the BST structure.
- **Why it's better:** The recursive approach is clean and intuitive. It leverages the BST property efficiently, ensuring we only traverse one path from root to leaf.

**1.4 Decomposition:**

1. Check if the current node is null. If so, create a new node with the value and return it.
2. Compare the value to insert with the current node's value.
3. If the value is less than the current node's value, recursively insert into the left subtree.
4. If the value is greater than or equal to the current node's value, recursively insert into the right subtree.
5. Return the current node (which may have been modified with a new child).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[4,2,7,1,3]$, $val = 5$

The BST structure:
```
      4
     / \
    2   7
   / \
  1   3
```

We need to insert value 5.

**2.2 Start Traversing:**

We begin at the root node (value 4).

**2.3 Trace Walkthrough:**

| Step | Current Node | Value to Insert | Comparison | Action |
|------|--------------|-----------------|------------|--------|
| 1 | 4 | 5 | $5 > 4$ | Go to right child (7) |
| 2 | 7 | 5 | $5 < 7$ | Go to left child (null) |
| 3 | null | 5 | - | Create new node with value 5 |

After insertion:
```
      4
     / \
    2   7
   / \ /
  1  3 5
```

**2.4 Return Result:**

The new node is created and linked as the left child of node 7. The root node (4) is returned.

> **Note:** The BST property ensures that we always know which direction to go. We never need to backtrack or check multiple paths.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root, val: int):
        # If tree is empty, create new node
        if not root:
            return TreeNode(val)
        
        # If val is less than root, insert into left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If val is greater than root, insert into right subtree
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
```

## 872. Leaf-Similar Trees [Easy]
https://leetcode.com/problems/leaf-similar-trees/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** Each tree can have up to 200 nodes.
* **Time Complexity:** O(n + m) - We traverse both trees once to collect leaves, where n and m are the number of nodes in each tree.
* **Space Complexity:** O(n + m) - We store leaf sequences for both trees, plus O(h) for recursion stack.
* **Edge Case:** If both trees are empty, they are leaf-similar (both have empty leaf sequences).

**1.2 High-level approach:**

The goal is to check if two binary trees have the same leaf value sequence. We collect leaves from left to right for both trees and compare the sequences.

![Tree traversal showing leaf collection from left to right]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Convert both trees to arrays using any traversal, then extract and compare leaves. This is inefficient.
* **Optimized (DFS with Leaf Collection):** Use DFS to collect leaves in order (left to right) for both trees, then compare the sequences. This is O(n + m) time.
* **Why it's better:** We only collect leaves, avoiding unnecessary processing of internal nodes, and compare sequences directly.

**1.4 Decomposition:**

1. Define a helper function to collect leaves from a tree using DFS.
2. For each node: if it's a leaf, add its value; otherwise, recursively collect from left and right subtrees.
3. Collect leaves from both trees.
4. Compare the two leaf sequences.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

We call `get_leaves(root1)` and `get_leaves(root2)`.

**2.2 Start Checking/Processing:**

We traverse each tree using DFS to collect leaves.

**2.3 Trace Walkthrough:**

For root1:
* Traverse left: 6 (leaf) → [6]
* Traverse right from 5: 7 (leaf) → [6,7]
* Continue: 4 (leaf) → [6,7,4]
* Continue: 9 (leaf) → [6,7,4,9]
* Continue: 8 (leaf) → [6,7,4,9,8]

For root2:
* Traverse left: 6 (leaf) → [6]
* Traverse right from 5: 7 (leaf) → [6,7]
* Continue: 4 (leaf) → [6,7,4]
* Continue: 9 (leaf) → [6,7,4,9]
* Continue: 8 (leaf) → [6,7,4,9,8]

**2.4 Increment and Loop:**

After collecting all leaves from both trees, we compare the sequences.

**2.5 Return Result:**

Both sequences are [6,7,4,9,8], so we return `True`.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)
        
        return get_leaves(root1) == get_leaves(root2)
```

## 876. Middle of the Linked List [Easy]
https://leetcode.com/problems/middle-of-the-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

Given the head of a singly linked list, we need to return the middle node of the linked list. If there are two middle nodes, return the second one.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be between $1$ and $100$.
- **Value Range:** Node values are between $1$ and $100$.
- **Time Complexity:** $O(n)$ - We traverse the list once with two pointers.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If the list has only one node, return that node. If the list has two nodes, return the second one.

**1.2 High-level approach:**

The goal is to find the middle node of a linked list.

We use the "tortoise and hare" approach: one pointer moves one step at a time (slow), and another moves two steps at a time (fast). When the fast pointer reaches the end, the slow pointer is at the middle.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** First pass to count nodes, second pass to find the middle node. This takes $O(n)$ time but requires two passes.
- **Optimized Strategy (Two Pointers):** Use two pointers moving at different speeds. This takes $O(n)$ time in a single pass.
- **Why it's better:** The two-pointer approach finds the middle in one pass instead of two, making it more efficient and elegant.

**1.4 Decomposition:**

1. Initialize two pointers (slow and fast) at the head.
2. Move slow one step and fast two steps at a time.
3. When fast reaches the end (null or last node), slow is at the middle.
4. Return the slow pointer.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $head = [1,2,3,4,5]$

We initialize:
- `slow = 1`
- `fast = 1`

**2.2 Start Processing:**

We begin moving the pointers.

**2.3 Trace Walkthrough:**

| Step | slow position | fast position | Action |
|------|---------------|---------------|--------|
| 0 | 1 | 1 | Start |
| 1 | 2 | 3 | Move slow 1, fast 2 |
| 2 | 3 | 5 | Move slow 1, fast 2 |
| 3 | 3 | null | fast.next is null, stop |

**2.4 Explanation:**

- When fast reaches the end (node 5, where fast.next is null), slow is at node 3, which is the middle node.

**2.5 Return Result:**

We return the node with value 3, which is the middle node.

> **Note:** The key insight is that when the fast pointer moves twice as fast, it covers twice the distance. When it reaches the end, the slow pointer has covered half the distance, which is exactly the middle.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        
        # Move fast pointer twice as fast as slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches the end, slow is at the middle
        return slow
```

## 901. Online Stock Span [Medium]
https://leetcode.com/problems/online-stock-span/

### Explanation

## 901. Online Stock Span [Medium]

https://leetcode.com/problems/online-stock-span

## Description
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

Implement the StockSpanner class:
- StockSpanner() Initializes the object of the class.
- int next(int price) Returns the span of the stock's price given that today's price is price.

## Examples

Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output:
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation:
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6

## Constraints
- 1 <= price <= 10^5
- At most 10^4 calls will be made to next.

## Hint
- We are interested in finding the span or reach back in time over consecutive elements that meet a certain criterion (in this case, previous stock prices that are less than or equal to the current day's price).
- A monotonic stack allows us to efficiently track and update spans as new prices come in, maintaining the necessary order of comparison and ensuring we can calculate each day's span in O(1) average time.

## Explanation

This problem is a classic application of the monotonic stack technique. We want to efficiently find, for each new price, how many consecutive previous days (including today) had prices less than or equal to today's price. By maintaining a stack of pairs (price, span), we can pop off all previous prices that are less than or equal to the current price, summing their spans, and push the current price and its total span. This allows each price to be processed in amortized O(1) time, making the solution efficient for large input sizes.

### Solution

```python
def __init__(self):
        self.stack = []  # Each element is a tuple (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _price, _span = self.stack.pop()
            span += _span
        self.stack.append([price, span])
        return span
```

## 933. Number of Recent Calls [Easy]
https://leetcode.com/problems/number-of-recent-calls/

### Explanation

## Explanation

### Strategy (The "Why")

We need to implement a `RecentCounter` class that counts the number of recent requests within the past 3000 milliseconds. Each call to `ping(t)` adds a new request at time $t$ and returns the number of requests in the range $[t-3000, t]$.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of calls to `ping` can be up to $10^4$.
- **Value Range:** Time values $t$ are strictly increasing and between $1$ and $10^9$.
- **Time Complexity:** $O(1)$ amortized - Each `ping` operation is $O(1)$ amortized because each request is added once and removed at most once.
- **Space Complexity:** $O(n)$ where $n$ is the number of requests in the current 3000ms window. In the worst case, if all requests are within 3000ms, this is $O(n)$.
- **Edge Case:** If `ping` is called with times that are more than 3000ms apart, old requests are removed from the queue.

**1.2 High-level approach:**

The goal is to maintain a sliding window of requests within the past 3000ms.

![Recent Counter](https://assets.leetcode.com/uploads/2021/09/03/chrome_2021-09-03_10-30-58.png)

We use a queue (deque) to store request times. When a new request arrives, we remove all requests outside the 3000ms window, then add the new request and return the queue size.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Store all requests in a list and filter out old ones each time. This could be inefficient if we check all requests.
- **Optimized Strategy (Queue):** Use a deque to store requests. Since times are strictly increasing, we only need to remove from the front. This is efficient.
- **Why it's better:** The queue approach allows us to efficiently remove old requests from the front while adding new ones at the back. Since times are increasing, we never need to check the middle of the queue.

**1.4 Decomposition:**

1. Initialize an empty deque in the constructor.
2. In `ping(t)`:
   - Add the current time $t$ to the queue.
   - Remove all requests from the front that are older than $t - 3000$.
   - Return the size of the queue (number of requests in the window).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `ping(1)`, `ping(100)`, `ping(3001)`, `ping(3002)`

We initialize:
- `queue = deque()`

**2.2 Start Processing:**

We process each ping call.

**2.3 Trace Walkthrough:**

| Call | Time | Queue Before | Remove Old | Queue After | Return |
|------|------|--------------|------------|-------------|--------|
| `ping(1)` | 1 | [] | None | [1] | 1 |
| `ping(100)` | 100 | [1] | None ($1 \geq 100-3000$) | [1, 100] | 2 |
| `ping(3001)` | 3001 | [1, 100] | Remove 1 ($1 < 3001-3000$) | [100, 3001] | 2 |
| `ping(3002)` | 3002 | [100, 3001] | Remove 100 ($100 < 3002-3000$) | [3001, 3002] | 2 |

**2.4 Explanation:**

- `ping(1)`: Window $[1-3000, 1] = [-2999, 1]$, contains [1] → return 1
- `ping(100)`: Window $[100-3000, 100] = [-2900, 100]$, contains [1, 100] → return 2
- `ping(3001)`: Window $[3001-3000, 3001] = [1, 3001]$, contains [100, 3001] (1 is removed) → return 2
- `ping(3002)`: Window $[3002-3000, 3002] = [2, 3002]$, contains [3001, 3002] (100 is removed) → return 2

**2.5 Return Result:**

Each `ping` call returns the number of requests in the current 3000ms window.

> **Note:** Since times are strictly increasing, we only need to check and remove from the front of the queue. All requests in the queue are already in order, so we never need to check the middle or back.

### Solution

```python
def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add current request time
        self.queue.append(t)
        
        # Remove requests outside the 3000ms window
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        
        # Return number of requests in the window
        return len(self.queue)
```

## 981. Time Based Key-Value Store [Medium]
https://leetcode.com/problems/time-based-key-value-store/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= key.length, value.length <= 100`, `1 <= timestamp <= 10^7`, at most `2 * 10^5` calls to set and get.
- **Time Complexity:** 
  - `set`: O(1) - append to list.
  - `get`: O(log m) where m is the number of timestamps for the key (binary search).
- **Space Complexity:** O(n) where n is the total number of set operations.
- **Edge Case:** If a key doesn't exist or no timestamp <= given timestamp exists, return empty string.

**1.2 High-level approach:**

The goal is to design a time-based key-value store that can store multiple values for the same key at different timestamps and retrieve the value associated with the largest timestamp that is <= the given timestamp. We use a dictionary to map keys to lists of (timestamp, value) pairs, and use binary search to efficiently find the correct value.

![Visualization showing how timestamps are stored and retrieved using binary search to find the largest timestamp <= target]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For `get`, iterate through all timestamps for a key to find the largest one <= target. This takes O(m) time where m is the number of timestamps.
- **Optimized Strategy:** Since timestamps are strictly increasing, we can use binary search to find the answer in O(log m) time.
- **Why it's better:** Binary search reduces the time complexity from O(m) to O(log m), which is crucial when there are many timestamps for a key.

**1.4 Decomposition:**

1. Initialize a dictionary to store key -> list of (timestamp, value) pairs.
2. For `set`: Append (timestamp, value) to the list for the key.
3. For `get`: Use binary search to find the largest timestamp <= target timestamp.
4. Return the corresponding value, or empty string if not found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through the example operations:
- `set("foo", "bar", 1)`
- `get("foo", 1)` -> should return "bar"
- `get("foo", 3)` -> should return "bar" (largest timestamp <= 3 is 1)
- `set("foo", "bar2", 4)`
- `get("foo", 4)` -> should return "bar2"
- `get("foo", 5)` -> should return "bar2" (largest timestamp <= 5 is 4)

**2.2 Start Checking:**

Initialize: `store = {}`

**2.3 Trace Walkthrough:**

| Operation | Key | Timestamp/Value | Store state | Action |
|-----------|-----|-----------------|-------------|--------|
| set | "foo" | ("bar", 1) | {"foo": [(1, "bar")]} | Append to list |
| get | "foo" | 1 | - | Binary search: find timestamp <= 1 |
| - | - | - | - | Found (1, "bar"), return "bar" |
| get | "foo" | 3 | - | Binary search: find timestamp <= 3 |
| - | - | - | - | Found (1, "bar"), return "bar" |
| set | "foo" | ("bar2", 4) | {"foo": [(1, "bar"), (4, "bar2")]} | Append to list |
| get | "foo" | 4 | - | Binary search: find timestamp <= 4 |
| - | - | - | - | Found (4, "bar2"), return "bar2" |
| get | "foo" | 5 | - | Binary search: find timestamp <= 5 |
| - | - | - | - | Found (4, "bar2"), return "bar2" |

Binary search details for `get("foo", 3)`:
- List: `[(1, "bar"), (4, "bar2")]`
- left = 0, right = 1
- mid = 0, values[0][0] = 1 <= 3, so res = "bar", left = 1
- left = 1, right = 1, mid = 1, values[1][0] = 4 > 3, so right = 0
- left = 1 > right = 0, exit loop
- Return "bar"

**2.4 Increment and Loop:**

Binary search continues until left > right.

**2.5 Return Result:**

Return the value associated with the largest timestamp <= target, or "" if not found.

### Solution

```python
def __init__(self):
        self.store = {}  # key -> list of (timestamp, value) pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        # Binary search for the largest timestamp <= given timestamp
        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
```

## 1161. Maximum Level Sum of a Binary Tree [Medium]
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The tree can have up to 10^4 nodes.
* **Time Complexity:** O(n) - We visit each node once using BFS, where n is the number of nodes.
* **Space Complexity:** O(w) where w is the maximum width of the tree. In worst case O(n).
* **Edge Case:** If the tree is empty, return 0. If all level sums are equal, return the smallest level (1).

**1.2 High-level approach:**

The goal is to find the level with the maximum sum of node values. We use BFS (level-order traversal) to process nodes level by level and track the sum for each level.

![BFS traversal showing level-by-level processing and sum calculation]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Use DFS to collect all nodes by level, then calculate sums. This requires extra space to store level information.
* **Optimized (BFS):** Use BFS to process one level at a time, calculating the sum as we go. This is O(n) time and naturally processes levels in order.
* **Why it's better:** BFS naturally processes levels sequentially, making it straightforward to track level sums without extra data structures.

**1.4 Decomposition:**

1. Use a queue for BFS traversal.
2. For each level:
   - Process all nodes at the current level.
   - Sum their values.
   - Track the maximum sum and corresponding level.
3. Return the smallest level with maximum sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = [1,7,0,7,-8,null,null]

We initialize:
* `queue = deque([root])`
* `max_sum = -inf`
* `res = 1`
* `level = 1`

**2.2 Start Checking/Processing:**

We enter a while loop while the queue is not empty.

**2.3 Trace Walkthrough:**

| Level | Nodes | Level Sum | max_sum | res |
|-------|-------|-----------|---------|-----|
| 1 | [1] | 1 | 1 | 1 |
| 2 | [7, 0] | 7 | 7 | 2 |
| 3 | [7, -8] | -1 | 7 | 2 |

**2.4 Increment and Loop:**

After processing each level, we increment the level counter and continue to the next level.

**2.5 Return Result:**

After processing all levels, `res = 2` is returned (level 2 has maximum sum of 7).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        from collections import deque
        queue = deque([root])
        max_sum = float('-inf')
        res = 1
        level = 1
        
        while queue:
            level_sum = 0
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                res = level
            
            level += 1
        
        return res
```

## 1207. Unique Number of Occurrences [Easy]
https://leetcode.com/problems/unique-number-of-occurrences/

### Explanation

## 1207. Unique Number of Occurrences [Easy]

https://leetcode.com/problems/unique-number-of-occurrences

## Description
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

**Examples**
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

**Constraints**
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

## Hint
Use a dictionary to count occurrences, then check if the counts are unique using a set.

## Explanation
We want to know if every number in the array appears a unique number of times. First, we count how many times each number appears using a dictionary. Then, we check if all those counts are different by putting them in a set.

We do this because using a dictionary makes counting fast and easy, and a set lets us quickly check for duplicates among the counts. This approach is efficient and avoids unnecessary loops.

### Solution

```python
def uniqueOccurrences(arr):
    from collections import Counter

    count = Counter(arr)
    return len(set(count.values())) == len(count)
```

## 1372. Longest ZigZag Path in a Binary Tree [Medium]
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

Given the root of a binary tree, we need to find the longest ZigZag path. A ZigZag path is defined as alternating between going left and right. The path length is the number of nodes visited minus 1 (number of edges).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of nodes can be up to $5 \times 10^4$.
- **Value Range:** Node values are between $1$ and $10^5$.
- **Time Complexity:** $O(n)$ - We visit each node at most a constant number of times.
- **Space Complexity:** $O(h)$ where $h$ is the height of the tree. In the worst case (skewed tree), $h = n$, so $O(n)$.
- **Edge Case:** If the tree has only one node, return 0 (no edges). If the tree has no left or right children, return 0.

**1.2 High-level approach:**

The goal is to find the longest path that alternates between left and right directions.

We use DFS to explore all possible ZigZag paths. For each node, we track the direction we came from (left or right) and the current path length. We can either continue the current path or start a new path.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths and find the longest ZigZag one. This would be exponential.
- **Optimized Strategy (DFS):** Use DFS to explore paths, tracking direction and length. This takes $O(n)$ time.
- **Why it's better:** The DFS approach efficiently explores all paths in a single traversal, avoiding the need to generate all possible paths explicitly.

**1.4 Decomposition:**

1. Start DFS from root's left and right children (if they exist).
2. For each node, track the direction we came from (is_left) and current path length.
3. If coming from left, go right (extend path) or go left (start new path).
4. If coming from right, go left (extend path) or go right (start new path).
5. Update the maximum path length seen.
6. Return the maximum path length.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = $[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]$

We initialize:
- `res = 0`

**2.2 Start DFS:**

We begin DFS from root's children.

**2.3 Trace Walkthrough:**

Starting from root:
- Go left: DFS(root.left, is_left=True, length=1)
- Go right: DFS(root.right, is_left=False, length=1)

For each path:
- If coming from left and node has right child: extend path (length+1)
- If coming from left and node has left child: start new path (length=1)
- Similar logic for coming from right

**2.4 Explanation:**

The algorithm explores all possible ZigZag paths:
- Path 1: root → right → left → right → ... (extending)
- Path 2: root → right → right → left → ... (restarting)

We track the maximum length found.

**2.5 Return Result:**

We return the maximum ZigZag path length found.

> **Note:** The key insight is that at each node, we can either continue the current ZigZag path (if going in the opposite direction) or start a new path (if going in the same direction). We need to explore both possibilities to find the maximum.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root) -> int:
        res = 0
        
        def dfs(node, is_left, length):
            nonlocal res
            if not node:
                return
            
            res = max(res, length)
            
            if is_left:
                # Coming from left, go right
                dfs(node.right, False, length + 1)
                # Or start new path going left
                dfs(node.left, True, 1)
            else:
                # Coming from right, go left
                dfs(node.left, True, length + 1)
                # Or start new path going right
                dfs(node.right, False, 1)
        
        if root:
            dfs(root.left, True, 1)
            dfs(root.right, False, 1)
        
        return res
```

## 1431. Kids With the Greatest Number of Candies [Easy]
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

### Explanation

## 1431. Kids With the Greatest Number of Candies [Easy]

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

## Description
There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i`th kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

**Examples**

```text
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

**Constraints**

```text
- n == candies.length
- 2 <= n <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
```

## Hint
For each kid, check if their candies plus `extraCandies` is at least as much as the current maximum.

## Explanation
First, you want to know the highest number of candies any kid currently has. This is important because you need a reference point to see if giving extra candies to a kid will make them "the greatest."

For each kid, you add the `extraCandies` to their current amount. You do this because you want to see if, after the bonus, they can reach or beat the current maximum. If they do, you mark them as `True` in our answer list; otherwise, False.

You only need to find the maximum once, and then just compare each kid's total to it. Don't need to recalculate the maximum for every kid.

### Solution

```python
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Find the current maximum
    return [(c + extraCandies) >= max_candies for c in candies]
```

## 1448. Count Good Nodes in Binary Tree [Medium]
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The tree can have up to 10^5 nodes.
* **Time Complexity:** O(n) - We visit each node once using DFS, where n is the number of nodes.
* **Space Complexity:** O(h) for the recursion stack where h is the height. In worst case O(n).
* **Edge Case:** The root is always a good node since there are no nodes above it.

**1.2 High-level approach:**

The goal is to count nodes where the path from root to that node has no node with value greater than the current node. We use DFS to traverse the tree, tracking the maximum value seen so far.

![Tree traversal showing how we track maximum values along paths]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** For each node, check all nodes on the path from root to it. This is O(n^2) in worst case.
* **Optimized (DFS with Max Tracking):** During DFS, pass the maximum value seen so far. If current node's value >= max, it's good. This is O(n) time.
* **Why it's better:** We check the condition during traversal without storing paths, making it O(n) instead of O(n^2).

**1.4 Decomposition:**

1. Use DFS to traverse the tree.
2. For each node, check if its value >= max_value_seen.
3. If yes, increment the count and update max_value_seen.
4. Recursively process left and right children with updated max_value.
5. Return the total count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: root = [3,1,4,3,null,1,5]

We initialize:
* `res = 0`
* Start DFS from root with `max_val = 3` (root value)

**2.2 Start Checking/Processing:**

We call `dfs(root, root.val)`.

**2.3 Trace Walkthrough:**

| Node | Value | max_val | Value >= max? | Action | res |
|------|-------|---------|---------------|--------|-----|
| 3 | 3 | 3 | Yes | Count++, max=3 | 1 |
| 1 | 1 | 3 | No | Skip | 1 |
| 3 | 3 | 3 | Yes | Count++, max=3 | 2 |
| 4 | 4 | 3 | Yes | Count++, max=4 | 3 |
| 1 | 1 | 4 | No | Skip | 3 |
| 5 | 5 | 4 | Yes | Count++, max=5 | 4 |

**2.4 Increment and Loop:**

After processing each node, we recursively process its children.

**2.5 Return Result:**

After processing all nodes, `res = 4` is returned (nodes 3, 3, 4, and 5 are good).

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node, max_val):
            nonlocal res
            if not node:
                return
            
            if node.val >= max_val:
                res += 1
                max_val = node.val
            
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, root.val)
        return res
```

## 1515. Best Position for a Service Centre [Hard]
https://leetcode.com/problems/best-position-for-a-service-centre/

### Explanation

## 1515. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K [Medium]

https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k

## Description
Given an integer `k`, *return the minimum number of Fibonacci numbers whose sum is equal to* `k`. The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:

- `F₁ = 1`
- `F₂ = 1`
- `Fₙ = Fₙ₋₁ + Fₙ₋₂` for `n > 2`

It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to `k`.

**Examples**

```tex
Example 1:
Input: k = 7
Output: 2
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
For k = 7 we can use 2 + 5 = 7.

Example 2:
Input: k = 10
Output: 2
Explanation: For k = 10 we can use 2 + 8 = 10.

Example 3:
Input: k = 19
Output: 3
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
```

**Constraints**
```tex
- 1 <= k <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given a target integer `k`, and you need to find the minimum number of Fibonacci numbers that sum to `k`. You can use the same Fibonacci number multiple times, and it's guaranteed that a solution exists.

This is a **greedy problem** that can be solved by always choosing the largest possible Fibonacci number that doesn't exceed the remaining sum.

**What is given?** A target integer `k` that can be very large (up to 10⁹).

**What is being asked?** Find the minimum number of Fibonacci numbers that sum to `k`.

**Constraints:** The target `k` can be up to 10⁹, which means we need an efficient approach.

**Edge cases:** 
- `k = 1` (single Fibonacci number)
- `k` is itself a Fibonacci number
- `k` requires multiple Fibonacci numbers

**High-level approach:**
The solution involves generating Fibonacci numbers up to `k`, then using a greedy approach to always select the largest possible Fibonacci number that fits in the remaining sum.

**Decomposition:**
1. **Generate Fibonacci numbers**: Create all Fibonacci numbers up to `k`
2. **Greedy selection**: Always choose the largest Fibonacci number that fits
3. **Subtract and repeat**: Subtract the chosen number and continue until sum reaches 0
4. **Count operations**: Track how many Fibonacci numbers were used

**Brute force vs. optimized strategy:**
- **Brute force**: Try all combinations of Fibonacci numbers. This is extremely inefficient.
- **Optimized**: Use greedy approach with pre-generated Fibonacci numbers. This takes O(log k) time.

### Steps
Let's walk through the solution step by step using the first example: `k = 7`

**Step 1: Generate Fibonacci numbers up to k**
- Start with F₁ = 1, F₂ = 1
- F₃ = F₂ + F₁ = 1 + 1 = 2
- F₄ = F₃ + F₂ = 2 + 1 = 3
- F₅ = F₄ + F₃ = 3 + 2 = 5
- F₆ = F₅ + F₄ = 5 + 3 = 8 (exceeds 7, stop)
- Fibonacci numbers up to 7: [1, 1, 2, 3, 5]

**Step 2: Greedy selection process**
- **Remaining sum**: 7
- **Largest Fibonacci ≤ 7**: 5
- **Use 5**: 7 - 5 = 2
- **Count**: 1

- **Remaining sum**: 2
- **Largest Fibonacci ≤ 2**: 2
- **Use 2**: 2 - 2 = 0
- **Count**: 2

- **Remaining sum**: 0
- **Process complete**

**Step 3: Result**
- Total Fibonacci numbers used: 2
- Solution: 5 + 2 = 7

**Why this works:**
The greedy approach works because:
1. **Optimal substructure**: If we can represent `k` with `n` Fibonacci numbers, then representing `k - F_max` with `n-1` numbers must also be optimal
2. **Greedy choice property**: Always choosing the largest possible Fibonacci number ensures we use the minimum number of terms
3. **Fibonacci properties**: Each Fibonacci number is the sum of the two preceding ones, making the greedy choice optimal

> **Note:** The key insight is that using the largest possible Fibonacci number at each step minimizes the total count. This works because Fibonacci numbers have the property that no smaller combination can sum to a larger value more efficiently.

**Time Complexity:** O(log k) - we generate Fibonacci numbers up to k, which grows exponentially  
**Space Complexity:** O(log k) - we store the generated Fibonacci numbers

### Solution

```python
def findMinFibonacciNumbers(k):
    """
    Find the minimum number of Fibonacci numbers whose sum equals k.
    
    Args:
        k: int - Target sum to achieve
        
    Returns:
        int - Minimum number of Fibonacci numbers needed
    """
    # Generate Fibonacci numbers up to k
    fib_numbers = [1, 1]
    
    # Keep generating Fibonacci numbers until we exceed k
    while fib_numbers[-1] <= k:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > k:
            break
        fib_numbers.append(next_fib)
    
    # Use greedy approach: always choose largest possible Fibonacci number
    count = 0
    remaining = k
    
    # Start from the largest Fibonacci number and work backwards
    for i in range(len(fib_numbers) - 1, -1, -1):
        if fib_numbers[i] <= remaining:
            remaining -= fib_numbers[i]
            count += 1
            
            # If we've reached the target, we're done
            if remaining == 0:
                break
    
    return count
```

## 1657. Determine if Two Strings Are Close [Medium]
https://leetcode.com/problems/determine-if-two-strings-are-close/

### Explanation

## 1657. Determine if Two Strings Are Close [Medium]

https://leetcode.com/problems/determine-if-two-strings-are-close

## Description
Two strings are considered close if you can attain one from the other using the following operations:
- Operation 1: Swap any two existing characters (i.e., freely reorder the string).
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character (i.e., swap all a's with b's, and all b's with a's).
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

**Examples**
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

**Constraints**
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 contain only lowercase English letters.

## Hint
Operation 1 allows you to freely reorder the string. Operation 2 allows you to freely reassign the letters' frequencies.

## Explanation
To determine if two strings are close, you need to check two things:
1. Both strings must have the same set of unique characters. If one string has a character the other doesn't, you can't transform one into the other.
2. The frequency of each character (regardless of which character) must be the same in both strings. This is because you can swap the frequencies between characters using Operation 2, but you can't create or destroy frequencies.

This means you can sort the frequency counts of each string and compare them. If both the set of unique characters and the sorted frequency counts match, the strings are close.

### Solution

```python
def closeStrings(word1, word2):
    if set(word1) != set(word2):
        return False
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
```

## 1798. Maximum Number of Consecutive Values You Can Make [Medium]
https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

### Explanation

## 1798. Maximum Number of Consecutive Values You Can Make [Medium]

https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make

## Description

You are given an integer array `coins` of length `n` which represents the `n` coins that you own. The value of the `i`th coin is `coins[i]`. You can **make** some value `x` if you can choose some of your `n` coins such that their values sum up to `x`.

Return the *maximum number of consecutive integer values that you **can** **make** with your coins **starting** from and **including** 0*.

Note that you may have multiple coins of the same value.

**Examples**

**Example 1:**

    Input: coins = [1,3]
    Output: 2
    Explanation: You can make the following values:
    - 0: take []
    - 1: take [1]
    You can make 2 consecutive integer values starting from 0.

**Example 2:**

    Input: coins = [1,1,1,4]
    Output: 8
    Explanation: You can make the following values:
    - 0: take []
    - 1: take [1]
    - 2: take [1,1]
    - 3: take [1,1,1]
    - 4: take [4]
    - 5: take [4,1]
    - 6: take [4,1,1]
    - 7: take [4,1,1,1]
    You can make 8 consecutive integer values starting from 0.

**Example 3:**

    Input: coins = [1,4,10,3,1]
    Output: 20

**Constraints**

```
coins.length == n
1 <= n <= 4 * 10^4
1 <= coins[i] <= 4 * 10^4
```

## Explanation

### Strategy

Let's restate the problem:
- You have a set of coins, each with a positive integer value.
- You can use any subset of these coins (including none) to make sums.
- What is the largest number of *consecutive* values (starting from 0) you can make?

Consecutive is 0, 1, 2, ... So when you have coins `[1,2,3]`:

    - sum of them is 6
    - consecutive sequence will be up to `6` starting from `0`: `0, 1, 2, 3, 4, 5, 6` 

**Type:** Array, Greedy, Sorting

**What is given:**
- An array of positive integers (the coin values).

**What is asked:**
- The maximum number of consecutive values (starting from 0) you can make by summing up any subset of the coins.

**Constraints/Edge Cases:**
- Coins can have repeated values.
- The array can be large (up to 40,000 elements).
- All coin values are at least 1.

**High-level plan:**
- Sort the coins in ascending order.
- Track the smallest value you *cannot* make yet (let's call it `res`, start at 1).
- For each coin:
    - If the coin is greater than `res`, you can't make `res` (or anything larger), so stop.
    - Otherwise, you can now make all values up to `res + coin - 1`, so update `res += coin`.
- Return `res`.

### Steps

Let's walk through an example: `coins = [1, 1, 1, 4]`

1. **Sort the coins:** `[1, 1, 1, 4]`
2. **Initialize `res = 1`** (the smallest value we can't make yet)
3. **First coin (1):**
    - 1 <= (sequence value 1), so we can make 1. Now we can make all values up to 1 + 1 - 1 = 1.
    - Update `res = 2`.
4. **Second coin (1):**
    - 1 <= (sequence value 2), so we can make 2. Now we can make up to 2 + 1 - 1 = 2.
    - Update `res = 3`.
5. **Third coin (1):**
    - 1 <= (sequence value 3), so we can make 3. Now we can make up to 3 + 1 - 1 = 3.
    - Update `res = 4`.
6. **Fourth coin (4):**
    - 4 <= (sequence value 4), so we can make 4. Now we can make up to 4 + 4 - 1 = 7.
    - Update `res = 8`.
7. **No more coins.**

So, we can make all values from 0 to 7 (8 values).

**Another example:** `coins = [1, 3]`
- Sort: [1, 3]
- res = 1
- First coin: 1 <= 1 → res = 2
- Second coin: 3 > 2 → stop
- Answer: 2

**Key insight:**
> If you ever encounter a coin that is greater than the smallest value you can't make yet, you can't fill the gap, so you must stop.

### Solution

```python
def getMaximumConsecutive(coins):
    res = 1
    for coin in sorted(coins):
        if coin > res:
            break
        res += coin
    return res
```

## 1963. Minimum Number of Swaps to Make the String Balanced [Medium]
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

### Explanation

## 1963. Find XOR Sum of All Pairs Bitwise AND [Hard]

https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and

## Description
The **XOR sum** of a list is the bitwise `XOR` of all its elements. If the list only contains one element, then its **XOR sum** will be equal to this element.

- For example, the **XOR sum** of `[1,2,3,4]` is equal to `1 XOR 2 XOR 3 XOR 4 = 4`, and the **XOR sum** of `[3]` is equal to `3`.

You are given two **0-indexed** arrays `arr1` and `arr2` that consist only of non-negative integers.

Consider the list containing the result of `arr1[i] AND arr2[j]` (bitwise `AND`) for every `(i, j)` pair where `0 <= i < arr1.length` and `0 <= j < arr2.length`.

Return *the **XOR sum** of the aforementioned list*.

**Examples**

```tex
Example 1:
Input: arr1 = [1,2,3], arr2 = [6,5]
Output: 0
Explanation: The list = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1].
The XOR sum = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0.

Example 2:
Input: arr1 = [12], arr2 = [4]
Output: 4
Explanation: The list = [12 AND 4] = [4]. The XOR sum = 4.
```

**Constraints**
```tex
- 1 <= arr1.length, arr2.length <= 10^5
- 0 <= arr1[i], arr2[j] <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given two arrays, and you need to compute the XOR sum of all possible bitwise AND results between pairs of elements from the two arrays. This involves understanding bitwise operations and finding an efficient way to compute the result without explicitly generating all pairs.

This is a **bit manipulation problem** that requires understanding the properties of XOR and AND operations to find an optimized solution.

**What is given?** Two arrays of non-negative integers, each potentially up to 100,000 elements long.

**What is being asked?** Find the XOR sum of all possible bitwise AND results between pairs from the two arrays.

**Constraints:** The arrays can be very large (up to 100,000 elements each), with values up to 10⁹.

**Edge cases:** 
- Single element arrays
- Arrays with all zeros
- Arrays with identical values

**High-level approach:**
The solution involves using mathematical properties of XOR and AND operations to avoid explicitly computing all pairs. We can use the distributive property and XOR properties to simplify the computation.

**Decomposition:**
1. **Understand the problem**: We need to compute XOR of all (arr1[i] AND arr2[j]) pairs
2. **Use mathematical properties**: Leverage XOR and AND properties to simplify
3. **Compute XOR sums**: Find XOR sum of each array separately
4. **Apply final operation**: Use the relationship between the XOR sums

**Brute force vs. optimized strategy:**
- **Brute force**: Generate all pairs, compute AND, then XOR. This takes O(n*m) time.
- **Optimized**: Use mathematical properties to compute in O(n+m) time.

### Steps
Let's walk through the solution step by step using the first example: `arr1 = [1,2,3]`, `arr2 = [6,5]`

**Step 1: Understand what we need to compute**
- We need: (1 AND 6) XOR (1 AND 5) XOR (2 AND 6) XOR (2 AND 5) XOR (3 AND 6) XOR (3 AND 5)
- This equals: 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0

**Step 2: Use the key mathematical property**
- For any element `a` in arr1: (a AND b₁) XOR (a AND b₂) XOR ... XOR (a AND bₘ) = a AND (b₁ XOR b₂ XOR ... XOR bₘ)
- This is because: (a AND b) XOR (a AND c) = a AND (b XOR c)

**Step 3: Apply the property to our problem**
- For arr1[0] = 1: (1 AND 6) XOR (1 AND 5) = 1 AND (6 XOR 5)
- For arr1[1] = 2: (2 AND 6) XOR (2 AND 5) = 2 AND (6 XOR 5)
- For arr1[2] = 3: (3 AND 6) XOR (3 AND 5) = 3 AND (6 XOR 5)

**Step 4: Compute intermediate values**
- `arr2_xor_sum = 6 XOR 5 = 3`
- `arr1_xor_sum = 1 XOR 2 XOR 3 = 0`

**Step 5: Apply the final relationship**
- Final result = (1 AND 3) XOR (2 AND 3) XOR (3 AND 3)
- = 1 XOR 2 XOR 3 = 0

**Why this works:**
The key insight is the distributive property of AND over XOR:
1. **Distributive property**: `(a AND b) XOR (a AND c) = a AND (b XOR c)`
2. **XOR properties**: XOR is associative and commutative
3. **Elimination**: We can eliminate the need to compute all pairs explicitly

> **Note:** The key insight is that we can compute the XOR sum of arr2 first, then for each element in arr1, compute its AND with the XOR sum, and finally XOR all these results together. This reduces the complexity from O(n*m) to O(n+m).

**Time Complexity:** O(n + m) - we only need to iterate through each array once  
**Space Complexity:** O(1) - we only need a few variables to store the XOR sums

### Solution

```python
def getXORSum(arr1, arr2):
    """
    Find the XOR sum of all pairs bitwise AND results.
    
    Args:
        arr1: List[int] - First array of integers
        arr2: List[int] - Second array of integers
        
    Returns:
        int - XOR sum of all (arr1[i] AND arr2[j]) pairs
    """
    # Compute XOR sum of arr2
    arr2_xor_sum = 0
    for num in arr2:
        arr2_xor_sum ^= num
    
    # For each element in arr1, compute (element AND arr2_xor_sum)
    # Then XOR all these results together
    result = 0
    for num in arr1:
        result ^= (num & arr2_xor_sum)
    
    return result
```

## 2095. Delete the Middle Node of a Linked List [Medium]
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The linked list can have up to 10^5 nodes.
* **Time Complexity:** O(n) - We traverse the list once to find the middle, where n is the number of nodes.
* **Space Complexity:** O(1) - We only use a constant amount of extra space for pointers.
* **Edge Case:** If the list has 0 or 1 node, return None (no middle node to delete).

**1.2 High-level approach:**

The goal is to delete the middle node of a linked list. The middle node is at index floor(n/2) using 0-based indexing. We use the two-pointer technique to find the middle node.

![Two-pointer technique showing fast and slow pointers finding the middle]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Traverse the list to count nodes, then traverse again to find and delete the middle node. This requires two passes.
* **Optimized (Two Pointers):** Use fast and slow pointers. When fast reaches the end, slow is at the middle. This is one pass.
* **Why it's better:** The two-pointer approach finds the middle in one pass, making it more efficient.

**1.4 Decomposition:**

1. Handle edge cases: if list has 0 or 1 node, return None.
2. Use two pointers: slow and fast, both starting at head.
3. Also track prev to point to the node before slow.
4. Move fast two steps and slow one step until fast reaches the end.
5. Delete the middle node by setting prev.next = slow.next.
6. Return head.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: head = [1,3,4,7,1,2,6]

We initialize:
* `slow = head` (node 1)
* `fast = head` (node 1)
* `prev = None`

**2.2 Start Checking/Processing:**

We enter a while loop while `fast` and `fast.next` exist.

**2.3 Trace Walkthrough:**

| Step | slow.val | fast.val | prev.val | Action |
|------|----------|----------|----------|--------|
| Initial | 1 | 1 | None | Setup |
| 1 | 3 | 4 | 1 | Move pointers |
| 2 | 4 | 1 | 3 | Move pointers |
| 3 | 7 | 2 | 4 | Move pointers |
| 4 | 1 | 6 | 7 | fast.next is None, stop |
| Final | 7 | - | 4 | Delete: prev.next = slow.next |

**2.4 Increment and Loop:**

After each iteration, we update prev = slow, then move slow and fast.

**2.5 Return Result:**

After deletion, the list is [1,3,4,1,2,6], and head is returned.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return head
```

## 2119. A Number After a Double Reversal [Easy]
https://leetcode.com/problems/a-number-after-a-double-reversal/

### Explanation

## 2119. Minimum Number of Operations to Make Array Continuous [Hard]

https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous

## Description
You are given an integer array `nums`. In one operation, you can replace **any** element in `nums` with **any** integer.

`nums` is considered **continuous** if both of the following conditions are fulfilled:

- All elements in `nums` are **unique**.
- The difference between the **maximum** element and the **minimum** element in `nums` equals `nums.length - 1`.

For example, `nums = [4, 2, 5, 3]` is **continuous**, but `nums = [1, 2, 3, 5, 6]` is **not continuous**.

Return *the **minimum** number of operations to make* `nums` **continuous**.

**Examples**

```tex
Example 1:
Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.

Example 2:
Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

Example 3:
Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.
```

**Constraints**
```tex
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given an array, and you need to find the minimum number of operations to make it continuous. A continuous array has unique elements where the difference between max and min equals the length minus 1.

This is a **sliding window problem** that requires understanding what makes an array continuous and finding the optimal window of elements to keep.

**What is given?** An array of integers that can be very large (up to 100,000 elements).

**What is being asked?** Find the minimum operations to make the array continuous.

**Constraints:** The array can be up to 100,000 elements long, with values up to 10⁹.

**Edge cases:** 
- Single element array
- Already continuous array
- Array with all identical values
- Very large gaps between elements

**High-level approach:**
The solution involves sorting the array and using a sliding window approach to find the optimal subset of elements that can form a continuous array with minimal operations.

**Decomposition:**
1. **Sort the array**: This helps us identify potential continuous subsequences
2. **Use sliding window**: Find the longest window that can be made continuous
3. **Calculate operations**: Determine how many elements need to be changed
4. **Find minimum**: Try different window sizes to find the optimal solution

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible subsets. This is extremely inefficient.
- **Optimized**: Use sliding window with binary search. This takes O(n log n) time.

### Steps
Let's walk through the solution step by step using the second example: `nums = [1,2,3,5,6]`

**Step 1: Sort the array**
- Original: [1,2,3,5,6]
- Sorted: [1,2,3,5,6] (already sorted)

**Step 2: Understand what makes an array continuous**
- For length 5, we need: max - min = 5 - 1 = 4
- So we need elements that span exactly 4 values
- Example: [1,2,3,4,5] has max=5, min=1, difference=4 ✓

**Step 3: Use sliding window approach**
- Start with window size = array length
- Try to find a window that can be made continuous
- For each window, calculate how many operations are needed

**Step 4: Calculate operations for different windows**
- **Window [1,2,3,5,6]**: 
  - Current span: 6 - 1 = 5
  - Need span: 5 - 1 = 4
  - Gap: 5 - 4 = 1
  - Operations needed: 1 (change 6 to 4)

- **Window [1,2,3,5]**:
  - Current span: 5 - 1 = 4
  - Need span: 4 - 1 = 3
  - Gap: 4 - 3 = 1
  - Operations needed: 1 (change 5 to 3)

- **Window [2,3,5,6]**:
  - Current span: 6 - 2 = 4
  - Need span: 4 - 1 = 3
  - Gap: 4 - 3 = 1
  - Operations needed: 1 (change 6 to 4)

**Step 5: Find optimal solution**
- Minimum operations: 1
- Optimal window: [1,2,3,5] → change 5 to 4 → [1,2,3,4]

**Why this works:**
The sliding window approach works because:
1. **Optimal substructure**: The best solution for a larger array must include the best solution for a smaller subarray
2. **Monotonicity**: If a window of size k can be made continuous, then a window of size k-1 can also be made continuous
3. **Efficiency**: We only need to check O(n) different window sizes instead of all possible subsets

> **Note:** The key insight is that we can use a sliding window to find the longest subsequence that can be made continuous, and then calculate the minimum operations needed. This avoids the need to try all possible combinations.

**Time Complexity:** O(n log n) - sorting takes O(n log n), sliding window takes O(n)  
**Space Complexity:** O(1) - we only need a few variables for the sliding window

### Solution

```python
def minOperations(nums):
    """
    Find the minimum number of operations to make the array continuous.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int - Minimum number of operations needed
    """
    # Handle edge case
    if len(nums) <= 1:
        return 0
    
    # Sort the array to work with ordered elements
    nums.sort()
    
    # Remove duplicates to work with unique elements
    unique_nums = []
    for i, num in enumerate(nums):
        if i == 0 or num != nums[i-1]:
            unique_nums.append(num)
    
    n = len(unique_nums)
    min_operations = float('inf')
    
    # Try different window sizes
    for i in range(n):
        # For each starting position, find the longest window that can be made continuous
        left = unique_nums[i]
        
        # Binary search for the rightmost element that can be part of a continuous sequence
        # starting from left
        right = left + len(nums) - 1
        
        # Find how many elements in unique_nums fall within [left, right]
        # This gives us the size of the window that can be made continuous
        count = 0
        for j in range(i, n):
            if unique_nums[j] <= right:
                count += 1
            else:
                break
        
        # Calculate operations needed
        # We need to change (len(nums) - count) elements
        operations = len(nums) - count
        min_operations = min(min_operations, operations)
    
    return min_operations
```

## 2130. Maximum Twin Sum of a Linked List [Medium]
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** The linked list has an even number of nodes, up to 10^5.
* **Time Complexity:** O(n) - We traverse the list to find the middle, reverse the second half, and compare pairs, where n is the number of nodes.
* **Space Complexity:** O(1) - We only use a constant amount of extra space for pointers.
* **Edge Case:** If the list has 2 nodes, return the sum of their values.

**1.2 High-level approach:**

The goal is to find the maximum sum of twin pairs. Twins are nodes at positions i and n-1-i. We split the list at the middle, reverse the second half, then compare pairs.

![Linked list showing twin pairs and their sums]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Store all node values in an array, then calculate all twin sums. This uses O(n) extra space.
* **Optimized (In-place Reversal):** Find the middle, reverse the second half in-place, then traverse both halves simultaneously to find max sum. This uses O(1) extra space.
* **Why it's better:** The in-place approach meets the O(1) space requirement and is more memory efficient.

**1.4 Decomposition:**

1. Use two pointers to find the middle of the list.
2. Reverse the second half of the list.
3. Traverse both halves simultaneously, calculating twin sums.
4. Track and return the maximum sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: head = [5,4,2,1]

We initialize:
* Find middle: after two-pointer, slow points to node 2 (middle).

**2.2 Start Checking/Processing:**

We reverse the second half starting from slow.

**2.3 Trace Walkthrough:**

| Step | First Half | Second Half (reversed) | Twin Sum | Max |
|------|------------|------------------------|----------|-----|
| Initial | [5,4] | [2,1] → reverse → [1,2] | - | 0 |
| 1 | 5 | 1 | 5+1=6 | 6 |
| 2 | 4 | 2 | 4+2=6 | 6 |

**2.4 Increment and Loop:**

After calculating each twin sum, we move both pointers forward and update the maximum.

**2.5 Return Result:**

After processing all pairs, `res = 6` is returned (both pairs sum to 6).

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        res = 0
        first = head
        second = prev
        while second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next
        
        return res
```

## 2215. Find the Difference of Two Arrays [Easy]
https://leetcode.com/problems/find-the-difference-of-two-arrays/

### Explanation

## 2215. Find the Difference of Two Arrays [Easy]

https://leetcode.com/problems/find-the-difference-of-two-arrays

## Description
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

**Examples**
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]

**Constraints**
- 1 <= nums1.length, nums2.length <= 1000
- -1000 <= nums1[i], nums2[i] <= 1000

## Hint
Use sets to efficiently find unique elements in each array.

## Explanation
Let's imagine you have two boxes of colored marbles (numbers). You want to find out which colors are only in the first box and which are only in the second. We use sets to quickly check for unique marbles in each box.

We do this because sets make it easy and fast to find differences—checking if something is in a set is much quicker than searching through a list. By converting the lists to sets, we can use set operations to get the answer efficiently.

### Solution

```python
def findDifference(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    return [list(set1 - set2), list(set2 - set1)]
```

## 2336. Smallest Number in Infinite Set [Medium]
https://leetcode.com/problems/smallest-number-in-infinite-set/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** At most 1000 calls to popSmallest and addBack. Numbers are between 1 and 1000.
* **Time Complexity:** O(log k) for popSmallest and addBack where k is the number of added-back numbers. O(1) for the infinite set part.
* **Space Complexity:** O(k) where k is the number of distinct numbers that have been popped and added back.
* **Edge Case:** If we pop all numbers 1-1000 and add some back, those added-back numbers should be returned before continuing with 1001+.

**1.2 High-level approach:**

The goal is to implement a set that contains all positive integers, with operations to pop the smallest and add numbers back. We use a min-heap for added-back numbers and track the next number in the infinite sequence.

![Data structure showing heap for added-back numbers and counter for infinite sequence]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Store all popped numbers in a set, then for popSmallest, iterate from 1 to find the first not in the set. This is O(n) per pop.
* **Optimized (Heap + Counter):** Use a min-heap for added-back numbers and a counter for the infinite sequence. popSmallest returns min(heap.pop(), counter++). This is O(log k) per pop.
* **Why it's better:** The heap allows O(log k) access to the minimum added-back number, and the counter handles the infinite sequence in O(1).

**1.4 Decomposition:**

1. Maintain a min-heap for numbers that were popped and added back.
2. Maintain a counter (next_num) for the infinite sequence starting from 1.
3. Maintain a set to track which numbers are currently removed.
4. For popSmallest: if heap is not empty, pop from heap; otherwise, return and increment counter.
5. For addBack: if number is in removed set, add it to heap and remove from set.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

We initialize:
* `removed = set()` (track removed numbers)
* `added_back = []` (min-heap)
* `next_num = 1` (next number in infinite sequence)

**2.2 Start Checking/Processing:**

Operations are called: addBack(2), popSmallest(), popSmallest(), popSmallest(), addBack(1), popSmallest()

**2.3 Trace Walkthrough:**

| Operation | added_back | next_num | removed | Return |
|-----------|------------|----------|---------|--------|
| addBack(2) | [] | 1 | {} | None (2 already in set) |
| popSmallest() | [] | 1 | {1} | 1, next_num=2 |
| popSmallest() | [] | 2 | {1,2} | 2, next_num=3 |
| popSmallest() | [] | 3 | {1,2,3} | 3, next_num=4 |
| addBack(1) | [1] | 4 | {2,3} | None |
| popSmallest() | [] | 4 | {2,3,1} | 1 (from heap), next_num=4 |

**2.4 Increment and Loop:**

After each operation, we update the data structures accordingly.

**2.5 Return Result:**

The operations return [null, 1, 2, 3, null, 1] as expected.

### Solution

```python
def __init__(self):
        self.removed = set()
        self.added_back = []
        self.next_num = 1

    def popSmallest(self) -> int:
        if self.added_back:
            res = heapq.heappop(self.added_back)
            self.removed.add(res)
            return res
        else:
            res = self.next_num
            self.next_num += 1
            self.removed.add(res)
            return res

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            heapq.heappush(self.added_back, num)
```

## 2352. Equal Row and Column Pairs [Medium]
https://leetcode.com/problems/equal-row-and-column-pairs/

### Explanation

## 2352. Equal Row and Column Pairs [Medium]

https://leetcode.com/problems/equal-row-and-column-pairs

## Description
Given a 0-indexed n x n integer matrix grid, return the number of pairs (r_i, c_j) such that row r_i and column c_j are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

**Examples**
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

**Constraints**
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5

## Hint
We can use nested loops to compare every row against every column. Another loop is necessary to compare the row and column element by element. It is also possible to hash the arrays and compare the hashed values instead.

## Explanation
To count equal row and column pairs, we can compare each row with each column. For each row, we check if it matches any column by comparing their elements one by one. To make this efficient, we can use tuples or hashable representations of rows and columns and count their occurrences. If a row matches a column, we increment our answer.

This approach is efficient for n up to 200, and using hash maps or tuples makes the comparison fast and easy to implement.

### Solution

```python
def equalPairs(grid):
    n = len(grid)
    row_counts = Counter(tuple(row) for row in grid)
    col_counts = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
    return sum(row_counts[row] * col_counts[row] for row in row_counts)
```

## 2627. Debounce [Medium]
https://leetcode.com/problems/debounce/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `0 <= t <= 1000`, `1 <= calls.length <= 10`.
- **Time Complexity:** O(1) per call - setTimeout/clearTimeout are O(1).
- **Space Complexity:** O(1) - we store one timeout ID.
- **Edge Case:** Multiple rapid calls, only the last one executes.

**1.2 High-level approach:**
The goal is to implement a debounce function that delays execution and cancels previous pending executions. We use setTimeout to delay, and clearTimeout to cancel previous timeouts.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - debounce pattern is standard.
- **Optimized Strategy:** Store timeout ID, clear on new call, set new timeout.

**1.4 Decomposition:**
1. Maintain a timeout ID variable.
2. When function is called, clear any existing timeout.
3. Set a new timeout to execute the function after delay `t`.
4. Return the debounced function.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `t = 50`, calls at times 50 and 75. We want the function to execute only once at time 125.

**2.2 Start Checking:**
We track timeout IDs and clear/set them appropriately.

**2.3 Trace Walkthrough:**

| Time | Call | Action | Timeout ID | Execution Time |
|------|------|--------|------------|----------------|
| 50 | dlog(1) | Set timeout | id1 | 100 (cancelled) |
| 75 | dlog(2) | Clear id1, set timeout | id2 | 125 |

**2.4 Increment and Loop:**
Not applicable - this handles individual calls.

**2.5 Return Result:**
Function executes at time 125 with input 2.

### Solution

```python
def debounce(self, fn, t):
        timeout_id = None
        
        def debounced(*args, **kwargs):
            nonlocal timeout_id
            if timeout_id:
                timeout_id.cancel()
            timeout_id = Timer(t / 1000.0, lambda: fn(*args, **kwargs))
            timeout_id.start()
        
        return debounced
```

## 2723. Add Two Promises [Easy]
https://leetcode.com/problems/add-two-promises/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** Two promises that resolve with numbers.
- **Time Complexity:** O(1) - we wait for both promises and add their values.
- **Space Complexity:** O(1) - constant space.
- **Edge Case:** Promises might resolve at different times.

**1.2 High-level approach:**
The goal is to return a new promise that resolves with the sum of two input promises. We use `Promise.all()` to wait for both promises, then add their resolved values.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - Promise.all() is the standard approach.
- **Optimized Strategy:** Use async/await with Promise.all() for clean code.

**1.4 Decomposition:**
1. Wait for both promises to resolve using Promise.all().
2. Extract the resolved values.
3. Add them together.
4. Return the sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `promise1` resolves to 2, `promise2` resolves to 5. We want to return a promise that resolves to 7.

**2.2 Start Checking:**
We await both promises and add their values.

**2.3 Trace Walkthrough:**

| Step | Operation | Result |
|------|-----------|--------|
| 1 | await Promise.all([promise1, promise2]) | [2, 5] |
| 2 | val1 = 2, val2 = 5 | - |
| 3 | res = 2 + 5 | 7 |

**2.4 Increment and Loop:**
Not applicable - this is a single async operation.

**2.5 Return Result:**
Return a promise that resolves to `res = 7`.

### Solution

```python
def addTwoPromises(self, promise1, promise2):
        val1 = await promise1
        val2 = await promise2
        res = val1 + val2
        return res
```

## 2807. Insert Greatest Common Divisors in Linked List [Medium]
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

### Explanation

## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nodes <= 5000`, `1 <= Node.val <= 1000`.
- **Time Complexity:** O(n) where n is the number of nodes - we visit each node once.
- **Space Complexity:** O(1) - we only create new nodes, no additional data structures.
- **Edge Case:** Single node list, no insertion needed.

**1.2 High-level approach:**
The goal is to insert a new node between every pair of adjacent nodes, where the new node's value is the GCD of the two adjacent nodes' values. We traverse the list and insert nodes as we go.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we must visit each node once.
- **Optimized Strategy:** Traverse the list once, calculating GCD and inserting nodes in-place.

**1.4 Decomposition:**
1. Implement GCD calculation using Euclidean algorithm.
2. Traverse the linked list.
3. For each pair of adjacent nodes, calculate their GCD.
4. Create a new node with the GCD value.
5. Insert it between the two nodes.
6. Continue to the next pair.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `head = [18,6,10,3]`. We start at the first node.

**2.2 Start Checking:**
We process each adjacent pair of nodes.

**2.3 Trace Walkthrough:**

| Current | Next | GCD(18,6) | GCD(6,10) | GCD(10,3) | Result |
|---------|------|-----------|-----------|-----------|--------|
| 18 | 6 | 6 | - | - | [18,6,6,...] |
| 6 | 10 | - | 2 | - | [18,6,6,2,10,...] |
| 10 | 3 | - | - | 1 | [18,6,6,2,10,1,3] |

**2.4 Increment and Loop:**
After inserting a node, we move to the node after the inserted one and continue.

**2.5 Return Result:**
Return the modified list `[18,6,6,2,10,1,3]` with GCD nodes inserted.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        current = head
        while current and current.next:
            # Calculate GCD of current and next node values
            gcd_value = gcd(current.val, current.next.val)
            
            # Create new node with GCD value
            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            
            # Move to the node after the inserted node
            current = new_node.next
        
        return head
```

## 2862. Maximum Element-Sum of a Complete Subset of Indices [Hard]
https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

### Explanation

## 2862. Maximum Element-Sum of a Complete Subset of Indices (Hard)

https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices

## Description

You are given a **1-indexed** array `nums`. Your task is to select a **complete subset** from `nums` where every pair of selected indices multiplied is a perfect square, i.e., if you select `a_i` and `a_j`, `i * j` must be a perfect square.

Return the *sum* of the complete subset with the *maximum sum*.

**Examples**

**Example 1:**

    Input: nums = [8,7,3,5,7,2,4,9]
    Output: 16
    Explanation: We select elements at indices 2 and 8 and 2 * 8 is a perfect square.

**Example 2:**

    Input: nums = [8,10,3,8,1,13,7,9,4]
    Output: 20
    Explanation: We select elements at indices 1, 4, and 9. 1 * 4, 1 * 9, 4 * 9 are perfect squares.

**Constraints**

```text
1 <= n == nums.length <= 10^4
1 <= nums[i] <= 10^9
```

## Explanation

### Strategy

Let's restate the problem:
- You have a 1-indexed array `nums`.
- You want to select a subset of indices such that for every pair `(i, j)` in the subset, `i * j` is a perfect square.
- What is the maximum possible sum of the elements at those indices?

**Type:** Array, Math, Number Theory

**What is given:**
- An array of positive integers (the values).

**What is asked:**
- The maximum sum of a complete subset (as defined above).

**Constraints/Edge Cases:**
- Array can be large (up to 10,000 elements).
- All values are positive integers.

**High-level plan:**
- For each index, compute its "key" (the product of primes with odd exponents in its factorization).
- Group indices by key, sum the corresponding values, and return the maximum sum.
- Alternatively, for each possible starting index, consider the sequence `i * m^2` and sum the values.

### Steps

Let's walk through an example: `nums = [8, 7, 3, 5, 7, 2, 4, 9]`

1. For each index, compute its key:
    - Index 1: key = 1
    - Index 2: key = 2
    - Index 3: key = 3
    - Index 4: key = 1 (since 4 = 2^2)
    - ...
2. Group indices by key and sum the corresponding values:
    - key 1: indices 1, 4, ...
    - key 2: indices 2, ...
    - ...
3. The answer is the maximum sum among all groups.

> Indices with the same key can be grouped together, and their products will always be perfect squares.

### Solution

```python
def maximumSum(nums):
    count = Counter()
    for i in range(len(nums)):
        x, v = i + 1, 2
        while x >= v * v:
            while x % (v * v) == 0:
                x //= v * v
            v += 1
        count[x] += nums[i]
    return max(count.values())
```

## 3607. Power Grid Maintenance [Medium]
https://leetcode.com/problems/power-grid-maintenance/

### Explanation

## 3607. Power Grid Maintenance [Medium]

https://leetcode.com/problems/power-grid-maintenance

## Description

You are given an integer `c` representing `c` power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing).

These stations are interconnected via `n` **bidirectional** cables, represented by a 2D array `connections`, where each element `connections[i] = [u_i, v_i]` indicates a connection between station `u_i` and station `v_i`. Stations that are directly or indirectly connected form a **power grid**.

Initially, **all** stations are online (operational).

You are also given a 2D array `queries`, where each query is one of the following two types:

- `[1, x]`: A maintenance check is requested for station `x`. If station `x` is online, it resolves the check by itself. If station `x` is offline, the check is resolved by the operational station with the smallest `id` in the same **power grid** as `x`. If **no** operational station exists in that grid, return -1.
- `[2, x]`: Station `x` goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type `[1, x]` in the **order** they appear.

**Note:** The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

**Examples**

**Example 1:**

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:
- Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
- Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
- Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
- Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
- Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
- Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.

**Example 2:**

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:
- There are no connections, so each station is its own isolated grid.
- Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
- Query [2,1]: Station 1 goes offline.
- Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.

**Constraints**
```text
1 <= c <= 10^5
0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)
connections[i].length == 2
1 <= u_i, v_i <= c
u_i != v_i
1 <= queries.length <= 2 * 10^5
queries[i].length == 2
queries[i][0] is either 1 or 2.
1 <= queries[i][1] <= c
```

## Explanation

### Strategy

Let's restate the problem:
- We have a set of power stations connected by cables, forming one or more power grids (connected components).
- Each station can go offline, but the grid structure does not change.
- For a maintenance check, if the station is online, it handles the check; if offline, the smallest online station in the same grid handles it (or -1 if none).

**Type:** Graph, Union Find, Heap, DFS, Ordered Set

**What is being asked?**
- Efficiently answer queries about which station can handle a maintenance check, considering online/offline status and grid structure.

**What is given?**
- Number of stations, connections, and a list of queries.

**Constraints/Edge Cases:**
- Up to 10^5 stations and 2*10^5 queries.
- Stations can go offline, but the grid structure is static.

**High-Level Plan:**
- Precompute connected components (power grids) using DFS or Union Find (DSU).
- For each component, maintain a data structure (set, heap, or sorted list) of online stations.
- For type 1 queries, if the station is online, return it; otherwise, return the smallest online station in its component, or -1 if none.
- For type 2 queries, mark the station as offline (remove from set/heap/list or mark in a boolean array).

### Steps

1. **Build the graph and find connected components:**
   - Use DFS or DSU to assign each station a component ID.
2. **For each component, track online stations:**
   - Use a set, heap, or sorted list for fast lookup of the smallest online station.
3. **Process queries:**
   - For `[1, x]`, if `x` is online, return `x`; else, return the smallest online station in the same component, or -1 if none.
   - For `[2, x]`, mark `x` as offline.

**Example Walkthrough:**

Suppose c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

- All stations are online and form a single grid.
- [1,3]: 3 is online → return 3
- [2,1]: 1 goes offline
- [1,1]: 1 is offline, smallest online in grid is 2 → return 2
- [2,2]: 2 goes offline
- [1,2]: 2 is offline, smallest online in grid is 3 → return 3

> **Note:** The grid structure is static; only online/offline status changes.

### Solution

```python
def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px


class Solution:
    def processQueries(self, n, connections, queries):
        dsu = DSU(n)
        online = [True] * (n + 1)
        for u, v in connections:
            dsu.union(u, v)
        component_heap = defaultdict(list)
        for station in range(1, n + 1):
            root = dsu.find(station)
            heapq.heappush(component_heap[root], station)
        result = []
        for typ, x in queries:
            if typ == 2:
                online[x] = False
            else:
                if online[x]:
                    result.append(x)
                else:
                    root = dsu.find(x)
                    heap = component_heap[root]
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    result.append(heap[0] if heap else -1)
        return result
```

## 3608. Minimum Time for K Connected Components [Medium]
https://leetcode.com/problems/minimum-time-for-k-connected-components/

### Explanation

## 3608. Minimum Time for K Connected Components [Medium]

https://leetcode.com/problems/minimum-time-for-k-connected-components

## Description
You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [u_i, v_i, time_i] indicates an undirected edge between nodes u_i and v_i that can be removed at time_i.

You are also given an integer k.

Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t, the graph contains at least k connected components.

Return the minimum time t.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

## Examples

**Example 1**
Input:
n = 2
edges = [[0,1,3]]
k = 2

Output:
3

Explanation:
- Initially, there is one connected component {0, 1}.
- At time = 1 or 2, the graph remains unchanged.
- At time = 3, edge [0, 1] is removed, resulting in k = 2 connected components {0}, {1}. Thus, the answer is 3.

**Example 2**
Input:
n = 3
edges = [[0,1,2],[1,2,4]]
k = 3

Output:
4

Explanation:
- Initially, there is one connected component {0, 1, 2}.
- At time = 2, edge [0, 1] is removed, resulting in two connected components {0}, {1, 2}.
- At time = 4, edge [1, 2] is removed, resulting in k = 3 connected components {0}, {1}, {2}. Thus, the answer is 4.

**Example 3**
Input:
n = 3
edges = [[0,2,5]]
k = 2

Output:
0

Explanation:
- Since there are already k = 2 disconnected components {1}, {0, 2}, no edge removal is needed. Thus, the answer is 0.

## Constraints
```
- 1 <= n <= 10^5
- 0 <= edges.length <= 10^5
- edges[i] = [u_i, v_i, time_i]
- 0 <= u_i, v_i < n
- u_i != v_i
- 1 <= time_i <= 10^9
- 1 <= k <= n
- There are no duplicate edges.
```

## Explanation

**Intuition**

We want to find the minimum time t such that, after removing all edges with time <= t, the graph splits into at least k connected components. This is a classic application of binary search combined with union-find (DSU) to efficiently count components after edge removals.

**Approach**

1. **Binary Search:**
   - Sort all unique edge times and use binary search to find the smallest t such that the number of connected components is at least k after removing all edges with time <= t.
2. **Union-Find (DSU):**
   - For each candidate t, use union-find to connect all nodes with edges having time > t, then count the number of connected components.
3. **Edge Cases:**
   - If the initial graph already has at least k components, return 0.

### Solution

```python
def count_components(n, edges_by_time, t):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    for u, v, time in edges_by_time:
        if time > t:
            union(u, v)
    comps = set(find(i) for i in range(n))
    return len(comps)


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if k == n:
            return 0
        if not edges:
            return 0 if k <= n else -1
        edges_by_time = sorted(edges, key=lambda x: x[2])
        lo, hi = 0, max(e[2] for e in edges)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            comps = count_components(n, edges_by_time, mid)
            if comps >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## 3623. Count Number of Trapezoids I [Medium]
https://leetcode.com/problems/count-number-of-trapezoids-i/

### Explanation

## Explanation

### Strategy

Let's restate the problem:
- We are given a set of points on a 2D plane.
- We want to count the number of ways to pick 4 distinct points that form a convex quadrilateral with at least one pair of horizontal sides (i.e., two sides parallel to the x-axis).

**Type:** Geometry, Combinatorics, Hash Map

**What is being asked?**
- Count the number of unique horizontal trapezoids (convex quadrilaterals with at least one pair of horizontal sides) that can be formed from the given points.

**What is given?**
- A list of points, all distinct.

**Constraints/Edge Cases:**
- Large input size (up to 10^5 points).
- All points are distinct.

**Why is the naive approach too slow?**
- The naive approach groups points by y-coordinate, then for every pair of y-levels, multiplies the number of ways to pick 2 points from each. This is O(K^2) where K is the number of y-levels with at least 2 points. For large K, this is too slow and leads to TLE.

**Optimized Plan:**
- Instead of iterating over all pairs, use the mathematical identity:
  - The total number of unordered pairs of y-levels is C(K,2).
  - If we precompute the number of ways to pick 2 points from each y-level (call this list `pairs`), then the sum over all pairs is:
    - sum_{i<j} pairs[i] * pairs[j] = (total_sum^2 - sum_of_squares) // 2
  - Where total_sum = sum(pairs), sum_of_squares = sum(x*x for x in pairs).
- This reduces the time complexity to O(N + K), which is efficient for large inputs.

### Steps

1. **Group points by y-coordinate:**
   - Use a hash map to group all points with the same y.
2. **For each group, count the number of ways to pick 2 points:**
   - For a group of size c, the number of ways to pick 2 points is C(c, 2) = c * (c-1) // 2.
   - Only consider groups with at least 2 points.
3. **Sum up all C(c,2) values:**
   - Let `pairs` be the list of C(c,2) for each y-level with at least 2 points.
4. **Compute the total number of trapezoids:**
   - Use the formula: res = (total_sum^2 - sum_of_squares) // 2
   - Return res modulo 10^9 + 7.

> **Note:**
> - We only consider y-levels with at least 2 points.
> - The order of y-levels does not matter (unordered pairs).
> - This approach avoids the O(K^2) double loop and is much faster.

#### Example Walkthrough
Suppose points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
- y=0: [1,0], [2,0], [3,0] (3 points)
- y=2: [2,2], [3,2] (2 points)
- C(3,2) = 3, C(2,2) = 1
- pairs = [3, 1]
- total_sum = 4, sum_of_squares = 9 + 1 = 10
- res = (4*4 - 10) // 2 = (16 - 10) // 2 = 3

### Complexity Analysis
- **Time Complexity:** O(N + K), where N is the number of points and K is the number of y-levels with at least 2 points.
- **Space Complexity:** O(N) for storing the groups.

```text
| Step | Operation         | Count |
| ---- | ----------------- | ----- |
| 1    | Group points by y | N     |
| 2    | Compute C(c,2)    | K     |
| 3    | Math formula      | K     |
```

### Solution

```python
def countTrapezoids(points):
    y_groups = defaultdict(int)
    for x, y in points:
        y_groups[y] += 1
    pairs = []
    for c in y_groups.values():
        if c >= 2:
            pairs.append(c * (c - 1) // 2)
    total_sum = sum(pairs)
    sum_of_squares = sum(x * x for x in pairs)
    res = (total_sum * total_sum - sum_of_squares) // 2
    return res % MOD
```
