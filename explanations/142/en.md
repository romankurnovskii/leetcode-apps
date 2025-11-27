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
