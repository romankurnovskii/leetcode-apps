## Explanation

### Strategy (The "Why")

Given an encoded string `s`, we need to decode it. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly $k$ times. $k$ is guaranteed to be a positive integer.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to $30$.
- **Value Range:** $k$ is between $1$ and $300$. The decoded string will not exceed $10^5$ characters.
- **Time Complexity:** $O(n)$ where $n$ is the length of the decoded string. We process each character once.
- **Space Complexity:** $O(n)$ - The stack can store at most $O(n)$ states, and the decoded string itself is $O(n)$.
- **Edge Case:** Nested brackets like `2[3[a]]` should be decoded as `aaa` repeated 2 times = `aaaaaa`.

**1.2 High-level approach:**

The goal is to decode a string with nested brackets and numbers.

![Decode String](https://assets.leetcode.com/uploads/2021/04/24/decode-string.jpg)

We use a stack to handle nested brackets. When we encounter `[`, we push the current state. When we encounter `]`, we pop and decode.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Recursively decode from the innermost brackets outward. This is actually similar to the stack approach but less intuitive.
- **Optimized Strategy (Stack):** Use a stack to maintain the state (current string and number) when encountering `[`. When we see `]`, pop and decode by repeating the current string the specified number of times.
- **Why it's better:** The stack approach is iterative and easier to understand. It naturally handles nested brackets by maintaining state at each nesting level.

**1.4 Decomposition:**

1. Iterate through each character in the string.
2. If it's a digit, build the number.
3. If it's `[`, push current state (string and number) to stack and reset.
4. If it's `]`, pop from stack and decode: `prev_string + current_string * num`.
5. If it's a regular character, append to current string.
6. Return the final decoded string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "3[a]2[bc]"$

We initialize:
- `stack = []`
- `current_string = ""`
- `current_num = 0`

**2.2 Start Processing:**

We iterate through each character.

**2.3 Trace Walkthrough:**

| Character | Action | Stack | current_string | current_num |
|-----------|--------|-------|----------------|-------------|
| '3' | Build number | [] | "" | 3 |
| '[' | Push state | [("", 3)] | "" | 0 |
| 'a' | Append | [("", 3)] | "a" | 0 |
| ']' | Pop and decode | [] | "aaa" | 0 |
| '2' | Build number | [] | "aaa" | 2 |
| '[' | Push state | [("aaa", 2)] | "" | 0 |
| 'b' | Append | [("aaa", 2)] | "b" | 0 |
| 'c' | Append | [("aaa", 2)] | "bc" | 0 |
| ']' | Pop and decode | [] | "aaabcbc" | 0 |

**2.4 Decoding Details:**

When we encounter `]`:
- Pop: `prev_string = "aaa"`, `num = 2`
- Decode: `"aaa" + "bc" * 2 = "aaa" + "bcbc" = "aaabcbc"`

**2.5 Return Result:**

We return `"aaabcbc"`, which is the decoded string.

> **Note:** The stack naturally handles nested brackets. Each `[` creates a new level, and each `]` closes the current level and applies the repetition to the string built at that level.

