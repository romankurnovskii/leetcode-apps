## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** At most 1000 calls to popSmallest and addBack. Numbers are between 1 and 1000.
* **Time Complexity:** O(log k) for popSmallest and addBack where k is the number of added-back numbers. O(1) for the infinite set part.
* **Space Complexity:** O(k) where k is the number of distinct numbers that have been popped and added back.
* **Edge Case:** If we pop all numbers 1-1000 and add some back, those added-back numbers should be returned before continuing with 1001+.

**1.2 High-level approach:**

The goal is to implement a set that contains all positive integers, with operations to pop the smallest and add numbers back. We use a min-heap for added-back numbers and track the next number in the infinite sequence.

![Data structure showing heap for added-back numbers and counter for infinite sequence]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Store all popped numbers in a set, then for popSmallest, iterate from 1 to find the first not in the set. This is O(n) per pop.
* **Optimized (Heap + Counter):** Use a min-heap for added-back numbers and a counter for the infinite sequence. popSmallest returns min(heap.pop(), counter++). This is O(log k) per pop.
* **Why it's better:** The heap allows O(log k) access to the minimum added-back number, and the counter handles the infinite sequence in O(1).

**1.4 Decomposition:**

1. Maintain a min-heap for numbers that were popped and added back.
2. Maintain a counter (next_num) for the infinite sequence starting from 1.
3. Maintain a set to track which numbers are currently removed.
4. For popSmallest: if heap is not empty, pop from heap; otherwise, return and increment counter.
5. For addBack: if number is in removed set, add it to heap and remove from set.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

We initialize:
* `removed = set()` (track removed numbers)
* `added_back = []` (min-heap)
* `next_num = 1` (next number in infinite sequence)

**2.2 Start Checking/Processing:**

Operations are called: addBack(2), popSmallest(), popSmallest(), popSmallest(), addBack(1), popSmallest()

**2.3 Trace Walkthrough:**

| Operation | added_back | next_num | removed | Return |
|-----------|------------|----------|---------|--------|
| addBack(2) | [] | 1 | {} | None (2 already in set) |
| popSmallest() | [] | 1 | {1} | 1, next_num=2 |
| popSmallest() | [] | 2 | {1,2} | 2, next_num=3 |
| popSmallest() | [] | 3 | {1,2,3} | 3, next_num=4 |
| addBack(1) | [1] | 4 | {2,3} | None |
| popSmallest() | [] | 4 | {2,3,1} | 1 (from heap), next_num=4 |

**2.4 Increment and Loop:**

After each operation, we update the data structures accordingly.

**2.5 Return Result:**

The operations return [null, 1, 2, 3, null, 1] as expected.

