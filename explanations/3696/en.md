## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of words, we need to find the maximum distance between two words that are different.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 words.
- **Time Complexity:** O(n^2) - we check all pairs of words, where n is the number of words.
- **Space Complexity:** O(1) - we only need variables to track maximum distance.
- **Edge Case:** If all words are the same, return 0. This is similar to problem 3706.

**1.2 High-level approach:**

The goal is to check all pairs of words and find the maximum distance between words that are different.

![Word distance visualization](https://assets.leetcode.com/static_assets/others/word-distance.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all pairs. This is O(n^2) which is acceptable.
- **Optimized Strategy:** Same as 3706 - check all pairs for different words.
- **Optimization:** The O(n^2) approach works for the given constraints.

**1.4 Decomposition:**

1. For each word at index i:
   - For each word at index j > i:
     - If words[i] != words[j], calculate distance = j - i.
     - Update maximum distance.
2. Return the maximum distance.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `words = ["a", "b", "a", "c"]`

- Array: `["a", "b", "a", "c"]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We check all pairs of different words.

**2.3 Trace Walkthrough:**

| Step | i | j | words[i] | words[j] | Different? | Distance | res |
| ---- | - | - | -------- | -------- | ---------- | -------- | --- |
| 1    | 0 | 1 | "a" | "b" | Yes | 1 | 1 |
| 2    | 0 | 3 | "a" | "c" | Yes | 3 | 3 |
| 3    | 1 | 2 | "b" | "a" | Yes | 1 | 3 |
| 4    | 1 | 3 | "b" | "c" | Yes | 2 | 3 |

**2.4 Increment and Loop:**

After checking each pair, we update the maximum.

**2.5 Return Result:**

The result is `3`, which is the maximum distance between different words.

