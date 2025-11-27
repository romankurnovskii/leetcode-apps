## Explanation

### Strategy (The "Why")

Given an array of $k$ linked lists, each sorted in ascending order, we need to merge all the linked lists into one sorted linked list and return it.

**1.1 Constraints & Complexity:**

- **Input Size:** $k$ can be up to $10^4$, and the total number of nodes can be up to $10^4$.
- **Value Range:** Node values are between $-10^4$ and $10^4$.
- **Time Complexity:** $O(n \log k)$ where $n$ is the total number of nodes. Each node is inserted/removed from the heap once, and heap operations take $O(\log k)$ time.
- **Space Complexity:** $O(k)$ - We maintain a heap of size at most $k$.
- **Edge Case:** If the array is empty, return null. If all lists are empty, return null.

**1.2 High-level approach:**

The goal is to merge $k$ sorted linked lists into one sorted list.

We use a min heap to always get the smallest node among all lists. We repeatedly extract the minimum, add it to the result, and add the next node from the same list to the heap.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Collect all nodes, sort them, then create a new linked list. This takes $O(n \log n)$ time.
- **Optimized Strategy (Min Heap):** Use a min heap to efficiently get the minimum node at each step. This takes $O(n \log k)$ time.
- **Why it's better:** When $k << n$, $O(n \log k)$ is significantly better than $O(n \log n)$. The heap approach also doesn't require storing all nodes at once.

**1.4 Decomposition:**

1. Create a min heap and add the first node from each non-empty list.
2. While the heap is not empty:
   - Extract the minimum node.
   - Add it to the result list.
   - Add the next node from the same list to the heap (if it exists).
3. Return the merged list.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $lists = [[1,4,5],[1,3,4],[2,6]]$

We initialize:
- `heap = [(1,0,node1), (1,1,node1), (2,2,node2)]`

**2.2 Start Merging:**

We begin extracting from the heap.

**2.3 Trace Walkthrough:**

| Step | Heap Top | Add to Result | Add Next to Heap | Result List |
|------|----------|---------------|------------------|-------------|
| 1 | (1,0) | 1 | (4,0) | 1 |
| 2 | (1,1) | 1 | (3,1) | 1→1 |
| 3 | (2,2) | 2 | (6,2) | 1→1→2 |
| 4 | (3,1) | 3 | (4,1) | 1→1→2→3 |
| 5 | (4,0) | 4 | (5,0) | 1→1→2→3→4 |
| 6 | (4,1) | 4 | - | 1→1→2→3→4→4 |
| ... | ... | ... | ... | ... |

**2.4 Final Result:**

After merging: $[1,1,2,3,4,4,5,6]$

**2.5 Return Result:**

We return the head of the merged list: $[1,1,2,3,4,4,5,6]$

> **Note:** The key insight is to use a min heap to efficiently get the smallest node among all lists at each step. This avoids the need to compare nodes from all lists explicitly.

