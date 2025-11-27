## Explanation

### Strategy (The "Why")

Given an integer array `nums` of unique elements, we need to return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $10$.
- **Value Range:** Array elements are between $-10$ and $10$, and all elements are unique.
- **Time Complexity:** $O(2^n \times n)$ - There are $2^n$ subsets, and each takes $O(n)$ time to build.
- **Space Complexity:** $O(2^n)$ - We store all $2^n$ subsets.
- **Edge Case:** If the array is empty, return `[[]]` (empty set is a subset). If the array has one element, return `[[], [element]]`.

**1.2 High-level approach:**

The goal is to generate all possible subsets of the array.

We use backtracking. For each element, we can either include it in the current subset or exclude it. We build subsets incrementally and add each subset to the result as we build it.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must generate all subsets.
- **Optimized Strategy (Backtracking):** Use backtracking to build subsets incrementally. This is the standard and efficient approach.
- **Why it's better:** Backtracking efficiently generates all subsets without storing unnecessary intermediate states.

**1.4 Decomposition:**

1. Use backtracking: for each element starting from a given index:
   - Include the element in the current subset and recurse.
   - Exclude the element (backtrack) and recurse.
2. At each step, add the current subset to results (before and after including elements).
3. Start with an empty subset and index 0.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1,2,3]$

We initialize:
- `res = []`
- `current_subset = []`

**2.2 Start Backtracking:**

We begin building subsets.

**2.3 Trace Walkthrough:**

| Step | index | current_subset | Action | res After |
|------|-------|----------------|--------|-----------|
| 1 | 0 | [] | Add [] | [[]] |
| 2 | 0 | [] | Include 1 | [[], [1]] |
| 3 | 1 | [1] | Add [1] | [[], [1]] |
| 4 | 1 | [1] | Include 2 | [[], [1], [1,2]] |
| 5 | 2 | [1,2] | Add [1,2] | [[], [1], [1,2]] |
| 6 | 2 | [1,2] | Include 3 | [[], [1], [1,2], [1,2,3]] |
| ... | ... | ... | ... | ... |

**2.4 All Subsets:**

- $[]$, $[1]$, $[2]$, $[3]$, $[1,2]$, $[1,3]$, $[2,3]$, $[1,2,3]$

**2.5 Return Result:**

We return all 8 subsets of $[1,2,3]$.

> **Note:** The key insight is to use backtracking where at each step, we add the current subset to results, then try including each remaining element. This ensures we generate all subsets exactly once.

