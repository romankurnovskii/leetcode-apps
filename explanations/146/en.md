# 146. LRU Cache

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/lru-cache/

## Problem Description

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Example 1:**
```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
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

```
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

### Solution

```python
class LRUCache:
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

**Time Complexity:** O(1) for both get and put operations  
**Space Complexity:** O(capacity) - we store at most capacity items 