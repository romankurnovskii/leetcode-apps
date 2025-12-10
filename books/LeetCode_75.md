# LeetCode 75

Problem list from official https://leetcode.com/studyplan/leetcode-75/

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
