## Explanation

### Strategy (The "Why")

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', we need to determine if the input string is valid. A string is valid if open brackets are closed by the same type of brackets in the correct order.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be between $1$ and $10^4$.
- **Value Range:** String contains only '(', ')', '{', '}', '[' and ']'.
- **Time Complexity:** $O(n)$ - We iterate through the string once.
- **Space Complexity:** $O(n)$ - In the worst case, the stack can contain all opening brackets.
- **Edge Case:** If the string is empty, it's technically valid (no brackets to match). If the string has only opening brackets, return false.

**1.2 High-level approach:**

The goal is to check if brackets are properly matched and nested.

We use a stack to track opening brackets. When we encounter a closing bracket, we check if it matches the most recent opening bracket. If the stack is empty or doesn't match, the string is invalid.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to match brackets. This would be exponential.
- **Optimized Strategy (Stack):** Use a stack to match brackets as we encounter them. This takes $O(n)$ time.
- **Why it's better:** The stack approach is optimal and straightforward. It processes the string in one pass, matching brackets as they appear.

**1.4 Decomposition:**

1. Create a mapping from closing brackets to opening brackets.
2. Use a stack to store opening brackets.
3. For each character:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket, check if the stack is empty or if the top doesn't match. If so, return false. Otherwise, pop from the stack.
4. After processing all characters, return true if the stack is empty, false otherwise.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "()[]{}"$

We initialize:
- `stack = []`
- `mapping = {')': '(', '}': '{', ']': '['}`

**2.2 Start Processing:**

We iterate through each character.

**2.3 Trace Walkthrough:**

| Character | Type | Action | stack After |
|-----------|------|--------|-------------|
| '(' | Opening | Push | ['('] |
| ')' | Closing | Pop (matches) | [] |
| '[' | Opening | Push | ['['] |
| ']' | Closing | Pop (matches) | [] |
| '{' | Opening | Push | ['{'] |
| '}' | Closing | Pop (matches) | [] |

**2.4 Final Check:**

After processing all characters, the stack is empty, so all brackets are matched.

**2.5 Return Result:**

We return `True` because all brackets are properly matched.

> **Note:** The key insight is to use a stack to track opening brackets. When we encounter a closing bracket, it must match the most recent opening bracket (LIFO - Last In First Out), which is exactly what a stack provides.

