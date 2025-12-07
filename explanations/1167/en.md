## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= sticks.length <= 10^4`, `1 <= sticks[i] <= 10^4`.
- **Time Complexity:** O(n log n) where n is the number of sticks. Each heap operation takes O(log n) and we perform O(n) operations.
- **Space Complexity:** O(n) for the heap.
- **Edge Case:** If there's only one stick, return 0 (no connection needed).

**1.2 High-level approach:**

The goal is to minimize the total cost of connecting all sticks, where the cost of connecting two sticks is the sum of their lengths. The key insight is to always connect the two shortest sticks first (greedy approach). This minimizes the cost because shorter sticks are used fewer times in the total sum. We use a min-heap to efficiently get the two shortest sticks at each step.

![Visualization showing how connecting shortest sticks first minimizes total cost, with a heap maintaining the shortest sticks]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible orders of connecting sticks. This is exponential and impractical.
- **Optimized Strategy:** Use a min-heap to always connect the two shortest sticks. This greedy approach is optimal.
- **Why it's better:** The greedy approach ensures that shorter sticks (which contribute less) are used in later connections, minimizing the total cost. This is similar to Huffman coding.

**1.4 Decomposition:**

1. Convert the sticks array into a min-heap.
2. While there's more than one stick in the heap:
   - Pop the two shortest sticks.
   - Calculate the cost of connecting them (sum of their lengths).
   - Add the cost to the total.
   - Push the merged stick (sum) back into the heap.
3. Return the total cost.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `sticks = [2, 4, 3]`.

We initialize:
- Heap: `[2, 3, 4]` (min-heap)
- `res = 0`

**2.2 Start Checking:**

Connect sticks until only one remains.

**2.3 Trace Walkthrough:**

| Step | Heap before | Pop 1 | Pop 2 | Cost | New stick | Heap after | Total cost |
|------|-------------|-------|-------|------|-----------|------------|------------|
| 1 | [2, 3, 4] | 2 | 3 | 5 | 5 | [4, 5] | 5 |
| 2 | [4, 5] | 4 | 5 | 9 | 9 | [9] | 5 + 9 = 14 |

Detailed steps:
- Step 1: Pop 2 and 3, cost = 2 + 3 = 5. Push 5 back. Heap: [4, 5]. Total: 5.
- Step 2: Pop 4 and 5, cost = 4 + 5 = 9. Push 9 back. Heap: [9]. Total: 5 + 9 = 14.
- Only one stick remains, so we're done.

**2.4 Increment and Loop:**

Continue until heap size is 1.

**2.5 Return Result:**

Return `res = 14` - the minimum total cost to connect all sticks.

