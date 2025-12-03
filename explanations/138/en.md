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

