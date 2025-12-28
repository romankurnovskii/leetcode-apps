## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum score achievable by forming words from a given list, using available letters. Each word can be used at most once, and each letter can only be used once. The score of a word is the sum of scores of its letters.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 14 words, each up to 15 characters, and up to 100 letters.
- **Time Complexity:** O(2^n × m) where n is the number of words and m is the average word length - we explore all subsets of words using backtracking.
- **Space Complexity:** O(26) = O(1) - we use a fixed-size array to count letters, plus O(n) for recursion stack.
- **Edge Case:** If no words can be formed with available letters, return 0.

**1.2 High-level approach:**

The goal is to find the optimal subset of words that maximizes the total score while respecting letter availability. We use backtracking to try all possible combinations of words.

![Word selection visualization](https://assets.leetcode.com/static_assets/others/word-selection.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Generate all 2^n subsets of words and check which ones are valid, then find the maximum score. This is O(2^n × m) time.
- **Optimized Strategy:** Use backtracking with pruning. For each word, we try both including and excluding it. We prune branches where we can't form the current word. This is still O(2^n × m) but with early termination.
- **Optimization:** By using backtracking, we can prune invalid branches early and avoid generating all subsets explicitly, making the solution more efficient in practice.

**1.4 Decomposition:**

1. Count available letters in a frequency array.
2. Use backtracking: for each word, try both including and excluding it.
3. When including a word, check if we have enough letters to form it.
4. If valid, subtract the letters used, add the word's score, and recurse.
5. Backtrack by restoring the letter counts.
6. Return the maximum score found across all combinations.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `words = ["dog","cat","dad","good"]`, `letters = ["a","a","c","d","d","d","g","o","o"]`

- Available letters: a(2), c(1), d(3), g(1), o(2)
- Scores: a=1, c=9, d=5, g=3, o=2

**2.2 Start Checking:**

We begin backtracking from the first word.

**2.3 Trace Walkthrough:**

| Step | Word | Can Form? | Action                    | Score | Total |
| ---- | ---- | --------- | ------------------------- | ----- | ----- |
| 1    | dog  | Yes       | Use "dog"                 | 3+2+3 | 8     |
| 2    | cat  | No        | Skip (need 'c', 'a', 't') | -     | 8     |
| 3    | dad  | Yes       | Use "dad"                 | 5+1+5 | 14    |
| 4    | good | Yes       | Use "good"                | 3+2+2+5| 23    |

**Alternative path:**
- Skip "dog", use "dad" and "good": 5+1+5 + 3+2+2+5 = 23 ✓

**2.4 Increment and Loop:**

For each word:
- We try skipping it (recurse without using it).
- We try using it (if we have enough letters):
  - Subtract letters used.
  - Add word score.
  - Recurse for remaining words.
  - Restore letters (backtrack).

**2.5 Return Result:**

The result is 23, achieved by forming "dad" and "good" using available letters: d(3), a(2), g(1), o(2).

