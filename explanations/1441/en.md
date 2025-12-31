## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to build a target array using stack operations (Push and Pop) from a stream of integers 1 to n. We can push numbers onto the stack or pop them, and we want to end up with the target array in the stack.

**1.1 Constraints & Complexity:**

- **Input Size:** The target array length can be up to 100, and n can be up to 100.
- **Time Complexity:** O(n) - we iterate through numbers from 1 to n at most once, and each number results in at most 2 operations (Push and possibly Pop).
- **Space Complexity:** O(1) - we don't need to store the actual stack, just track which numbers we've processed.
- **Edge Case:** If the target array is [1,2,3,...,n], we only need Push operations. If target is [1,3] and n=3, we need to Push 1, Push 2, Pop 2, Push 3.

**1.2 High-level approach:**

The goal is to simulate building the target array by processing numbers from 1 to n sequentially. For each number, we always Push it. If the number is in the target, we keep it. If not, we Pop it immediately.

![Stack operations visualization](https://assets.leetcode.com/static_assets/others/stack-operations.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible sequences of Push/Pop operations and check which ones result in the target. This is exponential and impractical.
- **Optimized Strategy:** Process numbers sequentially from 1 to n. For each number, Push it. If it matches the next target element, keep it (don't Pop). Otherwise, Pop it immediately. This is O(n) time.
- **Optimization:** By processing numbers in order and making greedy decisions, we avoid backtracking and solve the problem in linear time.

**1.4 Decomposition:**

1. Initialize an index to track our position in the target array.
2. Iterate through numbers from 1 to n.
3. For each number, always Push it onto the stack.
4. Check if the current number matches the next target element.
5. If it matches, increment the target index (keep the number).
6. If it doesn't match, Pop it immediately (discard the number).
7. Stop when we've built the complete target array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `target = [1,3]`, `n = 3`

- Target array: `[1, 3]`
- Target index: `idx = 0`
- Result list: `res = []`
- Current number: `i = 1`

**2.2 Start Checking:**

We begin processing numbers from 1 to n.

**2.3 Trace Walkthrough:**

| Step | i | target[idx] | Match? | Operations | res | idx |
| ---- | - | ---------- | ------ | ---------- | --- | --- |
| 1    | 1 | 1          | Yes    | Push       | ["Push"] | 1 |
| 2    | 2 | 3          | No     | Push, Pop  | ["Push", "Push", "Pop"] | 1 |
| 3    | 3 | 3          | Yes    | Push       | ["Push", "Push", "Pop", "Push"] | 2 |

**2.4 Increment and Loop:**

After processing each number, we increment `i` and continue until `idx >= len(target)` or `i > n`.

**2.5 Return Result:**

The result is `["Push", "Push", "Pop", "Push"]`, which builds the target array [1, 3] in the stack.

