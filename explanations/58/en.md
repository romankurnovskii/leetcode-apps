Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

```sh
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**

```sh
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**

```sh
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

## Explanation

### Strategy

This is a **string manipulation problem** that requires finding the length of the last word in a string. The key insight is to iterate from the end of the string and count characters until we encounter a space.

**Key observations:**
- We need to handle trailing spaces
- We need to find the last word by starting from the end
- We can skip trailing spaces and count characters until we hit a space
- We need to handle the case where the last word might be at the beginning

**High-level approach:**
1. **Start from the end**: Iterate from the last character
2. **Skip trailing spaces**: Move backwards until we find a non-space character
3. **Count characters**: Count characters until we hit a space or reach the beginning
4. **Return count**: Return the length of the last word

### Steps

Let's break down the solution step by step:

**Step 1: Initialize variables**
- `length = 0`: Track the length of the last word
- `i = len(s) - 1`: Start from the last character

**Step 2: Skip trailing spaces**
- Move backwards until we find a non-space character

**Step 3: Count characters**
- Count characters until we hit a space or reach the beginning

**Step 4: Return result**
- Return the count

**Example walkthrough:**
Let's trace through the second example:

```sh
s = "   fly me   to   the moon  "

Step 1: Start from end
i = 23 (last character is space)

Step 2: Skip trailing spaces
i = 22 (space)
i = 21 (space)
i = 20 (space)
i = 19 ('n' - found non-space character)

Step 3: Count characters
length = 1 ('n')
i = 18, length = 2 ('o')
i = 17, length = 3 ('o')
i = 16, length = 4 ('m')
i = 15 (space - stop counting)

Result: Return 4
```

> **Note:** The key insight is to work backwards from the end of the string. This approach is efficient because we only need to traverse the string once from the end, and we can handle trailing spaces naturally.

**Time Complexity:** O(n) - we visit each character at most once  
**Space Complexity:** O(1) - we only use a constant amount of extra space 