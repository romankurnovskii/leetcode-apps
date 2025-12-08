## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the minimum inversion count among all subarrays of length k. An inversion is a pair (i, j) where i < j and nums[i] > nums[j].

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 10^5`, `1 <= k <= n`
- **Time Complexity:** O(n log n) for compression + O(n log n) for sliding window with Fenwick Tree
- **Space Complexity:** O(n) for compression map and Fenwick Tree
- **Edge Case:** When k = 1, all subarrays have 0 inversions

**1.2 High-level approach:**
We compress the array values to a smaller range, then use a sliding window with a Fenwick Tree (Binary Indexed Tree) to efficiently maintain and update inversion counts as we slide the window.

![Fenwick Tree visualization](https://assets.leetcode.com/static_assets/others/fenwick-tree.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each subarray, count inversions by checking all pairs, which is O(n * k²)
- **Optimized Strategy:** Use Fenwick Tree to maintain counts and update inversion count in O(log n) per element, achieving O(n log n) time
- **Emphasize the optimization:** The Fenwick Tree allows efficient range queries and updates for maintaining inversion counts

**1.4 Decomposition:**
1. Compress array values to range [1, n] for efficient indexing
2. Initialize Fenwick Tree for the first window of size k
3. Calculate inversion count for the first window
4. Slide the window: remove leftmost element, add rightmost element, update inversion count
5. Track the minimum inversion count

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [3,1,2,5,4]`, `k = 3`
- Compressed: [3,1,2,5,4] (already in range 1-5)
- First window: [3,1,2]

**2.2 Start Processing:**
We calculate inversion count for the first window, then slide.

**2.3 Trace Walkthrough:**

| Window | Elements | Inversions | Count |
|--------|----------|------------|-------|
| [0:3] | [3,1,2] | (0,1), (0,2) | 2 |
| [1:4] | [1,2,5] | None | 0 |
| [2:5] | [2,5,4] | (1,2) | 1 |

**2.4 Increment and Loop:**
As we slide, we update the Fenwick Tree and recalculate inversions efficiently.

**2.5 Return Result:**
The minimum inversion count among all subarrays is 0, which is the result.
