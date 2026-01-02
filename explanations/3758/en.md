## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a string containing number words (like "one", "two") and digits, we need to convert all number words to their digit equivalents.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to 10^4.
- **Time Complexity:** O(n * m) where n is string length and m is the number of number words - we check each position against all words.
- **Space Complexity:** O(n) - we need to store the result string.
- **Edge Case:** If the string contains no number words, return as is. If a word is partially matched, we need to handle it correctly.

**1.2 High-level approach:**

The goal is to scan the string and replace number words with their corresponding digits while preserving other characters.

![Word to digit conversion visualization](https://assets.leetcode.com/static_assets/others/word-digit.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check each position against all possible number words. This is what we do, and it's reasonable for the constraints.
- **Optimized Strategy:** Use a trie or similar structure for faster matching. For the given constraints, simple matching is acceptable.
- **Optimization:** By checking longer words first, we can avoid partial matches, but for simplicity, we check in order.

**1.4 Decomposition:**

1. Create a mapping from number words to digits.
2. Iterate through the string character by character.
3. For each position, check if any number word starts here.
4. If found, replace with digit and skip the word length.
5. Otherwise, keep the character as is.
6. Return the converted string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "onetwothree"`

- Word mapping: `{"zero":"0", "one":"1", "two":"2", ...}`
- Result list: `res = []`
- Current position: `i = 0`

**2.2 Start Checking:**

We scan the string and look for number words.

**2.3 Trace Walkthrough:**

| Step | Position | Check | Match | Action | res |
| ---- | -------- | ----- | ----- | ------ | --- |
| 1    | 0 | "one" | Yes | Add "1", i+=3 | ["1"] |
| 2    | 3 | "two" | Yes | Add "2", i+=3 | ["1","2"] |
| 3    | 6 | "three" | Yes | Add "3", i+=5 | ["1","2","3"] |

**2.4 Increment and Loop:**

After each match, we skip the matched word length and continue.

**2.5 Return Result:**

The result is `"123"`, which is the string with all number words converted to digits.

