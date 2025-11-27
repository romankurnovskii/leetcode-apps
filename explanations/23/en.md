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

