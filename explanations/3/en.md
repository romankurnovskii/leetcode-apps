## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The string $s$ can have up to $5 \times 10^4$ characters ($N = 50,000$).
* **Character Set:** $s$ consists of English letters, digits, symbols, and spaces.
* **Time Complexity:** $O(n)$ where $n$ is the length of the string. We use a sliding window that visits each character at most twice (once when expanding, once when shrinking).
* **Space Complexity:** $O(min(n, m))$ where $m$ is the size of the character set (at most 128 for ASCII). The hash set stores unique characters in the current window.
* **Edge Case:** An empty string returns 0.

**1.2 High-level approach**

The goal is to find the longest substring without repeating characters. We can think of this as maintaining a "window" of characters that contains no duplicates.

![Sliding window visualization showing a window expanding and contracting to find the longest substring without duplicates]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Check all possible substrings $O(n^2)$ and verify each has no duplicates $O(n)$, resulting in $O(n^3)$ time complexity.
* **Optimized (Sliding Window):** Use two pointers to maintain a window of unique characters. When we encounter a duplicate, we shrink the window from the left until the duplicate is removed. This achieves $O(n)$ time complexity by visiting each character at most twice.

**1.4 Decomposition**

1. Use two pointers to define a sliding window of characters.
2. Expand the window by moving the right pointer and adding characters to a set.
3. When a duplicate is found, shrink the window from the left until the duplicate is removed.
4. Track the maximum window size encountered.

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $s = "abcabcbb"$.

We initialize:
* `char_set = {}` (empty set to track characters in current window)
* `left = 0` (start of window)
* `res = 0` (maximum length found)

**2.2 Start Checking/Processing**

We iterate through the string with the right pointer, starting at index 0.

**2.3 Trace Walkthrough**

| Right | Character | char_set | left | Window | res | Action |
|-------|------------|----------|------|--------|-----|--------|
| 0 | 'a' | {'a'} | 0 | "a" | 1 | Add 'a', update res |
| 1 | 'b' | {'a','b'} | 0 | "ab" | 2 | Add 'b', update res |
| 2 | 'c' | {'a','b','c'} | 0 | "abc" | 3 | Add 'c', update res |
| 3 | 'a' | {'a','b','c'} | 0 | "abc" | 3 | 'a' already in set |
| 3 | 'a' | {'b','c'} | 1 | "bca" | 3 | Remove 'a' from left, add 'a' |
| 4 | 'b' | {'b','c','a'} | 1 | "bcab" | 3 | 'b' already in set |
| 4 | 'b' | {'c','a'} | 2 | "cab" | 3 | Remove 'b' from left, add 'b' |
| 5 | 'c' | {'c','a','b'} | 2 | "cabc" | 3 | 'c' already in set |
| 5 | 'c' | {'a','b'} | 3 | "abc" | 3 | Remove 'c' from left, add 'c' |
| 6 | 'b' | {'a','b','c'} | 3 | "abcb" | 3 | 'b' already in set |
| 6 | 'b' | {'a','c'} | 4 | "cb" | 3 | Remove 'b' from left, add 'b' |
| 7 | 'b' | {'a','c','b'} | 4 | "cbb" | 3 | 'b' already in set |
| 7 | 'b' | {'c'} | 5 | "b" | 3 | Remove 'b' from left, add 'b' |

**2.4 Increment and Loop**

For each character at position `right`:
1. While the character is already in `char_set`, remove characters from the left and increment `left`.
2. Add the current character to `char_set`.
3. Update `res = max(res, right - left + 1)`.

**2.5 Return Result**

After processing all characters, `res = 3`, which is the length of the longest substring without repeating characters ("abc" appears at positions 0-2 and 3-5).

