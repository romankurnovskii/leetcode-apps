## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nums1.length, nums2.length <= 10^5`, `1 <= k <= 10^4`.
- **Time Complexity:** O(k log k) - we process k pairs and use a heap.
- **Space Complexity:** O(k) - we store at most k elements in the heap.
- **Edge Case:** k might be larger than total possible pairs.

**1.2 High-level approach:**
The goal is to find k pairs with smallest sums from two sorted arrays. We use a min-heap to efficiently find the next smallest pair. Start with pairs (nums1[0], nums2[j]) for all j, then expand.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Generate all pairs, sort, take first k - O(n*m log(n*m)) time.
- **Optimized Strategy:** Use heap to track candidates, expand incrementally - O(k log k) time.

**1.4 Decomposition:**
1. Initialize heap with pairs (nums1[0], nums2[j]) for j in range(min(k, len(nums2))).
2. Pop the smallest pair from heap.
3. Add the next pair from nums1 (same nums2 index, next nums1 index).
4. Repeat until we have k pairs.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `nums1 = [1,7,11]`, `nums2 = [2,4,6]`, `k = 3`. Initialize heap with (1+2,0,0), (1+4,0,1), (1+6,0,2).

**2.2 Start Checking:**
We pop from heap and add new candidates.

**2.3 Trace Walkthrough:**

| Step | Pop | Add | Result |
|------|-----|-----|--------|
| 1 | (3,0,0) | (9,1,0) | [[1,2]] |
| 2 | (5,0,1) | (11,1,1) | [[1,2],[1,4]] |
| 3 | (7,0,2) | - | [[1,2],[1,4],[1,6]] |

**2.4 Increment and Loop:**
After each pop, we add the next candidate from nums1 if available.

**2.5 Return Result:**
Return `res = [[1,2],[1,4],[1,6]]`.

