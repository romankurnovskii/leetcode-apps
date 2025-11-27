## Explanation

### Strategy (The "Why")

Given a string `s`, we need to reverse the order of words. A word is a sequence of non-space characters. The string may have leading or trailing spaces and multiple spaces between words.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to $10^4$.
- **Value Range:** The string contains English letters (upper and lower case), digits, and spaces.
- **Time Complexity:** $O(n)$ - We split the string (which takes $O(n)$) and then reverse and join (which also takes $O(n)$).
- **Space Complexity:** $O(n)$ - We create a list of words, which requires $O(n)$ space.
- **Edge Case:** If the string contains only spaces, return an empty string. Multiple spaces between words should be reduced to single spaces.

**1.2 High-level approach:**

The goal is to reverse the order of words in a string.

![Reverse Words](https://assets.leetcode.com/uploads/2021/10/20/reverse-words-example-1.png)

We split the string by spaces (which automatically handles multiple spaces), reverse the list of words, and join them back with single spaces.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Manually parse the string character by character, building words and handling spaces. This is more complex and error-prone.
- **Optimized Strategy (Split and Reverse):** Use Python's `split()` method which handles multiple spaces automatically, reverse the list, and join with spaces. This is simpler and cleaner.
- **Why it's better:** The split-and-reverse approach is more readable and less error-prone. Python's `split()` automatically handles multiple spaces and leading/trailing spaces correctly.

**1.4 Decomposition:**

1. Split the string by spaces using `split()`. This automatically handles multiple spaces and removes leading/trailing spaces.
2. Reverse the list of words.
3. Join the reversed words with single spaces.
4. Return the resulting string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "the sky is blue"$

We process:
- Split: $["the", "sky", "is", "blue"]$
- Reverse: $["blue", "is", "sky", "the"]$
- Join: $"blue is sky the"$

**2.2 Start Processing:**

We split the string by spaces.

**2.3 Trace Walkthrough:**

**Example 1:** $s = "the sky is blue"$
- `split()` → $["the", "sky", "is", "blue"]$
- `reversed()` → $["blue", "is", "sky", "the"]$
- `join()` → $"blue is sky the"$

**Example 2:** $s = "  hello world  "$
- `split()` → $["hello", "world"]$ (leading/trailing spaces removed)
- `reversed()` → $["world", "hello"]$
- `join()` → $"world hello"$

**Example 3:** $s = "a good   example"$
- `split()` → $["a", "good", "example"]$ (multiple spaces handled)
- `reversed()` → $["example", "good", "a"]$
- `join()` → $"example good a"$

**2.4 Return Result:**

We return the reversed string of words.

> **Note:** Python's `split()` method without arguments automatically splits on any whitespace (spaces, tabs, newlines) and removes empty strings from the result, which perfectly handles the problem requirements.
