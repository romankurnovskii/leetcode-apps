## Explanation

### Strategy (The "Why")

Given an array `costs` representing worker costs, we need to hire exactly $k$ workers. We can choose workers from the first `candidates` workers or the last `candidates` workers. After each hire, we can choose from the updated first or last `candidates` workers. We need to minimize the total cost.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be up to $10^5$, and $k$ can be up to $10^5$.
- **Value Range:** Worker costs are between $1$ and $10^5$.
- **Time Complexity:** $O(k \log(candidates) + candidates)$ - We maintain two heaps of size at most `candidates`, and we perform $k$ operations.
- **Space Complexity:** $O(candidates)$ - We maintain two heaps, each of size at most `candidates`.
- **Edge Case:** If $k$ equals the array length, we hire all workers. If `candidates` is large enough to cover all workers, we just choose the $k$ cheapest.

**1.2 High-level approach:**

The goal is to minimize the total cost of hiring $k$ workers by always choosing the cheapest available worker from the first or last `candidates`.

We use two min heaps: one for the first `candidates` workers and one for the last `candidates` workers. At each step, we choose the minimum from either heap, then add the next available worker to that heap.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to hire $k$ workers. This would be exponential.
- **Optimized Strategy (Two Heaps):** Use two min heaps to efficiently get the minimum cost worker from either end. This takes $O(k \log(candidates))$ time.
- **Why it's better:** The heap approach allows us to efficiently find the minimum cost worker from either end in $O(\log(candidates))$ time, avoiding the need to search through all candidates.

**1.4 Decomposition:**

1. Initialize two min heaps with the first and last `candidates` workers.
2. Maintain pointers to track the next available worker from each end.
3. For $k$ iterations:
   - Compare the minimum from both heaps.
   - Choose the smaller one and add its cost to the total.
   - Add the next available worker from that end to the heap.
4. Return the total cost.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $costs = [17,12,10,2,7,2,11,20,8]$, $k = 3$, $candidates = 4$

We initialize:
- `left_heap = [2, 7, 10, 12]` (first 4 workers)
- `right_heap = [2, 8, 11, 20]` (last 4 workers)
- `left_idx = 4`, `right_idx = 4`

**2.2 Start Hiring:**

We begin hiring workers.

**2.3 Trace Walkthrough:**

| Hire | left_heap[0] | right_heap[0] | Choose | Cost | left_heap After | right_heap After |
|------|--------------|---------------|--------|------|-----------------|------------------|
| 1 | 2 | 2 | Either (2) | 2 | [7,10,12,17] | [8,11,20] |
| 2 | 7 | 2 | Right (2) | 4 | [7,10,12,17] | [8,11,20] |
| 3 | 7 | 8 | Left (7) | 11 | [10,12,17] | [8,11,20] |

**2.4 Explanation:**

- First hire: Both heaps have minimum 2, choose from left (costs[3]=2)
- Second hire: Right heap has minimum 2 (costs[5]=2), choose from right
- Third hire: Left heap has minimum 7 (costs[4]=7), choose from left

**2.5 Return Result:**

We return 11, which is the total cost (2 + 2 + 7 = 11).

> **Note:** The key insight is to maintain two heaps for efficient access to the minimum cost workers from each end. After each hire, we add the next available worker from that end to maintain the heap size.

