## Explanation

### Strategy (The "Why")

Given an integer array `nums` of unique elements, we need to return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $10$.
- **Value Range:** Array elements are distinct and between $-10$ and $10$.
- **Time Complexity:** $O(2^n \times n)$ - There are $2^n$ subsets, and each takes $O(n)$ time to build.
- **Space Complexity:** $O(2^n)$ - We store all $2^n$ subsets. The recursion stack is $O(n)$.
- **Edge Case:** If the array is empty, return [[]]. If the array has one element, return [[], [element]].

**1.2 High-level approach:**

The goal is to generate all possible subsets of the array.

We use backtracking. For each element, we have two choices: include it or exclude it. We explore both choices recursively.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force alternative - we must generate all subsets.
- **Optimized Strategy (Backtracking):** Use backtracking to build subsets incrementally. This is the natural and efficient approach.
- **Why it's better:** Backtracking naturally generates all subsets without duplicates and handles the recursive structure elegantly.

**1.4 Decomposition:**

1. Use backtracking: for each element starting from `index`:
   - Add current subset to results (at each step, current is a valid subset).
   - Try including the current element.
   - Recursively process remaining elements.
   - Remove the element (backtrack).
2. Return all subsets.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1,2,3]$

We initialize:
- `res = []`
- `current = []`

**2.2 Start Backtracking:**

We begin building subsets.

**2.3 Trace Walkthrough:**

| Step | index | current | Action | res After |
|------|-------|---------|--------|-----------|
| 1 | 0 | [] | Add [] | [[]] |
| 2 | 0 | [] | Add 1 | [[]] |
| 3 | 1 | [1] | Add [1] | [[], [1]] |
| 4 | 1 | [1] | Add 2 | [[], [1]] |
| 5 | 2 | [1,2] | Add [1,2] | [[], [1], [1,2]] |
| 6 | 2 | [1,2] | Add 3 | [[], [1], [1,2]] |
| 7 | 3 | [1,2,3] | Add [1,2,3] | [[], [1], [1,2], [1,2,3]] |
| ... | ... | ... | ... | ... |

**2.4 Final Result:**

After backtracking: `[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]`

**2.5 Return Result:**

We return all 8 subsets (2^3 = 8).

> **Note:** The key insight is that at each step, the current combination is a valid subset, so we add it to results. Then we try including each remaining element to build larger subsets.

