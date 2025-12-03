## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** Values are in the range $[-2^{31}, 2^{31} - 1]$. At most $3 \times 10^4$ operations will be performed. Operations are called on non-empty stacks.
- **Time Complexity:** $O(1)$ for all operations (push, pop, top, getMin). Each operation is constant time.
- **Space Complexity:** $O(n)$ where $n$ is the number of elements pushed. We maintain two stacks.
- **Edge Case:** If we push the same minimum value multiple times, we need to track all occurrences to handle pops correctly.

**1.2 High-level approach:**

The goal is to design a stack that supports retrieving the minimum element in $O(1)$ time. We use two stacks: one for all elements and one to track minimum values. When pushing, if the new value is less than or equal to the current minimum, we also push it to the min stack.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Store all elements and scan for minimum when `getMin()` is called. This is $O(n)$ time for `getMin()`.
- **Optimized Strategy:** Maintain a separate stack for minimum values. When pushing, if the value is $\leq$ current min, push to min stack. When popping, if the popped value equals the current min, pop from min stack. This gives $O(1)$ for all operations.
- **Why optimized is better:** The optimized strategy achieves $O(1)$ time for `getMin()` by trading a small amount of space for constant-time operations.

**1.4 Decomposition:**

1. Maintain two stacks: `stack` for all elements and `min_stack` for minimum values.
2. `push(val)`: Push to `stack`. If `min_stack` is empty or `val <= min_stack[-1]`, push to `min_stack`.
3. `pop()`: Pop from `stack`. If the popped value equals `min_stack[-1]`, pop from `min_stack`.
4. `top()`: Return `stack[-1]`.
5. `getMin()`: Return `min_stack[-1]`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `["MinStack","push","push","push","getMin","pop","top","getMin"]` with values `[[],[-2],[0],[-3],[],[],[],[]]`

We initialize:
- `stack = []`
- `min_stack = []`

**2.2 Start Checking:**

We perform each operation in sequence.

**2.3 Trace Walkthrough:**

| Operation | Value | stack | min_stack | Return |
|-----------|-------|-------|-----------|--------|
| push(-2) | -2 | [-2] | [-2] | - |
| push(0) | 0 | [-2,0] | [-2] | - |
| push(-3) | -3 | [-2,0,-3] | [-2,-3] | - |
| getMin() | - | [-2,0,-3] | [-2,-3] | -3 |
| pop() | - | [-2,0] | [-2] | - |
| top() | - | [-2,0] | [-2] | 0 |
| getMin() | - | [-2,0] | [-2] | -2 |

**2.4 Increment and Loop:**

- **push(val)**: 
  - `stack.append(val)`
  - If `not min_stack or val <= min_stack[-1]`: `min_stack.append(val)`

- **pop()**: 
  - `val = stack.pop()`
  - If `val == min_stack[-1]`: `min_stack.pop()`

**2.5 Return Result:**

After all operations:
- `top()` returns `0` (the top element).
- `getMin()` returns `-2` (the minimum element in the remaining stack).

The stack correctly maintains both the elements and the minimum value in $O(1)$ time for all operations.

