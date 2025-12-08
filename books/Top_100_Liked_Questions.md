# Top 100 Liked Questions

Problem list from official https://leetcode.com/studyplan/top-100-liked/

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
