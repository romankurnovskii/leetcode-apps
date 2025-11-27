## 274. H-Index [Medium]

https://leetcode.com/problems/h-index

## Description
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `iᵗʰ` paper, return *the researcher's h-index*.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

**Examples**

```tex
Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
```

**Constraints**
```tex
- n == citations.length
- 1 <= n <= 5000
- 0 <= citations[i] <= 1000
```

## Explanation

### Strategy
Let's restate the problem: You're given an array representing the number of citations for each paper a researcher has published. You need to find the maximum value `h` such that the researcher has at least `h` papers with at least `h` citations each.

This is a **sorting problem** that requires understanding the definition of h-index and finding the optimal value efficiently.

**What is given?** An array of integers representing citation counts for each paper.

**What is being asked?** Find the maximum h-index value that satisfies the h-index definition.

**Constraints:** The array can be up to 5000 elements long, with citation counts ranging from 0 to 1000.

**Edge cases:** 
- Array with all zeros
- Array with all high citation counts
- Array with single element
- Array with mixed citation counts

**High-level approach:**
The solution involves understanding the h-index definition and using sorting to efficiently find the maximum valid h value.

**Decomposition:**
1. **Sort the array**: Arrange citations in descending order to easily check h-index conditions
2. **Iterate through sorted array**: Check each position as a potential h-index
3. **Verify h-index condition**: Ensure at least h papers have at least h citations
4. **Return maximum valid h**: Find the largest h that satisfies the condition

**Brute force vs. optimized strategy:**
- **Brute force**: Try each possible h value and check if it satisfies the condition. This takes O(n²) time.
- **Optimized**: Sort the array and use a single pass to find the h-index. This takes O(n log n) time.

### Steps
Let's walk through the solution step by step using the first example: `citations = [3,0,6,1,5]`

**Step 1: Sort the array in descending order**
- Original: `[3,0,6,1,5]`
- Sorted: `[6,5,3,1,0]`

**Step 2: Check each position as potential h-index**
- Position 0: `h = 1`, check if `citations[0] >= 1` ✓ (6 >= 1)
- Position 1: `h = 2`, check if `citations[1] >= 2` ✓ (5 >= 2)
- Position 2: `h = 3`, check if `citations[2] >= 3` ✓ (3 >= 3)
- Position 3: `h = 4`, check if `citations[3] >= 4` ✗ (1 < 4)

**Step 3: Find the maximum valid h**
- The largest h where `citations[h-1] >= h` is 3
- At position 2 (0-indexed), we have `h = 3` and `citations[2] = 3 >= 3`

**Step 4: Verify the h-index condition**
- We need at least 3 papers with at least 3 citations
- Papers with ≥3 citations: 6, 5, 3 (3 papers) ✓
- Remaining papers: 1, 0 (≤3 citations) ✓
- H-index is 3

**Why this works:**
After sorting in descending order, the array position `i` (0-indexed) represents `h = i + 1`. For a position to be a valid h-index, we need `citations[i] >= h`. The largest valid h is our answer.

> **Note:** The key insight is that after sorting, we can directly check each position as a potential h-index. The sorting makes it easy to verify the h-index condition in a single pass.

**Time Complexity:** O(n log n) - dominated by sorting the array  
**Space Complexity:** O(1) - we only use a constant amount of extra space (excluding the sorted array if we modify the input)
