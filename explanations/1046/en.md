## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Array length is between 1 and 30, and each stone weight is between 1 and 1000.
- **Time Complexity:** O(n log n) - We perform at most n operations, each involving heap operations that take O(log n) time.
- **Space Complexity:** O(n) - The heap stores at most n elements.
- **Edge Case:** If there's only one stone, return its weight.

**1.2 High-level approach:**
The goal is to simulate smashing the two heaviest stones together until at most one stone remains. We use a max-heap (implemented with negated values in a min-heap) to efficiently get the two heaviest stones at each step.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Sort the array, take the two largest, smash them, insert the result, and repeat. Sorting each time takes O(n log n), leading to O(n^2 log n) overall.
- **Optimized Strategy (Max Heap):** Use a max-heap to always get the two heaviest stones in O(log n) time. This reduces overall time to O(n log n).
- **Emphasize the optimization:** The heap data structure allows us to efficiently maintain and retrieve the maximum elements without full sorting.

**1.4 Decomposition:**
1. Convert the array into a max-heap (using negated values for Python's min-heap).
2. While there are at least 2 stones:
   - Pop the two heaviest stones.
   - If they're different, push their difference back into the heap.
3. Return the last stone's weight (or 0 if no stones remain).

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use an example: `stones = [2,7,4,1,8,1]`

Initialize:
- `heap = [-2,-7,-4,-1,-8,-1]` (negated for max-heap)
- `heapq.heapify(heap)`

**2.2 Start Processing:**
We repeatedly pop two stones and smash them.

**2.3 Trace Walkthrough:**

| Step | Pop 1 | Pop 2 | Difference | Heap After | Result |
|------|-------|-------|------------|------------|--------|
| 1 | 8 | 7 | 1 | [-4,-2,-1,-1,1] | Continue |
| 2 | 4 | 2 | 2 | [-2,-1,-1,1] | Continue |
| 3 | 2 | 1 | 1 | [-1,-1,1] | Continue |
| 4 | 1 | 1 | 0 | [-1] | Continue |
| 5 | 1 | - | - | [] | Done |

**2.4 Return Result:**
After all operations, one stone of weight 1 remains, so return 1.

