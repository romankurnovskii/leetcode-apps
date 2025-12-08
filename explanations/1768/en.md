## Explanation

### Strategy (The "Why")

Given two strings `word1` and `word2`, we need to merge them by alternating characters, starting with `word1`. If one string is longer, we append the remaining characters at the end.

**1.1 Constraints & Complexity:**

- **Input Size:** Each string can have length between 1 and 100.
- **Value Range:** Strings consist of lowercase English letters.
- **Time Complexity:** O(n + m) where n and m are the lengths of word1 and word2. We iterate through both strings once.
- **Space Complexity:** O(n + m) - We build a result list that contains all characters from both strings.
- **Edge Case:** When one string is empty, we simply return the other string. When strings have equal length, we alternate perfectly.

**1.2 High-level approach:**

The goal is to create a new string by taking one character from word1, then one from word2, repeating this pattern until one string runs out, then appending the rest.

![Merge Strings Alternately](https://assets.leetcode.com/uploads/2021/06/03/merge-alternately.png)

We use two pointers to track our position in each string. This allows us to alternate characters efficiently and ensures we don't miss any characters when one string is longer than the other.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Create a new string by concatenating characters one by one using string concatenation in a loop. This would be inefficient due to string immutability in Python, creating O(n²) time complexity.
- **Optimized Strategy (List Building):** Use a list to collect characters, then join them at the end. This is efficient because list appending is O(1) amortized, and joining is O(n).
- **Why it's better:** Building a list and joining once is much faster than repeatedly concatenating strings, which creates new string objects each time.

**1.4 Decomposition:**

1. Initialize two pointers, one for each string, and an empty list to collect characters.
2. Alternate between the two strings, appending one character from word1, then one from word2.
3. Continue until one string is exhausted.
4. Append all remaining characters from the longer string.
5. Join the list into a final string and return it.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `word1 = "ab"`, `word2 = "pqrs"`

We initialize:
- `res = []` (list to collect characters)
- `i = 0` (pointer for word1)
- `j = 0` (pointer for word2)

**2.2 Start Processing:**

We begin alternating between word1 and word2.

**2.3 Trace Walkthrough:**

| Step | i | word1[i] | j | word2[j] | Action | res |
|------|---|----------|---|----------|--------|-----|
| 1 | 0 | 'a' | 0 | 'p' | Append 'a', then 'p' | ['a', 'p'] |
| 2 | 1 | 'b' | 1 | 'q' | Append 'b', then 'q' | ['a', 'p', 'b', 'q'] |
| 3 | 2 | (end) | 2 | 'r' | word1 done, append rest of word2 | ['a', 'p', 'b', 'q', 'r', 's'] |

**2.4 Increment and Loop:**

- After each pair of characters, we increment both `i` and `j`.
- When `i >= len(word1)`, we stop alternating and append remaining characters from word2.
- When `j >= len(word2)`, we stop alternating and append remaining characters from word1.

**2.5 Return Result:**

We join the list `res` into a string: `''.join(res)` returns `"apbqrs"`.

> **Note:** Using a list to build the result and joining at the end is the Pythonic and efficient way to construct strings from multiple parts.
