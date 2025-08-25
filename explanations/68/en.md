Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**
- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than `0` and not exceed `maxWidth`.
- The input array `words` contains at least one word.

**Example 1:**
```text
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```

**Example 2:**
```text
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
 "What   must   be",
 "acknowledgment  ",
 "shall be        "
]
```

**Constraints:**
- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i]` consists of only English letters and symbols.
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`

## Explanation

### Strategy

This is a **string formatting problem** that requires careful handling of space distribution. The key insight is to process words line by line, calculating how many words can fit in each line and then distributing spaces appropriately.

**Key observations:**
- We need to pack words greedily (as many as possible per line)
- For non-last lines: distribute spaces evenly between words
- For the last line: left-justify with single spaces
- We need to handle edge cases (single word per line, last line)

**High-level approach:**
1. **Group words into lines**: Determine which words fit in each line
2. **Calculate space distribution**: For each line, calculate how to distribute spaces
3. **Format each line**: Apply the space distribution rules
4. **Handle special cases**: Last line and single-word lines

### Steps

Let's break down the solution step by step:

**Step 1: Initialize variables**
- `result = []`: Store formatted lines
- `current_line = []`: Words in current line
- `current_length = 0`: Length of current line

**Step 2: Group words into lines**
- For each word, check if it fits in current line
- If fits: add to current line
- If doesn't fit: format current line and start new line

**Step 3: Format non-last lines**
- Calculate total spaces needed: `maxWidth - word_lengths`
- Calculate spaces between words: `total_spaces // (num_words - 1)`
- Calculate extra spaces: `total_spaces % (num_words - 1)`
- Distribute spaces (more on left if uneven)

**Step 4: Format last line**
- Left-justify with single spaces
- Add remaining spaces at the end

**Example walkthrough:**
Let's trace through the first example:

```text
words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

Step 1: First line
current_line = ["This", "is", "an"]
word_lengths = 4 + 2 + 2 = 8
spaces_needed = 16 - 8 = 8
spaces_between = 8 // 2 = 4
extra_spaces = 8 % 2 = 0
result = ["This    is    an"]

Step 2: Second line
current_line = ["example", "of", "text"]
word_lengths = 7 + 2 + 4 = 13
spaces_needed = 16 - 13 = 3
spaces_between = 3 // 2 = 1
extra_spaces = 3 % 2 = 1
result = ["This    is    an", "example  of text"]

Step 3: Last line
current_line = ["justification."]
Left-justify: "justification.  "
result = ["This    is    an", "example  of text", "justification.  "]
```

> **Note:** The key insight is to separate the logic for regular lines (fully justified) and the last line (left-justified). For regular lines, we need to carefully calculate space distribution to ensure even spacing.

**Time Complexity:** O(n) - we visit each word once  
**Space Complexity:** O(n) - to store the result 