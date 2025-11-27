## Explanation

### Strategy (The "Why")

Given two strings `s` and `t`, we need to determine if they are isomorphic. Two strings are isomorphic if the characters in `s` can be replaced to get `t`, with a one-to-one mapping between characters.

**1.1 Constraints & Complexity:**

- **Input Size:** The string lengths can be up to $5 \times 10^4$.
- **Value Range:** Strings can contain any valid ASCII characters.
- **Time Complexity:** $O(n)$ where $n$ is the length of the strings. We iterate through both strings once.
- **Space Complexity:** $O(1)$ - In the worst case, we store at most 256 character mappings (ASCII), which is constant.
- **Edge Case:** If the strings have different lengths, they cannot be isomorphic.

**1.2 High-level approach:**

The goal is to check if there's a one-to-one character mapping between `s` and `t`.

We use two dictionaries to maintain bidirectional mappings: one maps characters from `s` to `t`, and another maps characters from `t` to `s`. This ensures the mapping is one-to-one.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible character mappings and check if any works. This would be exponential.
- **Optimized Strategy (Two Hash Maps):** Use two hash maps to maintain bidirectional mappings and check consistency. This takes $O(n)$ time.
- **Why it's better:** The hash map approach is efficient and ensures we can verify both directions of the mapping in one pass.

**1.4 Decomposition:**

1. Check if strings have the same length (if not, return false).
2. Create two dictionaries: one for mapping `s` to `t`, one for mapping `t` to `s`.
3. Iterate through each character pair.
4. For each pair, check if mappings are consistent in both directions.
5. If any inconsistency is found, return false. Otherwise, return true.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "egg"$, $t = "add"$

We initialize:
- `s_to_t = {}`
- `t_to_s = {}`

**2.2 Start Processing:**

We iterate through each character pair.

**2.3 Trace Walkthrough:**

| i | s[i] | t[i] | s_to_t | t_to_s | Action |
|---|------|------|--------|--------|--------|
| 0 | 'e' | 'a' | {'e': 'a'} | {'a': 'e'} | Add mappings |
| 1 | 'g' | 'd' | {'e': 'a', 'g': 'd'} | {'a': 'e', 'd': 'g'} | Add mappings |
| 2 | 'g' | 'd' | Check: 'g' -> 'd' ✓ | Check: 'd' -> 'g' ✓ | Consistent |

**2.4 Verification:**

- 'e' maps to 'a', and 'a' maps back to 'e' ✓
- 'g' maps to 'd', and 'd' maps back to 'g' ✓
- All mappings are consistent

**2.5 Return Result:**

We return `True` because the strings are isomorphic.

> **Note:** The key is to maintain bidirectional mappings. A character in `s` must map to exactly one character in `t`, and that character in `t` must map back to the same character in `s`. This ensures the mapping is one-to-one.
