## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** $n$ is between 1 and 8, so we need to generate at most $C(8,4) = 70$ combinations.
* **Time Complexity:** $O(\frac{4^n}{\sqrt{n}})$ which is the Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$. This represents the number of valid parentheses combinations.
* **Space Complexity:** $O(\frac{4^n}{\sqrt{n}})$ for storing all combinations, plus $O(n)$ for the recursion stack.
* **Edge Case:** When $n = 1$, the only valid combination is "()".

**1.2 High-level approach**

The goal is to generate all valid combinations of $n$ pairs of parentheses. A combination is valid if every opening parenthesis has a matching closing parenthesis, and they are properly nested.

![Backtracking tree visualization showing how valid parentheses combinations are generated]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Generate all possible strings of length $2n$ with $n$ '(' and $n$ ')', then filter out invalid ones. This generates $2^{2n}$ strings, most of which are invalid.
* **Optimized (Backtracking):** Use backtracking to only generate valid combinations by ensuring we never add a closing parenthesis when there are no unmatched opening parentheses. This only generates valid combinations.

**1.4 Decomposition**

1. Use backtracking to build combinations character by character.
2. Track the number of opening and closing parentheses used.
3. Add an opening parenthesis if we haven't used all $n$ opening parentheses.
4. Add a closing parenthesis only if there are more opening than closing parentheses (ensuring validity).
5. When we reach length $2n$, add the combination to the result.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $n = 3$.

We initialize:
* `res = []` (list to store all valid combinations)
* `current = ""` (current combination being built)
* `open_count = 0` (number of opening parentheses used)
* `close_count = 0` (number of closing parentheses used)

**2.2 Start Checking/Processing**

We call the backtrack function with the initial empty string and counts.

**2.3 Trace Walkthrough**

The backtracking process builds combinations recursively. Here's a partial trace:

| Step | current | open_count | close_count | Action | Result |
|------|---------|------------|-------------|--------|--------|
| 1 | "" | 0 | 0 | Add '(' | "(" |
| 2 | "(" | 1 | 0 | Add '(' | "((" |
| 3 | "((" | 2 | 0 | Add '(' | "(((" |
| 4 | "(((" | 3 | 0 | Add ')' | "((()" |
| 5 | "((()" | 3 | 1 | Add ')' | "((())" |
| 6 | "((())" | 3 | 2 | Add ')' | "((()))" |
| 7 | "((()))" | 3 | 3 | Complete | Add to res |

The algorithm explores all valid paths, generating: "((()))", "(()())", "(())()", "()(())", "()()()".

**2.4 Increment and Loop**

The backtracking function:
1. Base case: If `len(current) == 2 * n`, add `current` to `res` and return.
2. If `open_count < n`, recursively add '(' and increment `open_count`.
3. If `close_count < open_count`, recursively add ')' and increment `close_count`.
4. After each recursive call, backtrack by removing the last character.

**2.5 Return Result**

After backtracking completes, `res = ["((()))", "(()())", "(())()", "()(())", "()()()"]`, containing all 5 valid combinations of 3 pairs of parentheses.

