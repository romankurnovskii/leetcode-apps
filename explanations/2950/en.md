## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count the number of substrings in a string where the sum of mapped character values is divisible by 9. Characters are mapped to values 1-9 cyclically (a->1, b->2, ..., i->9, j->1, k->2, ...).

**1.1 Constraints & Complexity:**

- **Input Size:** String length can vary, but we need to check all substrings.
- **Time Complexity:** O(n^2) - we iterate over all n(n+1)/2 substrings, where n is the string length.
- **Space Complexity:** O(1) - we only use a constant amount of extra space for variables.
- **Edge Case:** An empty substring is not considered (substrings must have at least one character).

**1.2 High-level approach:**

The goal is to count all substrings whose character value sum is divisible by 9. We use prefix sums to efficiently calculate substring sums without recalculating from scratch.

![Prefix sum for substrings visualization](https://assets.leetcode.com/static_assets/others/prefix-substring.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each substring, calculate the sum by iterating through all characters. This requires O(n^3) time as we iterate over O(n^2) substrings and each sum calculation takes O(n).
- **Optimized Strategy:** Use prefix sums. For each starting position, maintain a running sum as we extend the substring. This allows us to calculate each substring sum in O(1) time. This is O(n^2) time.
- **Optimization:** By using prefix sums, we avoid recalculating sums for overlapping substrings and reduce time complexity from O(n^3) to O(n^2).

**1.4 Decomposition:**

1. Define a mapping function that maps each character to a value 1-9 cyclically.
2. For each starting position i, initialize a prefix sum to 0.
3. For each ending position j starting from i, add the mapped value of word[j] to the prefix sum.
4. Check if the prefix sum is divisible by 9.
5. If yes, increment the result counter.
6. Return the total count of divisible substrings.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `word = "abcd"`

- Character mapping: a->1, b->2, c->3, d->4
- We'll check all substrings starting from each position.

**2.2 Start Checking:**

We begin checking substrings starting from position 0.

**2.3 Trace Walkthrough:**

| Start | End | Substring | Sum | Sum % 9 | Divisible? | Count |
| ----- | --- | --------- | --- | ------- | --------- | ----- |
| 0     | 0   | "a"       | 1   | 1       | No        | 0     |
| 0     | 1   | "ab"      | 3   | 3       | No        | 0     |
| 0     | 2   | "abc"     | 6   | 6       | No        | 0     |
| 0     | 3   | "abcd"    | 10  | 1       | No        | 0     |
| 1     | 1   | "b"       | 2   | 2       | No        | 0     |
| 1     | 2   | "bc"      | 5   | 5       | No        | 0     |
| 1     | 3   | "bcd"     | 9   | 0       | Yes       | 1     |
| 2     | 2   | "c"       | 3   | 3       | No        | 1     |
| 2     | 3   | "cd"      | 7   | 7       | No        | 1     |
| 3     | 3   | "d"       | 4   | 4       | No        | 1     |

**2.4 Increment and Loop:**

For each starting position:
- We maintain a running prefix sum.
- As we extend the substring to the right, we add each new character's mapped value.
- We check divisibility by 9 after each addition.
- We continue until we've checked all substrings starting from that position.

**2.5 Return Result:**

The result is 1, which is the count of substrings whose character sum is divisible by 9. In this example, only "bcd" (sum = 9) is divisible by 9.

