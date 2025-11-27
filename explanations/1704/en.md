## Explanation

### Strategy (The "Why")

Given a string `s` of even length, we need to split it into two halves and determine if both halves have the same number of vowels. Vowels are 'a', 'e', 'i', 'o', 'u' in both lowercase and uppercase.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be between $2$ and $1000$ (even length).
- **Value Range:** String contains only letters (a-z, A-Z).
- **Time Complexity:** $O(n)$ - We iterate through the string once to count vowels in both halves.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for counters and the vowel set.
- **Edge Case:** If the string has only 2 characters, compare them directly. If there are no vowels in either half, return true.

**1.2 High-level approach:**

The goal is to check if the first half and second half of the string have the same number of vowels.

We split the string into two halves, count vowels in each half, and compare the counts.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must count vowels in both halves.
- **Optimized Strategy (Two Passes):** Count vowels in the first half, then count vowels in the second half, and compare. This is straightforward and efficient.
- **Why it's better:** The two-pass approach is simple and optimal. We can also do it in one pass, but two passes is clearer.

**1.4 Decomposition:**

1. Calculate the midpoint of the string.
2. Count vowels in the first half (indices 0 to mid-1).
3. Count vowels in the second half (indices mid to n-1).
4. Return true if counts are equal, false otherwise.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "book"$

We initialize:
- `n = 4`, `mid = 2`
- `vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}`
- `count_first = 0`
- `count_second = 0`

**2.2 Start Counting:**

We count vowels in each half.

**2.3 Trace Walkthrough:**

**First half (indices 0-1): "bo"**
- 'b': not a vowel
- 'o': vowel → `count_first = 1`

**Second half (indices 2-3): "ok"**
- 'o': vowel → `count_second = 1`
- 'k': not a vowel

**2.4 Comparison:**

- `count_first = 1`
- `count_second = 1`
- $1 == 1$ → True

**2.5 Return Result:**

We return `True` because both halves have the same number of vowels (1 each).

> **Note:** The key is to split the string into two equal halves and count vowels in each. Since the string length is even, the split is straightforward.

