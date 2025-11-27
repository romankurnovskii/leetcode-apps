## Explanation

### Strategy (The "Why")

Given a string containing digits from 2-9, we need to return all possible letter combinations that the number could represent (like on a phone keypad).

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be between $0$ and $4$.
- **Value Range:** Digits are between '2' and '9'.
- **Time Complexity:** $O(4^n)$ where $n$ is the length of digits. In the worst case, each digit maps to 4 letters, and we generate all combinations.
- **Space Complexity:** $O(4^n)$ - We store all combinations in the result list.
- **Edge Case:** If the input is empty, return an empty list.

**1.2 High-level approach:**

The goal is to generate all possible letter combinations for the given digits.

We use backtracking to build combinations. For each digit, we try each possible letter it can represent, recursively building combinations for the remaining digits.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must generate all combinations.
- **Optimized Strategy (Backtracking):** Use recursion to build combinations incrementally. This is the natural and efficient approach.
- **Why it's better:** Backtracking efficiently generates all combinations without storing intermediate states unnecessarily.

**1.4 Decomposition:**

1. Create a mapping from digits to letters.
2. Use backtracking: for each digit, try each possible letter.
3. Recursively process the next digit.
4. When all digits are processed, add the combination to results.
5. Return all combinations.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $digits = "23"$

We initialize:
- `digit_to_letters = {'2': 'abc', '3': 'def'}`
- `res = []`

**2.2 Start Backtracking:**

We begin building combinations.

**2.3 Trace Walkthrough:**

| Step | index | digit | letters | current_combination | Action |
|------|-------|-------|---------|---------------------|--------|
| 1 | 0 | '2' | 'abc' | "" | Try 'a' |
| 2 | 1 | '3' | 'def' | "a" | Try 'd' |
| 3 | 2 | - | - | "ad" | Add to res |
| 4 | 1 | '3' | 'def' | "a" | Try 'e' |
| 5 | 2 | - | - | "ae" | Add to res |
| ... | ... | ... | ... | ... | ... |

**2.4 Final Combinations:**

- "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"

**2.5 Return Result:**

We return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

> **Note:** The key is to use backtracking to explore all possible combinations. For each digit, we try all its possible letters, and recursively process the next digit. When we've processed all digits, we have a complete combination.

