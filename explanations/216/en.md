## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** k is between 2 and 9, n is between 1 and 60.
* **Time Complexity:** O(C(9,k)) where C(9,k) is the number of combinations. In the worst case with k=9, this is O(1) since there's only one combination. More generally, it's O(9 choose k) which is bounded by O(2^9) = O(1) for small k.
* **Space Complexity:** O(k) for the recursion stack and the current path, plus O(result_size) for storing results.
* **Edge Case:** If k=4 and n=1, no valid combination exists since the minimum sum of 4 distinct numbers from 1-9 is 1+2+3+4=10.

**1.2 High-level approach:**

The goal is to find all combinations of k distinct numbers from 1 to 9 that sum to n. We use backtracking to explore all valid combinations.

![Backtracking tree showing how combinations are built by selecting numbers from 1-9]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Generate all possible combinations of k numbers from 1-9, then filter those that sum to n. This generates C(9,k) combinations.
* **Optimized (Backtracking with Pruning):** Use backtracking to build combinations incrementally, pruning early when the remaining sum becomes negative or when we've used k numbers. This avoids generating invalid combinations.
* **Why it's better:** Early pruning saves computation by stopping exploration of invalid paths immediately.

**1.4 Decomposition:**

1. Start with an empty path and remaining sum equal to n.
2. For each number from start to 9, try adding it to the current path.
3. Recursively explore with the updated path and reduced remaining sum.
4. If the path length equals k and remaining sum is 0, add the path to results.
5. Backtrack by removing the number and trying the next one.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: k = 3, n = 7

We initialize:
* `res = []` (to store all valid combinations)
* `path = []` (current combination being built)
* `remaining = 7` (target sum)

**2.2 Start Checking/Processing:**

We call `backtrack(1, [], 7)` to start from number 1.

**2.3 Trace Walkthrough:**

| Step | Current Number | Path | Remaining | Action | Result |
|------|---------------|------|-----------|--------|--------|
| 1 | 1 | [1] | 6 | Add 1, recurse | Continue |
| 2 | 2 | [1,2] | 4 | Add 2, recurse | Continue |
| 3 | 3 | [1,2,3] | 1 | Add 3, recurse | Continue |
| 4 | 4 | [1,2,4] | 0 | Add 4, path length=3, remaining=0 | Add [1,2,4] to res |
| 5 | 5 | [1,2,5] | -1 | Add 5, remaining < 0 | Backtrack |
| 6 | 3 | [1,3] | 3 | Backtrack to 2, try 3 | Continue |
| 7 | 4 | [1,3,4] | -1 | Remaining < 0 | Backtrack |
| 8 | 2 | [2] | 5 | Backtrack to 1, try 2 | Continue |
| 9 | 3 | [2,3] | 2 | Continue | Continue |
| 10 | 4 | [2,3,4] | -2 | Remaining < 0 | Backtrack |

**2.4 Increment and Loop:**

After processing a number, we backtrack by removing it from the path and trying the next number in sequence.

**2.5 Return Result:**

After exploring all possibilities, `res = [[1,2,4]]` is returned.

