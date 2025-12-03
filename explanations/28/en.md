## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** Both `haystack` and `needle` can have length up to $10^4$.
* **Time Complexity:** $O(n \times m)$ where $n$ is the length of `haystack` and $m$ is the length of `needle`. For each position in `haystack`, we check if the substring matches `needle`.
* **Space Complexity:** $O(1)$ as we only use constant extra space.
* **Edge Case:** If `needle` is empty, return 0. If `needle` is longer than `haystack`, return -1.

**1.2 High-level approach**

The goal is to find the first occurrence of `needle` in `haystack`. This is a classic string matching problem where we check each possible starting position.

![String matching visualization showing the needle sliding through the haystack]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Check each possible starting position in `haystack` and compare the substring with `needle`. This is $O(n \times m)$ which is acceptable for the given constraints.
* **Optimized (KMP Algorithm):** Use the Knuth-Morris-Pratt algorithm for $O(n + m)$ time, but for the given constraints, the simple approach is sufficient and easier to understand.

**1.4 Decomposition**

1. Iterate through each possible starting position in `haystack`.
2. For each position, check if the substring of length `len(needle)` matches `needle`.
3. If a match is found, return the starting index.
4. If no match is found after checking all positions, return -1.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $haystack = "sadbutsad"$, $needle = "sad"$.

We initialize:
* `n = len(haystack) = 9`
* `m = len(needle) = 3`

**2.2 Start Checking/Processing**

We iterate through positions from 0 to $n - m$ (inclusive), checking each possible starting position.

**2.3 Trace Walkthrough**

| i | haystack[i:i+3] | Comparison with "sad" | Match? | Action |
|---|-----------------|------------------------|--------|--------|
| 0 | "sad" | "sad" == "sad" | Yes | Return 0 |

Since we found a match at position 0, we return immediately.

For a case where the match is not at the start, consider $haystack = "leetcode"$, $needle = "leeto"$:

| i | haystack[i:i+5] | Comparison with "leeto" | Match? | Action |
|---|-----------------|--------------------------|--------|--------|
| 0 | "leetc" | "leetc" != "leeto" | No | Continue |
| 1 | "eetco" | "eetco" != "leeto" | No | Continue |
| 2 | "etcode" | "etcode" != "leeto" | No | Continue |
| 3 | "tcode" | "tcode" != "leeto" | No | Continue |

After checking all positions, no match found, return -1.

**2.4 Increment and Loop**

For each position $i$ from 0 to $n - m$:
1. Extract substring: `substring = haystack[i:i + m]`
2. Compare: `if substring == needle:`
3. If match found, return $i$
4. Otherwise, continue to next position

**2.5 Return Result**

For $haystack = "sadbutsad"$, $needle = "sad"$:
* Match found at position 0
* Return `0`

Note: There's also a match at position 6, but we return the first occurrence.

