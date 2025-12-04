## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Numbers range from -10^5 to 10^5, and there are at most 5*10^4 calls to `addNum` and `findMedian`.
- **Time Complexity:** 
  - `addNum`: O(log n) to insert into a heap
  - `findMedian`: O(1) to access heap tops
- **Space Complexity:** O(n) to store all numbers in the heaps.
- **Edge Case:** If only one number has been added, the median is that number.

**1.2 High-level approach:**
The goal is to efficiently find the median of a stream of numbers. We maintain two heaps: a max-heap for the smaller half and a min-heap for the larger half. The median is the top of the larger heap or the average of both tops.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Store all numbers in a list and sort to find median. This is O(n log n) per median query.
- **Optimized Strategy:** Use two heaps to maintain the two halves. Insertion is O(log n) and median query is O(1).
- **Why optimized is better:** Heaps allow efficient insertion and constant-time median access, much better than sorting.

**1.4 Decomposition:**
1. Maintain two heaps: `max_heap` (smaller half, use negative values) and `min_heap` (larger half).
2. For `addNum`, insert into the appropriate heap and balance if needed (difference should be at most 1).
3. For `findMedian`, if heaps are equal size, return average of both tops; otherwise, return the top of the larger heap.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Initialize: `max_heap = []`, `min_heap = []`

Add numbers: 1, 2, 3

**2.2 Start Checking:**
After each addition, balance the heaps to maintain the property that the size difference is at most 1.

**2.3 Trace Walkthrough:**

| Step | Number | max_heap | min_heap | Action |
|------|--------|----------|----------|--------|
| 0 | - | [] | [] | Initialize |
| 1 | 1 | [-1] | [] | Add to max_heap |
| 2 | 2 | [-1] | [2] | Add to min_heap, balanced |
| 3 | 3 | [-1] | [2,3] | Add to min_heap, balance: move 2 to max_heap |
| 4 | - | [-2,-1] | [3] | Balanced, find median |

**2.4 Increment and Loop:**
For each `addNum`:
- Insert into appropriate heap
- Balance if size difference > 1

**2.5 Return Result:**
After adding 1, 2, 3:
- `max_heap = [-2, -1]`, `min_heap = [3]`
- Median = (-(-2) + 3) / 2 = (2 + 3) / 2 = 2.5 (if equal sizes)
- Or median = -(-2) = 2 (if max_heap is larger)

