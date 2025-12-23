## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to simulate executing a sequence of instructions. Each instruction is either "add" (add a value to score and move to next) or "jump" (move to a different index without changing score). The process stops when we go out of bounds or try to revisit an instruction we've already executed.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 100,000 instructions, each value can be between -100,000 and 100,000.
- **Time Complexity:** O(n) where n is the number of instructions. Each instruction is visited at most once, and we stop when we revisit or go out of bounds.
- **Space Complexity:** O(n) - we use a boolean array of size n to track visited instructions.
- **Edge Case:** If the first instruction is "jump" with value 0, we immediately revisit index 0 and stop with score 0.

**1.2 High-level approach:**

The goal is to simulate the execution step by step, tracking which instructions have been visited to detect cycles, and accumulating the score only when executing "add" instructions.

![Instruction simulation visualization](https://assets.leetcode.com/static_assets/others/instruction-simulation.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Recursively simulate with memoization, which could be more complex to implement.
- **Optimized Strategy:** Use iterative simulation with a visited array to track executed instructions. This is straightforward and efficient.
- **Optimization:** The visited array allows us to detect cycles in O(1) time, and the iterative approach is simpler than recursion.

**1.4 Decomposition:**

1. Initialize a visited array to track which instructions have been executed.
2. Start at index 0 with score 0.
3. While the current index is valid and not visited:
   - Mark the current index as visited.
   - If instruction is "add": add the value to score and move to next index (i+1).
   - If instruction is "jump": move to index (i + values[i]) without changing score.
4. Stop when index is out of bounds or already visited.
5. Return the final score.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `instructions = ["jump","add","add","jump","add","jump"]`, `values = [2,1,3,1,-2,-3]`

- Number of instructions: `n = 6`
- Visited array: `visited = [False, False, False, False, False, False]`
- Current index: `i = 0`
- Score: `score = 0`

**2.2 Start Checking:**

We begin executing instructions starting from index 0.

**2.3 Trace Walkthrough:**

| Step | i   | visited[i] | instruction | value | Action                    | New i | score |
| ---- | --- | ----------- | ----------- | ----- | ------------------------- | ----- | ----- |
| 1    | 0   | False       | "jump"      | 2     | Mark visited, jump to 2  | 2     | 0     |
| 2    | 2   | False       | "add"       | 3     | Mark visited, add 3, i+1  | 3     | 3     |
| 3    | 3   | False       | "jump"      | 1     | Mark visited, jump to 4   | 4     | 3     |
| 4    | 4   | False       | "add"       | -2    | Mark visited, add -2, i+1| 5     | 1     |
| 5    | 5   | False       | "jump"      | -3    | Mark visited, jump to 2   | 2     | 1     |
| 6    | 2   | True        | -           | -     | Already visited, STOP     | -     | 1     |

**2.4 Increment and Loop:**

After each instruction, we update the index based on the instruction type and continue until we hit a visited index or go out of bounds.

**2.5 Return Result:**

The result is 1, which is the final score after executing the instructions until we tried to revisit index 2.
