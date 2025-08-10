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
