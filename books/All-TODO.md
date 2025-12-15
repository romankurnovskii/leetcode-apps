# All-TODO



## 237. Delete Node in a Linked List [Medium]
https://leetcode.com/problems/delete-node-in-a-linked-list/

### Explanation

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

### Solution

```python
def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy value from next node
        node.val = node.next.val
        # Skip next node
        node.next = node.next.next
```

## 1008. Construct Binary Search Tree from Preorder Traversal [Medium]
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

### Explanation

## Explanation

### Strategy

**Restate the problem**  
Given preorder traversal of a BST, reconstruct the tree.

**1.1 Constraints & Complexity**  
- **Input Size:** up to 100 nodes.  
- **Time Complexity:** O(n) using a stack to place nodes.  
- **Space Complexity:** O(n) for the stack/tree nodes.  
- **Edge Case:** Single-node preorder list.

**1.2 High-level approach**  
Iterate preorder; use a stack of ancestors. Each value smaller than stack top goes left; otherwise pop until finding parent, then attach right.  
![BST reconstruction from preorder](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Insert each value via BST insert — still O(n²) worst case (sorted input).  
- **Optimized:** Monotonic stack to place nodes in O(n).

**1.4 Decomposition**  
1. Create root from first value; push to stack.  
2. For each next value:  
   - If value < stack top, set as left child of top.  
   - Else pop until stack empty or top > value; last popped is parent; attach as right child.  
3. Push new node to stack.  
4. Return root.

### Steps

**2.1 Initialization & Example Setup**  
Example: `[8,5,1,7,10,12]`; root = 8, stack = [8].

**2.2 Start Checking**  
Process each value, updating stack and children.

**2.3 Trace Walkthrough**  
| val | Stack before | Action                          | Child  |
|-----|--------------|---------------------------------|--------|
| 5   | [8]          | 5 < 8 → left of 8               | left   |
| 1   | [8,5]        | 1 < 5 → left of 5               | left   |
| 7   | [8,5,1]      | pop 1,5 (last popped=5) → right | right  |
| 10  | [8,7]        | pop 7,8 (last popped=8) → right | right  |
| 12  | [10]         | pop none → right of 10          | right  |

**2.4 Increment and Loop**  
Continue until all preorder values are attached.

**2.5 Return Result**  
Root of the constructed BST.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for val in preorder[1:]:
            node = TreeNode(val)
            
            # If current value is less than stack top, it's a left child
            if val < stack[-1].val:
                stack[-1].left = node
            else:
                # Find the parent where this node should be right child
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
            
            stack.append(node)
        
        return root
```

## 1038. Binary Search Tree to Greater Sum Tree [Medium]
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

### Explanation

## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The number of nodes is in the range `[1, 100]`, and node values are between 0 and 100.
  * **Time Complexity:** O(n) - We traverse each node exactly once in reverse inorder.
  * **Space Complexity:** O(h) - The recursion stack uses space proportional to the height of the tree, where h is at most n.
  * **Edge Case:** A tree with a single node returns itself with the same value.

**High-level approach**
We perform a reverse inorder traversal (right, root, left) of the BST. This visits nodes in descending order. As we traverse, we accumulate the sum of all values we've seen and update each node's value to be the sum of itself and all greater values.

**Brute force vs. optimized strategy**

  * **Brute Force:** Collect all values, sort them, and update nodes - but this requires extra space.
  * **Optimized Strategy:** Use reverse inorder traversal to visit nodes in descending order naturally, updating values in-place.

**Decomposition**

1.  **Initialize Accumulator:** Create a variable to track the running sum of all values seen.
2.  **Reverse Inorder Traversal:** Traverse right subtree first, then process current node, then left subtree.
3.  **Update Node Value:** Add current node's value to the accumulator and update the node.
4.  **Continue Traversal:** Process all nodes in descending order.

### Steps

1.  **Initialization & Example Setup:**
    Let's say we have a BST: `[4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]`
    We initialize `total = 0`.

2.  **Start Traversal:**
    We begin reverse inorder traversal (right, root, left).

3.  **Trace Walkthrough:**
    
    | Node Value | Total Before | Total After | Node Updated To |
    |------------|--------------|-------------|-----------------|
    | 8 | 0 | 8 | 8 |
    | 7 | 8 | 15 | 15 |
    | 6 | 15 | 21 | 21 |
    | 5 | 21 | 26 | 26 |
    | 4 | 26 | 30 | 30 |
    | 3 | 30 | 33 | 33 |
    | 2 | 33 | 35 | 35 |
    | 1 | 35 | 36 | 36 |
    | 0 | 36 | 36 | 36 |

4.  **Result:**
    The tree is updated in-place with new values.

5.  **Return Result:**
    Return the modified root of the tree.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        
        def reverse_inorder(node):
            nonlocal total
            if node:
                # Traverse right first (largest values)
                reverse_inorder(node.right)
                
                # Update current node value
                total += node.val
                node.val = total
                
                # Traverse left (smaller values)
                reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
```

## 1261. Find Elements in a Contaminated Binary Tree [Medium]
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

### Explanation

## Explanation

### Strategy

**Restate the problem**  
Recover a contaminated binary tree where original root was 0 and children follow `left = 2*x+1`, `right = 2*x+2`. Support queries to check if a target value exists.

**1.1 Constraints & Complexity**  
- **Input Size:** Up to `1e4` nodes, height <= 20.  
- **Time Complexity:** O(n) to recover; O(1) average for `find` via set lookup.  
- **Space Complexity:** O(n) to store recovered values.  
- **Edge Case:** Single-node tree.

**1.2 High-level approach**  
DFS from root, assign values by the given formulas, store all in a hash set for O(1) membership.  
![Tree recovery with value formulas](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Recover on every `find`, re-walking the tree — repeated O(n).  
- **Optimized:** Recover once, store in a set — O(n) build, O(1) queries.

**1.4 Decomposition**  
1. DFS from root with value parameter.  
2. Assign `val`, insert into set.  
3. Recurse to children with `2*val+1` and `2*val+2`.  
4. `find` checks membership in the set.

### Steps

**2.1 Initialization & Example Setup**  
Start at root with value 0, empty set.

**2.2 Start Processing**  
DFS visits each node, computing and storing values.

**2.3 Trace Walkthrough**  
| Node | Assigned val | Action        |
|------|--------------|---------------|
| root | 0            | add to set    |
| left | 1            | add to set    |
| right| 2            | add to set    |

**2.4 Increment and Loop**  
Continue recursively; each node’s children follow the formula.

**2.5 Return Result**  
`find(target)` returns `target in set`.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        
        def recover(node, val):
            if node:
                node.val = val
                self.values.add(val)
                recover(node.left, 2 * val + 1)
                recover(node.right, 2 * val + 2)
        
        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
```

## 2181. Merge Nodes in Between Zeros [Medium]
https://leetcode.com/problems/merge-nodes-in-between-zeros/

### Explanation

## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The number of nodes is in the range `[3, 2 * 10⁵]`, and node values are between 0 and 1000.
  * **Time Complexity:** O(n) - We traverse the linked list once, visiting each node exactly once.
  * **Space Complexity:** O(1) - We only use a constant amount of extra space (excluding the output list).
  * **Edge Case:** The list always starts and ends with zero nodes, and there are no two consecutive zeros.

**High-level approach**
We traverse the linked list, summing values between consecutive zero nodes. Each sum becomes a new node in the result list, and we skip the zero nodes.

**Brute force vs. optimized strategy**

  * **Brute Force:** Create a new list by collecting values between zeros - this is what we do, and it's optimal.
  * **Optimized Strategy:** Same approach - single pass through the list, summing values between zeros.

**Decomposition**

1.  **Skip First Zero:** Start from the node after the first zero.
2.  **Sum Values:** Accumulate values until we encounter the next zero.
3.  **Create Node:** Create a new node with the sum and add it to the result.
4.  **Repeat:** Continue until we've processed all nodes.

### Steps

1.  **Initialization & Example Setup:**
    Let's say we have a linked list: `[0, 3, 1, 0, 4, 5, 2, 0]`
    We skip the first zero and start with `current` pointing to node with value 3.

2.  **Start Processing:**
    We create a dummy node to build the result list: `dummy = ListNode(0)`, `tail = dummy`.

3.  **Trace Walkthrough:**
    
    | Current Node | Value | Sum | Action |
    |-------------|------|-----|--------|
    | 3 | 3 | 3 | Add to sum |
    | 1 | 1 | 4 | Add to sum |
    | 0 | 0 | - | Create node(4), reset sum |
    | 4 | 4 | 4 | Add to sum |
    | 5 | 5 | 9 | Add to sum |
    | 2 | 2 | 11 | Add to sum |
    | 0 | 0 | - | Create node(11), done |

4.  **Result:**
    After processing, we have a list: `[4, 11]`

5.  **Return Result:**
    Return `dummy.next` which points to the first merged node.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Skip the first zero
        current = head.next
        dummy = ListNode(0)
        tail = dummy
        
        while current:
            # Sum values until we hit the next zero
            total = 0
            while current and current.val != 0:
                total += current.val
                current = current.next
            
            # Create new node with the sum
            if total > 0:
                tail.next = ListNode(total)
                tail = tail.next
            
            # Move past the zero
            if current:
                current = current.next
        
        return dummy.next
```

## 2265. Count Nodes Equal to Average of Subtree [Medium]
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

### Explanation

## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Input Size:** The number of nodes is in the range `[1, 1000]`, and node values are between 0 and 1000.
  * **Time Complexity:** O(n) - We traverse each node exactly once in a DFS traversal.
  * **Space Complexity:** O(h) - The recursion stack uses space proportional to the height of the tree, where h is at most n.
  * **Edge Case:** A tree with a single node always satisfies the condition (node value equals its own average).

**High-level approach**
We perform a post-order DFS traversal. For each node, we calculate the sum and count of its subtree, compute the average, and check if the node's value equals this average.

**Brute force vs. optimized strategy**

  * **Brute Force:** For each node, separately calculate subtree sum and count - but this would cause redundant calculations.
  * **Optimized Strategy:** Use DFS to calculate sum and count in a single pass, reusing calculations from child subtrees.

**Decomposition**

1.  **DFS Traversal:** Perform post-order traversal (left, right, root).
2.  **Calculate Subtree Info:** For each node, compute sum and count of its subtree.
3.  **Compute Average:** Calculate average as sum // count (integer division).
4.  **Check Condition:** If node value equals average, increment the result counter.

### Steps

1.  **Initialization & Example Setup:**
    Let's say we have a tree: `[4, 8, 5, 0, 1, null, 6]`
    We initialize `res = 0`.

2.  **Start Traversal:**
    We perform DFS starting from the root.

3.  **Trace Walkthrough:**
    
    | Node | Left (sum, count) | Right (sum, count) | Subtree Sum | Subtree Count | Average | Node Value | Match? |
    |------|-------------------|-------------------|-------------|---------------|---------|------------|--------|
    | 0 | (0, 0) | (0, 0) | 0 | 1 | 0 | 0 | Yes |
    | 1 | (0, 0) | (0, 0) | 1 | 1 | 1 | 1 | Yes |
    | 6 | (0, 0) | (0, 0) | 6 | 1 | 6 | 6 | Yes |
    | 5 | (0, 0) | (6, 1) | 11 | 2 | 5 | 5 | Yes |
    | 8 | (0, 1) | (1, 1) | 9 | 3 | 3 | 8 | No |
    | 4 | (9, 3) | (11, 2) | 24 | 6 | 4 | 4 | Yes |

4.  **Result:**
    We count 5 nodes where value equals average: nodes 0, 1, 6, 5, and 4.

5.  **Return Result:**
    Return `res = 5`.

### Solution

```python
def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0  # sum, count
            
            # Get subtree info from children
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate current subtree sum and count
            subtree_sum = node.val + left_sum + right_sum
            subtree_count = 1 + left_count + right_count
            
            # Calculate average (integer division)
            avg = subtree_sum // subtree_count
            
            # Check if node value equals average
            if node.val == avg:
                res += 1
            
            return subtree_sum, subtree_count
        
        dfs(root)
        return res
```

## 2326. Spiral Matrix IV [Medium]
https://leetcode.com/problems/spiral-matrix-iv/

### Explanation

## Explanation

### Strategy

**Restate the problem**  
Fill an `m x n` matrix in spiral order using values from a linked list; remaining cells become -1.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= m*n <= 1e5`; list length up to `m*n`.  
- **Time Complexity:** O(m*n) to visit each cell once.  
- **Space Complexity:** O(1) extra (matrix output not counted).  
- **Edge Case:** List shorter than cells → trailing -1s.

**1.2 High-level approach**  
Track boundaries/directions for spiral traversal, place list values until exhausted, then fill -1 stays.  
![Spiral traversal boundaries](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Recompute visited checks with sets — higher overhead.  
- **Optimized:** Direction vectors with boundary checks — O(1) per move.

**1.4 Decomposition**  
1. Initialize matrix with -1.  
2. Set direction order: right, down, left, up.  
3. Walk cell by cell, placing list values.  
4. When the next cell is out-of-bounds or already filled, turn clockwise.  
5. Continue until list ends or all cells visited.

### Steps

**2.1 Initialization & Example Setup**  
Example: `m=3, n=5`, list `[3,0,2,6,8,1,7,9,4,2,5,5,0]`; start at `(0,0)`, dir=right.

**2.2 Start Checking**  
Place value, attempt next move; if blocked, rotate direction.

**2.3 Trace Walkthrough**  
| Step | Pos (r,c) | Dir    | Value placed | Next move valid? |
|------|-----------|--------|--------------|------------------|
| 1    | (0,0)     | right  | 3            | yes              |
| ...  | ...       | ...    | ...          | ...              |
| turn | boundary  | rotate | —            | —                |

**2.4 Increment and Loop**  
Advance through list nodes; rotate as needed until list ends.

**2.5 Return Result**  
Matrix filled in spiral with remaining cells as -1.

### Solution

```python
def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize matrix with -1
        res = [[-1] * n for _ in range(m)]
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        row, col = 0, 0
        
        current = head
        while current:
            res[row][col] = current.val
            current = current.next
            
            if not current:
                break
            
            # Try to move in current direction
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]
            
            # Check if we need to change direction
            if (next_row < 0 or next_row >= m or 
                next_col < 0 or next_col >= n or 
                res[next_row][next_col] != -1):
                dir_idx = (dir_idx + 1) % 4
            
            row += directions[dir_idx][0]
            col += directions[dir_idx][1]
        
        return res
```
