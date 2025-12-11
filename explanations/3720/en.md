## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the lexicographically smallest permutation of string s that is strictly greater than target. If no such permutation exists, return an empty string.

**1.1 Constraints & Complexity:**

* **Input Size:** Both strings have length n where 1 <= n <= 300.
* **Time Complexity:** O(n * 26) in worst case, but pruning makes it much faster in practice. We use backtracking with early termination.
* **Space Complexity:** O(n) - We store the frequency count array (size 26) and the path during backtracking.
* **Edge Case:** If all permutations of s are less than or equal to target, return empty string.

**1.2 High-level approach:**

The goal is to build the answer character by character, always choosing the smallest valid character at each position. We use backtracking to explore possibilities, but prune branches that cannot lead to a valid answer.


**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Generate all permutations of s, sort them, and find the first one greater than target. This is O(n! * n log n) which is infeasible for n=300.
* **Optimized (Backtracking with Pruning):** Build the permutation character by character. At each position, try characters in sorted order. Skip characters that would make the prefix smaller than target. Once we find a prefix that's already bigger than target, we can fill the rest with smallest available characters. This avoids generating all permutations.
* **Why it's better:** Pruning eliminates most of the search space, making it practical even for larger inputs.

**1.4 Decomposition:**

1. Count the frequency of each character in s.
2. Use backtracking to build the permutation character by character.
3. At each position, try characters in lexicographic order (a to z).
4. Skip characters that would make the prefix smaller than target (if not already bigger).
5. Once a valid permutation is found, return it immediately.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "abc"`, `target = "bba"`

We initialize:
* `cnt = [1, 1, 1, 0, ...]` (frequency: a=1, b=1, c=1)
* `res = []` (result list)
* `path = []` (current path in backtracking)

**2.2 Start Checking:**

We call `backtrack([], cnt, False)` to start building the permutation.

**2.3 Trace Walkthrough:**

| Step | pos | char tried | big   | path          | Action                    |
| ---- | --- | ---------- | ----- | ------------- | ------------------------- |
| 1    | 0   | 'a'        | False | -             | Skip (a < 'b')            |
| 2    | 0   | 'b'        | False | ['b']         | Continue (b == 'b')       |
| 3    | 1   | 'a'        | False | -             | Skip (a < 'b')            |
| 4    | 1   | 'b'        | False | -             | Skip (count=0, no more b) |
| 5    | 1   | 'c'        | True  | ['b','c']     | Continue (c > 'b'), big=True |
| 6    | 2   | 'a'        | True  | ['b','c','a'] | Found! Return "bca"       |

At step 6, we find that "bca" > "bba", so we return it.

**2.4 Increment and Loop:**

The backtracking function recursively tries each character, updating the path and frequency count, then backtracks if the path doesn't lead to a solution.

**2.5 Return Result:**

After backtracking completes, we return `"bca"`, which is the lexicographically smallest permutation greater than "bba".
