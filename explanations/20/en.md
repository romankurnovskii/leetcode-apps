## Explanation

### Strategy (The "Why")

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', we need to determine if the input string is valid. A string is valid if: open brackets are closed by the same type, open brackets are closed in the correct order, and every close bracket has a corresponding open bracket.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be between $1$ and $10^4$.
- **Value Range:** String contains only '(', ')', '{', '}', '[' and ']'.
- **Time Complexity:** $O(n)$ - We iterate through the string once.
- **Space Complexity:** $O(n)$ - In the worst case, the stack contains all opening brackets.
- **Edge Case:** If the string is empty, return true. If the string has only opening brackets, return false.

**1.2 High-level approach:**

The goal is to check if brackets are properly matched and nested.

We use a stack. When we encounter an opening bracket, we push it. When we encounter a closing bracket, we check if it matches the top of the stack. If the stack is empty or doesn't match, the string is invalid.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible ways to match brackets. This would be exponential.
- **Optimized Strategy (Stack):** Use a stack to match brackets as we encounter them. This takes $O(n)$ time.
- **Why it's better:** The stack approach is optimal and straightforward. It naturally handles the LIFO (Last In First Out) property needed for matching nested brackets.

**1.4 Decomposition:**

1. Create a mapping from closing brackets to opening brackets.
2. Use a stack to store opening brackets.
3. For each character:
   - If it's a closing bracket, check if stack top matches.
   - If it's an opening bracket, push it.
4. After processing, check if the stack is empty (all brackets matched).

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
| ')' | Closing | Pop, check match | [] |
| '[' | Opening | Push | ['['] |
| ']' | Closing | Pop, check match | [] |
| '{' | Opening | Push | ['{'] |
| '}' | Closing | Pop, check match | [] |

**2.4 Final Check:**

After processing, `stack = []` (empty), so all brackets are matched.

**2.5 Return Result:**

We return `True` because the string is valid.

> **Note:** The key insight is that brackets must be closed in the reverse order they were opened. A stack naturally provides this LIFO behavior, making it perfect for this problem.

