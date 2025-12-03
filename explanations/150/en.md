## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^4$ tokens. Each token is either an operator (`+`, `-`, `*`, `/`) or an integer in $[-200, 200]$. The expression is valid.
- **Time Complexity:** $O(n)$ where $n$ is the number of tokens. We process each token once.
- **Space Complexity:** $O(n)$ for the stack in the worst case when all tokens are operands.
- **Edge Case:** If there's only one token, it must be a number, return that number.

**1.2 High-level approach:**

The goal is to evaluate a Reverse Polish Notation (RPN) expression. RPN uses postfix notation where operators follow their operands. We use a stack: push operands, and when we encounter an operator, pop two operands, perform the operation, and push the result.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert to infix notation first, then evaluate. This is more complex and error-prone.
- **Optimized Strategy:** Use a stack to process tokens left to right. When an operator is encountered, pop two operands, compute, and push result. This is $O(n)$ time.
- **Why optimized is better:** The stack-based approach directly processes RPN as intended, making it straightforward and efficient.

**1.4 Decomposition:**

1. Initialize an empty stack.
2. Iterate through each token:
   - If token is a number, push it onto the stack.
   - If token is an operator, pop two operands, perform the operation, and push the result.
3. After processing all tokens, the stack contains one element: the result.
4. Return the top of the stack.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `tokens = ["2","1","+","3","*"]`

We initialize an empty stack: `stack = []`.

**2.2 Start Checking:**

We process each token from left to right.

**2.3 Trace Walkthrough:**

| Token | Type | Action | Stack State |
|-------|------|--------|-------------|
| "2" | Number | Push 2 | [2] |
| "1" | Number | Push 1 | [2, 1] |
| "+" | Operator | Pop 1, Pop 2, Compute 2+1=3, Push 3 | [3] |
| "3" | Number | Push 3 | [3, 3] |
| "*" | Operator | Pop 3, Pop 3, Compute 3*3=9, Push 9 | [9] |

**2.4 Increment and Loop:**

For each token:
- If token is `+`, `-`, `*`, or `/`:
  - Pop the right operand: `b = stack.pop()`
  - Pop the left operand: `a = stack.pop()`
  - Perform operation: `res = a op b` (for division, use `int(a / b)` to truncate toward zero)
  - Push result: `stack.append(res)`
- Otherwise (token is a number):
  - Push the number: `stack.append(int(token))`

**2.5 Return Result:**

After processing all tokens, the stack contains `[9]`. We return `stack[0]`, which is `9`. This represents the expression `((2 + 1) * 3) = 9`.

