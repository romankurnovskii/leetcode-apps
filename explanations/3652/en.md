## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given a binary string and can perform two types of operations: flip all characters from index 0 to i (cost: i+1) or flip all characters from index i to n-1 (cost: n-i). We need to find the minimum cost to make all characters equal.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length n can be up to 10^5, and each character is either '0' or '1'.
- **Time Complexity:** O(n) - we iterate through the string once to find all transitions.
- **Space Complexity:** O(1) - we only use a constant amount of extra space.
- **Edge Case:** If the string already has all characters equal, there are no transitions and the cost is 0.

**1.2 High-level approach:**

The goal is to find the minimum cost to eliminate all transitions (places where adjacent characters differ) in the string. When we encounter a transition, we can either flip the prefix or the suffix, and we choose the cheaper option.

![String transitions visualization](https://assets.leetcode.com/static_assets/others/string-transitions.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of operations, which would be exponential O(2^n) and too slow.
- **Optimized Strategy:** For each transition at position i, we can either flip [0, i-1] (cost i) or flip [i, n-1] (cost n-i). We choose min(i, n-i) and sum all transition costs. This is O(n) time.
- **Optimization:** By recognizing that each transition can be fixed independently with the cheaper operation, we avoid exponential search and solve in linear time.

**1.4 Decomposition:**

1. Iterate through the string from left to right.
2. For each position i, check if there's a transition (s[i] != s[i-1]).
3. If a transition exists, add the minimum cost (min(i, n-i)) to fix it.
4. Return the total cost.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "0011"`, `n = 4`.

- Initialize `res = 0` to track total cost.
- The string has one transition at position 2 (between '0' and '1').

**2.2 Start Checking:**

We iterate through the string starting from index 1, comparing each character with the previous one.

**2.3 Trace Walkthrough:**

| Position i | s[i] | s[i-1] | Transition? | Cost Option 1 (flip prefix) | Cost Option 2 (flip suffix) | Chosen Cost | res |
|------------|------|--------|-------------|---------------------------|----------------------------|-------------|-----|
| 1 | '0' | '0' | No | - | - | 0 | 0 |
| 2 | '1' | '0' | Yes | 2 | 2 | 2 | 2 |
| 3 | '1' | '1' | No | - | - | 0 | 2 |

**2.4 Increment and Loop:**

After checking all positions, we have found all transitions and calculated the minimum cost to fix each one.

**2.5 Return Result:**

The result is 2, which is the minimum cost to make all characters equal. We achieve this by flipping the suffix from index 2 to the end, changing "0011" to "0000".

