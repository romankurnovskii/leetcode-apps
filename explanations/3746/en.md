## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a string containing characters 'A', 'B', 'C', 'D', we need to remove pairs "AB" and "CD" repeatedly until no more can be removed, then return the minimum length.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to 10^5.
- **Time Complexity:** O(n) - we process each character once using a stack, where n is the string length.
- **Space Complexity:** O(n) - we need a stack to store characters.
- **Edge Case:** If the string is empty, return 0. If no pairs can be removed, return the original length.

**1.2 High-level approach:**

The goal is to use a stack to simulate the removal process: when we see 'B' and top is 'A', remove both; when we see 'D' and top is 'C', remove both.

![Balanced removal visualization](https://assets.leetcode.com/static_assets/others/balanced-remove.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Repeatedly scan and remove pairs until no more can be removed. This is O(n^2) in worst case.
- **Optimized Strategy:** Use a stack to process characters once, removing pairs as we encounter them. This is O(n) time.
- **Optimization:** By using a stack, we can efficiently check and remove pairs in a single pass.

**1.4 Decomposition:**

1. Initialize an empty stack.
2. For each character in the string:
   - If stack is not empty and top forms a removable pair (AB or CD), pop from stack.
   - Otherwise, push the character to stack.
3. Return the stack size (remaining characters).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "ABFCACDB"`

- Stack: `[]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We process each character.

**2.3 Trace Walkthrough:**

| Step | Char | Stack before | Action | Stack after |
| ---- | ---- | ------------ | ------ | ----------- |
| 1    | A | [] | Push | ['A'] |
| 2    | B | ['A'] | Remove AB | [] |
| 3    | F | [] | Push | ['F'] |
| 4    | C | ['F'] | Push | ['F','C'] |
| 5    | A | ['F','C'] | Push | ['F','C','A'] |
| 6    | C | ['F','C','A'] | Push | ['F','C','A','C'] |
| 7    | D | ['F','C','A','C'] | Remove CD | ['F','C','A'] |
| 8    | B | ['F','C','A'] | Push | ['F','C','A','B'] |

**2.4 Increment and Loop:**

After processing each character, we check for removable pairs.

**2.5 Return Result:**

The result is `4`, which is the length of the remaining string "FCAB" after removing all possible pairs.

