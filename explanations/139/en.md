## Explanation

### Strategy (The "Why")

Given a string `s` and a dictionary of strings `wordDict`, we need to determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length $n$ can be up to $300$, and the dictionary size can be up to $1000$.
- **Value Range:** String and words contain only lowercase English letters.
- **Time Complexity:** $O(n^2)$ - We have $n$ positions to check, and for each position, we check up to $n$ previous positions. The substring check takes $O(n)$ in the worst case, but with a set lookup it's $O(1)$.
- **Space Complexity:** $O(n)$ - We use a DP array of size $n+1$ and a set for the dictionary.
- **Edge Case:** If the string is empty, return true (can be segmented with zero words). If no word matches, return false.

**1.2 High-level approach:**

The goal is to determine if a string can be broken into dictionary words.

![Word Break](https://assets.leetcode.com/uploads/2020/11/08/wordbreak.jpg)

We use dynamic programming. `dp[i]` represents whether the substring `s[0:i]` can be segmented. For each position, we check if any previous position can be segmented and if the substring from that position to the current position is in the dictionary.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to break the string, checking if each segment is in the dictionary. This would be exponential time.
- **Optimized Strategy (DP):** Use DP to store whether each prefix can be segmented. For each position, check all previous positions to see if we can form a valid word ending at the current position.
- **Why it's better:** DP reduces the time complexity from exponential to polynomial by storing results of subproblems and avoiding redundant calculations.

**1.4 Decomposition:**

1. Convert `wordDict` to a set for $O(1)$ lookup.
2. Initialize a DP array where `dp[i]` represents if `s[0:i]` can be segmented.
3. Set `dp[0] = True` (empty string can always be segmented).
4. For each position $i$ from 1 to $n$:
   - Check all previous positions $j$ from 0 to $i-1$.
   - If `dp[j]` is true and `s[j:i]` is in the dictionary, set `dp[i] = True`.
5. Return `dp[n]`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "leetcode"$, $wordDict = ["leet","code"]$

We initialize:
- `word_set = {"leet", "code"}`
- `dp = [True, False, False, False, False, False, False, False, False]`
- `dp[0] = True` (empty string)

**2.2 Start Processing:**

We begin from position 1.

**2.3 Trace Walkthrough:**

| i | Check j | s[j:i] | dp[j] | In Dict? | dp[i] |
|---|---------|--------|-------|----------|-------|
| 1 | 0 | "l" | True | No | False |
| 2 | 0,1 | "le", "e" | True,False | No,No | False |
| 3 | 0,1,2 | "lee", "ee", "e" | True,False,False | No,No,No | False |
| 4 | 0 | "leet" | True | Yes | True |
| 5 | 0,4 | "leetc", "c" | True,True | No,No | False |
| 6 | 0,4,5 | "leetco", "co", "o" | True,True,False | No,No,No | False |
| 7 | 0,4,5,6 | "leetcod", "cod", "od", "d" | True,True,False,False | No,No,No,No | False |
| 8 | 4 | "code" | True | Yes | True |

**2.4 Final Result:**

- `dp[8] = True`, meaning "leetcode" can be segmented as "leet" + "code"

**2.5 Return Result:**

We return `True` because the string can be segmented into dictionary words.

> **Note:** The key insight is that if `s[0:j]` can be segmented and `s[j:i]` is a word, then `s[0:i]` can be segmented. This creates optimal substructure, making DP the perfect approach.

