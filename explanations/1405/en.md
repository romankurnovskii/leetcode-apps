## Explanation

### Strategy (The "Why")

**Restate the problem:** Given three integers a, b, and c representing the counts of characters 'a', 'b', and 'c', we need to construct the longest possible string without any three consecutive identical characters.

**1.1 Constraints & Complexity:**

- **Input Size:** Each count (a, b, c) can be up to 100.
- **Time Complexity:** O(a + b + c) - we process each character once, and the total number of characters is a + b + c.
- **Space Complexity:** O(a + b + c) - we need to store the result string, which has length at most a + b + c.
- **Edge Case:** If all counts are 0, return empty string. If one count is much larger than others, we need to alternate carefully to avoid three consecutive characters.

**1.2 High-level approach:**

The goal is to greedily use the character with the highest remaining count, but ensure we never place three of the same character consecutively. We use a max-heap to always select the character with the most remaining count.

![Happy string construction visualization](https://assets.leetcode.com/static_assets/others/happy-string.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible arrangements of characters and find the longest valid one. This is exponential and impractical.
- **Optimized Strategy:** Use a max-heap to greedily select characters, ensuring no three consecutive characters are the same. This is O(a + b + c) time.
- **Optimization:** By using a heap and checking for consecutive characters, we can construct the string efficiently without trying all arrangements.

**1.4 Decomposition:**

1. Create a max-heap containing all characters with non-zero counts.
2. While the heap is not empty:
   - Pop the character with the highest count.
   - Check if adding this character would create three consecutive identical characters.
   - If yes, use the second-highest count character instead (if available).
   - Add the chosen character(s) to the result and update counts.
3. Return the constructed string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `a = 1`, `b = 1`, `c = 7`

- Max-heap: `[(-7, 'c'), (-1, 'a'), (-1, 'b')]`
- Result string: `res = ""`
- Current state: No characters yet

**2.2 Start Checking:**

We begin constructing the string by popping from the heap.

**2.3 Trace Walkthrough:**

| Step | Heap Top | Last 2 chars | Would violate? | Action | res | Heap after |
| ---- | -------- | ------------ | -------------- | ------ | --- | ---------- |
| 1    | c (7)    | ""           | No             | Add c  | "c" | [(-6, 'c'), (-1, 'a'), (-1, 'b')] |
| 2    | c (6)    | "c"          | No             | Add c  | "cc" | [(-5, 'c'), (-1, 'a'), (-1, 'b')] |
| 3    | c (5)    | "cc"         | Yes            | Use a  | "cca" | [(-5, 'c'), (-1, 'b')] |
| 4    | c (5)    | "ca"         | No             | Add c  | "ccac" | [(-4, 'c'), (-1, 'b')] |
| 5    | c (4)    | "ac"         | No             | Add c  | "ccacc" | Continue... |

**2.4 Increment and Loop:**

After each character addition, we update the heap and continue until no more characters can be added.

**2.5 Return Result:**

The result is a string like `"ccacbcc"` (or similar), which is the longest possible string without three consecutive identical characters.

