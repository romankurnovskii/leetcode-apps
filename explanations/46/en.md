## Explanation

### Strategy (The "Why")

Given an array `nums` of distinct integers, we need to return all possible permutations of `nums`.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $6$.
- **Value Range:** Array elements are distinct and between $-10$ and $10$.
- **Time Complexity:** $O(n! \times n)$ - There are $n!$ permutations, and each takes $O(n)$ time to build.
- **Space Complexity:** $O(n!)$ - We store all $n!$ permutations. The recursion stack is $O(n)$.
- **Edge Case:** If the array has only one element, return that element. If the array is empty, return [[]].

**1.2 High-level approach:**

The goal is to generate all possible permutations of the array.

We use backtracking. For each position, we try each unused number. When we've used all numbers, we have a complete permutation.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force alternative - we must generate all permutations.
- **Optimized Strategy (Backtracking):** Use backtracking to build permutations one element at a time. This is the natural and efficient approach.
- **Why it's better:** Backtracking naturally generates all permutations without duplicates and handles the recursive structure elegantly.

**1.4 Decomposition:**

1. Use backtracking: for each unused number:
   - Add it to the current permutation.
   - Recursively build the rest of the permutation.
   - Remove it (backtrack).
2. Base case: if we've used all numbers, add the permutation to results.
3. Return all permutations.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1,2,3]$

We initialize:
- `res = []`
- `current = []`

**2.2 Start Backtracking:**

We begin building permutations.

**2.3 Trace Walkthrough:**

| Step | current | Available | Choose | current After | res After |
|------|---------|-----------|--------|---------------|-----------|
| 1 | [] | [1,2,3] | 1 | [1] | [] |
| 2 | [1] | [2,3] | 2 | [1,2] | [] |
| 3 | [1,2] | [3] | 3 | [1,2,3] | [[1,2,3]] |
| 4 | [1,2] | [3] | Backtrack | [1,2] | [[1,2,3]] |
| 5 | [1] | [2,3] | 3 | [1,3] | [[1,2,3]] |
| 6 | [1,3] | [2] | 2 | [1,3,2] | [[1,2,3], [1,3,2]] |
| ... | ... | ... | ... | ... | ... |

**2.4 Final Result:**

After backtracking: `[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]`

**2.5 Return Result:**

We return all 6 permutations.

> **Note:** The key is to use backtracking to explore all possible orderings. For each position, we try each unused number, building permutations recursively. When we've used all numbers, we have a complete permutation.

