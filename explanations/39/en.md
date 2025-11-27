## Explanation

### Strategy (The "Why")

Given an array of distinct integers `candidates` and a target integer, we need to return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. The same number may be chosen from `candidates` an unlimited number of times.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $30$, and target can be up to $500$.
- **Value Range:** Array elements are between $2$ and $40$, and all elements are distinct.
- **Time Complexity:** $O(2^n)$ in the worst case - We explore all possible combinations, though pruning reduces this significantly.
- **Space Complexity:** $O(target)$ - The recursion depth is at most $target$ (if we choose 1 each time), and we store combinations.
- **Edge Case:** If target is 0, return empty list (no combinations). If no combination sums to target, return empty list.

**1.2 High-level approach:**

The goal is to find all combinations that sum to the target, allowing repetition of candidates.

We use backtracking. For each candidate, we can choose to include it (and possibly include it again) or skip it. We build combinations incrementally and backtrack when the sum exceeds the target.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations with repetition. This would be exponential.
- **Optimized Strategy (Backtracking):** Use backtracking with pruning. When the current sum exceeds the target, we stop exploring that path. This reduces the search space significantly.
- **Why it's better:** Backtracking with pruning avoids exploring invalid paths early, making it more efficient than brute force while still being exponential in the worst case.

**1.4 Decomposition:**

1. Use backtracking: for each candidate starting from a given index:
   - Add the candidate to the current combination.
   - Recursively try to reach the target with the remaining sum.
   - Remove the candidate (backtrack).
2. Base cases:
   - If remaining sum is 0, add the combination to results.
   - If remaining sum is negative, return (pruning).
3. Start from index 0 and allow reusing candidates from the same index onward.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $candidates = [2,3,6,7]$, $target = 7$

We initialize:
- `res = []`

**2.2 Start Backtracking:**

We begin building combinations.

**2.3 Trace Walkthrough:**

| Step | remaining | combination | candidate | Action | combination After |
|------|-----------|-------------|-----------|--------|-------------------|
| 1 | 7 | [] | 2 | Add 2 | [2] |
| 2 | 5 | [2] | 2 | Add 2 | [2,2] |
| 3 | 3 | [2,2] | 2 | Add 2 | [2,2,2] |
| 4 | 1 | [2,2,2] | 2 | Add 2 | [2,2,2,2] |
| 5 | -1 | [2,2,2,2] | - | Prune | Backtrack |
| 6 | 3 | [2,2] | 3 | Add 3 | [2,2,3] |
| 7 | 0 | [2,2,3] | - | Found! | Add to res |
| ... | ... | ... | ... | ... | ... |

**2.4 Valid Combinations:**

- $[2,2,3]$ (sum = 7) ✓
- $[7]$ (sum = 7) ✓

**2.5 Return Result:**

We return `[[2,2,3],[7]]`, which are all combinations that sum to 7.

> **Note:** The key insight is to use backtracking and allow reusing candidates. By starting from the same index (or later) when recursing, we allow the same candidate to be used multiple times while avoiding duplicate combinations.

