Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Examples**

```text
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

**Constraints**
```text
1 <= s.length <= 10^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
```

## Explanation

### Strategy
- **Type:** String, Two Pointers, Simulation
- **Given:** A string `s` with words separated by spaces (possibly multiple spaces, leading/trailing spaces)
- **Asked:** Return a string with the words in reverse order, separated by a single space, with no leading/trailing spaces

#### What does "reverse words" mean?
- The order of the words is reversed, but the characters within each word remain in the same order.
- All extra spaces (leading, trailing, or between words) are reduced to a single space between words.

#### High-Level Plan
1. Split the string into words (ignoring extra spaces)
2. Reverse the list of words
3. Join the words back together with a single space

### Steps

Let's walk through an example: s = "a good   example"

1. Split into words: ["a", "good", "example"]
2. Reverse: ["example", "good", "a"]
3. Join: "example good a"

> **Note:**
> - Python's `split()` automatically removes extra spaces and splits on any whitespace.
> - This approach is both simple and efficient, making use of built-in functions.

- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(n)
