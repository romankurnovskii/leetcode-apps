## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to choose a subsequence of k indices from nums1, and our score is the sum of selected nums1 values multiplied by the minimum of selected nums2 values. We want to maximize this score.

**1.1 Constraints & Complexity:**
- Input size: `1 <= n <= 10^5`
- **Time Complexity:** O(n log n) for sorting + O(n log k) for heap operations = O(n log n)
- **Space Complexity:** O(k) for the heap
- **Edge Case:** When k = 1, we simply find the maximum of nums1[i] * nums2[i]

**1.2 High-level approach:**
We sort pairs by nums2 in descending order. As we process each pair, we maintain a min-heap of the k largest nums1 values. The current nums2 value becomes the minimum for our current selection, and we calculate the score.

![Greedy selection visualization](https://assets.leetcode.com/static_assets/others/greedy-selection.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all C(n,k) combinations, which is exponential
- **Optimized Strategy:** Sort by nums2 descending, use heap to maintain top k nums1 values, achieving O(n log n) time
- **Emphasize the optimization:** By sorting by nums2, we ensure that when we process a pair, its nums2 value is the minimum in our current selection

**1.4 Decomposition:**
1. Create pairs of (nums1[i], nums2[i]) and sort by nums2 in descending order
2. Use a min-heap to maintain the k largest nums1 values seen so far
3. For each pair, add nums1 to heap, maintain heap size k, calculate score
4. Track the maximum score encountered

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums1 = [1,3,3,2]`, `nums2 = [2,1,3,4]`, `k = 3`
- Sort pairs by nums2 descending: [(2,4), (3,3), (1,2), (3,1)]
- Initialize heap and sum: `heap = []`, `current_sum = 0`

**2.2 Start Processing:**
We iterate through sorted pairs.

**2.3 Trace Walkthrough:**

| Pair | Heap Before | Action | Heap After | Sum | Score | Max Score |
|------|-------------|--------|------------|-----|-------|-----------|
| (2,4) | [] | Push 2 | [2] | 2 | 2*4=8 | 8 |
| (3,3) | [2] | Push 3 | [2,3] | 5 | 5*3=15 | 15 |
| (1,2) | [2,3] | Push 1, Pop 1 | [2,3] | 5 | 5*2=10 | 15 |
| (3,1) | [2,3] | Push 3, Pop 2 | [3,3] | 6 | 6*1=6 | 15 |

**2.4 Increment and Loop:**
After processing all pairs, we continue tracking the maximum.

**2.5 Return Result:**
The maximum score encountered is 15, which is the result.
