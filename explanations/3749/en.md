## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a valid mathematical expression string, we need to evaluate it. The expression may contain numbers, operators (+, -, *), and parentheses.

**1.1 Constraints & Complexity:**

- **Input Size:** The expression length can be up to 10^4.
- **Time Complexity:** O(n) - we process each character once using a stack, where n is the expression length.
- **Space Complexity:** O(n) - we need a stack to handle parentheses and operations.
- **Edge Case:** If the expression is just a number, return that number. If there are nested parentheses, we need to handle them correctly.

**1.2 High-level approach:**

The goal is to use a stack to process the expression, handling parentheses by evaluating inner expressions first.

![Expression evaluation visualization](https://assets.leetcode.com/static_assets/others/expression-eval.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Recursively parse and evaluate. This is what we essentially do with a stack.
- **Optimized Strategy:** Use a stack to process the expression, evaluating parentheses from innermost to outermost. This is O(n) time.
- **Optimization:** By using a stack, we can handle nested parentheses naturally and evaluate in the correct order.

**1.4 Decomposition:**

1. Initialize a stack.
2. Process the expression character by character:
   - If digit, parse the number and push to stack.
   - If operator, push to stack.
   - If '(', push to stack.
   - If ')', pop until '(', evaluate the expression, push result.
3. After processing, evaluate remaining expression in stack.
4. Return the final result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `expression = "(1+(2*3))"`

- Stack: `[]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We process each character.

**2.3 Trace Walkthrough:**

| Step | Char | Stack before | Stack after |
| ---- | ---- | ------------ | ----------- |
| 1    | ( | [] | ['('] |
| 2    | 1 | ['('] | ['(', 1] |
| 3    | + | ['(', 1] | ['(', 1, '+'] |
| 4    | ( | ['(', 1, '+'] | ['(', 1, '+', '('] |
| 5-7  | 2*3 | ... | ['(', 1, '+', 6] |
| 8    | ) | ['(', 1, '+', 6] | [7] |

**2.4 Increment and Loop:**

After processing each character, we update the stack accordingly.

**2.5 Return Result:**

The result is `7`, which is the evaluated value of the expression (1 + (2 * 3) = 7).

