## Explanation

### Strategy (The "Why")

Given an array of distinct integers `candidates` and a target integer `target`, we need to find all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $30$, and target can be up to $500$.
- **Value Range:** Candidates are distinct positive integers between $2$ and $40$.
- **Time Complexity:** $O(2^n)$ in the worst case - We explore all possible combinations, though pruning reduces this.
- **Space Complexity:** $O(target)$ - The recursion stack can be as deep as target/min(candidates).
- **Edge Case:** If no combination sums to target, return empty list. If target is 0, return [[]] (empty combination).

**1.2 High-level approach:**

The goal is to find all combinations that sum to target, allowing repetition of candidates.

We use backtracking. For each candidate, we try including it (possibly multiple times) and recursively search for the remaining sum. We use a `start` index to avoid duplicate combinations.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of candidates. This would be exponential.
- **Optimized Strategy (Backtracking):** Use backtracking with pruning. When remaining sum becomes negative, we stop exploring that path. This reduces the search space.
- **Why it's better:** Backtracking with pruning avoids exploring invalid paths early, reducing the search space compared to brute force.

**1.4 Decomposition:**

1. Use backtracking: for each candidate starting from `start` index:
   - Add the candidate to the current combination.
   - Recursively search for `target - candidate`.
   - Remove the candidate (backtrack).
2. Base case: if remaining sum is 0, add combination to results.
3. Pruning: if remaining sum is negative, stop exploring.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $candidates = [2,3,6,7]$, $target = 7$

We initialize:
- `res = []`

**2.2 Start Backtracking:**

We begin building combinations.

**2.3 Trace Walkthrough:**

| Step | remaining | combination | candidate | Action | res After |
|------|-----------|-------------|-----------|--------|-----------|
| 1 | 7 | [] | 2 | Add 2 | [] |
| 2 | 5 | [2] | 2 | Add 2 | [] |
| 3 | 3 | [2,2] | 2 | Add 2 | [] |
| 4 | 1 | [2,2,2] | 2 | Add 2 | [] |
| 5 | -1 | [2,2,2,2] | - | Prune | [] |
| 6 | 1 | [2,2,2] | 3 | Add 3 | [] |
| 7 | -2 | [2,2,2,3] | - | Prune | [] |
| ... | ... | ... | ... | ... | ... |
| N | 0 | [7] | - | **Found!** | [[7]] |
| M | 0 | [2,2,3] | - | **Found!** | [[7], [2,2,3]] |

**2.4 Final Result:**

After backtracking: `[[7], [2,2,3]]`

**2.5 Return Result:**

We return `[[7], [2,2,3]]`, which are all unique combinations that sum to 7.

> **Note:** The key is to use backtracking to explore all possible combinations. By using a `start` index, we avoid duplicate combinations (e.g., [2,3] and [3,2]). We prune paths where the remaining sum becomes negative.

