## Explanation

### Strategy (The "Why")

Given an array `nums` of distinct integers, we need to return all possible permutations of `nums`.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $6$.
- **Value Range:** Array elements are between $-10$ and $10$, and all elements are distinct.
- **Time Complexity:** $O(n! \times n)$ - There are $n!$ permutations, and each takes $O(n)$ time to build.
- **Space Complexity:** $O(n!)$ - We store all $n!$ permutations.
- **Edge Case:** If the array has only one element, return that element. If the array is empty, return empty list.

**1.2 High-level approach:**

The goal is to generate all possible arrangements (permutations) of the array elements.

We use backtracking. For each position, we try each remaining element, recursively build permutations for the remaining positions, then backtrack to try the next element.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must generate all permutations.
- **Optimized Strategy (Backtracking):** Use backtracking to build permutations incrementally. This is the standard and efficient approach.
- **Why it's better:** Backtracking efficiently generates all permutations without storing unnecessary intermediate states.

**1.4 Decomposition:**

1. Use backtracking: for each remaining element:
   - Choose the element (add to current permutation).
   - Recursively build permutations with the remaining elements.
   - Unchoose the element (backtrack).
2. Base case: when no elements remain, add the current permutation to results.
3. Start with an empty permutation and all elements available.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1,2,3]$

We initialize:
- `res = []`
- `current_permutation = []`
- `remaining = [1,2,3]`

**2.2 Start Backtracking:**

We begin building permutations.

**2.3 Trace Walkthrough:**

| Step | remaining | Choose | current_permutation | remaining After | Action |
|------|-----------|--------|---------------------|------------------|--------|
| 1 | [1,2,3] | 1 | [1] | [2,3] | Recurse |
| 2 | [2,3] | 2 | [1,2] | [3] | Recurse |
| 3 | [3] | 3 | [1,2,3] | [] | Add to res |
| 4 | [2,3] | 3 | [1,3] | [2] | Recurse |
| 5 | [2] | 2 | [1,3,2] | [] | Add to res |
| ... | ... | ... | ... | ... | ... |

**2.4 All Permutations:**

- $[1,2,3]$, $[1,3,2]$, $[2,1,3]$, $[2,3,1]$, $[3,1,2]$, $[3,2,1]$

**2.5 Return Result:**

We return all 6 permutations of $[1,2,3]$.

> **Note:** The key insight is to use backtracking to try each element at each position. By maintaining a list of remaining elements and building the permutation incrementally, we generate all possible arrangements efficiently.

