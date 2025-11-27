## Explanation

### Strategy (The "Why")

Given a string containing digits from 2-9, we need to return all possible letter combinations that the number could represent (like old phone keypads).

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be between $0$ and $4$.
- **Value Range:** Digits are between '2' and '9'.
- **Time Complexity:** $O(4^n \times n)$ where $n$ is the length of digits. In the worst case, each digit maps to 4 letters, and we generate $4^n$ combinations, each of length $n$.
- **Space Complexity:** $O(4^n)$ - We store all combinations. The recursion stack is $O(n)$.
- **Edge Case:** If the input is empty, return an empty list.

**1.2 High-level approach:**

The goal is to generate all possible letter combinations for a given digit string.

We use backtracking. For each digit, we try all possible letters it can represent, recursively building combinations.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force alternative - we must generate all combinations.
- **Optimized Strategy (Backtracking):** Use recursion to build combinations digit by digit. This is the natural and efficient approach.
- **Why it's better:** Backtracking naturally generates all combinations without duplicates and handles the recursive structure elegantly.

**1.4 Decomposition:**

1. Create a mapping from digits to letters.
2. Use backtracking: for each digit, try all its possible letters.
3. When we've processed all digits, add the current combination to results.
4. Return all combinations.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $digits = "23"$

We initialize:
- `digit_map = {'2': 'abc', '3': 'def'}`
- `res = []`

**2.2 Start Backtracking:**

We begin building combinations.

**2.3 Trace Walkthrough:**

| Step | index | current | Action | res After |
|------|-------|---------|--------|-----------|
| 1 | 0 | "" | Try 'a' | [] |
| 2 | 1 | "a" | Try 'd' | [] |
| 3 | 2 | "ad" | **Complete!** | ["ad"] |
| 4 | 1 | "a" | Try 'e' | ["ad"] |
| 5 | 2 | "ae" | **Complete!** | ["ad", "ae"] |
| ... | ... | ... | ... | ... |

**2.4 Final Combinations:**

After backtracking: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`

**2.5 Return Result:**

We return all 9 combinations.

> **Note:** The key is to use backtracking to explore all possible paths. For each digit, we try all its letters, and when we've processed all digits, we have a complete combination.

