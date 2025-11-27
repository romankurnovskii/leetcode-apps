# LeetCode 75

Problem list from official https://leetcode.com/studyplan/leetcode-75/

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
