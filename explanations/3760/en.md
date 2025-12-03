## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^5$ where $n$ is the string length. String contains only lowercase English letters.
- **Time Complexity:** $O(n)$ where $n$ is the string length. We iterate once to count distinct characters.
- **Space Complexity:** $O(1)$ since there are at most 26 distinct lowercase letters.
- **Edge Case:** If all characters are the same (e.g., "aaaa"), return 1.

**1.2 High-level approach:**

The goal is to split the string into the maximum number of substrings where each substring starts with a distinct character. Since each character can only start one substring, the maximum number equals the number of distinct characters in the string.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to split the string and check which gives maximum distinct starting characters. This is exponential time.
- **Optimized Strategy:** Count the number of distinct characters. This is the maximum possible substrings since each character can start exactly one substring. This is $O(n)$ time.
- **Why optimized is better:** The greedy insight that we should use every distinct character as a starting point immediately gives us the optimal answer without trying all combinations.

**1.4 Decomposition:**

1. Count the number of distinct characters in the string.
2. Return this count as the maximum number of substrings.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "abab"`

We want to find the maximum number of substrings with distinct starting characters.

**2.2 Start Checking:**

We count distinct characters in the string.

**2.3 Trace Walkthrough:**

| Character | Seen Before? | Distinct Count |
|-----------|--------------|----------------|
| 'a' | No | 1 |
| 'b' | No | 2 |
| 'a' | Yes | 2 |
| 'b' | Yes | 2 |

**2.4 Increment and Loop:**

We iterate through the string and use a set to track distinct characters:
- `distinct = set(s)`
- `return len(distinct)`

**2.5 Return Result:**

For `s = "abab"`, we have 2 distinct characters ('a' and 'b'), so the maximum number of substrings is 2. For example, we can split as `["a", "bab"]` where 'a' and 'b' are the starting characters.

