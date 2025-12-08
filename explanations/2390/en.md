## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to remove stars from a string. Each star removes the closest non-star character to its left, along with the star itself.

**1.1 Constraints & Complexity:**
- Input size: `1 <= s.length <= 10^5`
- **Time Complexity:** O(n) where n is the length of the string, as we process each character once
- **Space Complexity:** O(n) for the stack to store characters
- **Edge Case:** If the string contains only stars, all characters will be removed, resulting in an empty string

**1.2 High-level approach:**
We use a stack to simulate the removal process. When we encounter a star, we pop the most recent character (the one to the left). When we encounter a non-star, we push it onto the stack.

![Stack visualization](https://assets.leetcode.com/static_assets/others/stack-operation.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each star, find and remove the closest non-star to the left by scanning backwards, which would be O(n²) in worst case
- **Optimized Strategy:** Use a stack to maintain characters, allowing O(1) removal of the most recent character, resulting in O(n) time
- **Emphasize the optimization:** The stack allows us to efficiently track and remove the "closest left" character without scanning

**1.4 Decomposition:**
1. Initialize an empty stack to store characters
2. Iterate through each character in the string
3. If the character is a star, remove the top element from the stack (if it exists)
4. If the character is not a star, add it to the stack
5. Convert the remaining stack elements to a string and return

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `s = "leet**cod*e"`
- Initialize an empty stack: `stack = []`

**2.2 Start Processing:**
We iterate through each character in the string from left to right.

**2.3 Trace Walkthrough:**

| Character | Stack Before | Action | Stack After |
|-----------|--------------|--------|-------------|
| 'l' | [] | Push 'l' | ['l'] |
| 'e' | ['l'] | Push 'e' | ['l', 'e'] |
| 'e' | ['l', 'e'] | Push 'e' | ['l', 'e', 'e'] |
| 't' | ['l', 'e', 'e'] | Push 't' | ['l', 'e', 'e', 't'] |
| '*' | ['l', 'e', 'e', 't'] | Pop 't' | ['l', 'e', 'e'] |
| '*' | ['l', 'e', 'e'] | Pop 'e' | ['l', 'e'] |
| 'c' | ['l', 'e'] | Push 'c' | ['l', 'e', 'c'] |
| 'o' | ['l', 'e', 'c'] | Push 'o' | ['l', 'e', 'c', 'o'] |
| 'd' | ['l', 'e', 'c', 'o'] | Push 'd' | ['l', 'e', 'c', 'o', 'd'] |
| '*' | ['l', 'e', 'c', 'o', 'd'] | Pop 'd' | ['l', 'e', 'c', 'o'] |
| 'e' | ['l', 'e', 'c', 'o'] | Push 'e' | ['l', 'e', 'c', 'o', 'e'] |

**2.4 Increment and Loop:**
After processing all characters, we continue to the next step.

**2.5 Return Result:**
The final stack contains `['l', 'e', 'c', 'o', 'e']`, which when joined gives `"lecoe"`, which is the result.
