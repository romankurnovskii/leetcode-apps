## Explanation

### Strategy (The "Why")

Given an array of stones with positive weights, we repeatedly smash the two heaviest stones together. If they're equal, both are destroyed. If they're different, the smaller is destroyed and the larger becomes the difference. We need to find the weight of the last remaining stone, or 0 if none remain.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be up to $30$.
- **Value Range:** Stone weights are between $1$ and $1000$.
- **Time Complexity:** $O(n \log n)$ - We use a heap, and each operation takes $O(\log n)$ time. We perform at most $n$ operations.
- **Space Complexity:** $O(n)$ - We use a heap to store all stones.
- **Edge Case:** If there's only one stone, return its weight. If all stones have the same weight and there are an even number, return 0.

**1.2 High-level approach:**

The goal is to simulate the stone smashing process until at most one stone remains.

We use a max heap to always get the two heaviest stones. Since Python's heapq is a min heap, we negate values to simulate a max heap. We repeatedly extract the two largest, smash them, and add the result back if non-zero.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Sort the array repeatedly and process the two largest. This takes $O(n^2 \log n)$ time due to repeated sorting.
- **Optimized Strategy (Max Heap):** Use a max heap to efficiently get the two largest stones. This takes $O(n \log n)$ time.
- **Why it's better:** The heap approach reduces time complexity by maintaining the stones in a heap structure, allowing efficient extraction of the maximum elements.

**1.4 Decomposition:**

1. Create a max heap (using negated values) from all stones.
2. While there's more than one stone:
   - Extract the two largest stones.
   - If they're different, add their difference back to the heap.
3. Return the last stone's weight, or 0 if no stones remain.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $stones = [2,7,4,1,8,1]$

We initialize:
- `heap = [-2, -7, -4, -1, -8, -1]` (negated for max heap)
- After heapify: `[-8, -7, -4, -1, -2, -1]`

**2.2 Start Processing:**

We begin smashing stones.

**2.3 Trace Walkthrough:**

| Step | Heap Before | Extract | Smash | Heap After |
|------|-------------|---------|-------|------------|
| 1 | [-8,-7,-4,-1,-2,-1] | 8, 7 | 8-7=1 | [-4,-2,-1,-1,-1] |
| 2 | [-4,-2,-1,-1,-1] | 4, 2 | 4-2=2 | [-2,-1,-1,-1] |
| 3 | [-2,-1,-1,-1] | 2, 1 | 2-1=1 | [-1,-1] |
| 4 | [-1,-1] | 1, 1 | 1-1=0 | [] |

**2.4 Final Result:**

After all smashing, the heap is empty, so no stones remain.

**2.5 Return Result:**

We return 0, as no stones remain.

> **Note:** The key insight is to use a max heap to efficiently get the two largest stones at each step. By negating values, we can use Python's min heap as a max heap.

