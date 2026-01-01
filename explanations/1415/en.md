## Explanation

### Strategy (The "Why")

**Restate the problem:** A "happy string" is a string where no two consecutive characters are the same. Given integers n and k, we need to find the k-th lexicographically smallest happy string of length n.

**1.1 Constraints & Complexity:**

- **Input Size:** n can be up to 10, and k can be up to 100.
- **Time Complexity:** O(3^n) in worst case - we may need to generate all happy strings, but we can stop early when we find the k-th one.
- **Space Complexity:** O(n) - we need to store the current path during backtracking, which has length n.
- **Edge Case:** If k is greater than the total number of happy strings, return empty string. If n = 1, there are 3 happy strings: "a", "b", "c".

**1.2 High-level approach:**

The goal is to use backtracking to generate happy strings in lexicographical order until we find the k-th one. We build strings character by character, ensuring no two consecutive characters are the same.

![Happy string generation visualization](https://assets.leetcode.com/static_assets/others/happy-string-gen.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Generate all possible strings of length n and filter for happy strings, then sort. This is inefficient.
- **Optimized Strategy:** Use backtracking to generate happy strings in lexicographical order, stopping when we reach the k-th one. This avoids generating unnecessary strings.
- **Optimization:** By generating strings in order and stopping early, we can find the k-th string without generating all possibilities.

**1.4 Decomposition:**

1. Use backtracking to build strings character by character.
2. For each position, try characters 'a', 'b', 'c' in order.
3. Ensure the current character is different from the previous character.
4. When we complete a string of length n, increment a counter.
5. When the counter reaches k, return that string.
6. If we finish generating all strings and counter < k, return empty string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 3`, `k = 9`

- Characters available: `['a', 'b', 'c']`
- Current path: `path = []`
- Result list: `res = []`
- Counter: We'll track how many strings we've generated

**2.2 Start Checking:**

We begin building strings using backtracking.

**2.3 Trace Walkthrough:**

| Step | Path | Last char | Next char | New path | Complete? | Count |
| ---- | ---- | --------- | --------- | -------- | --------- | ----- |
| 1    | []   | -         | 'a'       | ['a']    | No        | 0     |
| 2    | ['a']| 'a'       | 'b'       | ['a','b']| No        | 0     |
| 3    | ['a','b']| 'b'    | 'a'       | ['a','b','a']| Yes   | 1     |
| ...  | ...  | ...       | ...       | ...      | ...       | ...   |
| 9    | ...  | ...       | ...       | ['c','a','c']| Yes | 9     |

**2.4 Increment and Loop:**

After completing each string, we check if we've reached the k-th string. If not, we continue backtracking.

**2.5 Return Result:**

The result is `"cac"` (or the 9th happy string), which is the k-th lexicographically smallest happy string of length n.

